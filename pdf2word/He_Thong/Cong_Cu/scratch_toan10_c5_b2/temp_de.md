
\begin{center}
	{\Large\bfseries\color{blue!80!black} CHƯƠNG V. CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM}\\[6pt]
	{\large\bfseries\color{red!80!black} BÀI 2. CÁC SỐ ĐẶC TRƯNG ĐO XU THẾ TRUNG TÂM}
\end{center}




# I. TÓM TẮT LÝ THUYẾT





## 1. Số trung bình cộng (Số trung bình)



	
-  Cho mẫu số liệu gồm $n$ giá trị $x_1, x_2, \ldots, x_n$. Số trung bình cộng kí hiệu là $\overline{x}$, được tính bởi:
	\[\overline{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}.\]
	
-  Khi mẫu số liệu cho dưới dạng bảng phân bố tần số (giá trị $x_i$ có tần số $n_i$ tương ứng, $\sum n_i = n$):
	\[\overline{x} = \frac{n_1 x_1 + n_2 x_2 + \cdots + n_k x_k}{n}.\]
	
-  Khi cho dưới dạng tần số tương đối $f_i = \dfrac{n_i}{n}$:
	\[\overline{x} = f_1 x_1 + f_2 x_2 + \cdots + f_k x_k.\]
	
-  **Ý nghĩa:** Số trung bình cho biết vị trí trung tâm của mẫu số liệu và được dùng làm giá trị đại diện khi các số liệu ít phân tán, ít sai lệch.




## 2. Trung vị



	
-  Sắp xếp mẫu số liệu gồm $n$ số liệu theo thứ tự không giảm (hoặc không tăng):
	
		
-  Nếu $n$ lẻ: Số liệu đứng ở vị trí chính giữa (thứ $\dfrac{n+1}{2}$) gọi là trung vị.
		
-  Nếu $n$ chẵn: Trung vị là số trung bình cộng của hai số liệu đứng ở vị trí thứ $\dfrac{n}{2}$ và $\dfrac{n}{2} + 1$.
	
	
-  Kí hiệu trung vị là $M_e$.
	
-  **Ý nghĩa:** Trung vị chia mẫu số liệu thành hai phần có số phần tử bằng nhau. Trung vị không bị ảnh hưởng bởi các giá trị bất thường (quá lớn hoặc quá nhỏ).




## 3. Tứ phân vị



	
-  Sắp thứ tự mẫu số liệu gồm $n$ số liệu thành dãy không giảm. Tứ phân vị là bộ ba giá trị $Q_1, Q_2, Q_3$ chia mẫu số liệu thành 4 phần bằng nhau về số lượng:
	
		
-  $Q_2 = M_e$ (trung vị của toàn bộ mẫu).
		
-  $Q_1$ (tứ phân vị thứ nhất hay tứ phân vị dưới): là trung vị của nửa dãy phía dưới.
		
-  $Q_3$ (tứ phân vị thứ ba hay tứ phân vị trên): là trung vị của nửa dãy phía trên.
		
-  *Lưu ý:* Nếu $n$ lẻ thì nửa dãy dưới và nửa dãy trên không bao gồm $Q_2$. Nếu $n$ chẵn thì nửa dãy dưới gồm $\dfrac{n}{2}$ số liệu đầu và nửa dãy trên gồm $\dfrac{n}{2}$ số liệu sau.
	
	
-  **Ý nghĩa:** $Q_1, Q_2, Q_3$ chia mẫu thành 4 phần, mỗi phần chứa $25\%$ số giá trị, đo xu thế trung tâm của từng phần mẫu.




## 4. Mốt



	
-  Mốt của mẫu số liệu (kí hiệu $M_o$) là giá trị có tần số xuất hiện lớn nhất trong bảng phân bố tần số.
	
-  Một mẫu số liệu có thể có một hoặc nhiều mốt. Nếu tất cả các giá trị đều có tần số bằng nhau thì mẫu không có mốt.
	
-  **Ý nghĩa:** Mốt đặc trưng cho giá trị phổ biến nhất, hay gặp nhất trong đời sống thực tế (ví dụ: cỡ áo bán chạy nhất).





# II. CÁC VÍ DỤ MINH HỌA






	**Ví dụ 1.** Trong một cuộc thi tìm hiểu lịch sử địa phương, kết quả điểm số của 30 học sinh một lớp được ghi lại trong bảng sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|}
		\hline
		Số học sinh ($n_i$) & 5 & 12 & 10 & 3 \\
		\hline
		Số điểm ($x_i$) & 5 & 6 & 7 & 9 \\
		\hline
	\end{tabular}
	\end{center}
	Hỏi trung bình mỗi học sinh trong lớp đạt bao nhiêu điểm?
	







	**Ví dụ 2.** Nghiên cứu tuổi thọ của 10 bóng đèn (tính theo giờ) được ghi lại như sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|}
		\hline
		Số bóng đèn ($n_i$) & 2 & 3 & 4 & 1 \\
		\hline
		Tuổi thọ (giờ) ($x_i$) & 1150 & 1160 & 1170 & 1180 \\
		\hline
	\end{tabular}
	\end{center}
	Hỏi tuổi thọ trung bình của các bóng đèn là bao nhiêu giờ?
	







	**Ví dụ 3.** Trong đợt kiểm tra bắn súng AK, mỗi người bắn 5 phát. Thang điểm là các số $0, 4, 5, 6, 7, 8, 9, 10$. Ở 4 lần bắn trước, anh Nam đạt được $8; 7; 0; 9$ điểm. Để vượt qua bài kiểm tra, điểm trung bình 5 lần phải từ $6{,}5$ trở lên. Tính số điểm ít nhất anh Nam cần đạt ở lần bắn thứ 5.
	







	**Ví dụ 4.** Điểm thi của 7 học sinh là: $89, 69, 65, 0, 80, 0, 90$. Tìm trung vị của mẫu số liệu trên.
	







	**Ví dụ 5.** Số áo bán được trong một quý của một cửa hàng được ghi lại như sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|}
		\hline
		Cỡ số & 36 & 37 & 38 & 39 & 40 & 41 & 42 \\
		\hline
		Số áo bán được & 13 & 45 & 126 & 110 & 126 & 40 & 5 \\
		\hline
	\end{tabular}
	\end{center}
	Hãy tìm trung vị của mẫu số liệu trên.
	







	**Ví dụ 6.** Số tấn hàng bán ra trong 6 tháng đầu năm của một công ty là: $4, 7, 9, 11, 12, 20$. Tìm tứ phân vị dưới của mẫu số liệu.
	







	**Ví dụ 7.** Số buổi nghỉ học của một nhóm học sinh là: $5, 8, 10, 11, 15, 18, 23$. Tìm tứ phân vị trên của mẫu số liệu.
	







	**Ví dụ 8.** Giá thành một sản phẩm (nghìn đồng) của 20 cơ sở sản xuất:
	\begin{center}
	\begin{tabular}{cccccccccc}
		15 & 25 & 25 & 30 & 20 & 25 & 35 & 30 & 25 & 30 \\
		25 & 20 & 35 & 30 & 15 & 25 & 25 & 20 & 25 & 25
	\end{tabular}
	\end{center}
	Tìm mốt của mẫu số liệu trên.
	







	**Ví dụ 9.** Cân nặng của 20 học sinh:
	\begin{center}
	\begin{tabular}{cccccccccc}
		28 & 35 & 29 & 37 & 30 & 35 & 37 & 30 & 35 & 29 \\
		30 & 37 & 35 & 35 & 42 & 28 & 35 & 29 & 37 & 20
	\end{tabular}
	\end{center}
	Tìm mốt của mẫu số liệu trên.
	







# III. BÀI TẬP VẬN DỤNG





## PHẦN I. CÂU HỎI TRẮC NGHIỆM


*\small (Mỗi câu học sinh chỉ chọn một phương án trả lời đúng)*
\setcounter{ex}{0}

% Câu 1



	Điều tra về số con của 40 gia đình ở khu vực, kết quả thu được như sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Giá trị (số con) & 0 & 1 & 2 & 3 & 4 & Tổng \\
		\hline
		Tần số & 5 & 9 & 19 & 5 & 2 & $N = 40$ \\
		\hline
	\end{tabular}
	\end{center}
	Số trung bình $\overline{x}$ của mẫu số liệu trên là
	

@@TAB@@**A.** $\overline{x@@TAB@@**B.** ,@@TAB@@**C.** $\overline{x@@TAB@@**D.** $\overline{x





% Câu 2



	Kết quả điểm kiểm tra môn Toán của 40 học sinh lớp 10A được trình bày ở bảng sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|}
		\hline
		Điểm & 4 & 5 & 6 & 7 & 8 & 9 & 10 & Cộng \\
		\hline
		Tần số & 2 & 8 & 7 & 10 & 8 & 3 & 2 & 40 \\
		\hline
	\end{tabular}
	\end{center}
	Tính số trung bình cộng của bảng trên (làm tròn kết quả đến một chữ số thập phân).
	

@@TAB@@**A.** $6{,@@TAB@@**B.** $6{,@@TAB@@**C.** $7{,@@TAB@@**D.** $6{,





% Câu 3



	Tiền thưởng (triệu đồng) của cán bộ và nhân viên trong một công ty được cho ở bảng sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Tiền thưởng & 2 & 3 & 4 & 5 & 6 & Cộng \\
		\hline
		Tần số & 5 & 15 & 10 & 6 & 4 & 40 \\
		\hline
	\end{tabular}
	\end{center}
	Tính tiền thưởng trung bình.
	

@@TAB@@**A.** $3\,725\,000$ đồng@@TAB@@**B.** $3\,745\,000$ đồng@@TAB@@**C.** $3\,715\,000$ đồng@@TAB@@**D.** $3\,625\,000$ đồng





% Câu 4



	Để được cấp chứng chỉ A- Anh văn của một trung tâm ngoại ngữ, học viên phải trải qua 6 lần kiểm tra trắc nghiệm, thang điểm mỗi lần là 100 và phải đạt điểm trung bình từ 70 điểm trở lên. Qua 5 lần thi Minh đạt điểm trung bình là 64,5 điểm. Hỏi trong lần kiểm tra cuối cùng Minh phải đạt ít nhất bao nhiêu điểm để được cấp chứng chỉ?
	

@@TAB@@**A.** $97{,@@TAB@@**B.** $96{,@@TAB@@**C.** $94{,@@TAB@@**D.** $93{,





% Câu 5



	Học sinh tỉnh A (gồm lớp 11 và lớp 12) tham dự kì thi học sinh giỏi Toán của Tỉnh (thang điểm 20) và điểm trung bình của họ là 10. Biết rằng số học sinh lớp 11 nhiều hơn số học sinh lớp 12 là $50\%$ và điểm trung bình của khối 12 cao hơn điểm trung bình của khối 11 là $50\%$. Điểm trung bình của khối 12 là
	

@@TAB@@**A.** $10$@@TAB@@**B.** $11{,@@TAB@@**C.** $12{,@@TAB@@**D.** $15$





% Câu 6



	Điểm thi học kì của một học sinh như sau: $4; 6; 2; 7; 3; 5; 9; 8; 7; 10; 9$. Số trung bình và số trung vị lần lượt là
	

@@TAB@@**A.** $7$ và $6$@@TAB@@**B.** $6{,@@TAB@@**C.** $6{,@@TAB@@**D.** $6$ và $6$





% Câu 7



	Cho các số liệu thống kê về sản lượng chè thu được trong một năm (kg/sào) của 20 hộ gia đình:
	\begin{center}
	\begin{tabular}{cccccccccc}
		111 & 112 & 112 & 113 & 114 & 114 & 115 & 114 & 115 & 116 \\
		112 & 113 & 113 & 114 & 115 & 114 & 116 & 117 & 113 & 115
	\end{tabular}
	\end{center}
	Số trung vị của bảng số liệu thống kê trên là
	

@@TAB@@**A.** $113$@@TAB@@**B.** $114$@@TAB@@**C.** $116$@@TAB@@**D.** $115$





% Câu 8



	Điểm học kì một của một học sinh được cho bởi bảng số liệu sau (đơn vị: điểm):
	\[5;\; 6;\; 6;\; 7;\; 7;\; 8;\; 8;\; 8{,}5;\; 9.\]
	Số trung vị của bảng trên là
	

@@TAB@@**A.** $7$@@TAB@@**B.** $8$@@TAB@@**C.** $9$@@TAB@@**D.** $11$





% Câu 9



	Thống kê điểm kiểm tra môn Lịch sử của 45 học sinh lớp 10A như sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Điểm & 5 & 6 & 7 & 8 & 9 & 10 \\
		\hline
		Số học sinh & 2 & 11 & 9 & 16 & 4 & 3 \\
		\hline
	\end{tabular}
	\end{center}
	Số trung vị trong điểm các bài kiểm tra đó là
	

@@TAB@@**A.** $7{,@@TAB@@**B.** điểm@@TAB@@**C.** $7{,@@TAB@@**D.** điểm





% Câu 10



	Cho bảng số liệu thống kê chiều cao của một nhóm học sinh như sau:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		151 & 152 & 153 & 154 & 155 & 160 & 160 & 162 & 163 & 165 & 165 & 165 & 166 & 167 & 167
	\end{tabular}
	\end{center}
	Số trung vị của bảng số liệu nói trên là
	

@@TAB@@**A.** $160$@@TAB@@**B.** $162$@@TAB@@**C.** $167$@@TAB@@**D.** $161$





% Câu 11



	Cho mẫu số liệu: $5; 13; 5; 7; 10; 2; 3$. Tứ phân vị thứ nhất, thứ hai, thứ ba lần lượt là
	

@@TAB@@**A.** $3; 5; 10$@@TAB@@**B.** $5; 3; 10$@@TAB@@**C.** $10; 3; 5$@@TAB@@**D.** $10; 5; 3$





% Câu 12



	Cho mẫu số liệu: $2; 3; 10; 13; 5; 15; 5; 7$. Tứ phân vị thứ nhất, thứ hai, thứ ba lần lượt là
	

@@TAB@@**A.** $11{,@@TAB@@**B.** $4; 6; 11{,@@TAB@@**C.** $6; 4; 11{,@@TAB@@**D.** $6; 11{,





% Câu 13



	Cho mẫu số liệu: $21; 35; 17; 43; 8; 59; 72; 119$. Tứ phân vị thứ nhất, thứ hai, thứ ba lần lượt là
	

@@TAB@@**A.** $19; 39; 65{,@@TAB@@**B.** $26; 43; 65{,@@TAB@@**C.** $39; 19; 65{,@@TAB@@**D.** $43; 26; 65{,





% Câu 14



	Các giá trị xuất hiện nhiều nhất trong mẫu dữ liệu được gọi là
	

@@TAB@@**A.** Mốt@@TAB@@**B.** Số trung vị@@TAB@@**C.** Số trung bình@@TAB@@**D.** Độ lệch chuẩn





% Câu 15



	Cho bảng phân bố tần số tiền thưởng (triệu đồng) cho cán bộ và nhân viên trong một công ty:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Tiền thưởng & 2 & 3 & 4 & 5 & 6 & Cộng \\
		\hline
		Tần số & 5 & 15 & 10 & 6 & 7 & 43 \\
		\hline
	\end{tabular}
	\end{center}
	Mốt của bảng phân bố tần số đã cho là
	

@@TAB@@**A.** $5\text{ triệu đồng@@TAB@@**B.** $6\text{ triệu đồng@@TAB@@**C.** $3\text{ triệu đồng@@TAB@@**D.** $2\text{ triệu đồng





% Câu 16



	Tiền thưởng (triệu đồng) của cán bộ và nhân viên trong một công ty được cho ở bảng sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Tiền lương & 1 & 2 & 3 & 4 & 5 & Cộng \\
		\hline
		Tần số & 10 & 12 & 11 & 15 & 2 & 50 \\
		\hline
	\end{tabular}
	\end{center}
	Tính mốt $M_o$.
	

@@TAB@@**A.** $M_o = 4$@@TAB@@**B.** $M_o = 5$@@TAB@@**C.** $M_o = 15$@@TAB@@**D.** $M_o = 11$





% Câu 17



	Điểm kiểm tra môn Toán của 35 học sinh lớp 10A được thống kê trong bảng phân bố tần số sau (thang điểm 10):
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		Điểm & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & Cộng \\
		\hline
		Tần số & 2 & 1 & 2 & 1 & 2 & 3 & $x$ & 5 & $y$ & 4 & 3 & $n = 35$ \\
		\hline
	\end{tabular}
	\end{center}
	Biết rằng mẫu số liệu trên có 2 mốt. Giá trị của $x \cdot y$ là
	

@@TAB@@**A.** $36$@@TAB@@**B.** $35$@@TAB@@**C.** $27$@@TAB@@**D.** $32$





% Câu 18



	Cho bảng phân bố tần số sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|}
		\hline
		Giá trị & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ \\
		\hline
		Tần số & 3 & 5 & $n + 6$ & $20 - n$ & 9 \\
		\hline
	\end{tabular}
	\end{center}
	Trong đó $n$ là số tự nhiên và giá trị $x_4$ là mốt duy nhất của bảng số liệu. Tìm số $n$.
	

@@TAB@@**A.** $n \in [0; 7)$@@TAB@@**B.** $n \in [0; 8)$@@TAB@@**C.** $n \in (0; 7)$@@TAB@@**D.** $n \in (0; 7]$





% Câu 19



	Cho bảng phân bố tần số:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|}
		\hline
		Giá trị & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ \\
		\hline
		Tần số & 2 & $x + y$ & $2x - y$ & 5 & 6 \\
		\hline
	\end{tabular}
	\end{center}
	với $x, y$ là các số tự nhiên. Có tất cả bao nhiêu cặp số $(x; y)$ để $x_5$ là mốt của bảng số liệu đã cho?
	

@@TAB@@**A.** $13$@@TAB@@**B.** $12$@@TAB@@**C.** $14$@@TAB@@**D.** $16$





% Câu 20



	Cho bảng phân bố tần số:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|}
		\hline
		Giá trị & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ \\
		\hline
		Tần số & 6 & $3x + y$ & $3y - 3x$ & $x + y$ & 4 \\
		\hline
	\end{tabular}
	\end{center}
	với $x, y$ là các số tự nhiên. Có bao nhiêu cặp số $(x; y)$ để bảng số liệu có mốt là 3 giá trị khác nhau?
	

@@TAB@@**A.** $2$@@TAB@@**B.** $1$@@TAB@@**C.** $3$@@TAB@@**D.** $4$








## PHẦN II. CÂU HỎI TỰ LUẬN


*\small (Học sinh trình bày chi tiết lời giải các bài toán sau)*
\setcounter{ex}{0}

% Bài 1



	**Bài 1.** Khối lượng 30 chi tiết máy được cho bởi bảng sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|}
		\hline
		Khối lượng (gam) & 250 & 300 & 350 & 400 & 450 & 500 & Cộng \\
		\hline
		Tần số & 4 & 4 & 5 & 6 & 4 & 7 & 30 \\
		\hline
	\end{tabular}
	\end{center}
	Tính số trung bình $\overline{x}$ (làm tròn đến chữ số thứ hai sau dấu phẩy) của bảng nói trên.
	




% Bài 2



	**Bài 2.** Bảng số liệu sau đây thống kê thời gian nảy mầm của một loại hạt mới trong các điều kiện khác nhau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Thời gian (phút) & 420 & 440 & 450 & 480 & 500 & 540 \\
		\hline
		Tần số & 8 & 17 & 18 & 16 & 11 & 10 \\
		\hline
	\end{tabular}
	\end{center}
	Tính giá trị trung bình $\overline{x}$ (làm tròn đến hai chữ số sau dấu phẩy) về thời gian nảy mầm loại hạt mới nói trên.
	




% Bài 3



	**Bài 3.** Điều tra số học sinh giỏi khối 10 của 15 trường cấp ba trên địa bàn tỉnh A, ta được bảng số liệu như sau:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		22 & 29 & 29 & 29 & 30 & 31 & 32 & 32 & 33 & 34 & 34 & 35 & 35 & 35 & 36
	\end{tabular}
	\end{center}
	Tính số trung vị của bảng nói trên.
	




% Bài 4



	**Bài 4.** Điều tra số học sinh của 30 lớp học, ta được bảng số liệu như sau:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		35 & 39 & 39 & 40 & 40 & 41 & 41 & 41 & 41 & 44 & 44 & 45 & 45 & 45 & 46 \\
		48 & 48 & 48 & 48 & 49 & 49 & 49 & 49 & 49 & 49 & 50 & 50 & 50 & 50 & 51
	\end{tabular}
	\end{center}
	Tính số trung vị của bảng nói trên.
	




% Bài 5



	**Bài 5.** Tuổi thọ của 30 bóng đèn được thắp thử (đơn vị: giờ) được cho bởi bảng số liệu thống kê dưới đây:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		1180 & 1150 & 1190 & 1170 & 1180 & 1170 & 1160 & 1170 & 1160 & 1150 & 1190 & 1180 & 1170 & 1170 & 1170 \\
		1190 & 1170 & 1170 & 1170 & 1180 & 1170 & 1160 & 1160 & 1160 & 1170 & 1160 & 1180 & 1180 & 1150 & 1170
	\end{tabular}
	\end{center}
	Hãy tính mốt của bảng số liệu thống kê trên.
	




% Bài 6



	**Bài 6.** Kết quả kiểm tra chất lượng đầu năm (thang điểm 30) của 41 học sinh của một lớp được cho bởi bảng số liệu thống kê dưới đây:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		Điểm & 9 & 11 & 14 & 16 & 17 & 18 & 20 & 21 & 23 & 25 & Tổng \\
		\hline
		Tần số & 3 & 7 & 4 & 4 & 6 & 7 & 3 & 3 & 2 & 2 & 41 \\
		\hline
	\end{tabular}
	\end{center}
	Hãy tính mốt của bảng số liệu thống kê trên.
	




% Bài 7



	**Bài 7.** Chiều cao (đơn vị: xăng-ti-mét) của các bạn tổ I ở lớp 10A lần lượt là:
	\[165;\; 155;\; 171;\; 167;\; 159;\; 175;\; 165;\; 160;\; 158.\]
	Đối với mẫu số liệu trên, hãy tìm:
	
		
-  Số trung bình cộng.
		
-  Trung vị.
		
-  Mốt.
		
-  Tứ phân vị.
	
	




% Bài 8



	**Bài 8.** Số đôi giày bán ra trong Quý IV năm 2020 của một cửa hàng được thống kê trong bảng tần số sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|}
		\hline
		Cỡ giày & 37 & 38 & 39 & 40 & 41 & 42 & 43 & 44 \\
		\hline
		Tần số (số đôi bán được) & 40 & 48 & 52 & 70 & 54 & 47 & 28 & 3 \\
		\hline
	\end{tabular}
	\end{center}
	
		
-  Mốt của mẫu số liệu trên là bao nhiêu?
		
-  Cửa hàng đó nên nhập về nhiều hơn cỡ giày nào để bán trong tháng tiếp theo?
	
	




% Bài 9



	**Bài 9.** Cho biết nhiệt độ trung bình các tháng trong năm ở Hà Nội:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		Tháng & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\
		\hline
		Nhiệt độ ($^\circ\text{C}$) & 16,4 & 17,0 & 20,2 & 23,7 & 27,3 & 28,8 & 28,9 & 28,2 & 27,2 & 24,6 & 21,4 & 18,2 \\
		\hline
	\end{tabular}
	\end{center}
	
		
-  Nhiệt độ trung bình trong năm ở Hà Nội là bao nhiêu?
		
-  Nhiệt độ trung bình của tháng có giá trị thấp nhất là bao nhiêu $^\circ\text{C}$? Cao nhất là bao nhiêu $^\circ\text{C}$?
	
	




% Bài 10



	**Bài 10.** Cho biết tổng diện tích rừng từ năm 2008 đến năm 2019 ở nước ta (triệu ha):
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|c|}
		\hline
		Năm & 2008 & 2009 & 2010 & 2011 & 2012 & 2013 & 2014 & 2015 & 2016 & 2017 & 2018 & 2019 \\
		\hline
		DT rừng & 13,1 & 13,2 & 13,4 & 13,5 & 13,9 & 14,0 & 13,8 & 14,1 & 14,4 & 14,4 & 14,5 & 14,6 \\
		\hline
	\end{tabular}
	\end{center}
	
		
-  Diện tích rừng trung bình của nước ta từ năm 2008 đến năm 2019 là bao nhiêu?
		
-  Từ năm 2008 đến năm 2019, diện tích rừng thấp nhất và cao nhất là bao nhiêu triệu héc-ta?
		
-  So với năm 2008, tỉ lệ tổng diện tích rừng năm 2019 tăng lên bao nhiêu phần trăm?
	
	




% Bài 11



	**Bài 11.** Tìm số trung bình, trung vị, mốt và tứ phân vị của mỗi mẫu số liệu sau đây:
	
		
-  Số điểm mà năm vận động viên bóng rổ ghi được trong một trận đấu: $9;\; 8;\; 15;\; 8;\; 20$.
		
-  Giá của một số loại giày (nghìn đồng): $350;\; 300;\; 650;\; 300;\; 450;\; 500;\; 300;\; 250$.
		
-  Số kênh được chiếu của một số hãng truyền hình cáp: $36;\; 38;\; 33;\; 34;\; 32;\; 30;\; 34;\; 35$.
	
	




% Bài 12



	**Bài 12.** Chọn số đặc trưng đo xu thế trung tâm phù hợp cho mỗi mẫu số liệu sau, giải thích và tính giá trị của số đặc trưng đó:
	
		
-  Số mặt trăng đã biết của 8 hành tinh: $0;\; 0;\; 1;\; 2;\; 63;\; 34;\; 27;\; 13$.
		
-  Số đường chuyền thành công của một cầu thủ: $32;\; 24;\; 20;\; 14;\; 23$.
		
-  Chỉ số IQ của nhóm học sinh: $60;\; 72;\; 63;\; 83;\; 68;\; 74;\; 90;\; 86;\; 74;\; 80$.
		
-  Các sai số trong một phép đo: $10;\; 15;\; 18;\; 15;\; 14;\; 13;\; 42;\; 15;\; 12;\; 14;\; 42$.
	
	




% Bài 13



	**Bài 13.** Số lượng học sinh giỏi Quốc gia năm học 2018 - 2019 của 10 trường THPT:
	\[0;\; 0;\; 4;\; 0;\; 0;\; 0;\; 10;\; 0;\; 6;\; 0.\]
	
		
-  Tìm số trung bình, mốt, các tứ phân vị của mẫu số liệu trên.
		
-  Giải thích tại sao tứ phân vị thứ nhất và trung vị trùng nhau.
	
	




% Bài 14



	**Bài 14.** Cho biết số chỗ ngồi của một số sân vận động: Cẩm Phả ($20\,120$), Thiên Trường ($21\,315$), Hàng Đẫy ($23\,405$), Thanh Hóa ($20\,120$), Mỹ Đình ($37\,546$). Các giá trị số trung bình, trung vị, mốt bị ảnh hưởng thế nào nếu bỏ đi số liệu của Sân vận động Quốc gia Mỹ Đình?
	




% Bài 15



	**Bài 15.** Tuổi của 30 bệnh nhân đau mắt hột:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		21 & 17 & 22 & 18 & 20 & 17 & 15 & 13 & 15 & 20 & 15 & 12 & 18 & 17 & 25 \\
		17 & 21 & 15 & 12 & 18 & 16 & 23 & 14 & 18 & 19 & 13 & 16 & 19 & 18 & 17
	\end{tabular}
	\end{center}
	Tính mốt $M_o$ của bảng số liệu đã cho.
	




% Bài 16



	**Bài 16.** Điểm kiểm tra môn Toán của 40 học sinh lớp 11A1 được thống kê như sau:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|}
		\hline
		Điểm & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & Cộng \\
		\hline
		Số học sinh & 2 & 3 & $3n - 8$ & $2n + 4$ & 3 & 2 & 4 & 5 & 40 \\
		\hline
	\end{tabular}
	\end{center}
	Trong đó $n \in \mathbb{N}, n \ge 4$. Tính mốt của bảng số liệu thống kê đã cho.
	




% Bài 17



	**Bài 17.** Cho bảng phân bố tần số:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|}
		\hline
		Giá trị & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ \\
		\hline
		Tần số & 12 & 5 & $n^2$ & 16 & $6n - 5$ \\
		\hline
	\end{tabular}
	\end{center}
	Tìm tất cả các số tự nhiên $n$ để $M_o = x_3$ là mốt duy nhất của bảng phân bố tần số đã cho.
	




% Bài 18



	**Bài 18.** Cho bảng phân bố tần số:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|}
		\hline
		Giá trị & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ \\
		\hline
		Tần số & 5 & 2 & $n$ & $20 - n$ & 8 \\
		\hline
	\end{tabular}
	\end{center}
	Tìm các số tự nhiên $n$ để $M_o = x_4$ là mốt duy nhất của bảng số liệu thống kê đã cho.
	




% Bài 19



	**Bài 19.** Cho bảng phân bố tần số:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|}
		\hline
		Giá trị & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ & $x_6$ \\
		\hline
		Tần số & 5 & $n^2 + 3$ & 3 & $7n - 9$ & $n + 1$ & 7 \\
		\hline
	\end{tabular}
	\end{center}
	Gọi $S$ là tập hợp tất cả các số $n$ nguyên dương sao cho $M_o = x_2$ và $M_o = x_4$ là hai mốt của bảng phân bố tần số đã cho. Tính số phần tử của tập hợp $S$.
	




% Bài 20



	**Bài 20.** Quan sát 9 con chuột chạy qua một mê cung và ghi lại thời gian (phút) của chúng:
	\begin{center}
	\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|}
		\hline
		Con chuột & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
		\hline
		Thời gian chạy & 1 & 2,5 & 3 & 1,5 & 2 & 1,25 & 1 & 0,9 & 30 \\
		\hline
	\end{tabular}
	\end{center}
	
		
-  Tính số trung bình, số trung vị và mốt của thời gian chuột ra khỏi mê cung.
		
-  Trong trường hợp này nên chọn đại lượng nào để thể hiện xu thế trung bình của mẫu?
	
	





---

<p align='center'>**--------- HẾT ---------**</p>
