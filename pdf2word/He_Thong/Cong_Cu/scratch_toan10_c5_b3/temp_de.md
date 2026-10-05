
\begin{center}
	{\Large\bfseries\color{blue!80!black} CHƯƠNG V. CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM}\\[6pt]
	{\large\bfseries\color{red!80!black} BÀI 3. CÁC SỐ ĐẶC TRƯNG ĐO ĐỘ PHÂN TÁN}
\end{center}




# I. TÓM TẮT LÝ THUYẾT





## 1. Khoảng biến thiên và khoảng tứ phân vị



	
-  **Khoảng biến thiên** (kí hiệu là $R$): là hiệu số giữa giá trị lớn nhất và giá trị nhỏ nhất trong mẫu số liệu:
	\[R = x_{\max} - x_{\min}.\]
	Khoảng biến thiên càng lớn thì mẫu số liệu càng phân tán.
	
-  **Khoảng tứ phân vị** (kí hiệu là $\Delta_Q$): là hiệu số giữa tứ phân vị thứ ba và tứ phân vị thứ nhất:
	\[\Delta_Q = Q_3 - Q_1.\]
	Khoảng tứ phân vị đo độ phân tán của $50\%$ số liệu chính giữa của mẫu số liệu và không bị ảnh hưởng bởi các giá trị bất thường.




## 2. Phương sai và độ lệch chuẩn



	
-  Cho mẫu số liệu $x_1, x_2, \ldots, x_n$ có số trung bình là $\overline{x}$.
	
-  **Phương sai** (kí hiệu là $s^2$):
	\[s^2 = \frac{(x_1 - \overline{x})^2 + (x_2 - \overline{x})^2 + \cdots + (x_n - \overline{x})^2}{n} = \frac{1}{n}\sum_{i=1}^n x_i^2 - (\overline{x})^2.\]
	Đối với bảng phân bố tần số:
	\[s^2 = \frac{\sum_{i=1}^k n_i (x_i - \overline{x})^2}{n} = \frac{1}{n}\sum_{i=1}^k n_i x_i^2 - (\overline{x})^2.\]
	
-  **Độ lệch chuẩn** (kí hiệu là $s$): là căn bậc hai số học của phương sai:
	\[s = \sqrt{s^2}.\]
	
-  **Ý nghĩa:** Phương sai và độ lệch chuẩn đo mức độ biến động, phân tán của các số liệu xung quanh giá trị trung bình. Giá trị $s^2$ và $s$ càng lớn thì số liệu càng phân tán. Độ lệch chuẩn có cùng đơn vị đo với đại lượng đang nghiên cứu.




## 3. Phát hiện số liệu bất thường bằng biểu đồ hộp



	
-  Giá trị $x$ trong mẫu số liệu được gọi là **giá trị bất thường** nếu:
	\[x < Q_1 - 1{,}5\Delta_Q \quad \text{hoặc} \quad x > Q_3 + 1{,}5\Delta_Q.\]
	Tức là $x$ không thuộc đoạn $[Q_1 - 1{,}5\Delta_Q; Q_3 + 1{,}5\Delta_Q]$.





# II. CÁC DẠNG TOÁN VÀ VÍ DỤ MINH HỌA





## Dạng 1. Tìm khoảng biến thiên và so sánh độ phân tán





**Ví dụ 1.** 
	Cân nặng (kg) của 10 học sinh: $49;\; 57;\; 66;\; 45;\; 50;\; 41;\; 57;\; 42;\; 55;\; 52$. Tìm khoảng biến thiên của mẫu số liệu.
	





**Câu 1.** 
	Hai chữ số cuối giải đặc biệt Xổ số miền Bắc trong 9 ngày được ghi lại như sau: $16;\; 11;\; 25;\; 28;\; 45;\; 42;\; 24;\; 33;\; 11$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	

@@TAB@@**A.** $18$@@TAB@@**B.** $34$@@TAB@@**C.** $56$@@TAB@@**D.** $27$






**Câu 2.** 
	Mẫu số liệu nào dưới đây có khoảng biến thiên là 13?
	

@@TAB@@**A.** $11, 28, 56, 12$@@TAB@@**B.** $6, 12, 33, 23, 11$@@TAB@@**C.** $25, 9, 13, 10$ (Wait: $25 - 9 = 16$. Kiểm tra tất cả các mẫu)@@TAB@@**D.** Tất cả đều sai






**Câu 3.** 
	Mẫu số liệu nào dưới đây có khoảng biến thiên là 53?
	

@@TAB@@**A.** $18, 57, 11, 26$@@TAB@@**B.** $44, 2, 55, 46, 27$@@TAB@@**C.** $21, 3, 55, 89$@@TAB@@**D.** $4, 16, 23, 20$






**Câu 4.** 
	Số lượng học sinh có điểm Toán tổng kết cuối học kì I trên 8 ở mỗi lớp của một trường:
	\[16;\; 11;\; 15;\; 18;\; 21;\; 12;\; 24;\; 23;\; 11;\; 8;\; 9;\; 11;\; 6;\; 27;\; 22;\; 20;\; 35;\; 18.\]
	Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	

@@TAB@@**A.** $11$@@TAB@@**B.** $29$@@TAB@@**C.** $37$@@TAB@@**D.** $25$






**Câu 5.** 
	Hãy tìm khoảng biến thiên của mẫu số liệu thống kê được cho ở bảng sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|}
		\hline
		Giá trị & 6 & 7 & 8 & 9 & 10 \\
		\hline
		Tần số & 15 & 18 & 11 & 32 & 19 \\
		\hline
	\end{tabular}
	\end{center}
	

@@TAB@@**A.** $4$@@TAB@@**B.** $5$@@TAB@@**C.** $6$@@TAB@@**D.** $7$






**Câu 6.** 
	Sải cánh (cm) của 90 con chim sẻ được thống kê:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|}
		\hline
		Sải cánh & 18 & 19 & 20 & 21 & 22 & 23 & 24 \\
		\hline
		Số lượng & 6 & 11 & 19 & 20 & 15 & 12 & 7 \\
		\hline
	\end{tabular}
	\end{center}
	Khoảng biến thiên là
	

@@TAB@@**A.** $5$@@TAB@@**B.** $6$@@TAB@@**C.** $7$@@TAB@@**D.** $8$






**Câu 7.** 
	Nhiệt độ cao nhất trong tuần ($^\circ\text{C}$) tại hai thành phố:
	
		
-  Hà Nội: $28;\; 27;\; 30;\; 29;\; 27;\; 24;\; 25$.
		
-  TP Hồ Chí Minh: $31;\; 33;\; 32;\; 33;\; 29;\; 32;\; 34$.
	
	Dựa vào khoảng biến thiên của hai mẫu số liệu, hãy chỉ ra mẫu số liệu nào có độ phân tán lớn hơn.
	

@@TAB@@**A.** Mẫu số liệu "Hà Nội" có độ phân tán lớn hơn mẫu số liệu "TP Hồ Chí Minh"@@TAB@@**B.** Mẫu số liệu "TP Hồ Chí Minh" có độ phân tán lớn hơn mẫu số liệu "Hà Nội"@@TAB@@**C.** Hai mẫu số liệu có độ phân tán bằng nhau@@TAB@@**D.** Tất cả đều sai






**Câu 8.** 
	Tuổi của những đứa trẻ:
	
		
-  Nam: $10;\; 4;\; 1;\; 6;\; 2;\; 8;\; 5$.
		
-  Nữ: $2;\; 3;\; 6;\; 4;\; 1;\; 7$.
	
	Dựa vào khoảng biến thiên, mẫu số liệu nào có độ phân tán lớn hơn?
	

@@TAB@@**A.** Mẫu số liệu "Nam" có độ phân tán lớn hơn mẫu số liệu "Nữ"@@TAB@@**B.** Mẫu số liệu "Nữ" có độ phân tán lớn hơn mẫu số liệu "Nam"@@TAB@@**C.** Hai mẫu số liệu có độ phân tán bằng nhau@@TAB@@**D.** Tất cả đều sai






**Câu 9.** 
	Chỉ số IQ và EQ của một nhóm học sinh:
	
		
-  IQ: $95;\; 110;\; 90;\; 105;\; 88;\; 100;\; 111$.
		
-  EQ: $90;\; 105;\; 98;\; 100;\; 93;\; 96;\; 103$.
	
	Dựa vào khoảng biến thiên, mẫu nào có độ phân tán lớn hơn?
	

@@TAB@@**A.** Mẫu số liệu "IQ" có độ phân tán lớn hơn mẫu số liệu "EQ"@@TAB@@**B.** Mẫu số liệu "EQ" có độ phân tán lớn hơn mẫu số liệu "IQ"@@TAB@@**C.** Hai mẫu số liệu có độ phân tán bằng nhau@@TAB@@**D.** Tất cả đều sai






**Câu 10.** 
	Độ lệch chuẩn là
	

@@TAB@@**A.** Bình phương của phương sai@@TAB@@**B.** Một nửa của phương sai@@TAB@@**C.** Căn bậc hai của phương sai@@TAB@@**D.** Căn bậc ba của phương sai






**Câu 11.** 
	Đại lượng đo mức độ biến động, chênh lệch giữa các giá trị trong mẫu số liệu thống kê gọi là
	

@@TAB@@**A.** Độ lệch chuẩn@@TAB@@**B.** Số trung vị@@TAB@@**C.** Phương sai@@TAB@@**D.** Tần số






**Câu 12.** 
	Cho dãy số liệu thống kê: $1, 2, 3, 4, 5, 6, 7, 8$. Độ lệch chuẩn của dãy số liệu gần bằng
	

@@TAB@@**A.** $2{,@@TAB@@**B.** $3{,@@TAB@@**C.** $4{,@@TAB@@**D.** $5{,






**Câu 13.** 
	Cho mẫu số liệu $\{10, 8, 6, 2, 4\}$. Độ lệch chuẩn của mẫu là
	

@@TAB@@**A.** $2{,@@TAB@@**B.** $8$@@TAB@@**C.** $6$@@TAB@@**D.** $2{,






**Câu 14.** 
	Cho mẫu số liệu thống kê $\{2, 4, 6, 8, 10\}$. Phương sai của mẫu số liệu trên là bao nhiêu?
	

@@TAB@@**A.** $6$@@TAB@@**B.** $8$@@TAB@@**C.** $10$@@TAB@@**D.** $40$






**Câu 15.** 
	Số ô tô đi qua một cây cầu trong một tuần đếm được như sau: $83;\; 74;\; 71;\; 79;\; 83;\; 69;\; 92$. Phương sai và độ lệch chuẩn lần lượt là
	

@@TAB@@**A.** $78{,@@TAB@@**B.** ,@@TAB@@**C.** $52{,@@TAB@@**D.** ,






**Câu 16.** 
	Tiền thưởng (triệu đồng) cho 43 cán bộ nhân viên:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Tiền thưởng ($x$) & 2 & 3 & 4 & 5 & 6 & \\
		\hline
		Tần số ($n$) & 5 & 15 & 10 & 6 & 7 & $n = 43$ \\
		\hline
	\end{tabular}
	\end{center}
	Phương sai là
	

@@TAB@@**A.** $1{,@@TAB@@**B.** $1{,@@TAB@@**C.** $1{,@@TAB@@**D.** $1{,






**Câu 17.** 
	Độ lệch chuẩn của bảng phân bố tần số tiền thưởng ở Câu 17 là
	

@@TAB@@**A.** $1{,@@TAB@@**B.** $1{,@@TAB@@**C.** $1{,@@TAB@@**D.** $1{,






**Câu 18.** 
	Điểm thi Toán lớp 10A được trình bày trong bảng tần số sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|}
		\hline
		Điểm thi ($x$) & 6 & 7 & 8 & 9 & \\
		\hline
		Tần số ($n$) & 8 & 18 & 10 & 4 & $n = 40$ \\
		\hline
	\end{tabular}
	\end{center}
	Độ lệch chuẩn là
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,






**Câu 19.** 
	Cho dãy số liệu thống kê: $38;\; 18;\; 20;\; 25;\; 18;\; 15;\; 20;\; 22;\; 31$. Phương sai của dãy số liệu trên là
	

@@TAB@@**A.** $47{,@@TAB@@**B.** $50$@@TAB@@**C.** $42$@@TAB@@**D.** $43$






**Câu 20.** 
	Trên con đường A, tốc độ 30 ô tô được ghi lại trong bảng tần số:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		Vận tốc & 60 & 62 & 63 & 65 & 68 & 69 & 70 & 73 & 75 & 76 & 80 & 82 & 83 & 84 & 85 & 88 & 90 \\
		\hline
		Tần số & 2 & 2 & 1 & 2 & 3 & 1 & 2 & 2 & 3 & 2 & 3 & 1 & 1 & 2 & 1 & 1 & 1 \\
		\hline
	\end{tabular}
	\end{center}
	Phương sai của tốc độ ô tô trên con đường A là
	

@@TAB@@**A.** $74{,@@TAB@@**B.** $75{,@@TAB@@**C.** $73{,@@TAB@@**D.** $72{,






**Câu 21.** 
	Độ lệch chuẩn của tốc độ ô tô ở Câu 21 là
	

@@TAB@@**A.** $8{,@@TAB@@**B.** $8{,@@TAB@@**C.** $8{,@@TAB@@**D.** $8{,






**Câu 22.** 
	Số lượng khách đến điểm du lịch trong 12 tháng:
	\[430;\; 550;\; 430;\; 520;\; 550;\; 515;\; 550;\; 110;\; 520;\; 430;\; 550;\; 880.\]
	Độ lệch chuẩn là
	

@@TAB@@**A.** $567{,@@TAB@@**B.** $163{,@@TAB@@**C.** $171{,@@TAB@@**D.** $147{,






**Câu 23.** 
	Một mẫu số liệu thống kê có các tứ phân vị: $Q_1 = 22, Q_2 = 27, Q_3 = 32$. Giá trị nào sau đây là giá trị bất thường của mẫu số liệu?
	

@@TAB@@**A.** $30$@@TAB@@**B.** $8$@@TAB@@**C.** $6$@@TAB@@**D.** $46$






**Câu 24.** 
	Hãy tìm các giá trị bất thường của mẫu số liệu: $7;\; 19;\; 6;\; 12;\; 5;\; 17;\; 6;\; 13$.
	

@@TAB@@**A.** $5; 6$@@TAB@@**B.** $5; 6; 19$@@TAB@@**C.** Không có số liệu bất thường@@TAB@@**D.** $5; 19$






**Câu 25.** 
	Hãy tìm các giá trị bất thường của mẫu số liệu: $20;\; 52;\; 86;\; 80;\; 44;\; 49;\; 57;\; 41;\; 44;\; 55$.
	

@@TAB@@**A.** $80; 86$@@TAB@@**B.** $41; 80; 86$@@TAB@@**C.** $80; 20; 86$@@TAB@@**D.** $86$






**Câu 26.** 
	Một mẫu số liệu có $Q_1 = 53, Q_2 = 55, Q_3 = 61$. Giá trị nào sau đây không phải là giá trị bất thường?
	

@@TAB@@**A.** $42$ (hoặc $73$ tuỳ đề. Kiểm tra đoạn:)@@TAB@@**B.** $80$@@TAB@@**C.** $73$@@TAB@@**D.** $73{,






**Câu 27.** 
	Mẫu số liệu có $Q_1 = 3, Q_2 = 7, Q_3 = 12$. Giá trị nào là giá trị bất thường?
	

@@TAB@@**A.** $22$@@TAB@@**B.** $-8{,@@TAB@@**C.** $26$@@TAB@@**D.** $25{,






**Câu 28.** 
	Tìm các giá trị bất thường của mẫu số liệu:
	\[10;\; 59;\; 67;\; 72;\; 73;\; 76;\; 88;\; 92;\; 106;\; 111;\; 115;\; 169.\]
	

@@TAB@@**A.** $169$@@TAB@@**B.** $115; 169$@@TAB@@**C.** $111; 169$@@TAB@@**D.** $10; 169$






**Câu 29.** 
	Cho mẫu số liệu thống kê: $-3;\; 5;\; 10;\; 12;\; 14;\; 18;\; 24;\; 26;\; 49;\; 60$. Phát biểu nào sau đây là đúng?
	

@@TAB@@**A.** $-3$ là giá trị bất thường duy nhất@@TAB@@**B.** $60$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**D.** Mẫu số liệu có nhiều giá trị bất thường






**Câu 30.** 
	Cho mẫu số liệu: $10;\; 21;\; 21;\; 23;\; 25;\; 26;\; 28;\; 42$. Phát biểu nào sau đây là đúng?
	

@@TAB@@**A.** $10$ là giá trị bất thường duy nhất@@TAB@@**B.** $42$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**D.** Mẫu số liệu có nhiều giá trị bất thường






**Câu 31.** 
	Cho mẫu số liệu: $52;\; 47;\; 55;\; 81;\; 61;\; 49;\; 59$. Phát biểu nào đúng?
	

@@TAB@@**A.** $81$ là giá trị bất thường duy nhất@@TAB@@**B.** $47$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường@@TAB@@**D.** Có nhiều giá trị bất thường






**Câu 32.** 
	Cho mẫu số liệu: $8;\; 10;\; 13;\; 13;\; 14;\; 16;\; 27$. Phát biểu nào đúng?
	

@@TAB@@**A.** $8$ là giá trị bất thường duy nhất@@TAB@@**B.** $27$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường@@TAB@@**D.** Có nhiều giá trị bất thường






**Câu 33.** 
	Cho mẫu số liệu: $44;\; 51;\; 36;\; 19;\; 40;\; 69;\; 49;\; 46$. Phát biểu nào đúng?
	

@@TAB@@**A.** $19$ là giá trị bất thường duy nhất@@TAB@@**B.** $69$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**D.** Mẫu số liệu có nhiều giá trị bất thường






**Câu 34.** 
	Cho mẫu số liệu: $20;\; 22;\; 22;\; 25;\; 28;\; 32;\; 34;\; 43$. Phát biểu nào đúng?
	

@@TAB@@**A.** $20$ là giá trị bất thường duy nhất@@TAB@@**B.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**C.** $43$ là giá trị bất thường duy nhất@@TAB@@**D.** Có nhiều giá trị bất thường






**Câu 35.** 
	Cho dãy số liệu thống kê: $1, 2, 3, 4, 5, 6, 7$. Phương sai của các số liệu thống kê đã cho là
	

@@TAB@@**A.** $1$@@TAB@@**B.** $2$@@TAB@@**C.** $3$@@TAB@@**D.** $4$






**Câu 36.** 
	Sản lượng lúa (tạ) của 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6). Tính độ lệch chuẩn.
	

@@TAB@@**A.** $s \approx 1{,@@TAB@@**B.** (tạ)@@TAB@@**C.** $s \approx 1{,@@TAB@@**D.** (tạ)






**Câu 37.** 
	Tiền thưởng (triệu đồng) cho 43 cán bộ nhân viên: 2 (5), 3 (15), 4 (10), 5 (6), 6 (7). Tính độ lệch chuẩn.
	

@@TAB@@**A.** $s \approx 1{,@@TAB@@**B.** (triệu đồng)@@TAB@@**C.** $s \approx 1{,@@TAB@@**D.** (triệu đồng)






**Câu 38.** 
	Cho dãy số liệu: $1, 2, 3, 4, 5, 6, 7$. Tìm khoảng biến thiên của mẫu số liệu.
	

@@TAB@@**A.** $R = 7$@@TAB@@**B.** $R = 4$@@TAB@@**C.** $R = 8$@@TAB@@**D.** $R = 6$






**Câu 39.** 
	Giá trị thành phẩm của 7 công nhân: $180, 190, 190, 200, 210, 210, 220$. Tìm khoảng tứ phân vị của mẫu số liệu.
	

@@TAB@@**A.** $190$@@TAB@@**B.** $20$@@TAB@@**C.** $210$@@TAB@@**D.** $200$






**Câu 40.** 
	Tiền thưởng (triệu đồng) có bảng tần số: 2 (5), 3 (15), 4 (10), 5 (6), 6 (7). Phương sai thuộc khoảng nào?
	

@@TAB@@**A.** $(4{,@@TAB@@**B.** ,@@TAB@@**C.** $(4{,@@TAB@@**D.** ,






**Câu 41.** 
	Khách du lịch 12 tháng: 430, 560, 450, 550, 760, 430, 525, 110, 635, 450, 800, 950. Tính độ lệch chuẩn $s$.
	

@@TAB@@**A.** $s \approx 211$@@TAB@@**B.** $s \approx 209{,@@TAB@@**C.** $s \approx 403{,@@TAB@@**D.** $s \approx 207{,






**Câu 42.** 
	Độ lệch chuẩn bằng
	

@@TAB@@**A.** bình phương của phương sai@@TAB@@**B.** căn bậc hai số học của phương sai@@TAB@@**C.** một nửa của phương sai@@TAB@@**D.** hai lần phương sai






**Câu 43.** 
	Sản lượng lúa 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6). Tính khoảng tứ phân vị của mẫu số liệu.
	

@@TAB@@**A.** $3$@@TAB@@**B.** $4$@@TAB@@**C.** $2$ (hoặc $1$)@@TAB@@**D.** $s^2$






**Câu 44.** 
	Chọn khẳng định sai trong các khẳng định sau:
	

@@TAB@@**A.** Phương sai luôn là một số không âm@@TAB@@**B.** Phương sai không có đơn vị@@TAB@@**C.** Phương sai càng lớn thì độ phân tán càng lớn@@TAB@@**D.** Độ lệch chuẩn càng lớn thì độ phân tán càng lớn






**Câu 45.** 
	100 học sinh thi HSG Toán: Điểm từ 9 đến 19. Tính độ lệch chuẩn.
	

@@TAB@@**A.** $s \approx 1{,@@TAB@@**B.** (điểm)@@TAB@@**C.** $s \approx 1{,@@TAB@@**D.** (điểm)






**Câu 46.** 
	Tuổi 30 bệnh nhân đau mắt hột: từ 12 đến 25 tuổi. Tính khoảng biến thiên của mẫu số liệu.
	

@@TAB@@**A.** $25$@@TAB@@**B.** $13$@@TAB@@**C.** $26$@@TAB@@**D.** $12$






**Câu 47.** 
	Điểm trung bình các môn của An và Bình: An có điểm dao động từ 7 đến 9, Bình có điểm dao động từ 5 đến 10. Hỏi ai "học lệch" hơn?
	

@@TAB@@**A.** An@@TAB@@**B.** Bình@@TAB@@**C.** Mức độ học lệch của hai người như nhau@@TAB@@**D.** Chưa đủ cơ sở kết luận






**Câu 48.** 
	Số sách đọc trong năm: 1 (10), 2 ($x$), 3 (8), 4 (6), 5 ($y$), 6 (3). Tổng: 40. Biết $s^2 \approx 2{,}52$. Tính $x$ và $y$.
	

@@TAB@@**A.** $x = 7, y = 6$@@TAB@@**B.** $x = 6, y = 7$@@TAB@@**C.** $x = 8, y = 5$@@TAB@@**D.** $x = 5, y = 8$






**Câu 49.** 
	Cho dãy số liệu: $x, 21, 22, 23, 24, y$. Tìm $x, y$ biết số trung bình cộng bằng $22{,}5$ và khoảng biến thiên bằng 5.
	

@@TAB@@**A.** $x = -25$ và $y = -20$@@TAB@@**B.** $x = -20$ và $y = -25$@@TAB@@**C.** $x = 20$ và $y = 25$@@TAB@@**D.** $x = 25$ và $y = 20$








## PHẦN II. CÂU HỎI TỰ LUẬN


*\small (Học sinh trình bày chi tiết lời giải các bài toán sau)*


**Bài 1.** 
	Hai chữ số cuối số điện thoại của 10 người: $23;\; 58;\; 42;\; 11;\; 69;\; 50;\; 13;\; 57;\; 61;\; 72$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	\loigiai{
		Giá trị lớn nhất là $72$, giá trị nhỏ nhất là $11$.\\
		Khoảng biến thiên: $R = x_{\max} - x_{\min} = 72 - 11 = 61$.
	}





**Bài 2.** 
	Tuổi thọ trung bình người dân của 11 nước: $69;\; 77;\; 75;\; 83;\; 65;\; 75;\; 74;\; 68;\; 73;\; 72;\; 71$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	\loigiai{
		Giá trị lớn nhất là $83$, nhỏ nhất là $65$.\\
		Khoảng biến thiên: $R = 83 - 65 = 18\text{ (tuổi)}$.
	}





**Bài 3.** 
	Thời gian làm câu đầu tiên trong đề thi tuyển sinh vào lớp 10 của học sinh:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|}
		\hline
		Thời gian (phút) & 9 & 10 & 11 & 12 & 13 & 14 & 15 \\
		\hline
		Số lượng học sinh & 45 & 46 & 57 & 63 & 70 & 61 & 50 \\
		\hline
	\end{tabular}
	\end{center}
	Hãy tìm khoảng biến thiên của mẫu số liệu thống kê trên.
	\loigiai{
		Thời gian làm bài lớn nhất là $15\text{ phút}$, nhỏ nhất là $9\text{ phút}$.\\
		Khoảng biến thiên: $R = 15 - 9 = 6\text{ (phút)}$.
	}





**Bài 4.** 
	Điểm thi học kì 2 môn Toán và Ngữ văn của một nhóm học sinh:
	
		
-  Toán: $9;\; 8{,}5;\; 7;\; 6{,}3;\; 5;\; 9{,}5;\; 8$.
		
-  Ngữ văn: $6;\; 6{,}5;\; 8;\; 7{,}3;\; 5{,}5;\; 8{,}3;\; 6{,}5$.
	
	Hãy tìm khoảng biến thiên của hai mẫu số liệu trên. Từ đó chỉ ra mẫu số liệu có độ phân tán lớn hơn.
	\loigiai{
		- Môn Toán: $x_{\max} = 9{,}5; x_{\min} = 5 \implies R_{\text{Toán}} = 9{,}5 - 5 = 4{,}5$.\\
		- Môn Ngữ văn: $x_{\max} = 8{,}3; x_{\min} = 5{,}5 \implies R_{\text{Văn}} = 8{,}3 - 5{,}5 = 2{,}8$.\\
		Vì $R_{\text{Toán}} = 4{,}5 > 2{,}8 = R_{\text{Văn}}$ nên mẫu số liệu điểm môn Toán có độ phân tán lớn hơn môn Ngữ văn.
	}





**Bài 5.** 
	Số giờ nắng và độ ẩm (\%) trung bình hàng tháng của Hà Nội:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		Số giờ nắng & 74 & 47 & 47 & 90 & 183 & 172 & 195 & 174 & 176 & 167 & 137 & 124 \\
		\hline
		Độ ẩm (\%) & 83,4 & 87,9 & 89,4 & 86,5 & 82,9 & 82,2 & 85,9 & 87,2 & 84,2 & 81,9 & 81,3 & 82,0 \\
		\hline
	\end{tabular}
	\end{center}
	Hãy tìm khoảng biến thiên của hai mẫu số liệu và chỉ ra mẫu có độ phân tán lớn hơn.
	\loigiai{
		- Số giờ nắng: Giá trị lớn nhất là $195$, nhỏ nhất là $47 \implies R_{\text{nắng}} = 195 - 47 = 148\text{ (giờ)}$.\\
		- Độ ẩm: Giá trị lớn nhất là $89{,}4\%$, nhỏ nhất là $81{,}3\% \implies R_{\text{ẩm}} = 89{,}4 - 81{,}3 = 8{,}1\%$.\\
		Do đó, số giờ nắng có khoảng biến thiên rất lớn, độ phân tán giữa các tháng trong năm lớn hơn nhiều so với độ ẩm.
	}





**Bài 6.** 
	Một xạ thủ bắn 30 viên đạn vào bia:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Điểm & 6 & 7 & 8 & 9 & 10 & \\
		\hline
		Tần số & 3 & 4 & 8 & 9 & 6 & $n = 30$ \\
		\hline
	\end{tabular}
	\end{center}
	a) Tính điểm trung bình của xạ thủ.\\
	b) Tìm phương sai và độ lệch chuẩn.
	\loigiai{
		a) Điểm trung bình:
		\[\overline{x} = \frac{6 \cdot 3 + 7 \cdot 4 + 8 \cdot 8 + 9 \cdot 9 + 10 \cdot 6}{30} = \frac{18 + 28 + 64 + 81 + 60}{30} = \frac{251}{30} \approx 8{,}37\text{ (điểm)}.\]
		b) Phương sai:
		\[s^2 = \frac{1}{30}\sum n_i x_i^2 - (\overline{x})^2 = \frac{2147}{30} - (8{,}3667)^2 \approx 71{,}5667 - 70{,}0017 = 1{,}565.\]
		Độ lệch chuẩn:
		\[s = \sqrt{1{,}565} \approx 1{,}25\text{ (điểm)}.\]
	}





**Bài 7.** 
	Kết quả thi môn Toán của 2 lớp:
	
		
-  Lớp 10A1: Điểm 5 (3), 6 (7), 7 (12), 8 (14), 9 (3), 10 (1). Tổng: 40 hs.
		
-  Lớp 10A2: Điểm 6 (8), 7 (18), 8 (10), 9 (4). Tổng: 40 hs.
	
	a) Tính phương sai, độ lệch chuẩn của từng lớp.\\
	b) Lớp nào học đồng đều hơn?
	\loigiai{
		- Lớp 10A1: $\overline{x}_1 = 7{,}225; s_1^2 \approx 1{,}32; s_1 \approx 1{,}15$.\\
		- Lớp 10A2: $\overline{x}_2 = 7{,}25; s_2^2 \approx 0{,}79; s_2 \approx 0{,}89$.\\
		Vì $s_2 < s_1$ nên lớp 10A2 có kết quả thi môn Toán đồng đều hơn lớp 10A1.
	}





**Bài 8.** 
	Tuổi thọ của 30 bóng đèn thắp thử (giờ): các bóng quanh 1178 - 1198 giờ, có 2 bóng là 1568 và 1569. Hãy tìm các số liệu bất thường.
	\loigiai{
		Sắp xếp dãy số: 28 bóng đèn có tuổi thọ nằm trong khoảng từ 1178 đến 1198 giờ, với $Q_1 = 1179$ và $Q_3 = 1187 \implies \Delta_Q = 8$.\\
		$Q_3 + 1{,}5\Delta_Q = 1187 + 12 = 1199$.\\
		Hai giá trị $1568$ và $1569$ lớn hơn $1199$ rất nhiều.\\
		Vậy hai giá trị bất thường là **1568** và **1569** giờ.
	}





**Bài 9.** 
	Thời gian hoàn thành sản phẩm (phút) của 20 công nhân: $7, 12, 13, 15, 11, 13, 16, 18, 19, 21, 23, 21, 15, 17, 16, 15, 20, 13, 16, 29$. Tìm số liệu bất thường.
	\loigiai{
		Sắp xếp ($n = 20$): $7, 11, 12, 13, 13, 13, 15, 15, 15, 16, 16, 16, 17, 18, 19, 20, 21, 21, 23, 29$.\\
		$Q_1 = 13, Q_3 = 19{,}5 \implies \Delta_Q = 6{,}5$.\\
		$[13 - 9{,}75; 19{,}5 + 9{,}75] = [3{,}25; 29{,}25]$.\\
		Mọi giá trị đều nằm trong đoạn này nên không có số liệu bất thường (hoặc giá trị 29 và 7 nằm sát biên).
	}





**Bài 10.** 
	Điểm kiểm tra Toán của 21 học sinh lớp 10A:
	\[10;\; 6;\; 7;\; 7;\; 1;\; 7;\; 6;\; 9;\; 9;\; 10;\; 8;\; 8;\; 7;\; 8;\; 6;\; 7;\; 5;\; 6;\; 7;\; 8;\; 9.\]
	Hãy tìm các số liệu bất thường trong mẫu số liệu trên.
	\loigiai{
		Sắp xếp ($n = 21$): $1, 5, 6, 6, 6, 6, 7, 7, 7, 7, \mathbf{7}, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10$.\\
		$Q_2 = 7$.\\
		Nửa dưới (10 số): $1, 5, 6, 6, 6, 6, 7, 7, 7, 7 \implies Q_1 = 6$.\\
		Nửa trên (10 số): $7, 8, 8, 8, 8, 9, 9, 9, 10, 10 \implies Q_3 = 8{,}5$.\\
		$\Delta_Q = 8{,}5 - 6 = 2{,}5$.\\
		$Q_1 - 1{,}5\Delta_Q = 6 - 3{,}75 = 2{,}25$.\\
		Giá trị $1 < 2{,}25$ nên là giá trị bất thường.\\
		Vậy giá trị bất thường là **1**.
	}





**Bài 11.** 
	Tốc độ (km/h) của 25 chiếc xe qua trạm: các xe từ 40 đến 80 km/h, có 1 xe chạy 20 km/h và 1 xe chạy 135 km/h. Hãy tìm các số liệu bất thường.
	\loigiai{
		Sắp xếp mẫu số liệu, tính tứ phân vị: $Q_1 = 52, Q_3 = 65 \implies \Delta_Q = 13$.\\
		$[52 - 19{,}5; 65 + 19{,}5] = [32{,}5; 84{,}5]$.\\
		Số $20 < 32{,}5$ và số $135 > 84{,}5$ nằm ngoài đoạn bình thường.\\
		Vậy hai giá trị bất thường là **20 km/h** và **135 km/h**.
	}





**Bài 12.** 
	Điểm thi Toán của 450 học sinh: điểm 1 (1), 2 (1), 3 (1), 4 (1), 5 (120), 6 (200), 7 (119), 8 (5), 9 (1), 10 (1). Tìm các số liệu bất thường.
	\loigiai{
		Do đại đa số học sinh (439/450) tập trung ở điểm 5, 6, 7 nên $Q_1 = 5, Q_3 = 7 \implies \Delta_Q = 2$.\\
		$[Q_1 - 1{,}5\Delta_Q; Q_3 + 1{,}5\Delta_Q] = [5 - 3; 7 + 3] = [2; 10]$.\\
		Giá trị $1 < 2$ nằm ngoài đoạn trên.\\
		Vậy giá trị bất thường là **1**.
	}





**Bài 13.** 
	Cho mẫu gồm 15 số dương. Các số đo độ phân tán (khoảng biến thiên $R$, khoảng tứ phân vị $\Delta_Q$, độ lệch chuẩn $s$) thay đổi thế nào nếu:
	
		
-  Nhân mỗi giá trị với 3?
		
-  Cộng mỗi giá trị với 3?
	
	\loigiai{
		
			
-  Khi nhân mỗi giá trị với 3: các giá trị mới là $x'_i = 3x_i$.\\
			- $R' = 3x_{\max} - 3x_{\min} = 3R$ (tăng lên 3 lần).\\
			- $\Delta_Q' = 3Q_3 - 3Q_1 = 3\Delta_Q$ (tăng lên 3 lần).\\
			- $s' = 3s$ (tăng lên 3 lần).\\
			
-  Khi cộng mỗi giá trị với 3: các giá trị mới là $x'_i = x_i + 3$.\\
			- $R' = (x_{\max} + 3) - (x_{\min} + 3) = R$ (không đổi).\\
			- $\Delta_Q' = (Q_3 + 3) - (Q_1 + 3) = \Delta_Q$ (không đổi).\\
			- $s' = s$ (không đổi, vì độ lệch so với trung bình giữ nguyên).
		
	}





**Bài 14.** 
	Sản lượng lúa (tạ) của 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6).
	
		
-  Tính sản lượng trung bình của 40 thửa ruộng.
		
-  Tính phương sai và độ lệch chuẩn.
	
	\loigiai{
		
			
-  Sản lượng trung bình: $\overline{x} = 22{,}1$ tạ.
			
-  Phương sai: $s^2 = 1{,}54$ tạ$^2$. Độ lệch chuẩn: $s = \sqrt{1{,}54} \approx 1{,}24$ tạ.
		
	}





**Bài 15.** 
	Số máy tính bán được trong 7 tháng: $83;\; 79;\; 92;\; 71;\; 69;\; 83;\; 74$.
	
		
-  Tính khoảng biến thiên, khoảng tứ phân vị của mẫu số liệu.
		
-  Tính số trung bình, phương sai và độ lệch chuẩn.
	
	\loigiai{
		Sắp xếp ($n = 7$): $69, 71, 74, 79, 83, 83, 92$.\\
		
			
-  Khoảng biến thiên: $R = 92 - 69 = 23$.\\
			Tứ phân vị: $Q_1 = 71, Q_3 = 83 \implies \Delta_Q = 83 - 71 = 12$.
			
-  Số trung bình: $\overline{x} = \dfrac{551}{7} \approx 78{,}71$.\\
			Phương sai: $s^2 \approx 57{,}06$. Độ lệch chuẩn: $s \approx 7{,}55$.
		
	}





**Bài 16.** 
	Điểm thi kết thúc học kì của bạn Hoa: Văn (6,0), Địa (8,0), Lý (7,5), Hóa (8,5), Toán (7,0), Anh văn (7,5). Tìm số trung bình, phương sai và độ lệch chuẩn.
	\loigiai{
		Mẫu số liệu 6 môn: $6{,}0;\; 7{,}0;\; 7{,}5;\; 7{,}5;\; 8{,}0;\; 8{,}5$.\\
		- Số trung bình:
		\[\overline{x} = \frac{6{,}0 + 7{,}0 + 7{,}5 + 7{,}5 + 8{,}0 + 8{,}5}{6} = \frac{44{,}5}{6} \approx 7{,}42\text{ (điểm)}.\]
		- Phương sai:
		\[s^2 = \frac{(6-7{,}42)^2 + (7-7{,}42)^2 + 2(7{,}5-7{,}42)^2 + (8-7{,}42)^2 + (8{,}5-7{,}42)^2}{6} \approx 0{,}62.\]
		- Độ lệch chuẩn:
		\[s = \sqrt{0{,}62} \approx 0{,}79\text{ (điểm)}.\]
	}





**Bài 17.** 
	Bán xe máy trong các ngày: 0 xe (2 ngày), 1 xe (13 ngày), 2 xe (15 ngày), 3 xe (12 ngày), 4 xe (7 ngày), 5 xe (3 ngày).
	
		
-  Tính khoảng biến thiên, khoảng tứ phân vị.
		
-  Tính số trung bình, phương sai và độ lệch chuẩn.
	
	\loigiai{
		Tổng số ngày: $n = 52$ ngày.\\
		
			
-  Khoảng biến thiên: $R = 5 - 0 = 5$ xe.\\
			Tứ phân vị: $Q_1 = 1, Q_3 = 3 \implies \Delta_Q = 3 - 1 = 2$ xe.
			
-  Số trung bình: $\overline{x} = \dfrac{0(2) + 1(13) + 2(15) + 3(12) + 4(7) + 5(3)}{52} = \dfrac{122}{52} \approx 2{,}35$ xe.\\
			Phương sai: $s^2 \approx 1{,}47$. Độ lệch chuẩn: $s \approx 1{,}21$ xe.
		
	}





**Bài 18.** 
	Tốc độ (km/h) của 20 ô tô: từ 40 đến 110 km/h. Tìm các giá trị bất thường.
	\loigiai{
		Sắp xếp dãy số ($n = 20$), tính được: $Q_1 = 66, Q_3 = 82{,}5 \implies \Delta_Q = 16{,}5$.\\
		$[66 - 24{,}75; 82{,}5 + 24{,}75] = [41{,}25; 107{,}25]$.\\
		Số $40 < 41{,}25$ và số $110 > 107{,}25$ đều nằm ngoài đoạn bình thường.\\
		Vậy hai giá trị bất thường là **40 km/h** và **110 km/h**.
	}





**Bài 19.** 
	Tốc độ ô tô trên 2 con đường A và B (30 xe mỗi đường):
	
		
-  Tính khoảng biến thiên, khoảng tứ phân vị của mỗi con đường.
		
-  Tính số trung bình, phương sai và độ lệch chuẩn.
		
-  Theo em chạy xe trên con đường nào an toàn hơn?
	
	\loigiai{
		
			
-  
			- Đường A: Tốc độ từ 60 đến 90 km/h $\implies R_A = 30$ km/h; $\Delta_{Q_A} \approx 14$ km/h.\\
			- Đường B: Tốc độ từ 58 đến 82 km/h $\implies R_B = 24$ km/h; $\Delta_{Q_B} \approx 10$ km/h.
			
-  
			- Đường A: $\overline{x}_A \approx 73{,}6$ km/h; $s_A \approx 8{,}65$ km/h.\\
			- Đường B: $\overline{x}_B \approx 70{,}8$ km/h; $s_B \approx 6{,}32$ km/h.
			
-  Con đường B có độ lệch chuẩn và khoảng biến thiên nhỏ hơn nhiều so với con đường A ($s_B < s_A$), các xe lưu thông với tốc độ đồng đều và ít chênh lệch hơn, do đó lưu thông trên **con đường B an toàn hơn**.
		
	}





**Bài 20.** 
	Điểm thi Toán lớp 10A và 10B (mỗi lớp 45 học sinh):
	
		
-  Tính số trung bình, phương sai, độ lệch chuẩn mỗi lớp.
		
-  Lớp nào học đồng đều hơn?
	
	\loigiai{
		
			
-  
			- Lớp 10A: $\overline{x}_A \approx 6{,}71$; $s_A^2 \approx 4{,}78$; $s_A \approx 2{,}19$.\\
			- Lớp 10B: $\overline{x}_B \approx 6{,}69$; $s_B^2 \approx 3{,}14$; $s_B \approx 1{,}77$.
			
-  Lớp 10B có phương sai và độ lệch chuẩn nhỏ hơn lớp 10A ($s_B < s_A$), nên kết quả học tập của **lớp 10B đồng đều hơn lớp 10A**.
		
	}





**Bài 21.** 
	Lãi hàng tháng (triệu đồng) của cửa hàng A trong 12 tháng:
	\[12;\; 15;\; 18;\; 13;\; 18;\; 16;\; 17;\; 14;\; 18;\; 17;\; 20;\; 17.\]
	Tìm số trung bình, phương sai và độ lệch chuẩn.
	\loigiai{
		Tổng 12 tháng: $195$ triệu đồng.\\
		- Số trung bình: $\overline{x} = \dfrac{195}{12} = 16{,}25$ triệu đồng.\\
		- Phương sai: $s^2 \approx 4{,}52$ (triệu đồng)$^2$.\\
		- Độ lệch chuẩn: $s = \sqrt{4{,}52} \approx 2{,}13$ triệu đồng.
	}





**Bài 22.** 
	Cho biểu đồ biểu diễn kết quả học tập của học sinh trong một lớp qua một bài kiểm tra:
	\begin{center}
		

@@IMAGE_BAI22@@


	\end{center}
	Từ biểu đồ trên hãy:
	
		
-  Viết mẫu số liệu thống kê kết quả học tập của học sinh một lớp nhận được từ biểu đồ đã cho.
		
-  Tìm khoảng biến thiên của mẫu số liệu đó.
		
-  Tìm khoảng tứ phân vị trong mẫu số liệu đó.
		
-  Tính phương sai và độ lệch chuẩn của mẫu số liệu đó.
	
	\loigiai{
		
			
-  Từ biểu đồ ta có bảng phân bố tần số kết quả học tập của học sinh:
			\begin{center}
			\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|}
				\hline
				Điểm ($x$) & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & Cộng \\
				\hline
				Số học sinh ($m$) & 1 & 2 & 4 & 2 & 7 & 8 & 6 & 2 & 1 & 33 \\
				\hline
			\end{tabular}
			\end{center}
			*(Lưu ý: tại điểm $x = 1$, tần số $m = 0$ nên có thể bỏ qua hoặc ghi tần số 0)*.\\
			Tổng số học sinh tham gia kiểm tra là $n = 33$.
			
-  Khoảng biến thiên của mẫu số liệu:
			\[R = x_{\max} - x_{\min} = 10 - 2 = 8\text{ (điểm)}.\]
			
-  Tứ phân vị ($n = 33$ học sinh):
			
				
-  Vì $n = 33$ lẻ nên trung vị $Q_2$ là điểm của học sinh ở vị trí thứ $\dfrac{33 + 1}{2} = 17$.\\
				Tần số tích lũy đến điểm 6 là $1 + 2 + 4 + 2 + 7 = 16$ học sinh. Do đó học sinh thứ 17 đạt điểm 7 $\implies Q_2 = 7$ điểm.
				
-  Nửa dãy phía dưới gồm 16 học sinh đầu (từ vị trí 1 đến 16). Tứ phân vị thứ nhất $Q_1$ là trung bình cộng của học sinh thứ 8 và thứ 9. Cả hai học sinh này đều đạt điểm 5 $\implies Q_1 = 5$ điểm.
				
-  Nửa dãy phía trên gồm 16 học sinh cuối (từ vị trí 18 đến 33). Tứ phân vị thứ ba $Q_3$ là trung bình cộng của học sinh thứ 25 và thứ 26 ($17 + 8 = 25$ và 26). Cả hai học sinh này đều đạt điểm 8 $\implies Q_3 = 8$ điểm.
			
			Khoảng tứ phân vị:
			\[\Delta_Q = Q_3 - Q_1 = 8 - 5 = 3\text{ (điểm)}.\]
			
-  Số trung bình:
			\[\overline{x} = \frac{2(1) + 3(2) + 4(4) + 5(2) + 6(7) + 7(8) + 8(6) + 9(2) + 10(1)}{33} = \frac{208}{33} \approx 6{,}30\text{ (điểm)}.\]
			Phương sai:
			\[s^2 = \frac{1}{33}\sum m_i x_i^2 - (\overline{x})^2 = \frac{1426}{33} - \left(\frac{208}{33}\right)^2 \approx 43{,}2121 - 39{,}7319 \approx 3{,}48\text{ (điểm}^2\text{)}.\]
			Độ lệch chuẩn:
			\[s = \sqrt{s^2} \approx \sqrt{3{,}48} \approx 1{,}87\text{ (điểm)}.\]
		
	}





---

<p align='center'>**--------- HẾT ---------**</p>
