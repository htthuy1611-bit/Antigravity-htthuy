
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






	**Ví dụ 1.** Cân nặng (kg) của 10 học sinh: $49;\; 57;\; 66;\; 45;\; 50;\; 41;\; 57;\; 42;\; 55;\; 52$. Tìm khoảng biến thiên của mẫu số liệu.
	







	**Ví dụ 2.** Chiều cao (m) của các bạn học sinh trong một lớp học:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Chiều cao & 1,60 & 1,61 & 1,62 & 1,63 & 1,64 & 1,65 \\
		\hline
		Số lượng & 3 & 5 & 8 & 9 & 7 & 6 \\
		\hline
	\end{tabular}
	\end{center}
	Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	







	**Ví dụ 3.** Điểm kiểm tra môn Toán của học sinh Tổ 1 và Tổ 2:
	
		
-  Tổ 1: $6;\; 9;\; 4;\; 2;\; 7;\; 9;\; 6;\; 10$.
		
-  Tổ 2: $4;\; 5;\; 6;\; 3;\; 9;\; 5;\; 8;\; 4$.
	
	Tìm khoảng biến thiên trong hai mẫu số liệu và chỉ ra tổ nào học đồng đều hơn.
	






## Dạng 2. Tính phương sai và độ lệch chuẩn






	**Ví dụ 1.** Sản lượng lúa (tạ) của 40 thửa ruộng:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Sản lượng ($x$) & 20 & 21 & 22 & 23 & 24 & \\
		\hline
		Tần số ($n$) & 5 & 8 & 11 & 10 & 6 & $n = 40$ \\
		\hline
	\end{tabular}
	\end{center}
	a) Tính sản lượng trung bình của 40 thửa ruộng.\\
	b) Tính phương sai và độ lệch chuẩn.
	







	**Ví dụ 2.** 100 học sinh thi học sinh giỏi Toán (thang điểm 20):
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		Điểm & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & \\
		\hline
		Tần số & 1 & 1 & 3 & 5 & 8 & 13 & 19 & 24 & 14 & 10 & 2 & $n = 100$ \\
		\hline
	\end{tabular}
	\end{center}
	a) Tính số trung bình.\\
	b) Tìm phương sai và độ lệch chuẩn.
	






## Dạng 3. Tìm các số liệu bất thường của mẫu số liệu






	**Ví dụ 1.** Điểm kiểm tra môn Toán của 10 học sinh sau:
	\[1;\; 7;\; 10;\; 7;\; 7;\; 6;\; 9;\; 8;\; 10;\; 8.\]
	Hãy tìm các số liệu bất thường trong mẫu số liệu trên.
	







# III. BÀI TẬP VẬN DỤNG





## PHẦN I. CÂU HỎI TRẮC NGHIỆM


*\small (Mỗi câu học sinh chỉ chọn một phương án trả lời đúng)*
\setcounter{ex}{0}

% Câu 1



	Hãy tìm khoảng biến thiên của mẫu số liệu thống kê sau: $22;\; 26;\; 31;\; 15;\; 12;\; 4;\; 18;\; 93;\; 17;\; 64;\; 10$.
	

@@TAB@@**A.** $33$@@TAB@@**B.** $83$@@TAB@@**C.** $89$@@TAB@@**D.** $97$





% Câu 2



	Hai chữ số cuối giải đặc biệt Xổ số miền Bắc trong 9 ngày được ghi lại như sau: $16;\; 11;\; 25;\; 28;\; 45;\; 42;\; 24;\; 33;\; 11$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	

@@TAB@@**A.** $18$@@TAB@@**B.** $34$@@TAB@@**C.** $56$@@TAB@@**D.** $27$





% Câu 3



	Mẫu số liệu nào dưới đây có khoảng biến thiên là 13?
	

@@TAB@@**A.** $11, 28, 56, 12$@@TAB@@**B.** $6, 12, 33, 23, 11$@@TAB@@**C.** $25, 9, 13, 10$ (Wait: $25 - 9 = 16$. Kiểm tra tất cả các mẫu)@@TAB@@**D.** Tất cả đều sai





% Câu 4



	Mẫu số liệu nào dưới đây có khoảng biến thiên là 53?
	

@@TAB@@**A.** $18, 57, 11, 26$@@TAB@@**B.** $44, 2, 55, 46, 27$@@TAB@@**C.** $21, 3, 55, 89$@@TAB@@**D.** $4, 16, 23, 20$





% Câu 5



	Số lượng học sinh có điểm Toán tổng kết cuối học kì I trên 8 ở mỗi lớp của một trường:
	\[16;\; 11;\; 15;\; 18;\; 21;\; 12;\; 24;\; 23;\; 11;\; 8;\; 9;\; 11;\; 6;\; 27;\; 22;\; 20;\; 35;\; 18.\]
	Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	

@@TAB@@**A.** $11$@@TAB@@**B.** $29$@@TAB@@**C.** $37$@@TAB@@**D.** $25$





% Câu 6



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





% Câu 7



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





% Câu 8



	Nhiệt độ cao nhất trong tuần ($^\circ\text{C}$) tại hai thành phố:
	
		
-  Hà Nội: $28;\; 27;\; 30;\; 29;\; 27;\; 24;\; 25$.
		
-  TP Hồ Chí Minh: $31;\; 33;\; 32;\; 33;\; 29;\; 32;\; 34$.
	
	Dựa vào khoảng biến thiên của hai mẫu số liệu, hãy chỉ ra mẫu số liệu nào có độ phân tán lớn hơn.
	

@@TAB@@**A.** Mẫu số liệu "Hà Nội" có độ phân tán lớn hơn mẫu số liệu "TP Hồ Chí Minh"@@TAB@@**B.** Mẫu số liệu "TP Hồ Chí Minh" có độ phân tán lớn hơn mẫu số liệu "Hà Nội"@@TAB@@**C.** Hai mẫu số liệu có độ phân tán bằng nhau@@TAB@@**D.** Tất cả đều sai





% Câu 9



	Tuổi của những đứa trẻ:
	
		
-  Nam: $10;\; 4;\; 1;\; 6;\; 2;\; 8;\; 5$.
		
-  Nữ: $2;\; 3;\; 6;\; 4;\; 1;\; 7$.
	
	Dựa vào khoảng biến thiên, mẫu số liệu nào có độ phân tán lớn hơn?
	

@@TAB@@**A.** Mẫu số liệu "Nam" có độ phân tán lớn hơn mẫu số liệu "Nữ"@@TAB@@**B.** Mẫu số liệu "Nữ" có độ phân tán lớn hơn mẫu số liệu "Nam"@@TAB@@**C.** Hai mẫu số liệu có độ phân tán bằng nhau@@TAB@@**D.** Tất cả đều sai





% Câu 10



	Chỉ số IQ và EQ của một nhóm học sinh:
	
		
-  IQ: $95;\; 110;\; 90;\; 105;\; 88;\; 100;\; 111$.
		
-  EQ: $90;\; 105;\; 98;\; 100;\; 93;\; 96;\; 103$.
	
	Dựa vào khoảng biến thiên, mẫu nào có độ phân tán lớn hơn?
	

@@TAB@@**A.** Mẫu số liệu "IQ" có độ phân tán lớn hơn mẫu số liệu "EQ"@@TAB@@**B.** Mẫu số liệu "EQ" có độ phân tán lớn hơn mẫu số liệu "IQ"@@TAB@@**C.** Hai mẫu số liệu có độ phân tán bằng nhau@@TAB@@**D.** Tất cả đều sai





% Câu 11



	Độ lệch chuẩn là
	

@@TAB@@**A.** Bình phương của phương sai@@TAB@@**B.** Một nửa của phương sai@@TAB@@**C.** Căn bậc hai của phương sai@@TAB@@**D.** Căn bậc ba của phương sai





% Câu 12



	Đại lượng đo mức độ biến động, chênh lệch giữa các giá trị trong mẫu số liệu thống kê gọi là
	

@@TAB@@**A.** Độ lệch chuẩn@@TAB@@**B.** Số trung vị@@TAB@@**C.** Phương sai@@TAB@@**D.** Tần số





% Câu 13



	Cho dãy số liệu thống kê: $1, 2, 3, 4, 5, 6, 7, 8$. Độ lệch chuẩn của dãy số liệu gần bằng
	

@@TAB@@**A.** $2{,@@TAB@@**B.** $3{,@@TAB@@**C.** $4{,@@TAB@@**D.** $5{,





% Câu 14



	Cho mẫu số liệu $\{10, 8, 6, 2, 4\}$. Độ lệch chuẩn của mẫu là
	

@@TAB@@**A.** $2{,@@TAB@@**B.** $8$@@TAB@@**C.** $6$@@TAB@@**D.** $2{,





% Câu 15



	Cho mẫu số liệu thống kê $\{2, 4, 6, 8, 10\}$. Phương sai của mẫu số liệu trên là bao nhiêu?
	

@@TAB@@**A.** $6$@@TAB@@**B.** $8$@@TAB@@**C.** $10$@@TAB@@**D.** $40$





% Câu 16



	Số ô tô đi qua một cây cầu trong một tuần đếm được như sau: $83;\; 74;\; 71;\; 79;\; 83;\; 69;\; 92$. Phương sai và độ lệch chuẩn lần lượt là
	

@@TAB@@**A.** $78{,@@TAB@@**B.** ,@@TAB@@**C.** $52{,@@TAB@@**D.** ,





% Câu 17



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





% Câu 18



	Độ lệch chuẩn của bảng phân bố tần số tiền thưởng ở Câu 17 là
	

@@TAB@@**A.** $1{,@@TAB@@**B.** $1{,@@TAB@@**C.** $1{,@@TAB@@**D.** $1{,





% Câu 19



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





% Câu 20



	Cho dãy số liệu thống kê: $38;\; 18;\; 20;\; 25;\; 18;\; 15;\; 20;\; 22;\; 31$. Phương sai của dãy số liệu trên là
	

@@TAB@@**A.** $47{,@@TAB@@**B.** $50$@@TAB@@**C.** $42$@@TAB@@**D.** $43$





% Câu 21



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





% Câu 22



	Độ lệch chuẩn của tốc độ ô tô ở Câu 21 là
	

@@TAB@@**A.** $8{,@@TAB@@**B.** $8{,@@TAB@@**C.** $8{,@@TAB@@**D.** $8{,





% Câu 23



	Số lượng khách đến điểm du lịch trong 12 tháng:
	\[430;\; 550;\; 430;\; 520;\; 550;\; 515;\; 550;\; 110;\; 520;\; 430;\; 550;\; 880.\]
	Độ lệch chuẩn là
	

@@TAB@@**A.** $567{,@@TAB@@**B.** $163{,@@TAB@@**C.** $171{,@@TAB@@**D.** $147{,





% Câu 24



	Một mẫu số liệu thống kê có các tứ phân vị: $Q_1 = 22, Q_2 = 27, Q_3 = 32$. Giá trị nào sau đây là giá trị bất thường của mẫu số liệu?
	

@@TAB@@**A.** $30$@@TAB@@**B.** $8$@@TAB@@**C.** $6$@@TAB@@**D.** $46$





% Câu 25



	Hãy tìm các giá trị bất thường của mẫu số liệu: $7;\; 19;\; 6;\; 12;\; 5;\; 17;\; 6;\; 13$.
	

@@TAB@@**A.** $5; 6$@@TAB@@**B.** $5; 6; 19$@@TAB@@**C.** Không có số liệu bất thường@@TAB@@**D.** $5; 19$





% Câu 26



	Hãy tìm các giá trị bất thường của mẫu số liệu: $20;\; 52;\; 86;\; 80;\; 44;\; 49;\; 57;\; 41;\; 44;\; 55$.
	

@@TAB@@**A.** $80; 86$@@TAB@@**B.** $41; 80; 86$@@TAB@@**C.** $80; 20; 86$@@TAB@@**D.** $86$





% Câu 27



	Một mẫu số liệu có $Q_1 = 53, Q_2 = 55, Q_3 = 61$. Giá trị nào sau đây không phải là giá trị bất thường?
	

@@TAB@@**A.** $42$ (hoặc $73$ tuỳ đề. Kiểm tra đoạn:)@@TAB@@**B.** $80$@@TAB@@**C.** $73$@@TAB@@**D.** $73{,





% Câu 28



	Mẫu số liệu có $Q_1 = 3, Q_2 = 7, Q_3 = 12$. Giá trị nào là giá trị bất thường?
	

@@TAB@@**A.** $22$@@TAB@@**B.** $-8{,@@TAB@@**C.** $26$@@TAB@@**D.** $25{,





% Câu 29



	Tìm các giá trị bất thường của mẫu số liệu:
	\[10;\; 59;\; 67;\; 72;\; 73;\; 76;\; 88;\; 92;\; 106;\; 111;\; 115;\; 169.\]
	

@@TAB@@**A.** $169$@@TAB@@**B.** $115; 169$@@TAB@@**C.** $111; 169$@@TAB@@**D.** $10; 169$





% Câu 30



	Cho mẫu số liệu thống kê: $-3;\; 5;\; 10;\; 12;\; 14;\; 18;\; 24;\; 26;\; 49;\; 60$. Phát biểu nào sau đây là đúng?
	

@@TAB@@**A.** $-3$ là giá trị bất thường duy nhất@@TAB@@**B.** $60$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**D.** Mẫu số liệu có nhiều giá trị bất thường





% Câu 31



	Cho mẫu số liệu: $10;\; 21;\; 21;\; 23;\; 25;\; 26;\; 28;\; 42$. Phát biểu nào sau đây là đúng?
	

@@TAB@@**A.** $10$ là giá trị bất thường duy nhất@@TAB@@**B.** $42$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**D.** Mẫu số liệu có nhiều giá trị bất thường





% Câu 32



	Cho mẫu số liệu: $52;\; 47;\; 55;\; 81;\; 61;\; 49;\; 59$. Phát biểu nào đúng?
	

@@TAB@@**A.** $81$ là giá trị bất thường duy nhất@@TAB@@**B.** $47$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường@@TAB@@**D.** Có nhiều giá trị bất thường





% Câu 33



	Cho mẫu số liệu: $8;\; 10;\; 13;\; 13;\; 14;\; 16;\; 27$. Phát biểu nào đúng?
	

@@TAB@@**A.** $8$ là giá trị bất thường duy nhất@@TAB@@**B.** $27$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường@@TAB@@**D.** Có nhiều giá trị bất thường





% Câu 34



	Cho mẫu số liệu: $44;\; 51;\; 36;\; 19;\; 40;\; 69;\; 49;\; 46$. Phát biểu nào đúng?
	

@@TAB@@**A.** $19$ là giá trị bất thường duy nhất@@TAB@@**B.** $69$ là giá trị bất thường duy nhất@@TAB@@**C.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**D.** Mẫu số liệu có nhiều giá trị bất thường





% Câu 35



	Cho mẫu số liệu: $20;\; 22;\; 22;\; 25;\; 28;\; 32;\; 34;\; 43$. Phát biểu nào đúng?
	

@@TAB@@**A.** $20$ là giá trị bất thường duy nhất@@TAB@@**B.** Không có giá trị bất thường trong mẫu số liệu@@TAB@@**C.** $43$ là giá trị bất thường duy nhất@@TAB@@**D.** Có nhiều giá trị bất thường





% Câu 36



	Cho dãy số liệu thống kê: $1, 2, 3, 4, 5, 6, 7$. Phương sai của các số liệu thống kê đã cho là
	

@@TAB@@**A.** $1$@@TAB@@**B.** $2$@@TAB@@**C.** $3$@@TAB@@**D.** $4$





% Câu 37



	Sản lượng lúa (tạ) của 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6). Tính độ lệch chuẩn.
	

@@TAB@@**A.** $s \approx 1{,@@TAB@@**B.** (tạ)@@TAB@@**C.** $s \approx 1{,@@TAB@@**D.** (tạ)





% Câu 38



	Tiền thưởng (triệu đồng) cho 43 cán bộ nhân viên: 2 (5), 3 (15), 4 (10), 5 (6), 6 (7). Tính độ lệch chuẩn.
	

@@TAB@@**A.** $s \approx 1{,@@TAB@@**B.** (triệu đồng)@@TAB@@**C.** $s \approx 1{,@@TAB@@**D.** (triệu đồng)





% Câu 39



	Cho dãy số liệu: $1, 2, 3, 4, 5, 6, 7$. Tìm khoảng biến thiên của mẫu số liệu.
	

@@TAB@@**A.** $R = 7$@@TAB@@**B.** $R = 4$@@TAB@@**C.** $R = 8$@@TAB@@**D.** $R = 6$





% Câu 40



	Giá trị thành phẩm của 7 công nhân: $180, 190, 190, 200, 210, 210, 220$. Tìm khoảng tứ phân vị của mẫu số liệu.
	

@@TAB@@**A.** $190$@@TAB@@**B.** $20$@@TAB@@**C.** $210$@@TAB@@**D.** $200$





% Câu 41



	Tiền thưởng (triệu đồng) có bảng tần số: 2 (5), 3 (15), 4 (10), 5 (6), 6 (7). Phương sai thuộc khoảng nào?
	

@@TAB@@**A.** $(4{,@@TAB@@**B.** ,@@TAB@@**C.** $(4{,@@TAB@@**D.** ,





% Câu 42



	Khách du lịch 12 tháng: 430, 560, 450, 550, 760, 430, 525, 110, 635, 450, 800, 950. Tính độ lệch chuẩn $s$.
	

@@TAB@@**A.** $s \approx 211$@@TAB@@**B.** $s \approx 209{,@@TAB@@**C.** $s \approx 403{,@@TAB@@**D.** $s \approx 207{,





% Câu 43



	Độ lệch chuẩn bằng
	

@@TAB@@**A.** bình phương của phương sai@@TAB@@**B.** căn bậc hai số học của phương sai@@TAB@@**C.** một nửa của phương sai@@TAB@@**D.** hai lần phương sai





% Câu 44



	Sản lượng lúa 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6). Tính khoảng tứ phân vị của mẫu số liệu.
	

@@TAB@@**A.** $3$@@TAB@@**B.** $4$@@TAB@@**C.** $2$ (hoặc $1$)@@TAB@@**D.** $s^2$





% Câu 45



	Chọn khẳng định sai trong các khẳng định sau:
	

@@TAB@@**A.** Phương sai luôn là một số không âm@@TAB@@**B.** Phương sai không có đơn vị@@TAB@@**C.** Phương sai càng lớn thì độ phân tán càng lớn@@TAB@@**D.** Độ lệch chuẩn càng lớn thì độ phân tán càng lớn





% Câu 46



	100 học sinh thi HSG Toán: Điểm từ 9 đến 19. Tính độ lệch chuẩn.
	

@@TAB@@**A.** $s \approx 1{,@@TAB@@**B.** (điểm)@@TAB@@**C.** $s \approx 1{,@@TAB@@**D.** (điểm)





% Câu 47



	Tuổi 30 bệnh nhân đau mắt hột: từ 12 đến 25 tuổi. Tính khoảng biến thiên của mẫu số liệu.
	

@@TAB@@**A.** $25$@@TAB@@**B.** $13$@@TAB@@**C.** $26$@@TAB@@**D.** $12$





% Câu 48



	Điểm trung bình các môn của An và Bình: An có điểm dao động từ 7 đến 9, Bình có điểm dao động từ 5 đến 10. Hỏi ai "học lệch" hơn?
	

@@TAB@@**A.** An@@TAB@@**B.** Bình@@TAB@@**C.** Mức độ học lệch của hai người như nhau@@TAB@@**D.** Chưa đủ cơ sở kết luận





% Câu 49



	Số sách đọc trong năm: 1 (10), 2 ($x$), 3 (8), 4 (6), 5 ($y$), 6 (3). Tổng: 40. Biết $s^2 \approx 2{,}52$. Tính $x$ và $y$.
	

@@TAB@@**A.** $x = 7, y = 6$@@TAB@@**B.** $x = 6, y = 7$@@TAB@@**C.** $x = 8, y = 5$@@TAB@@**D.** $x = 5, y = 8$





% Câu 50



	Cho dãy số liệu: $x, 21, 22, 23, 24, y$. Tìm $x, y$ biết số trung bình cộng bằng $22{,}5$ và khoảng biến thiên bằng 5.
	

@@TAB@@**A.** $x = -25$ và $y = -20$@@TAB@@**B.** $x = -20$ và $y = -25$@@TAB@@**C.** $x = 20$ và $y = 25$@@TAB@@**D.** $x = 25$ và $y = 20$








## PHẦN II. CÂU HỎI TỰ LUẬN


*\small (Học sinh trình bày chi tiết lời giải các bài toán sau)*
\setcounter{ex}{0}

% Bài 1



	**Bài 1.** Hai chữ số cuối số điện thoại của 10 người: $23;\; 58;\; 42;\; 11;\; 69;\; 50;\; 13;\; 57;\; 61;\; 72$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	




% Bài 2



	**Bài 2.** Tuổi thọ trung bình người dân của 11 nước: $69;\; 77;\; 75;\; 83;\; 65;\; 75;\; 74;\; 68;\; 73;\; 72;\; 71$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	




% Bài 3



	**Bài 3.** Thời gian làm câu đầu tiên trong đề thi tuyển sinh vào lớp 10 của học sinh:
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
	




% Bài 4



	**Bài 4.** Điểm thi học kì 2 môn Toán và Ngữ văn của một nhóm học sinh:
	
		
-  Toán: $9;\; 8{,}5;\; 7;\; 6{,}3;\; 5;\; 9{,}5;\; 8$.
		
-  Ngữ văn: $6;\; 6{,}5;\; 8;\; 7{,}3;\; 5{,}5;\; 8{,}3;\; 6{,}5$.
	
	Hãy tìm khoảng biến thiên của hai mẫu số liệu trên. Từ đó chỉ ra mẫu số liệu có độ phân tán lớn hơn.
	




% Bài 5



	**Bài 5.** Số giờ nắng và độ ẩm (\%) trung bình hàng tháng của Hà Nội:
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
	




% Bài 6



	**Bài 6.** Một xạ thủ bắn 30 viên đạn vào bia:
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
	




% Bài 7



	**Bài 7.** Kết quả thi môn Toán của 2 lớp:
	
		
-  Lớp 10A1: Điểm 5 (3), 6 (7), 7 (12), 8 (14), 9 (3), 10 (1). Tổng: 40 hs.
		
-  Lớp 10A2: Điểm 6 (8), 7 (18), 8 (10), 9 (4). Tổng: 40 hs.
	
	a) Tính phương sai, độ lệch chuẩn của từng lớp.\\
	b) Lớp nào học đồng đều hơn?
	




% Bài 8



	**Bài 8.** Tuổi thọ của 30 bóng đèn thắp thử (giờ): các bóng quanh 1178 - 1198 giờ, có 2 bóng là 1568 và 1569. Hãy tìm các số liệu bất thường.
	




% Bài 9



	**Bài 9.** Thời gian hoàn thành sản phẩm (phút) của 20 công nhân: $7, 12, 13, 15, 11, 13, 16, 18, 19, 21, 23, 21, 15, 17, 16, 15, 20, 13, 16, 29$. Tìm số liệu bất thường.
	




% Bài 10



	**Bài 10.** Điểm kiểm tra Toán của 21 học sinh lớp 10A:
	\[10;\; 6;\; 7;\; 7;\; 1;\; 7;\; 6;\; 9;\; 9;\; 10;\; 8;\; 8;\; 7;\; 8;\; 6;\; 7;\; 5;\; 6;\; 7;\; 8;\; 9.\]
	Hãy tìm các số liệu bất thường trong mẫu số liệu trên.
	




% Bài 11



	**Bài 11.** Tốc độ (km/h) của 25 chiếc xe qua trạm: các xe từ 40 đến 80 km/h, có 1 xe chạy 20 km/h và 1 xe chạy 135 km/h. Hãy tìm các số liệu bất thường.
	




% Bài 12



	**Bài 12.** Điểm thi Toán của 450 học sinh: điểm 1 (1), 2 (1), 3 (1), 4 (1), 5 (120), 6 (200), 7 (119), 8 (5), 9 (1), 10 (1). Tìm các số liệu bất thường.
	




% Bài 13



	**Bài 13.** Cho mẫu gồm 15 số dương. Các số đo độ phân tán (khoảng biến thiên $R$, khoảng tứ phân vị $\Delta_Q$, độ lệch chuẩn $s$) thay đổi thế nào nếu:
	
		
-  Nhân mỗi giá trị với 3?
		
-  Cộng mỗi giá trị với 3?
	
	




% Bài 14



	**Bài 14.** Sản lượng lúa (tạ) của 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6).
	
		
-  Tính sản lượng trung bình của 40 thửa ruộng.
		
-  Tính phương sai và độ lệch chuẩn.
	
	




% Bài 15



	**Bài 15.** Số máy tính bán được trong 7 tháng: $83;\; 79;\; 92;\; 71;\; 69;\; 83;\; 74$.
	
		
-  Tính khoảng biến thiên, khoảng tứ phân vị của mẫu số liệu.
		
-  Tính số trung bình, phương sai và độ lệch chuẩn.
	
	




% Bài 16



	**Bài 16.** Điểm thi kết thúc học kì của bạn Hoa: Văn (6,0), Địa (8,0), Lý (7,5), Hóa (8,5), Toán (7,0), Anh văn (7,5). Tìm số trung bình, phương sai và độ lệch chuẩn.
	




% Bài 17



	**Bài 17.** Bán xe máy trong các ngày: 0 xe (2 ngày), 1 xe (13 ngày), 2 xe (15 ngày), 3 xe (12 ngày), 4 xe (7 ngày), 5 xe (3 ngày).
	
		
-  Tính khoảng biến thiên, khoảng tứ phân vị.
		
-  Tính số trung bình, phương sai và độ lệch chuẩn.
	
	




% Bài 18



	**Bài 18.** Tốc độ (km/h) của 20 ô tô: từ 40 đến 110 km/h. Tìm các giá trị bất thường.
	




% Bài 19



	**Bài 19.** Tốc độ ô tô trên 2 con đường A và B (30 xe mỗi đường):
	
		
-  Tính khoảng biến thiên, khoảng tứ phân vị của mỗi con đường.
		
-  Tính số trung bình, phương sai và độ lệch chuẩn.
		
-  Theo em chạy xe trên con đường nào an toàn hơn?
	
	




% Bài 20



	**Bài 20.** Điểm thi Toán lớp 10A và 10B (mỗi lớp 45 học sinh):
	
		
-  Tính số trung bình, phương sai, độ lệch chuẩn mỗi lớp.
		
-  Lớp nào học đồng đều hơn?
	
	




% Bài 21



	**Bài 21.** Lãi hàng tháng (triệu đồng) của cửa hàng A trong 12 tháng:
	\[12;\; 15;\; 18;\; 13;\; 18;\; 16;\; 17;\; 14;\; 18;\; 17;\; 20;\; 17.\]
	Tìm số trung bình, phương sai và độ lệch chuẩn.
	




% Bài 22



	**Bài 22.** Cho biểu đồ biểu diễn kết quả học tập của học sinh qua một bài kiểm tra:
	\begin{center}
	*[Biểu đồ tần số xem trong bản PDF]*
	\end{center}
	
		
-  Viết mẫu số liệu thống kê kết quả học tập từ biểu đồ đã cho.
		
-  Tìm khoảng biến thiên của mẫu số liệu.
		
-  Tìm khoảng tứ phân vị trong mẫu số liệu.
		
-  Tính phương sai và độ lệch chuẩn của mẫu số liệu.
	
	





---

<p align='center'>**--------- HẾT ---------**</p>
