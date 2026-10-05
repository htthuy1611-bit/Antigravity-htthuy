
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





**Ví dụ 1.** 
	Trong một cuộc thi tìm hiểu lịch sử địa phương, kết quả điểm số của 30 học sinh một lớp được ghi lại trong bảng sau:
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
	





**Câu 1.** 
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






**Câu 2.** 
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






**Câu 3.** 
	Để được cấp chứng chỉ A- Anh văn của một trung tâm ngoại ngữ, học viên phải trải qua 6 lần kiểm tra trắc nghiệm, thang điểm mỗi lần là 100 và phải đạt điểm trung bình từ 70 điểm trở lên. Qua 5 lần thi Minh đạt điểm trung bình là 64,5 điểm. Hỏi trong lần kiểm tra cuối cùng Minh phải đạt ít nhất bao nhiêu điểm để được cấp chứng chỉ?
	

@@TAB@@**A.** $97{,@@TAB@@**B.** $96{,@@TAB@@**C.** $94{,@@TAB@@**D.** $93{,






**Câu 4.** 
	Học sinh tỉnh A (gồm lớp 11 và lớp 12) tham dự kì thi học sinh giỏi Toán của Tỉnh (thang điểm 20) và điểm trung bình của họ là 10. Biết rằng số học sinh lớp 11 nhiều hơn số học sinh lớp 12 là $50\%$ và điểm trung bình của khối 12 cao hơn điểm trung bình của khối 11 là $50\%$. Điểm trung bình của khối 12 là
	

@@TAB@@**A.** $10$@@TAB@@**B.** $11{,@@TAB@@**C.** $12{,@@TAB@@**D.** $15$






**Câu 5.** 
	Điểm thi học kì của một học sinh như sau: $4; 6; 2; 7; 3; 5; 9; 8; 7; 10; 9$. Số trung bình và số trung vị lần lượt là
	

@@TAB@@**A.** $7$ và $6$@@TAB@@**B.** $6{,@@TAB@@**C.** $6{,@@TAB@@**D.** $6$ và $6$






**Câu 6.** 
	Cho các số liệu thống kê về sản lượng chè thu được trong một năm (kg/sào) của 20 hộ gia đình:
	\begin{center}
	\begin{tabular}{cccccccccc}
		111 & 112 & 112 & 113 & 114 & 114 & 115 & 114 & 115 & 116 \\
		112 & 113 & 113 & 114 & 115 & 114 & 116 & 117 & 113 & 115
	\end{tabular}
	\end{center}
	Số trung vị của bảng số liệu thống kê trên là
	

@@TAB@@**A.** $113$@@TAB@@**B.** $114$@@TAB@@**C.** $116$@@TAB@@**D.** $115$






**Câu 7.** 
	Điểm học kì một của một học sinh được cho bởi bảng số liệu sau (đơn vị: điểm):
	\[5;\; 6;\; 6;\; 7;\; 7;\; 8;\; 8;\; 8{,}5;\; 9.\]
	Số trung vị của bảng trên là
	

@@TAB@@**A.** $7$@@TAB@@**B.** $8$@@TAB@@**C.** $9$@@TAB@@**D.** $11$






**Câu 8.** 
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






**Câu 9.** 
	Cho bảng số liệu thống kê chiều cao của một nhóm học sinh như sau:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		151 & 152 & 153 & 154 & 155 & 160 & 160 & 162 & 163 & 165 & 165 & 165 & 166 & 167 & 167
	\end{tabular}
	\end{center}
	Số trung vị của bảng số liệu nói trên là
	

@@TAB@@**A.** $160$@@TAB@@**B.** $162$@@TAB@@**C.** $167$@@TAB@@**D.** $161$






**Câu 10.** 
	Cho mẫu số liệu: $5; 13; 5; 7; 10; 2; 3$. Tứ phân vị thứ nhất, thứ hai, thứ ba lần lượt là
	

@@TAB@@**A.** $3; 5; 10$@@TAB@@**B.** $5; 3; 10$@@TAB@@**C.** $10; 3; 5$@@TAB@@**D.** $10; 5; 3$






**Câu 11.** 
	Cho mẫu số liệu: $2; 3; 10; 13; 5; 15; 5; 7$. Tứ phân vị thứ nhất, thứ hai, thứ ba lần lượt là
	

@@TAB@@**A.** $11{,@@TAB@@**B.** $4; 6; 11{,@@TAB@@**C.** $6; 4; 11{,@@TAB@@**D.** $6; 11{,






**Câu 12.** 
	Cho mẫu số liệu: $21; 35; 17; 43; 8; 59; 72; 119$. Tứ phân vị thứ nhất, thứ hai, thứ ba lần lượt là
	

@@TAB@@**A.** $19; 39; 65{,@@TAB@@**B.** $26; 43; 65{,@@TAB@@**C.** $39; 19; 65{,@@TAB@@**D.** $43; 26; 65{,






**Câu 13.** 
	Các giá trị xuất hiện nhiều nhất trong mẫu dữ liệu được gọi là
	

@@TAB@@**A.** Mốt@@TAB@@**B.** Số trung vị@@TAB@@**C.** Số trung bình@@TAB@@**D.** Độ lệch chuẩn






**Câu 14.** 
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






**Câu 15.** 
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






**Câu 16.** 
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






**Câu 17.** 
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






**Câu 18.** 
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






**Câu 19.** 
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


**Bài 1.** 
	Khối lượng 30 chi tiết máy được cho bởi bảng sau:
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
	\loigiai{
		Khối lượng trung bình của 30 chi tiết máy là:
		\[\overline{x} = \frac{250 \cdot 4 + 300 \cdot 4 + 350 \cdot 5 + 400 \cdot 6 + 450 \cdot 4 + 500 \cdot 7}{30}\]
		\[= \frac{1000 + 1200 + 1750 + 2400 + 1800 + 3500}{30} = \frac{11\,650}{30} \approx 388{,}33\text{ (gam)}.\]
	}





**Bài 2.** 
	Bảng số liệu sau đây thống kê thời gian nảy mầm của một loại hạt mới trong các điều kiện khác nhau:
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
	\loigiai{
		Tổng số hạt theo dõi là:
		\[n = 8 + 17 + 18 + 16 + 11 + 10 = 80.\]
		Thời gian nảy mầm trung bình là:
		\[\overline{x} = \frac{420 \cdot 8 + 440 \cdot 17 + 450 \cdot 18 + 480 \cdot 16 + 500 \cdot 11 + 540 \cdot 10}{80}\]
		\[= \frac{3360 + 7480 + 8100 + 7680 + 5500 + 5400}{80} = \frac{37\,520}{80} = 469\text{ (phút)}.\]
		Kết quả chính xác là $469$ phút (hay $469{,}00$ phút).
	}





**Bài 3.** 
	Điều tra số học sinh giỏi khối 10 của 15 trường cấp ba trên địa bàn tỉnh A, ta được bảng số liệu như sau:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		22 & 29 & 29 & 29 & 30 & 31 & 32 & 32 & 33 & 34 & 34 & 35 & 35 & 35 & 36
	\end{tabular}
	\end{center}
	Tính số trung vị của bảng nói trên.
	\loigiai{
		Mẫu số liệu đã được sắp xếp theo thứ tự không giảm gồm $n = 15$ trường (số lẻ).\\
		Số trung vị là giá trị đứng ở vị trí thứ $\dfrac{15 + 1}{2} = 8$.\\
		Đếm từ trái sang phải, giá trị ở vị trí thứ 8 là $32$.\\
		Vậy số trung vị là $M_e = 32$ học sinh.
	}





**Bài 4.** 
	Điều tra số học sinh của 30 lớp học, ta được bảng số liệu như sau:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		35 & 39 & 39 & 40 & 40 & 41 & 41 & 41 & 41 & 44 & 44 & 45 & 45 & 45 & 46 \\
		48 & 48 & 48 & 48 & 49 & 49 & 49 & 49 & 49 & 49 & 50 & 50 & 50 & 50 & 51
	\end{tabular}
	\end{center}
	Tính số trung vị của bảng nói trên.
	\loigiai{
		Mẫu số liệu gồm $n = 30$ số liệu đã được sắp xếp tăng dần.\\
		Vì $n = 30$ chẵn nên số trung vị là trung bình cộng của hai số liệu ở vị trí thứ $15$ và thứ $16$:\\
		- Giá trị thứ 15 là $46$.\\
		- Giá trị thứ 16 là $48$.\\
		Vậy số trung vị là:
		\[M_e = \frac{46 + 48}{2} = 47\text{ (học sinh)}.\]
	}





**Bài 5.** 
	Tuổi thọ của 30 bóng đèn được thắp thử (đơn vị: giờ) được cho bởi bảng số liệu thống kê dưới đây:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		1180 & 1150 & 1190 & 1170 & 1180 & 1170 & 1160 & 1170 & 1160 & 1150 & 1190 & 1180 & 1170 & 1170 & 1170 \\
		1190 & 1170 & 1170 & 1170 & 1180 & 1170 & 1160 & 1160 & 1160 & 1170 & 1160 & 1180 & 1180 & 1150 & 1170
	\end{tabular}
	\end{center}
	Hãy tính mốt của bảng số liệu thống kê trên.
	\loigiai{
		Ta đếm tần số của từng giá trị tuổi thọ bóng đèn:
		
			
-  Giá trị $1150$: xuất hiện 3 lần.
			
-  Giá trị $1160$: xuất hiện 6 lần.
			
-  Giá trị $1170$: xuất hiện 12 lần.
			
-  Giá trị $1180$: xuất hiện 6 lần.
			
-  Giá trị $1190$: xuất hiện 3 lần.
		
		Giá trị $1170$ xuất hiện nhiều nhất với tần số là 12 lần.\\
		Vậy mốt của bảng số liệu là $M_o = 1170$ giờ.
	}





**Bài 6.** 
	Kết quả kiểm tra chất lượng đầu năm (thang điểm 30) của 41 học sinh của một lớp được cho bởi bảng số liệu thống kê dưới đây:
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
	\loigiai{
		Nhìn vào bảng tần số, tần số lớn nhất là $7$, đạt được tại hai giá trị điểm là $11$ và $18$.\\
		Do đó, mẫu số liệu có 2 mốt là:
		\[M_{o1} = 11\text{ và } M_{o2} = 18.\]
	}





**Bài 7.** 
	Chiều cao (đơn vị: xăng-ti-mét) của các bạn tổ I ở lớp 10A lần lượt là:
	\[165;\; 155;\; 171;\; 167;\; 159;\; 175;\; 165;\; 160;\; 158.\]
	Đối với mẫu số liệu trên, hãy tìm:
	
		
-  Số trung bình cộng.
		
-  Trung vị.
		
-  Mốt.
		
-  Tứ phân vị.
	
	\loigiai{
		Sắp xếp mẫu số liệu theo thứ tự không giảm ($n = 9$):
		\[155;\; 158;\; 159;\; 160;\; \mathbf{165};\; 165;\; 167;\; 171;\; 175.\]
		
			
-  Số trung bình cộng:
			\[\overline{x} = \frac{155 + 158 + 159 + 160 + 165 + 165 + 167 + 171 + 175}{9} = \frac{1475}{9} \approx 163{,}89\text{ (cm)}.\]
			
-  Trung vị: Cỡ mẫu $n = 9$ lẻ nên trung vị là số ở vị trí thứ $5$:
			\[M_e = 165\text{ cm}.\]
			
-  Mốt: Giá trị $165$ xuất hiện 2 lần (nhiều nhất), các giá trị khác xuất hiện 1 lần.
			\[M_o = 165\text{ cm}.\]
			
-  Tứ phân vị:
			
				
-  $Q_2 = M_e = 165\text{ cm}$.
				
-  Nửa dãy dưới: $155, 158, 159, 160 \implies Q_1 = \dfrac{158 + 159}{2} = 158{,}5\text{ cm}$.
				
-  Nửa dãy trên: $165, 167, 171, 175 \implies Q_3 = \dfrac{167 + 171}{2} = 169\text{ cm}$.
			
		
	}





**Bài 8.** 
	Số đôi giày bán ra trong Quý IV năm 2020 của một cửa hàng được thống kê trong bảng tần số sau:
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
	
	\loigiai{
		
			
-  Tần số lớn nhất trong bảng là $70$, ứng với cỡ giày $40$. Vậy mốt của mẫu số liệu là $M_o = 40$.
			
-  Cỡ giày 40 là cỡ giày có sức mua cao nhất (bán chạy nhất), do đó cửa hàng nên ưu tiên nhập về nhiều hơn cỡ giày **40** trong tháng tiếp theo để đáp ứng nhu cầu khách hàng.
		
	}





**Bài 9.** 
	Cho biết nhiệt độ trung bình các tháng trong năm ở Hà Nội:
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
	
	\loigiai{
		
			
-  Nhiệt độ trung bình cả năm (12 tháng) ở Hà Nội là:
			\[\overline{x} = \frac{16{,}4 + 17{,}0 + 20{,}2 + 23{,}7 + 27{,}3 + 28{,}8 + 28{,}9 + 28{,}2 + 27{,}2 + 24{,}6 + 21{,}4 + 18{,}2}{12}\]
			\[= \frac{281{,}9}{12} \approx 23{,}49^\circ\text{C}.\]
			
-  Nhìn vào bảng số liệu:
			
				
-  Nhiệt độ thấp nhất là vào Tháng 1 với $16{,}4^\circ\text{C}$.
				
-  Nhiệt độ cao nhất là vào Tháng 7 với $28{,}9^\circ\text{C}$.
			
		
	}





**Bài 10.** 
	Cho biết tổng diện tích rừng từ năm 2008 đến năm 2019 ở nước ta (triệu ha):
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
	
	\loigiai{
		
			
-  Diện tích rừng trung bình qua 12 năm:
			\[\overline{x} = \frac{13{,}1 + 13{,}2 + 13{,}4 + 13{,}5 + 13{,}9 + 14{,}0 + 13{,}8 + 14{,}1 + 14{,}4 + 14{,}4 + 14{,}5 + 14{,}6}{12}\]
			\[= \frac{166{,}9}{12} \approx 13{,}91\text{ (triệu ha)}.\]
			
-  Giá trị thấp nhất là năm 2008 với $13{,}1\text{ triệu ha}$. Giá trị cao nhất là năm 2019 với $14{,}6\text{ triệu ha}$.
			
-  Tỉ lệ tăng diện tích rừng từ năm 2008 đến năm 2019:
			\[\frac{14{,}6 - 13{,}1}{13{,}1} \times 100\% = \frac{1{,}5}{13{,}1} \times 100\% \approx 11{,}45\%.\]
			Tỉ lệ tăng $11{,}45\%$ sau 11 năm là một mức tăng trưởng tích cực, cho thấy nỗ lực trồng rừng và bảo vệ môi trường đạt kết quả tốt.
		
	}





**Bài 11.** 
	Tìm số trung bình, trung vị, mốt và tứ phân vị của mỗi mẫu số liệu sau đây:
	
		
-  Số điểm mà năm vận động viên bóng rổ ghi được trong một trận đấu: $9;\; 8;\; 15;\; 8;\; 20$.
		
-  Giá của một số loại giày (nghìn đồng): $350;\; 300;\; 650;\; 300;\; 450;\; 500;\; 300;\; 250$.
		
-  Số kênh được chiếu của một số hãng truyền hình cáp: $36;\; 38;\; 33;\; 34;\; 32;\; 30;\; 34;\; 35$.
	
	\loigiai{
		
			
-  Mẫu số liệu: $9, 8, 15, 8, 20$. Sắp xếp: $8, 8, 9, 15, 20$ ($n = 5$).
			
				
-  Số trung bình: $\overline{x} = \dfrac{8 + 8 + 9 + 15 + 20}{5} = \dfrac{60}{5} = 12$.
				
-  Trung vị: $M_e = Q_2 = 9$.
				
-  Mốt: $M_o = 8$ (xuất hiện 2 lần).
				
-  Tứ phân vị: Nửa dưới là $8, 8 \implies Q_1 = 8$. Nửa trên là $15, 20 \implies Q_3 = \dfrac{15 + 20}{2} = 17{,}5$.
			
			
-  Mẫu: $350, 300, 650, 300, 450, 500, 300, 250$. Sắp xếp: $250, 300, 300, 300, 350, 450, 500, 650$ ($n = 8$).
			
				
-  Số trung bình: $\overline{x} = \dfrac{3100}{8} = 387{,}5$ nghìn đồng.
				
-  Trung vị: $M_e = Q_2 = \dfrac{300 + 350}{2} = 325$ nghìn đồng.
				
-  Mốt: $M_o = 300$ nghìn đồng (xuất hiện 3 lần).
				
-  Tứ phân vị: Nửa dưới $250, 300, 300, 300 \implies Q_1 = 300$. Nửa trên $350, 450, 500, 650 \implies Q_3 = \dfrac{450 + 500}{2} = 475$ nghìn đồng.
			
			
-  Mẫu: $36, 38, 33, 34, 32, 30, 34, 35$. Sắp xếp: $30, 32, 33, 34, 34, 35, 36, 38$ ($n = 8$).
			
				
-  Số trung bình: $\overline{x} = \dfrac{282}{8} = 35{,}25$.
				
-  Trung vị: $M_e = Q_2 = \dfrac{34 + 34}{2} = 34$.
				
-  Mốt: $M_o = 34$ (xuất hiện 2 lần).
				
-  Tứ phân vị: Nửa dưới $30, 32, 33, 34 \implies Q_1 = \dfrac{32 + 33}{2} = 32{,}5$. Nửa trên $34, 35, 36, 38 \implies Q_3 = \dfrac{35 + 36}{2} = 35{,}5$.
			
		
	}





**Bài 12.** 
	Chọn số đặc trưng đo xu thế trung tâm phù hợp cho mỗi mẫu số liệu sau, giải thích và tính giá trị của số đặc trưng đó:
	
		
-  Số mặt trăng đã biết của 8 hành tinh: $0;\; 0;\; 1;\; 2;\; 63;\; 34;\; 27;\; 13$.
		
-  Số đường chuyền thành công của một cầu thủ: $32;\; 24;\; 20;\; 14;\; 23$.
		
-  Chỉ số IQ của nhóm học sinh: $60;\; 72;\; 63;\; 83;\; 68;\; 74;\; 90;\; 86;\; 74;\; 80$.
		
-  Các sai số trong một phép đo: $10;\; 15;\; 18;\; 15;\; 14;\; 13;\; 42;\; 15;\; 12;\; 14;\; 42$.
	
	\loigiai{
		
			
-  Mẫu số liệu có sự chênh lệch rất lớn giữa các hành tinh (Mộc tinh có 63, Thổ tinh 34 trong khi Thủy tinh, Kim tinh có 0). Có các giá trị bất thường lớn nên **trung vị** là số đo đại diện phù hợp nhất.\\
			Sắp xếp dãy ($n = 8$): $0, 0, 1, 2, 13, 27, 34, 63 \implies M_e = \dfrac{2 + 13}{2} = 7{,}5$ mặt trăng.
			
-  Các số liệu phân bố tương đối đều, không có giá trị bất thường nên chọn **số trung bình cộng**:
			\[\overline{x} = \frac{32 + 24 + 20 + 14 + 23}{5} = \frac{113}{5} = 22{,}6\text{ (đường chuyền)}.\]
			
-  Mẫu số liệu IQ không có giá trị quá dị biệt nên **số trung bình** là đại diện tốt nhất:
			\[\overline{x} = \frac{60 + 72 + 63 + 83 + 68 + 74 + 90 + 86 + 74 + 80}{10} = \frac{750}{10} = 75.\]
			(Hoặc dùng trung vị $M_e = 74$).
			
-  Mẫu có hai giá trị $42$ lớn bất thường so với phần còn lại (quanh 10 - 18), do đó nên dùng **trung vị**:\\
			Sắp xếp ($n = 11$): $10, 12, 13, 14, 14, \mathbf{15}, 15, 15, 18, 42, 42 \implies M_e = 15$.
		
	}





**Bài 13.** 
	Số lượng học sinh giỏi Quốc gia năm học 2018 - 2019 của 10 trường THPT:
	\[0;\; 0;\; 4;\; 0;\; 0;\; 0;\; 10;\; 0;\; 6;\; 0.\]
	
		
-  Tìm số trung bình, mốt, các tứ phân vị của mẫu số liệu trên.
		
-  Giải thích tại sao tứ phân vị thứ nhất và trung vị trùng nhau.
	
	\loigiai{
		Sắp xếp mẫu số liệu theo thứ tự không giảm ($n = 10$):
		\[0;\; 0;\; 0;\; 0;\; 0;\; 0;\; 0;\; 4;\; 6;\; 10.\]
		
			
-  
			
				
-  Số trung bình: $\overline{x} = \dfrac{0 \cdot 7 + 4 + 6 + 10}{10} = \dfrac{20}{10} = 2$.
				
-  Mốt: $M_o = 0$ (xuất hiện 7 lần).
				
-  Trung vị $Q_2 = \dfrac{0 + 0}{2} = 0$.
				
-  Tứ phân vị: Nửa dưới gồm 5 số $0 \implies Q_1 = 0$. Nửa trên gồm $0, 0, 4, 6, 10 \implies Q_3 = 4$.
			
			
-  Tứ phân vị thứ nhất và trung vị trùng nhau ($Q_1 = Q_2 = 0$) vì trong mẫu số liệu có đa số các giá trị là $0$ (chiếm tới $70\%$ số quan sát), dẫn tới cả vị trí của trung vị nửa dưới và trung vị toàn mẫu đều rơi vào giá trị $0$.
		
	}





**Bài 14.** 
	Cho biết số chỗ ngồi của một số sân vận động: Cẩm Phả ($20\,120$), Thiên Trường ($21\,315$), Hàng Đẫy ($23\,405$), Thanh Hóa ($20\,120$), Mỹ Đình ($37\,546$). Các giá trị số trung bình, trung vị, mốt bị ảnh hưởng thế nào nếu bỏ đi số liệu của Sân vận động Quốc gia Mỹ Đình?
	\loigiai{
		Mẫu ban đầu (5 sân, sắp xếp): $20\,120;\; 20\,120;\; 21\,315;\; 23\,405;\; 37\,546$.\\
		- Số trung bình ban đầu: $\overline{x} = \dfrac{122\,506}{5} = 24\,501{,}2$.\\
		- Trung vị ban đầu: $M_e = 21\,315$.\\
		- Mốt ban đầu: $M_o = 20\,120$.\\
		Khi bỏ đi sân Mỹ Đình ($37\,546$ chỗ - giá trị lớn nhất): Mẫu còn 4 sân: $20\,120;\; 20\,120;\; 21\,315;\; 23\,405$.\\
		- Số trung bình mới: $\overline{x}' = \dfrac{84\,960}{4} = 21\,240$ (giảm mạnh từ $24\,501{,}2$ xuống $21\,240$, giảm $3261{,}2$).\\
		- Trung vị mới: $M_e' = \dfrac{20\,120 + 21\,315}{2} = 20\,717{,}5$ (giảm nhẹ từ $21\,315$ xuống $20\,717{,}5$).\\
		- Mốt mới: $M_o' = 20\,120$ (không đổi).\\
		**Kết luận:** Số trung bình bị ảnh hưởng nhiều nhất (giảm mạnh), trung vị bị ảnh hưởng ít hơn, mốt không bị ảnh hưởng.
	}





**Bài 15.** 
	Tuổi của 30 bệnh nhân đau mắt hột:
	\begin{center}
	\begin{tabular}{ccccccccccccccc}
		21 & 17 & 22 & 18 & 20 & 17 & 15 & 13 & 15 & 20 & 15 & 12 & 18 & 17 & 25 \\
		17 & 21 & 15 & 12 & 18 & 16 & 23 & 14 & 18 & 19 & 13 & 16 & 19 & 18 & 17
	\end{tabular}
	\end{center}
	Tính mốt $M_o$ của bảng số liệu đã cho.
	\loigiai{
		Đếm số lần xuất hiện của các độ tuổi:
		
			
-  Tuổi 12: 2 người; Tuổi 13: 2 người; Tuổi 14: 1 người; Tuổi 15: 4 người; Tuổi 16: 2 người;
			
-  Tuổi 17: 5 người; Tuổi 18: 5 người; Tuổi 19: 2 người; Tuổi 20: 2 người; Tuổi 21: 2 người;
			
-  Tuổi 22: 1 người; Tuổi 23: 1 người; Tuổi 25: 1 người.
		
		Hai độ tuổi $17$ và $18$ cùng có tần số xuất hiện cao nhất là 5 lần.\\
		Vậy bảng số liệu có 2 mốt: $M_{o1} = 17$ tuổi và $M_{o2} = 18$ tuổi.
	}





**Bài 16.** 
	Điểm kiểm tra môn Toán của 40 học sinh lớp 11A1 được thống kê như sau:
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
	\loigiai{
		Tổng số học sinh là 40, do đó:
		\[2 + 3 + (3n - 8) + (2n + 4) + 3 + 2 + 4 + 5 = 40 \iff 5n + 11 = 40 \iff 5n = 29.\]
		Wait: $2+3-8+4+3+2+4+5 = 11$. $5n = 29 \implies n$ không nguyên. Ta kiểm tra lại đề bài:\\
		Nếu đề in tổng là 40, kiểm tra hệ số: $3n - 8 + 2n + 4 = 5n - 4$. Tổng các số còn lại: $2 + 3 + 3 + 2 + 4 + 5 = 19$. $19 + 5n - 4 = 5n + 15 = 40 \iff 5n = 25 \iff n = 5$ (thỏa mãn $n \in \mathbb{N}, n \ge 4$).\\
		Với $n = 5$:\\
		- Số học sinh đạt điểm 5 là: $3(5) - 8 = 7$.\\
		- Số học sinh đạt điểm 6 là: $2(5) + 4 = 14$.\\
		Tần số lớn nhất trong bảng là $14$, ứng với điểm 6.\\
		Vậy mốt của bảng số liệu là $M_o = 6$ điểm.
	}





**Bài 17.** 
	Cho bảng phân bố tần số:
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
	\loigiai{
		Để $M_o = x_3$ là mốt duy nhất thì tần số $n^2$ của $x_3$ phải lớn hơn hẳn tần số của tất cả các giá trị còn lại:\\
		1) $n^2 > 16 \iff n > 4$ (vì $n \in \mathbb{N}$).\\
		2) $n^2 > 12$ (thỏa mãn khi $n > 4$).\\
		3) $n^2 > 6n - 5 \iff n^2 - 6n + 5 > 0 \iff (n - 1)(n - 5) > 0 \iff n < 1$ hoặc $n > 5$.\\
		Kết hợp các điều kiện trên với $n \in \mathbb{N}$:\\
		Ta cần $n > 4$ và $(n < 1 \text{ hoặc } n > 5) \implies n > 5$.\\
		Đồng thời tần số $6n - 5 \ge 0 \iff n \ge 1$ (thỏa mãn khi $n > 5$).\\
		Vậy tất cả các số tự nhiên $n \ge 6$ (tức $n \in \{6, 7, 8, \ldots\}$) thì $x_3$ là mốt duy nhất.
	}





**Bài 18.** 
	Cho bảng phân bố tần số:
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
	\loigiai{
		Để $x_4$ là mốt duy nhất thì tần số $20 - n$ của $x_4$ phải lớn hơn hẳn tần số của các giá trị khác:\\
		1) $20 - n > 8 \iff n < 12$.\\
		2) $20 - n > n \iff 2n < 20 \iff n < 10$.\\
		3) $20 - n > 5 \iff n < 15$.\\
		4) $20 - n > 2 \iff n < 18$.\\
		Vì các tần số phải không âm: $n \ge 0$ và $20 - n \ge 0 \implies 0 \le n \le 20$.\\
		Do đó ta cần $0 \le n < 10$.\\
		Vì $n \in \mathbb{N}$ nên $n \in \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.
	}





**Bài 19.** 
	Cho bảng phân bố tần số:
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
	\loigiai{
		Để $x_2$ và $x_4$ là hai mốt của bảng số liệu thì tần số của chúng phải bằng nhau và lớn hơn tần số của tất cả các giá trị còn lại:\\
		1) $n^2 + 3 = 7n - 9 \iff n^2 - 7n + 12 = 0 \iff (n - 3)(n - 4) = 0 \iff n = 3$ hoặc $n = 4$.\\
		Kiểm tra từng giá trị:\\
		- Với $n = 3$:\\
		Tần số $x_2 = 3^2 + 3 = 12$; tần số $x_4 = 7(3) - 9 = 12$.\\
		Tần số $x_5 = 3 + 1 = 4$.\\
		Các tần số khác là $5, 3, 7$ đều $< 12$. Do đó $x_2, x_4$ là 2 mốt duy nhất (thỏa mãn).\\
		- Với $n = 4$:\\
		Tần số $x_2 = 4^2 + 3 = 19$; tần số $x_4 = 7(4) - 9 = 19$.\\
		Tần số $x_5 = 4 + 1 = 5$.\\
		Các tần số khác là $5, 3, 7$ đều $< 19$. Do đó $x_2, x_4$ là 2 mốt duy nhất (thỏa mãn).\\
		Vậy tập hợp $S = \{3; 4\}$, số phần tử của tập $S$ là 2.
	}





**Bài 20.** 
	Quan sát 9 con chuột chạy qua một mê cung và ghi lại thời gian (phút) của chúng:
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
	
	\loigiai{
		Sắp xếp thời gian chạy theo thứ tự không giảm ($n = 9$):
		\[0{,}9;\; 1;\; 1;\; 1{,}25;\; \mathbf{1{,}5};\; 2;\; 2{,}5;\; 3;\; 30.\]
		
			
-  
			
				
-  Số trung bình:
				\[\overline{x} = \frac{0{,}9 + 1 + 1 + 1{,}25 + 1{,}5 + 2 + 2{,}5 + 3 + 30}{9} = \frac{43{,}15}{9} \approx 4{,}79\text{ (phút)}.\]
				
-  Số trung vị: $n = 9$ lẻ nên trung vị là số ở vị trí thứ $5$:
				\[M_e = 1{,}5\text{ phút}.\]
				
-  Mốt: Giá trị $1$ phút xuất hiện 2 lần:
				\[M_o = 1\text{ phút}.\]
			
			
-  Trong mẫu số liệu này có giá trị $30$ phút lớn bất thường so với các con chuột khác (chỉ chạy từ $0{,}9$ đến $3$ phút), làm cho số trung bình $\overline{x} \approx 4{,}79$ phút bị kéo lên cao và không phản ánh đúng năng lực chung của bầy chuột. Vì vậy, ta nên chọn **trung vị ($M_e = 1{,**5$ phút)} để đại diện cho xu thế trung tâm của mẫu số liệu.
		
	}





---

<p align='center'>**--------- HẾT ---------**</p>
