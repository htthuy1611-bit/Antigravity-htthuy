# BẢNG QUY TẮC BẮT BUỘC HỆ THỐNG - GHI NHỚ VĨNH VIỄN

> **LƯU Ý ĐẶC BIỆT**: Toàn bộ hệ thống, các Script tự động và các Agent phải tuân thủ nghiêm ngặt bảng quy tắc này trong mọi hoàn cảnh.

---

## 1. PHÂN BIỆT MÔN HỌC & BẢN QUYỀN GIÁO VIÊN

Khi nhận 1 đề mới đưa lên, **BẮT BUỘC PHẢI PHÂN BIỆT ĐƯỢC ĐÓ LÀ MÔN TOÁN HAY MÔN VẬT LÝ** để đính đúng bản quyền và thông tin giáo viên:

| Thuộc tính | MÔN TOÁN $\longrightarrow$ CÔ THÚY | MÔN VẬT LÝ $\longrightarrow$ THẦY NGỌC |
| :--- | :--- | :--- |
| **Giáo viên** | **HỒ THỊ THÚY** | **TRẦN VĂN THIỆN NGỌC** (Chồng Cô Thúy) |
| **Thương hiệu** | **LỚP TOÁN CÔ THÚY** | **LỚP LÝ THẦY NGỌC** |
| **Số điện thoại** | **0935.322.328** | **0935216256** (hoặc `0935.216.256`) |
| **Địa chỉ / Cơ sở** | **50/2C Phạm Thị Liên** | **CS1:** 50/2C PHẠM THỊ LIÊN<br>**CS2:** P A15 TRƯỜNG THPT NGUYỄN HUỆ<br>**CS3:** 24 ĐẶNG THÁI THÂN |
| **Footer (Chân trang)** | `Lớp Toán Cô Thúy -- SĐT: 0935.322.328 -- 50/2C Phạm Thị Liên` | `Lớp Lý Thầy Ngọc -- SĐT: 0935.216.256 -- CS1: 50/2C Phạm Thị Liên` |

---

## 2. QUY ĐỊNH ĐỊNH DẠNG XUẤT BẢN
1. **MẶC ĐỊNH LUÔN LÀ LATEX**:
   - Mọi tài liệu đề thi, bài giảng, hướng dẫn giải đều xuất bản bằng LaTeX.
   - Biên dịch 2 lượt `pdflatex` đạt chuẩn 0 lỗi, xuất file PDF vector sắc nét.
2. **CHỈ CHUYỂN SANG WORD KHI ĐƯỢC YÊU CẦU**:
   - Tuyệt đối KHÔNG tự ý chuyển sang Word trừ khi người dùng có yêu cầu rõ ràng.

---

## 3. TƯƠNG THÍCH TEXSTUDIO (THẦY CÔ TỰ BUILD F5)
- Thầy cô có thể mở trực tiếp các file `.tex` trong **TeXstudio** và nhấn **F5** để build ra PDF ngay mà không bị lỗi.
- Đặt magic comment ở đầu mỗi file wrapper:
  ```latex
  % !TeX program = pdflatex
  ```
- Luôn đảm bảo gói lệnh `ex_test.sty` và các tài nguyên hình ảnh có sẵn trong thư mục làm việc hoặc có đường dẫn tương đối chuẩn xác.

---

## 4. DÙNG MACRO ĐỂ SỬA TIÊU ĐỀ LINH HOẠT
- Sử dụng các Macro trong `Master_De.tex` và `Master_HDG.tex` để dễ dàng đổi thông tin:
  - `\brandname`: Tên thương hiệu hiển thị
  - `\giaovien`: Tên giáo viên
  - `\sdt`: Số điện thoại
  - `\diachi`: Địa chỉ
  - `\brandinfo`: Khối thông tin chi tiết (dành cho nhiều cơ sở)
  - `\brand`: Thông tin bản quyền footer

---

## 5. QUY TẮC XỬ LÝ HÌNH ẢNH
1. **PDF gốc rõ nét / vector**: **BẮT BUỘC CROP ẢNH** từ PDF gốc (độ phân giải cao 300 DPI), **KHÔNG TỰ Ý VẼ LẠI BẰNG TIKZ**.
2. **Bảng biến thiên (BBT)**: Bắt buộc vẽ lại bằng TikZ / `tkz-tab`.
3. **TikZ hình học/đồ thị**: CHỈ vẽ lại khi PDF gốc là ảnh chụp máy ảnh/điện thoại bị mờ, nghiêng, méo không thể crop sạch.
