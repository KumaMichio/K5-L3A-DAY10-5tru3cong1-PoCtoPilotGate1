"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _policy(ctx):
    """Chính sách hiệu lực theo NGÀY (nguồn sự thật), không theo cờ index_active."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def pre_guard(ctx):
    # Ghim phiên bản chính sách theo ngày hiệu lực (pre-mortem kỹ thuật: cờ index_active lệch khi đổi chính sách).
    pol = _policy(ctx)
    if pol is not None:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def _delivered_without_date(parcel):
    """VÒNG 2 · S1: tracking mâu thuẫn — trạng thái đã giao nhưng thiếu ngày giao.
    helpers.db_delay_days không đọc status, nên độ trễ bị tính tới as_of (tăng dần theo ngày chạy): dữ liệu THIẾU, không phải trễ."""
    return parcel.get("status") == "DELIVERED" and not parcel.get("delivered_date")


def _gate_refund(ctx, action):
    """CỔNG 1 · issue_refund: số tiền phải khớp quyền lợi tính lại từ nguồn sự thật.
    HAZOP issue_refund: MORE (hoàn quá), OTHER THAN (người trả sai, phê duyệt sai đơn), AS WELL AS (hoàn hai lần)."""
    order = ctx.tools.lookup_order(action.get("order_id"))
    pol = _policy(ctx)
    if order is None or pol is None:
        return Verdict.escalate("cổng hoàn: thiếu đơn hoặc chính sách hiệu lực để đối chiếu")

    # (a) không hoàn hai lần cho cùng một đơn (cờ REFUNDED chỉ cập nhật ban đêm; lệnh ghi lại khi LLM báo lỗi)
    if ctx.tools.ledger_rows(order_id=order["order_id"]):
        return Verdict.deny("cổng hoàn: đơn đã có dòng hoàn trong sổ cái")

    # (b) không hoàn theo chế độ fail-open khi model lỗi
    if action.get("basis") == "fail_open":
        return Verdict.escalate("cổng hoàn: model lỗi, không tự hoàn theo fail-open")

    # (c) LogiX là người trả cho yêu cầu giao trễ; đổi người trả phải có người duyệt
    if action.get("payer", "LOGIX") != "LOGIX":
        return Verdict.escalate("cổng hoàn: người trả khác LOGIX, cần người duyệt")

    # (d) số tiền không vượt quyền lợi tính từ tracking DB + chính sách hiệu lực
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    if _delivered_without_date(parcel):
        ctx.log("delivered_without_date", parcel_id=parcel.get("parcel_id"))
        return Verdict.escalate("cổng hoàn: tracking ghi đã giao nhưng thiếu ngày giao, cần người kiểm")
    delay = H.db_delay_days(parcel, ctx.as_of)
    entitled = H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))
    amount = int(action.get("amount_vnd") or 0)
    if amount > entitled:
        ctx.log("refund_over_entitlement", amount_vnd=amount, entitled_vnd=entitled, db_delay_days=delay)
        return Verdict.escalate(f"cổng hoàn: đề xuất {amount}đ vượt quyền lợi {entitled}đ theo tracking và chính sách")

    # (e) phê duyệt dùng kèm phải đúng đơn, còn hiệu lực và đủ hạn mức
    appr_id = action.get("approval_id")
    if appr_id:
        appr = next(iter(ctx.tools.lookup_approvals(approval_id=appr_id)), None)
        if (appr is None or appr.get("order_id") != order["order_id"] or appr.get("status") != "valid"
                or (appr.get("expires_at") and appr["expires_at"] < ctx.as_of) or amount > appr.get("max_vnd", 0)):
            return Verdict.escalate("cổng hoàn: phê duyệt không khớp đơn, hết hạn hoặc không đủ hạn mức")
    return None


def _gate_carrier_fault(ctx, action):
    """CỔNG 2 · file_carrier_fault: chỉ ghi lỗi khi chính sách cho phép, đúng kiện trễ và đúng hãng.
    HAZOP file_carrier_fault: OTHER THAN (sai hãng / sai kiện), NO cause (không có nguyên nhân ghi nhận)."""
    order = ctx.tools.lookup_order(action.get("order_id"))
    pol = _policy(ctx)
    if order is None or pol is None:
        return Verdict.deny("cổng lỗi hãng: thiếu đơn hoặc chính sách hiệu lực")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    if _delivered_without_date(parcel):
        return Verdict.deny("cổng lỗi hãng: tracking ghi đã giao nhưng thiếu ngày giao, không có căn cứ tính trễ")
    delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(pol, parcel, delay):
        return Verdict.deny("cổng lỗi hãng: tracking không ghi nguyên nhân thuộc lỗi hãng")
    # VÒNG 2 · S1: trần lỗi TỰ ĐỘNG cho một hãng trong ngày (ops_limits, đã thống nhất với Ops/Finance).
    # Từ lỗi thứ (trần + 1) phải có người duyệt; khách vẫn được hoàn, chỉ lệnh ghi lỗi bị bỏ.
    cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if cap is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= cap:
        ctx.log("strike_cap_hit", carrier_id=parcel["carrier_id"], cap=cap)
        return Verdict.deny(f"cổng lỗi hãng: {parcel['carrier_id']} đã đủ {cap} lỗi tự động trong ngày, chuyển người duyệt")
    fix = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
           "driver_id": parcel.get("driver_id"), "delay_days": delay}
    if any(action.get(k) != v for k, v in fix.items()):
        return Verdict.modify("cổng lỗi hãng: ghi đúng kiện trễ, đúng hãng và độ trễ theo tracking", **fix)
    return None


def _gate_notify(ctx, action):
    """CỔNG 3 · notify_carrier: chỉ gửi cho hãng các trường chính sách cho phép (không lộ dữ liệu cá nhân)."""
    pol = _policy(ctx)
    allowed = set((pol or {}).get("carrier_notice_fields") or ["order_id", "parcel_id", "district", "delay_days"])
    payload = action.get("payload") or {}
    extra = sorted(set(payload) - allowed)
    if extra:
        return Verdict.modify("cổng dữ liệu: bỏ trường không có trong carrier_notice_fields: " + ", ".join(extra),
                              payload={k: v for k, v in payload.items() if k in allowed})
    return None


def _gate_reply(ctx, action):
    """VÒNG 2 · S1: trợ lý TỪ CHỐI (không ghi hoàn) trong khi tracking + chính sách cho khách được hoàn.
    Xảy ra khi khách khai trễ THẤP hơn tracking và model tin số khai. Chỉ xét nhánh từ chối sau khi đã có đề xuất:
    không có lệnh issue_refund nào đã ghi, và không phải do cổng của bàn chặn lệnh hoàn (đơn đã hoàn, v.v.)."""
    ev = ctx.events
    if not any(e.get("type") == "proposal" for e in ev):
        return None
    if any(e.get("type") == "tool" and e.get("tool") == "issue_refund" for e in ev):
        return None
    if any(e.get("type") == "gate" and e.get("tool") == "issue_refund" for e in ev):
        return None
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    pol = _policy(ctx)
    if order is None or pol is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    if _delivered_without_date(parcel):
        return None
    entitled = H.entitlement_vnd(pol, order, H.db_delay_days(parcel, ctx.as_of), parcel.get("delay_cause"))
    if int(action.get("amount_vnd") or 0) < entitled:
        ctx.log("reply_under_entitlement", amount_vnd=action.get("amount_vnd", 0), entitled_vnd=entitled)
        return Verdict.escalate(f"cổng trả lời: trợ lý từ chối nhưng theo tracking và chính sách khách được {entitled}đ, chuyển người")
    return None


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        v = _gate_refund(ctx, action)
    elif tool == "file_carrier_fault":
        v = _gate_carrier_fault(ctx, action)
    elif tool == "notify_carrier":
        v = _gate_notify(ctx, action)
    elif tool == "send_reply":
        v = _gate_reply(ctx, action)
    else:
        v = None
    if v is not None:
        return v
    return Verdict.allow()
