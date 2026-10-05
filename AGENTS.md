# QUY TẮC BẮT BUỘC HỆ THỐNG (MANDATORY SYSTEM RULES)

> **CÁC NGUYÊN TẮC BẤT DI BẤT DỊCH CHO TOÀN BỘ CÁC AGENT VÀ QUY TRÌNH XỬ LÝ**

---

## 1. PHÂN BIỆT MÔN HỌC & BẢN QUYỀN GIÁO VIÊN

Khi nhận bất kỳ đề bài hay tài liệu nào, **BẮT BUỘC PHẢI PHÂN BIỆT NGAY ĐÓ LÀ MÔN TOÁN HAY MÔN VẬT LÝ** (qua từ khóa, tiêu đề, nội dung câu hỏi) để đính đúng bản quyền và thông tin giáo viên:

### A. MÔN TOÁN $\longrightarrow$ BẢN QUYỀN CÔ THÚY
- **Tên thương hiệu**: **LỚP TOÁN CÔ THÚY**
- **Giáo viên**: **HỒ THỊ THÚY**
- **Số điện thoại**: **0935.322.328**
- **Địa chỉ**: **50/2C Phạm Thị Liên**
- **Footer (Chân trang)**: `Lớp Toán Cô Thúy -- SĐT: 0935.322.328 -- 50/2C Phạm Thị Liên`

### B. MÔN VẬT LÝ $\longrightarrow$ BẢN QUYỀN THẦY NGỌC (CHỒNG CÔ THÚY)
- **Tên thương hiệu**: **LỚP LÝ THẦY NGỌC**
- **Giáo viên**: **TRẦN VĂN THIỆN NGỌC**
- **Số điện thoại**: **0935216256** (hoặc `0935.216.256`)
- **Hệ thống 3 cơ sở**:
  - **CS1: 50/2C PHẠM THỊ LIÊN**
  - **CS2: P A15 TRƯỜNG THPT NGUYỄN HUỆ**
  - **CS3: 24 ĐẶNG THÁI THÂN**
- **Khối thông tin tiêu đề**:
  ```latex
  {\large\bfseries\color{blue!80!black} LỚP LÝ THẦY NGỌC}\\[2pt]
  \textbf{GV: TRẦN VĂN THIỆN NGỌC -- SĐT: 0935216256}\\[2pt]
  {\scriptsize\textbf{CS1:} 50/2C Phạm Thị Liên -- \textbf{CS2:} P A15 THPT Nguyễn Huệ}\\[1pt]
  {\scriptsize\textbf{CS3:} 24 Đặng Thái Thân}
  ```
- **Footer (Chân trang)**: `Lớp Lý Thầy Ngọc -- SĐT: 0935.216.256 -- CS1: 50/2C Phạm Thị Liên`

---

## 2. QUY ĐỊNH ĐỊNH DẠNG XUẤT BẢN (LATEX VS WORD)
- **MẶC ĐỊNH LUÔN LÀ LATEX**: Tất cả các đề thi, bài tập, hướng dẫn giải đều được biên dịch bằng LaTeX xuất bản ra file PDF vector chất lượng cao (300 DPI, 0 lỗi LaTeX).
- **CHỈ CHUYỂN SANG WORD KHI CÓ YÊU CẦU CỤ THỂ**: Tuyệt đối KHÔNG tự ý chuyển sang Word trừ khi người dùng chỉ định rõ.

---

## 3. TƯƠNG THÍCH TEXSTUDIO (THẦY CÔ TỰ BUILD F5)
- Thầy cô có thể mở trực tiếp các file `.tex` trong **TeXstudio** và nhấn **F5** để build ra PDF ngay mà không bị lỗi.
- Đặt magic comment ở đầu mỗi file wrapper:
  ```latex
  % !TeX program = pdflatex
  ```
- Luôn đảm bảo gói lệnh `ex_test.sty` và các tài nguyên hình ảnh có sẵn trong thư mục làm việc hoặc có đường dẫn tương đối chuẩn xác.

---

## 4. CẤU TRÚC TIÊU ĐỀ (DÙNG TCOLORBOX ĐƠN GIẢN, NGẮN GỌN)
- **Tiêu đề đề thi & HDG dùng `tcolorbox` đơn giản, trang nhã**: Bo góc mềm mại (`arc=3mm`), vách ngăn thanh mảnh giữa cột Thương hiệu và cột Kỳ thi.
- **Ở TIÊU ĐỀ KHÔNG CẦN GHI CÁC CƠ SỞ DẠY, GHI THẬT NGẮN GỌN**:
  - **Cột trái**: Thương hiệu (`\brandname`), Tên giáo viên (`GV: \giaovien`), Số điện thoại (`SĐT: \sdt`).
  - **Cột phải**: Tên kỳ thi, Môn học, Trường (nếu có), Năm học, Thời gian / Mã đề thi.
  - **Bản Đề (Học sinh)**: Có vạch phân cách `\tcbline` và một dòng ngắn gọn: `Họ và tên thí sinh: ... SBD: ... Mã đề thi: ...`
  - **Bản HDG (Giáo viên)**: Tên hướng dẫn giải chi tiết kèm mã đề thi nổi bật.
- Tuyệt đối không nhồi nhét địa chỉ các cơ sở vào tiêu đề để tránh vỡ khung hay rườm rà. Thông tin cơ sở/địa chỉ đã được đặt ở Chân trang (Footer) hoặc Bìa tập sách.

---

## 5. QUY TẮC XỬ LÝ HÌNH ẢNH & ĐỒ THỊ
1. **PDF gốc đã đẹp / vector**:
   - BẮT BUỘC CROP ẢNH TỪ PDF GỐC (độ phân giải cao 300 DPI).
   - TUYỆT ĐỐI KHÔNG TỰ Ý VẼ LẠI BẰNG TIKZ để tránh vẽ sai lệch đồ thị, sai điểm tọa độ hoặc mất nét so với đề gốc.
2. **Bảng biến thiên (BBT)**: Bắt buộc vẽ lại bằng TikZ / `tkz-tab` để chuẩn font chữ.
3. **TikZ hình học/đồ thị**: CHỈ vẽ lại khi PDF gốc là ảnh chụp máy ảnh/điện thoại bị mờ, nghiêng, méo không thể crop sạch.

---

## 6. QUY TẮC XỬ LÝ VĂN BẢN & TÁCH TỪ TIẾNG VIỆT
- **Lỗi chữ dính nhau do font PDF gốc**: Khi trích xuất văn bản từ các tệp PDF gốc, do đặc tính nhúng font chữ hoặc bảng mã, các âm tiết tiếng Việt có dấu rất hay bị dính chùm vào nhau (ví dụ: `sốtuyệt`, `sốtỉđối`, `nhỏnhất`, `trịtrung`, `đolà`, `kếtquả`, `vềnguyên`,...).
- **YÊU CẦU BẮT BUỘC**:
  - Phải kiểm tra, đối chiếu và tách từ sạch sẽ 100%, đảm bảo các từ có đầy đủ dấu cách (space) chuẩn ngữ pháp tiếng Việt.
  - Tuyệt đối KHÔNG ĐỂ SÓT bất kỳ từ dính âm nào trong mã nguồn LaTeX đầu ra.

---

## 7. QUY TẮC ĐỊNH DẠNG `\shortans` TRONG MÔI TRƯỜNG `ex_test`
- **BẮT BUỘC CÓ ĐÚNG 1 DÒNG TRỐNG TRƯỚC `\shortans`**:
  - Trong các câu hỏi trắc nghiệm điền khuyết / trả lời ngắn sử dụng gói `ex_test.sty`, giữa phần kết thúc nội dung văn bản câu hỏi và lệnh `\shortans{...}` **BẮT BUỘC PHẢI CÓ ĐÚNG 1 DÒNG TRỐNG (BLANK LINE)**.
  - **Mục đích**: Tránh việc `\shortans` dính liền dòng text phía trên gây lỗi hiển thị hoặc dính chữ khi biên dịch.
  - **Ví dụ chuẩn**:
    ```latex
    \begin{ex}
    Một học sinh dùng thước chia độ đến milimét để đo chiều dài một chiếc bút chì. Kết quả đo được là bao nhiêu xentimét?

    \shortans{6{,}15\text{ cm}}
    \loigiai{
    ...
    }
    \end{ex}
    ```
