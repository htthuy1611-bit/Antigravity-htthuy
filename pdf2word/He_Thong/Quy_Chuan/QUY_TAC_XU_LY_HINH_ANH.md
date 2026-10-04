# QUY TẮC BẮT BUỘC VỀ XỬ LÝ HÌNH ẢNH VÀ ĐỒ THỊ TRONG HỆ THỐNG

> **Quy định được thiết lập theo chỉ đạo của Giáo viên: HỒ THỊ THÚY (Lớp Toán Cô Thúy)**

---

### 1. QUY TẮC CỐT LÕI (BẢN QUYỀN HÌNH ẢNH)

1. **PDF gốc đã đẹp / tài liệu vector rõ nét**:
   - **BẮT BUỘC CROP ẢNH TỪ PDF GỐC** (trích xuất hình ảnh chất lượng cao 300 DPI hoặc crop vector PDF).
   - **TUYỆT ĐỐI KHÔNG TỰ Ý VẼ LẠI BẰNG TIKZ** để tránh vẽ sai lệch đồ thị, sai điểm tọa độ, sai tỉ lệ hoặc mất nét so với đề gốc.
   - Sử dụng lệnh `\includegraphics` trong LaTeX và chèn ảnh tương ứng vào Word.

2. **Bảng biến thiên (BBT)**:
   - **BẮT BUỘC VẼ LẠI** bằng TikZ / `tkz-tab` hoặc kẻ bảng chuẩn để công thức toán học và văn bản hiển thị sắc nét, đồng bộ font chữ chuẩn của tài liệu.

3. **Chỉ vẽ lại bằng TikZ khi nào?**:
   - **CHỈ CÓ các file PDF được gộp lại từ các ảnh CHỤP từ máy ảnh** (ảnh chụp điện thoại, máy ảnh bị mờ, méo, nghiêng, vỡ hạt, bóng mờ không thể crop sạch) thì **MỚI vẽ lại bằng TikZ**.

---

### 2. QUY TRÌNH THỰC HIỆN KHI CÓ HÌNH ẢNH
1. Kiểm tra nguồn PDF:
   - Nếu là PDF vector / file in: Dùng PyMuPDF (`fitz`) crop chính xác vùng chứa hình ảnh với độ phân giải cao (`Matrix(4, 4)` ~ 300 DPI), lưu vào thư mục `He_Thong/Hinh_Anh/` hoặc thư mục bài học.
   - Nếu là Bảng biến thiên: Dựng TikZ chuẩn theo cấu trúc mũi tên và giới hạn hàm số.
2. Kiểm tra trực quan (visual inspection) trước khi xuất bản bản Đề và Hướng dẫn giải.
