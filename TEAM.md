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
