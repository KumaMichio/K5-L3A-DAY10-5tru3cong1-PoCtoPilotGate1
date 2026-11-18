"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def max_auto_strikes_one_carrier(trials):
    """VÒNG 2 · S1 (vận hành): số lỗi TỰ ĐỘNG nhiều nhất mà một hãng bị ghi trong một ngày vận hành.
    Đếm sự kiện tool file_carrier_fault theo (seed, day, carrier_id). Không cần nhãn.
    Báo động khi > ops_limits.max_auto_strikes_per_carrier_per_day (= 2); hợp đồng GHSH tạm ngưng tuyến ở 3 lỗi/7 ngày."""
    counts = {}
    for t in trials:
        for e in t.get("events") or []:
            if e.get("type") == "tool" and e.get("tool") == "file_carrier_fault":
                k = (t.get("seed"), t.get("day"), e.get("carrier_id"))
                counts[k] = counts.get(k, 0) + 1
    return max(counts.values(), default=0)


def claim_override_rate(trials):
    """VÒNG 2 · S1 (kỹ thuật): tỉ lệ lần chạy mà model đè số ngày trễ khách tự khai lên tracking DB
    (sự kiện model_override của agent), theo CẢ HAI chiều: khai cao (hoàn oan, ghi lỗi oan) và khai thấp (từ chối oan).
    Không cần nhãn: đây là tín hiệu có sẵn trong production."""
    hit = sum(any(e.get("type") == "model_override" for e in (t.get("events") or [])) for t in trials)
    return round(hit / max(1, len(trials)), 4)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "max_auto_strikes_one_carrier": max_auto_strikes_one_carrier,
    "claim_override_rate": claim_override_rate,
}
STARTER_MONITORS = ("escalation_rate",)
