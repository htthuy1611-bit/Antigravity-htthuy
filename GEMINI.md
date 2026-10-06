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
- **ẨN SỐ TRANG SÁCH GỐC Ở TIÊU ĐỀ BẢN HỌC SINH**: Đối với tiêu đề bài học (`\tieudebaihoc`), thông tin số trang sách gốc `(Trang X -- Y)` chỉ hiển thị ở bản Giáo viên, **TUYỆT ĐỐI ẨN HOÀN TOÀN Ở BẢN HỌC SINH** (thông qua toggle macro `\hienthitrang`) để đảm bảo đề bài độc lập, chuyên nghiệp.

---

## 5. QUY TẮC XỬ LÝ HÌNH ẢNH & ĐỒ THỊ
1. **PDF gốc đã đẹp / vector**:
   - BẮT BUỘC CROP ẢNH TỪ PDF GỐC (độ phân giải cao 300 DPI).
   - TUYỆT ĐỐI KHÔNG TỰ Ý VẼ LẠI BẰNG TIKZ để tránh vẽ sai lệch đồ thị, sai điểm tọa độ hoặc mất nét so với đề gốc.
   - **CẮT HÌNH PHẢI CHÍNH XÁC KHUNG HÌNH (BOUNDING BOX)**:
     + Tuyệt đối không cắt lẹm vào hình làm mất trục, mất chữ, mất số hoặc mất nét đồ thị.
     + Tuyệt đối không lấy dư các dòng chữ lý thuyết, đường nét kẻ đứt phân cách, hoặc tiêu đề trang ở bên trên/bên dưới hình vẽ.
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

---

## 8. QUY TẮC CUỐI CÁC PHƯƠNG ÁN (`\choice` & `\choiceTF`): KHÔNG CÓ DẤU CHẤM TRƯỚC `}`
- **Nguyên lý của gói `ex_test.sty`**: Mặc định gói lệnh `ex_test` đã tự động chèn dấu chấm `.` vào cuối mỗi phương án lựa chọn và mệnh đề đúng sai qua lệnh `\dotEX`.
- **YÊU CẦU BẮT BUỘC**:
  - Ở cuối nội dung của TẤT CẢ các phương án trong `\choice` và `\choiceTF`, **TUYỆT ĐỐI KHÔNG ĐƯỢC CÓ DẤU CHẤM `.` TRƯỚC DẤU ĐÓNG NGOẶC `}`** (chỉ có `}` chứ không được `.}`, ví dụ: `{... 19{,}9\text{ mm}}` thay vì `{... 19{,}9\text{ mm}.}`).
  - Nếu để dấu chấm `.` trước `}`, gói lệnh sẽ in ra hai dấu chấm liên tiếp `..` cạnh nhau ở cuối phương án.

---

## 9. QUY TẮC TUYỆT ĐỐI KHÔNG HARDCODE "CHỌN ĐÁP ÁN..." TRONG LỜI GIẢI
- **Nguyên lý của gói `ex_test.sty`**: Gói lệnh đã tự động trích xuất đáp án từ thẻ `\True` và hiển thị khối đáp án chuẩn:
  + Đối với trắc nghiệm 4 phương án: tự động in `Chọn đáp án (A) . . . . . . □`.
  + Đối với Đúng/Sai: tự động in `Chọn đáp án [ a đúng | b sai | c đúng | d sai ] . . . . . . □`.
- **YÊU CẦU BẮT BUỘC**:
  - **TUYỆT ĐỐI KHÔNG ghi thủ công (hardcode) dòng chữ `Chọn đáp án ...` vào trong phần `\loigiai{...}`**.
  - Việc hardcode thủ công sẽ gây trùng lặp 2 lần dòng "Chọn đáp án" trong PDF, đồng thời khi hoán vị/xáo trộn đề (shuffle options), đáp án hardcode sẽ bị sai lệch hoàn toàn so với khóa đáp án.

---

## 10. QUY TẮC LỜI GIẢI CÂU ĐÚNG / SAI (`\choiceTF`): BẮT BUỘC DÙNG `\itemch`
- **Cấu trúc chuẩn**: Trong phần `\loigiai{...}` của câu hỏi Đúng/Sai (`\choiceTF`), **BẮT BUỘC PHẢI DÙNG môi trường `itemchoice` với các lệnh `\itemch`**:
  ```latex
  \loigiai{
  \begin{itemchoice}
      \itemch Lời giải giải thích cho mệnh đề a.
      \itemch Lời giải giải thích cho mệnh đề b.
      \itemch Lời giải giải thích cho mệnh đề c.
      \itemch Lời giải giải thích cho mệnh đề d.
  \end{itemchoice}
  }
  ```
- **Lưu ý**: Lệnh `\itemch` tự động tạo nhãn `a) Đ` hoặc `a) S` dựa trên thuộc tính `\True` của từng ý trong đề bài. Tuyệt đối không gõ thủ công `a) Đ Đúng...` hay `b) S Sai...`.

---

## 11. QUY TẮC LỜI GIẢI CÂU TRẢ LỜI NGẮN (`\shortans`): KHÔNG THỪA DÒNG "ĐÁP ÁN: ..."
- **Nguyên lý của gói `ex_test.sty`**: Lệnh `\shortans{...}` đã tự động tạo dòng kết luận chuẩn: `Đáp án: [Giá trị] . . . . . . □`.
- **YÊU CẦU BẮT BUỘC**:
  - Trong phần `\loigiai{...}` của câu hỏi trả lời ngắn, **TUYỆT ĐỐI KHÔNG ghi thừa dòng `Đáp án: ...`**.
  - Phần lời giải chỉ tập trung trình bày các bước suy luận, công thức và phép tính toán ra kết quả cuối cùng.

---

## 12. QUY TẮC MÃ CÂU HỎI (`\macau{...}`) CHO TẤT CẢ CÂU HỎI, VÍ DỤ, BÀI TẬP
- **YÊU CẦU BẮT BUỘC**:
  - MỌI câu hỏi trắc nghiệm / Đúng--Sai / trả lời ngắn (`\begin{ex}`), MỌI ví dụ mẫu (`Ví dụ`), MỌI bài tập tự luyện sau khi LaTeX hóa **BẮT BUỘC PHẢI CÓ ĐÚNG 1 MÃ CÂU HỎI DUY NHẤT** thông qua macro `\macau{...}`.
  - Cấu trúc mã rõ ràng, dễ nhận biết và tìm kiếm theo bài/chương (ví dụ: `[ID: C1B3-VD01]`, `[ID: C1B3-D1-P1-C01]`, `[ID: C2B1-VD01]`, `[ID: C2B1-D1-P2-C03]`,...).
  - **MÃ CÂU HỎI CHỈ ĐƯỢC HIỂN THỊ Ở BẢN GIÁO VIÊN, HOÀN TOÀN ẨN Ở BẢN HỌC SINH**:
    + Trong wrapper bản Giáo viên (`main_Teacher.tex`):
      ```latex
      \newcommand{\macau}[1]{{\color{blue!80!black}\bfseries\footnotesize [#1]}\space}
      ```
    + Trong wrapper bản Học sinh (`main_Student.tex`):
      ```latex
      \newcommand{\macau}[1]{}
      ```
  - **Vị trí chèn macro `\macau{...}`**:
    + Đối với câu hỏi `\begin{ex}`: Đặt ngay đầu nội dung câu hỏi (hoặc ngay đầu tham số thứ nhất của `\immini`).
    + Đối với ví dụ mẫu: Đặt kèm theo tiêu đề ví dụ (ví dụ: `\noindent\textbf{Ví dụ 1} \macau{ID: C2B1-VD01}: ...`).
  - **Mục đích sử dụng**: Mã câu hỏi này không cần tái sử dụng, mà đóng vai trò làm định danh cố định để khi người dùng yêu cầu: *"Hãy trích xuất các câu có mã câu hỏi sau: ... và biên dịch thành đề mới"*, hệ thống có thể tự động tìm đúng file `.tex`, trích xuất chính xác câu hỏi và xuất bản đề thi theo yêu cầu.

---

## 13. QUY TẮC RESIZE KÍCH THƯỚC HÌNH ẢNH VÀ BỐ CỤC `\immini` NẰM BÊN PHẢI
- **YÊU CẦU RESIZE TẤT CẢ CÁC HÌNH ẢNH**:
  - **TẤT CẢ các hình ảnh** khi chèn vào bài học/câu hỏi/ví dụ **PHẢI ĐƯỢC RESIZE GỌN GÀNG, TINH TẾ**, tuyệt đối không để bất kỳ hình nào quá to làm vỡ trang in hoặc chiếm dụng diện tích trang giấy.
  - **Kích thước chiều rộng chuẩn**:
    + Sơ đồ mũi tên, tam giác nhỏ, hình minh họa đơn giản: `width=1.6cm` -- `2.2cm`.
    + Hình thang máy, vòng tròn, đồ thị nhỏ: `width=2.5cm` -- `3.2cm`.
    + Hệ toạ độ Oxy, bản đồ vị trí, hình khối chi tiết: `width=3.2cm` -- `3.8cm` (tối đa không vượt quá `4.0cm` với hình thông thường).
    + Đối với sơ đồ trục tọa độ dài nằm ngang hoặc hình phong cảnh/trường học dàn hàng ngang: tối đa `5.0cm` -- `7.0cm` (hoặc `width=0.55\linewidth` -- `0.65\linewidth`).
- **QUY TẮC BỐ CỤC `\immini` ĐẶT HÌNH BÊN PHẢI**:
  - Khi câu hỏi/ví dụ có hình minh họa, **BẮT BUỘC DÙNG `\immini{Nội dung bên trái}{Hình ảnh bên phải}`** để hình luôn nằm bên phải và văn bản nằm bên trái.
  - **TUYỆT ĐỐI KHÔNG dùng môi trường `minipage` tự do** bên trong `\begin{ex}` vì nhãn câu (`Câu X.`) sẽ làm tụt dòng hoặc đẩy hình sang trái.
  - **ĐỐI VỚI CÂU HỎI ĐÚNG / SAI (`\choiceTF`)**: BẮT BUỘC chỉ đặt phần dẫn đề vào `\immini`, còn khối `\choiceTF` **PHẢI ĐẶT SAU `\immini`** để các ý a), b), c), d) dàn đều toàn bộ chiều rộng trang giấy (100% full width) và tránh lỗi box của LaTeX.

---

## 14. QUY TẮC XỬ LÝ CÂU HỎI CHÙM (DÙNG CHUNG NGỮ CẢNH / DỮ KIỆN / HÌNH VẼ)
- **Vấn đề cốt lõi**: Trong sách/đề gốc hay có các đoạn dữ kiện chung: *"Sử dụng thông tin sau cho Câu 3 và Câu 4"*, *"Sử dụng dữ kiện sau cho Câu 13 đến Câu 18"*. Nếu ghi cứng (hardcode) số thứ tự như vậy, khi trích xuất hoặc đảo/xáo trộn đề, số câu sẽ bị sai hoàn toàn, đồng thời nếu tách riêng từng câu sẽ bị thiếu dữ kiện.
- **YÊU CẦU BẮT BUỘC**:
  1. **TUYỆT ĐỐI KHÔNG HARDCODE SỐ CÂU**: Xóa bỏ hoàn toàn cụm *"cho Câu X và Câu Y"*, *"cho Câu X đến Câu Y"*.
  2. **DÙNG TIÊU ĐỀ CHUẨN KÈM SỐ CÂU TƯƠNG ĐỐI & MÃ CHÙM `\macauchum{...}`**:
     - Đếm số lượng câu hỏi thuộc chùm (ví dụ $N = 2, 3, 4, 6\dots$).
     - Tiêu chuẩn:
       `\noindent\textbf{Thông tin dùng chung cho N câu hỏi ngay sau} \macauchum{ID: <MÃ_CHÙM>}: <Nội dung ngữ cảnh/dữ kiện chung>`
       (hoặc: `\noindent\textbf{Sử dụng thông tin sau cho N câu hỏi ngay sau} \macauchum{ID: <MÃ_CHÙM>}: <Nội dung>`)
     - Nếu có hình vẽ minh họa cho dữ kiện chùm:
       `\immini{\noindent\textbf{Thông tin dùng chung cho N câu hỏi ngay sau} \macauchum{ID: <MÃ_CHÙM>}: <Nội dung>}{\includegraphics[width=...]{...}}`
     - Tuyệt đối không ghi số thứ tự tuyệt đối (`cho Câu 3 và Câu 4`), mà ghi số lượng câu tương đối (`cho 2 câu hỏi ngay sau`). Khi trích xuất hoặc đảo đề sang bất kỳ vị trí mới nào, lời dẫn vẫn luôn chính xác 100%.
  3. **CẤU TRÚC MÃ CHÙM**:
     - Cấu trúc: `\macauchum{ID: C<Chương>B<Bài>-CH<SốChùm>}` (Ví dụ: `C2B1-CH01`, `C2B1-CH02`,...).
  4. **HIỂN THỊ ĐẶC QUYỀN TRÊN BẢN GIÁO VIÊN, ẨN Ở BẢN HỌC SINH**:
     - Trong `main_Teacher.tex`:
       ```latex
       \newcommand{\macauchum}[1]{{\color{purple!80!black}\bfseries\footnotesize [#1]}\space}
       ```
     - Trong `main_Student.tex`:
       ```latex
       \newcommand{\macauchum}[1]{}
       ```
  5. **MỤC ĐÍCH TRÍCH XUẤT TỰ ĐỘNG**: Khi người dùng yêu cầu trích xuất một câu nằm trong chùm, công cụ trích xuất sẽ tự động lấy kèm khối dữ kiện mang mã `\macauchum` tương ứng, đảm bảo đề thi độc lập không bao giờ bị thiếu dữ kiện ngữ cảnh.
---

## 15. QUY TẮC LỜI GIẢI `\itemch`: TUYỆT ĐỐI CHỈ GHI NỘI DUNG GIẢI THÍCH, KHÔNG THỪA NHÃN `a) ĐÚNG / SAI`
- **Nguyên lý của gói `ex_test.sty`**: Lệnh `\itemch` bên trong môi trường `itemchoice` **ĐÃ TỰ ĐỘNG SINH** nhãn thứ tự và huy hiệu đúng/sai dạng vòng tròn đỏ nổi bật `a) (Đ)` hoặc `a) (S)`.
- **YÊU CẦU BẮT BUỘC**:
  - Sau lệnh `\itemch`, **TUYỆT ĐỐI CHỈ GHI TRỰC TIẾP LỜI GIẢI THÍCH**, KHÔNG ĐƯỢC gõ các tiền tố như: `a) SAI:`, `a) ĐÚNG:`, `b) Đúng.`, `b) Sai.`, `Đúng.`, `Sai.`, `ĐÚNG:`, `SAI:`.
  - **Lý do**: Nếu gõ thêm các tiền tố trên, tài liệu PDF sẽ bị in lặp 2 lần nhãn ngớ ngẩn (ví dụ: `a) (S) a) SAI: ...`). Đồng thời khi hệ thống thực hiện xáo trộn/hoán vị đề (shuffle options), ý `a)` chuyển thành `c)` thì chữ gõ cứng `a)` sẽ làm sai hoàn toàn logic đề thi!
  - **Ví dụ chuẩn 100%**:
    ```latex
    \loigiai{
    \begin{itemchoice}
        \itemch Nội năng của khối khí giảm vì khí thực hiện công lên môi trường ngoài.
        \itemch Theo quy ước dấu của định luật I nhiệt động lực học, nhiệt lượng truyền ra ngoài môi trường nên $Q < 0$.
        \itemch Khối khí nhận công từ ngoại lực tác dụng nén khí nên $A > 0$.
        \itemch Áp suất của khối khí tăng theo định luật Boyle khi thể tích giảm ở nhiệt độ không đổi.
    \end{itemchoice}
    }
    ```

---

## 16. QUY TẮC TUYỆT ĐỐI KHÔNG HARDCODE "Chọn A.", "Chọn B.", "Chọn C.", "Chọn D." TRONG LỜI GIẢI
- **Nguyên lý của gói `ex_test.sty`**: Gói lệnh đã tự động trích xuất đáp án từ thẻ `\True` và hiển thị khối đáp án chuẩn:
  `Chọn đáp án (D) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . □`
- **YÊU CẦU BẮT BUỘC**:
  - Ở cuối nội dung `\loigiai{...}`, **TUYỆT ĐỐI KHÔNG GÕ THÊM** các cụm từ: `Chọn A.`, `Chọn B.`, `Chọn C.`, `Chọn D.`, `Chọn phương án A.`, `Ta chọn B.`,...
  - Xóa bỏ 100% các dòng này khỏi lời giải để tránh trùng lặp 2 lần đáp án và không làm sai lệch khi xáo trộn phương án.

---

## 17. QUY TẮC CÂU TRẢ LỜI NGẮN: BẮT BUỘC DÙNG `\par\shortans[oly]{...}`
- **YÊU CẦU BẮT BUỘC**:
  - Tất cả các câu hỏi trắc nghiệm điền khuyết / trả lời ngắn sử dụng gói `ex_test.sty`, lệnh khai báo đáp án **BẮT BUỘC PHẢI DÙNG ĐÚNG CÚ PHÁP**:
    ```latex
    \par\shortans[oly]{<giá_trị_đáp_án>}
    ```
  - **Giải thích**: 
    + Tiền tố `\par` đảm bảo tách dòng triệt để với phần thân câu hỏi bên trên.
    + Tùy chọn `[oly]` kích hoạt tính năng vẽ 4 ô ly điền số chuẩn theo cấu trúc đề thi tốt nghiệp THPT mới của Bộ Giáo dục & Đào tạo.

---

## 18. QUY TẮC BẢN CHỮA BÀI TRỰC TUYẾN (DÒNG CHẤM CHO GIÁO VIÊN LIVESTREAM / DẠY ONLINE)
- **Mục đích**: Phục vụ Thầy Ngọc chiếu lên màn hình TV hoặc máy chiếu từ xa trong lớp học và phát trực tuyến (Livestream/Online), giúp các bạn ngồi xa ở các góc phòng vẫn thấy to, rõ nét và Thầy có không gian ghi chú, chữa bài.
- **YÊU CẦU BẮT BUỘC**:
  1. **Định dạng khổ giấy**: **Khổ A5 (`a5paper`)** (thay vì A4). Khổ A5 khi chiếu lên màn hình TV tỷ lệ 16:9 sẽ tự động phóng to chữ (zoom to) gấp gần 2 lần so với A4, không bị nhỏ chữ.
  2. **Tất cả các phương án `\choice` chuyển thành `\motcot` (1 cột 4 hàng)**: Cả 4 phương án A, B, C, D phải xếp dọc trên 1 cột 4 hàng để bóp hẹp chiều ngang, tăng kích thước font chữ và tránh bị tràn dòng khi chiếu màn hình xa.
  3. **4 dòng kẻ chấm `\dotfill` CHỈ DÀNH CHO PHẦN TRẢ LỜI NGẮN VÀ TỰ LUẬN**:
     - **TRẮC NGHIỆM ABCD VÀ ĐÚNG/SAI TUYỆT ĐỐI KHÔNG CÓ DÒNG CHẤM**: Thầy khoanh hoặc tích Đ/S trực tiếp trên câu hỏi, không cần dòng kẻ chấm để tránh lãng phí diện tích màn hình TV.
     - **CHỈ CÓ phần Trắc nghiệm trả lời ngắn và Tự luận** mới in 4 dòng kẻ chấm `\dotfill` cách đều nhau `5.5pt` dưới mỗi câu để Thầy viết các bước giải/trình bày.
     - Cơ chế xử lý trong `Master_ChuaBai.tex`: Dùng `\ifcase\chType` để tự động phân loại: `\chType=0` (ABCD) và `\chType=1` (Đúng/Sai) thì bỏ qua dòng chấm (`\par\vspace{1pt}`); các trường hợp còn lại (`\chType=-1` trả lời ngắn, `\chType=9` tự luận) mới in 4 dòng chấm.
  4. **Hiển thị mã câu hỏi màu xanh `\macau{ID: ...}`** và ẩn hoàn toàn đáp án đúng.
---

## 19. QUY TẮC ĐỊNH DẠNG NHÃN PHƯƠNG ÁN (A. B. C. D. VS a) b) c) d)) VÀ FOOTER BẢN CHỮA BÀI
- **PHÂN BIỆT NHÃN PHƯƠNG ÁN RÕ RÀNG**:
  + **Trắc nghiệm nhiều lựa chọn (`\choice`)**: BẮT BUỘC nhãn là chữ cái in hoa kèm dấu chấm: **`A.` `B.` `C.` `D.`**. Tuyệt đối KHÔNG được in nhãn chữ thường `a)` `b)` `c)` `d)` (trong bản chữa bài `Master_ChuaBai.tex` khi chuyển sang `\motcot` bắt buộc phải kích hoạt `\gdef\chType{0}\setcounter{dapan}{0}` để giữ nguyên nhãn `A. B. C. D.`).
  + **CHỈ CÓ trắc nghiệm Đúng/Sai (`\choiceTF` / `itemchoice` / `\itemch`) và các ý câu hỏi Tự luận**: mới được dùng nhãn chữ cái thường đóng ngoặc: **`a)` `b)` `c)` `d)`**.
- **FOOTER BẢN CHỮA BÀI TRỰC TUYẾN A5 CHỈ GHI THÔNG TIN THẦY VÀ TRANG**:
  + Do khổ giấy A5 có chiều ngang hẹp, chân trang (Footer) của bản chữa bài **TUYỆT ĐỐI KHÔNG ghi địa chỉ cơ sở hay tên mã đề dài dòng** tránh bị đè chữ lên số trang.
  + **Định dạng chuẩn chân trang**:
    ```latex
    \lfoot{\scriptsize\textsl{Lớp Lý Thầy Ngọc -- SĐT: 0935.216.256}}
    \rfoot{\scriptsize\textsl{Trang \thepage/\pageref{LastPage}}}
    ```
