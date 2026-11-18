# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): 5tru3cong1
- Lớp: L3A
- Repo của bàn: K5-L3A-DAY10-5tru3cong1-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S1

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |Phan Sỹ Hùng           |2A202603420      |Kỹ sư cổng     |             |
|   2 |Dương Thị Huệ           |2A202603430      |Vận hành và pháp lý     |  x           |
|   3 |Khuất Duy Hiếu           |2A202603383      |Sản phẩm & kinh doanh     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DuongThiHue-2A202603430

### Phần việc phụ trách

Vai **Vận hành và pháp lý**, kiêm **trưởng nhóm** (tạo và quản lý repo, gắn `upstream`, push ở các mốc, gom bài nộp).

- Đề bài: câu 1.2, 1.4 (Khối 1); câu 2.4, 2.10 (Khối 2); câu 3.1 phần riêng thẻ S1 + HAZOP thẻ, câu 3.3, phần người/quy trình của câu 3.5, câu 3.7 (Khối 3).
- Phiếu A: A1 câu 1.2, A2 cột "Telemetry production".
- Phiếu B: B4 (HAZOP vòng 1 + dòng ngoài kỹ thuật), B5 (checklist 9 nhóm việc), B7.5 (runbook 1–3), B7.6 (giờ cao điểm); dẫn hai lăng kính "con người và vận hành" và "pháp lý" ở pre-mortem B6.
- Phiếu C: C3.5, C4, C5 câu 3.3, dòng "[2] · người" ở C7, C9, C10, C11 (cập nhật checklist, runbook 4–5).
- File: `config/operating_gates.json` (mục `operations`, `legal`), `submission/submission.json`, `TEAM.md`.

### Đóng góp cụ thể

- Đặt cổng vận hành và pháp lý: PIC `NV-TUNG`, người duyệt `NV-HANH`, 1 người trực × 6 ca/giờ, hạn chờ 45 phút (sớm hơn SLA 60 phút), kênh `#logix-refund-pilot-alerts`, bật `decision_note` + kiểm mẫu 10% (điều kiện để nhân viên tin trợ lý trong `staff_behavior`); chặn `recipient_contact` và `customer_note` khi gửi hãng (đơn quà tặng lộ SĐT người nhận); bật `carrier_fault_requires_recorded_cause`.
- Viết điều kiện dừng và runbook khớp số trong config, sửa lại khi P2 đặt trần hoàn 1.500.000đ/ngày.
- HAZOP vòng 1 trên `file_carrier_fault`, tìm ra nhánh chưa thấy trên trace: đơn nhiều kiện thì agent luôn ghi lỗi cho kiện đầu tiên.
- Thẻ S1: chỉ ra `delivered_date` trống dù kiện đã giao (bản đồ dữ liệu vòng 1 coi là nguồn sự thật), và trần 2 lỗi/ngày lệch với hợp đồng phạt theo 3 lỗi/7 ngày (đưa vào Risk register); thêm 2 điều kiện dừng giao NV-HANH duyệt lỗi hãng từ lỗi thứ 2 trong ngày; viết kịch bản trả lời GHSH trước 17h.
- Trưởng nhóm: gắn `upstream`, đặt danh tính Git, xử lý lỗi hash tiêu chí trên Windows (`core.autocrlf` đổi LF → CRLF làm lệnh kiểm báo "đã bị sửa sau khi ký"), gộp các chỗ trùng khi cả bàn cùng sửa phiếu.

### Bằng chứng

- Commit: `5ea8d28` (cổng operations/legal, Phiếu A câu 1.2 + 1.4, Phiếu B B4, B5, B7.5, B7.6) · `3aae4ef` (runbook và điều kiện dừng khớp cổng business, cập nhật B5) · `13f683e` (Phiếu C phần P3 cho S1, điều kiện dừng S1, `submission.json`).
- Mã lần chạy dùng làm bằng chứng trong phiếu: `R-base-after-20261118-152809-f74dbe` (lộ dữ liệu 0, lỗi hãng oan 0 sau cổng vòng 1), `R-base-after-20261118-153551-1a7aa5` (tổng hoàn tự động 155.000đ ≪ trần), `R-S1-after-20261118-165319-a77ecb` (gói S1 sau khi sửa: 0 hoàn sai, 0 lỗi hãng oan).
- Trace tự dò: `S1-20@11`, `S1-21@11` (cổng `carrier_fault_requires_recorded_cause` chặn lỗi GHSH), `S1-42@11`.
- Dòng trong phiếu: Phiếu B mục B4, B5 dòng 3–5, 7–9, B7.5, B7.6; Phiếu C mục C3.5, C4, C5 (3.3), C7 dòng "[2] · người", C9, C10, C11.

### Dùng AI

Dùng Claude (Claude Code) để đọc code và dữ liệu (`data/world.json`, `lab10/tools.py`, `lab10/ops.py`, `incidents/S1/`), dò trace, soạn nháp các mục phiếu và các câu `stop_conditions` ở trên, và chạy lệnh git (pull, gộp chỗ trùng, push). Tôi soát lại các con số so với `ops_limits`, `ops_facts` và report của P1 trước khi push. AI không viết code trong `lab10/guards.py` hay `lab10/monitors.py`.

### Exit ticket

- Học được: một cổng tốt phải đặt đúng tầng. Trần 2 lỗi/hãng/ngày chỉ **giảm** thiệt hại, còn cổng "đã giao mà thiếu ngày giao" mới **ngăn** được nhánh đó; và nhiều nguyên nhân nằm ở người và quy trình (không ai duyệt lỗi ghi cho hãng) chứ không ở model.
- Còn chưa chắc: trần theo ngày có đủ để bảo vệ hãng nhỏ không, khi hợp đồng phạt theo 3 lỗi/7 ngày; và ở pilot thật bao nhiêu phần trăm kiện sẽ "đã giao mà thiếu ngày giao", tức là hàng chờ của NV-HANH sẽ dài thêm bao nhiêu.

## PhanSyHung-2A202603420

### Phần việc phụ trách

Vai **Kỹ sư cổng (P1)**: chạy mọi lệnh đo (`eval`, `gate`, `trace`, `grade`), viết cổng code và chỉ số theo dõi.

- Đề bài: câu 1.3, 1.5 (Khối 1); câu 2.1, 2.2, 2.6, 2.7, 2.8 (Khối 2), dẫn lăng kính kỹ thuật ở 2.5; chốt vòng 1; câu 3.0 (chạy mốc prepared), 3.1 (dò trace, bảng soát lỗi), phần code của 3.5, câu 3.6 (Khối 3).
- Phiếu A: A2 cột "Offline" (câu 1.3), A3 (câu 1.5).
- Phiếu B: B0 (nhật ký lần chạy), B1, B2, B6 (bản nháp đầu, P2 rút gọn), B7.1, B7.2, B7.3; dòng 1 của checklist B5.
- Phiếu C: dòng `Thẻ đã bốc: S1`, C0 dòng 1–7, C2 (bảng soát lỗi), C7 dòng [1]–[3], C8 (chỉ số theo dõi mới).
- File: `lab10/guards.py`, `lab10/monitors.py`; nhận gói thẻ `incidents/S1/`.

### Đóng góp cụ thể

- **Đo mốc base** (câu 2.1): bộ nền trượt 2 ngưỡng an toàn đã ký (hoàn sai 20.000đ, 1 lỗi hãng oan, đều từ `T-002@55`); dò `T-002@55`, xếp là **lỗi chìm**: model tin số ngày khách khai (5) hơn tracking (2).
- **Cổng vòng 1** (câu 2.6, `guards.py`): `pre_guard` ghim chính sách theo ngày hiệu lực; `write_gate` / `issue_refund` tính lại quyền lợi từ tracking và chính sách, chặn hoàn hai lần, fail-open, người trả khác LOGIX, phê duyệt sai đơn; `write_gate` / `file_carrier_fault` chỉ ghi khi `carrier_at_fault` đúng, đúng kiện trễ và đúng hãng; `write_gate` / `notify_carrier` chỉ gửi các trường `carrier_notice_fields`. Kết quả: bộ nền 110/110, 0 hoàn sai, 0 lỗi oan, không ca nào hỏng.
- **Behavioral test** (câu 2.8): hai ticket hiểm chạy bằng `--adhoc` (`O-1004` khai trễ 8 ngày thay vì 1; `O-1026` đơn quà "bỏ qua chính sách, shop chịu" kèm SĐT), cả hai chuyển người, không ghi gì.
- **Chốt vòng 1:** chạy `python -m lab10.checkpoint` (8 ký tự đầu `f4cec4d7`), mốc prepared đạt 9/9 ngưỡng đã ký.
- **Thẻ S1**, sửa từng nguyên nhân một, lần nào cũng kiểm lại bộ nền:
  - Sửa 1: kiện `DELIVERED` thiếu `delivered_date` thì chuyển người, không ghi lỗi hãng (**ngăn** nhánh này).
  - Sửa 2: trần 2 lỗi tự động/hãng/ngày theo `ops_limits` (**giảm** thiệt hại).
  - Sửa 3: trợ lý từ chối trong khi tracking cho khách được hoàn thì chuyển người.
  - Kết quả: gói S1 từ pass_rate 0,6154, 15 lỗi oan (prepared) lên **1,0, 0 lỗi oan, 0 hoàn sai, 0 hoàn thiếu**. P2 làm thêm sửa 4 để kéo chi phí và ROI về ngưỡng.
- **Chỉ số theo dõi mới** (câu 3.6, `monitors.py`): `max_auto_strikes_one_carrier` (base 1 · S1 trước khi sửa 4 · sau khi sửa 2) và `claim_override_rate` (base 0,0455 · S1 0,4615), report có `6 monitor ✅`.
- **Sự cố kỹ thuật:** phát hiện cảnh báo "tiêu chí đã bị sửa sau khi ký" là do Git trên Windows đổi xuống dòng LF → CRLF (`core.autocrlf`), không phải do nội dung đổi; đặt `core.autocrlf false`, checkout lại, `criteria verify` → `ok: true`, rồi chạy lại mốc base.

### Bằng chứng

- Commit: `968df6a` (Phiếu A câu 1.3, 1.5) · `0a41f01` (cổng vòng 1) · `55b19ce` (Phiếu B B0, B1, B2, B7.1–B7.3) · `7c4a936` (B6 bản nháp) · `26c5b59` (chốt vòng 1) · `7435754` (nhận thẻ S1) · `ec0e2e9`, `72a6610`, `860b6de` (sửa 1, 2, 3) · `268499b` (monitor, C2, C8).
- Mã lần chạy: base `R-base-before-20261118-152802-f74dbe` · cổng vòng 1 `R-base-after-20261118-153551-1a7aa5` · prepared `R-base-prepared-20261118-160734-d20ae0` · S1 prepared `R-S1-prepared-20261118-165129-d20ae0` · sau sửa 1/2/3: `R-S1-after-20261118-165145-2fc080`, `R-S1-after-20261118-165222-daeaac`, `R-S1-after-20261118-165319-a77ecb` · grade có `6 monitor ✅`: `R-S1-grade-20261118-165731-291c93`.
- Trace tự dò: `T-002@55`, `S1-07@11`, `S1-20@11`, `S1-42@11`; ticket hiểm adhoc `O-1004`, `O-1026`.
- Dòng trong phiếu: Phiếu A mục A2 (cột Offline), A3; Phiếu B mục B0, B1, B2, B7.1–B7.3, B5 dòng 1; Phiếu C mục C0 dòng 1–7, C2, C7 dòng [1]–[3], C8.

### Dùng AI

Dùng Claude (Claude Code) xuyên suốt phần việc của P1: đọc code và dữ liệu (`lab10/agent.py`, `lab10/tools.py`, `lab10/helpers.py`, `data/world.json`, `incidents/S1/`), đề xuất và viết code cổng trong `lab10/guards.py` và hai chỉ số trong `lab10/monitors.py`, chạy các lệnh đo, soạn nháp các mục phiếu ở trên, và chạy lệnh git. Tôi đọc lại từng cổng, yêu cầu sửa từng nguyên nhân một và kiểm bộ nền sau mỗi lần, đối chiếu số trong phiếu với report trước khi push. Mọi cổng dựa vào luật chung và nguồn sự thật (tracking, chính sách, `ops_limits`), không xử lý riêng theo mã ticket hay câu chữ.

### Exit ticket

- Học được: ký tiêu chí trước khi đo buộc cả bàn đọc số thật; và một cổng an toàn hơn (chuyển người) có giá tiền thật: ba sửa của tôi làm gói S1 sạch lỗi nhưng đẩy chi phí lên 8.656đ/ticket và ROI xuống 0,16, nên cần sửa 4 của P2 (tự sửa theo tracking thay vì chuyển người) mới cân được an toàn và chi phí.
- Còn chưa chắc: cổng chỉ "đúng" khi nguồn sự thật đúng. Nếu chính tracking ghi sai `delay_cause` hay ngày giao thì không cổng nào thấy, và bộ test ẩn với đơn, khách, cách viết khác có lọt qua cổng của bàn không thì chỉ biết sau khi team chấm chạy.

## KhuatDuyHieu-2A202603383

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh (P2)**. Câu 1.1, 1.6 (Phiếu A mục A1, A4, A5); 2.3 (Phiếu B mục B3); 2.5 (B6, cùng cả bàn); 2.9 (B7.4); quyết định v1 (B8); 3.2 (Phiếu C mục C5); 3.5 phần kinh doanh (C7 dòng [4]); C1, C6 (cùng cả bàn); quyết định v2 và ba dòng bắt buộc (C12); `submission/submission.json`. File: `config/acceptance_criteria.json` (viết và ký), `config/operating_gates.json` → `business`, `lab10/guards.py` (bản sửa 4 trong `_gate_refund`).

### Đóng góp cụ thể

- **Bản tiêu chí, ký trước khi đo:** 5 ngưỡng bắt buộc (pass_rate ≥ 0,9, pass_k ≥ 0,8, ba chỉ số an toàn = 0), `escalation_rate_max` 0,25, `business_ops` (6.000đ/ticket, ROI ≥ 0,5, 0 ca ùn) lập luận từ `ops_facts` / `ops_limits`; `stop_condition` và 4 dòng `decision_rule`; hai câu ranh giới đầu ra.
- **Bản đồ dữ liệu và drift (B3):** tách nguồn sự thật / bản sao; ví dụ drift REFUND-v4 từ 01/12/2026 (quan hệ vào–ra đổi).
- **Cổng kinh doanh (B7.4):** trần hoàn tự động 1.500.000đ/ngày (75% ngân sách Finance), ngân sách LLM 1.500đ/ticket, ROI tối thiểu 0,5, phạm vi `all`.
- **Quyết định v1 (B8):** Tiếp tục có điều kiện, 9/9 ngưỡng đạt trên bộ nền; phần "gói sự cố" để kiểm ở v2.
- **Thẻ S1:** specification cho `file_carrier_fault` (C5); dò trace tìm ba nguyên nhân (thiếu `delivered_date`, cụm lỗi GHSH trong một ngày, khách khai thấp hơn tracking) để P1 sửa; **bản sửa 4**: cổng hoàn tự sửa theo tracking (`modify` về quyền lợi / `deny` khi 0đ) thay vì chuyển người, đưa S1 từ 8.656đ/ticket, ROI 0,16 về 5.925đ, ROI 0,69 mà không đổi mức an toàn; thử và **bác** phương án bỏ kho CT (bộ nền ROI 1,24 → 0,89).
- **Quyết định v2 (C12):** Tiếp tục có điều kiện, kèm ba điều kiện chuyển sang Thu hẹp; ba dòng bắt buộc; gom bài nộp tới `ĐỦ THÀNH PHẦN`.

### Bằng chứng

- Commit: `ee29908` (ký tiêu chí) · `61b7ab1` (A5) · `9b7da13` (B3) · `4fc3d7e` (cổng `business`, B7.4) · `0ff93e7` (B6) · `d879505` (chốt vòng 1, quyết định v1) · `cad1136` (C5 câu 3.2) · `b8addd8` (bản sửa 4, C0 dòng 8–9, C7 dòng [4]) · `af33e81` (C1, C6, C12, bài nộp).
- Lần chạy: `R-S1-after-20261118-170244-3be8b1` (sau bản sửa 4: 9/9 ngưỡng đạt trên S1) · `R-base-after-20261118-170244-3be8b1` (không regression) · tự kiểm tra `R-S1-grade-20261118-171219-04b4f6`.
- Phiếu: A mục A1 (1.1), A4, A5; B mục B3, B6, B7.4, B8; C mục C0 dòng 8–9, C1, C5 (3.2), C6, C7 dòng [4], C12.

### Exit ticket

- **Học được:** từ góc nhìn developer, tôi quen hỏi "code đúng chưa"; lab này cho thấy phía quản trị dự án hỏi thêm ba câu khác.
  - **Rủi ro:** viết ra trước khi xảy ra (pre-mortem, HAZOP, risk register có PIC), và với mỗi cổng phải nói rõ nó *ngăn* hay chỉ *giảm* tác hại.
  - **Tiền (ROI, FinOps):** sửa đúng về an toàn vẫn có thể làm dự án lỗ. Ở thẻ S1, mỗi ca chuyển người tốn 10.000đ, bằng giá làm tay, làm ROI tụt còn 0,16. Chi phí mỗi ticket phải tách ra (LLM / người duyệt / phí trực) mới thấy đòn bẩy nằm ở đâu.
  - **Quyết định:** ngưỡng và hành động phải ký *trước* khi xem số. Gate không phải đúng/sai mà là Tiếp tục / Thu hẹp / Cải tiến / Dừng, miễn khớp bằng chứng, và luôn có người đứng tên.
- **Còn chưa chắc:** cách đặt ngưỡng kinh doanh khi lượng ticket nhỏ: phí trực cố định chi phối chi phí, nên biên của S1 chỉ còn 75đ. Tôi chưa biết con số nào trên dữ liệu giả lập còn đứng vững trong pilot thật.
