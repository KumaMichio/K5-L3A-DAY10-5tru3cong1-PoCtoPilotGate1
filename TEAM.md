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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

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
