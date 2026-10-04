
\begin{center}
	{\Large\bfseries\color{blue!80!black} CHƯƠNG V. CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM}\\[6pt]
	{\large\bfseries\color{red!80!black} BÀI 1. SỐ GẦN ĐÚNG VÀ SAI SỐ}
\end{center}




# I. TÓM TẮT LÝ THUYẾT





## 1. Số gần đúng


Trong thực tế, ta thường không biết hoặc khó biết giá trị chính xác (số đúng, kí hiệu $\overline{a}$) mà chỉ tìm được giá trị xấp xỉ nó. Giá trị này được gọi là **số gần đúng**, kí hiệu là $a$.



## 2. Sai số tuyệt đối và sai số tương đối



	
-  **Sai số tuyệt đối:** Giá trị $\Delta_a = |\overline{a} - a|$ phản ánh mức độ sai lệch giữa số đúng $\overline{a}$ và số gần đúng $a$, được gọi là sai số tuyệt đối của số gần đúng $a$.
	
-  **Độ chính xác của số gần đúng:** Nếu $\Delta_a \le d$ thì $a - d \le \overline{a} \le a + d$. Khi đó ta viết $\overline{a} = a \pm d$ và hiểu là số đúng $\overline{a}$ nằm trong đoạn $[a - d; a + d]$. Đại lượng $d > 0$ được gọi là **độ chính xác** của số gần đúng $a$. Giá trị $d$ càng nhỏ thì $a$ càng gần $\overline{a}$.
	
-  **Sai số tương đối:** Tỉ số $\delta_a = \dfrac{\Delta_a}{|a|}$ được gọi là **sai số tương đối** của số gần đúng $a$. Nếu $\overline{a} = a \pm d$ thì $\delta_a \le \dfrac{d}{|a|}$. Tỉ số $\dfrac{d}{|a|}$ càng nhỏ thì chất lượng phép đo càng cao. Người ta thường biểu diễn sai số tương đối dưới dạng phần trăm (\%).




## 3. Quy tròn số gần đúng



	
-  **Quy tắc quy tròn số:**
	\begin{enumerate}
		
-  Đối với chữ số hàng làm tròn: Giữ nguyên nếu chữ số ngay bên phải nó nhỏ hơn 5; tăng 1 đơn vị nếu chữ số ngay bên phải nó lớn hơn hoặc bằng 5.
		
-  Đối với các chữ số sau hàng làm tròn: Bỏ đi nếu ở phần thập phân; thay bởi các chữ số 0 nếu ở phần nguyên.
	
	
-  **Đánh giá sai số khi quy tròn:** Khi thay số đúng bởi số quy tròn đến một hàng nào đó thì sai số tuyệt đối của số quy tròn không vượt quá nửa đơn vị của hàng làm tròn.
	
-  **Quy tắc làm tròn số gần đúng $a$ với độ chính xác $d$:** Khi yêu cầu làm tròn số gần đúng $a$ với độ chính xác $d$, ta làm tròn số $a$ đến hàng cao hơn hàng của độ chính xác một bậc (tức là hàng thấp nhất mà $d$ nhỏ hơn một đơn vị của hàng đó).





# II. CÁC DẠNG TOÁN VÀ VÍ DỤ MINH HỌA





## Dạng 1. Xác định số gần đúng và đánh giá độ chính xác






	**Ví dụ 1.** Đỉnh Everest được mệnh danh là "nóc nhà của thế giới" với nhiều con số từng công bố như: $8848\text{ m}$; $8848{,}13\text{ m}$; $8844{,}43\text{ m}$; $8850\text{ m}$. Hãy giải thích tại sao các con số này đều là số gần đúng.
	







	**Ví dụ 2.** Xác định các thông tin sau là số đúng hay số gần đúng:
	
		
-  Bán kính đường Xích Đạo của Trái Đất là $6\,378\text{ km}$.
		
-  Khoảng cách từ Mặt Trăng đến Trái Đất là $384\,400\text{ km}$.
		
-  $1\text{ m} = 100\text{ cm}$.
	
	







	**Ví dụ 3.** Gọi $d$ là độ dài đường chéo của hình vuông có cạnh bằng 1. Trong hai số $\sqrt{2}$ và $1{,}41$, số nào là số đúng, số nào là số gần đúng của $d$?
	







	**Ví dụ 4.** Giả sử khối lượng đúng của một hộp kẹo là $0{,}85\text{ kg}$. Hai bạn Bình và An cân hộp kẹo này và ghi nhận kết quả lần lượt là $0{,}8\text{ kg}$ và $1\text{ kg}$.
	
		
-  Tìm sai số tuyệt đối của kết quả cân của mỗi bạn.
		
-  Kết quả cân của bạn nào chính xác hơn? Vì sao?
	
	







	**Ví dụ 5.** Người ta dùng một đồng hồ bấm giờ có độ chia nhỏ nhất là $0{,}1\text{ giây}$ để đo thời gian hoàn thành cự li bơi của một vận động viên và được kết quả là $27{,}2\text{ giây}$.
	
		
-  Tìm độ chính xác $d$ của phép đo.
		
-  Nếu thời gian đúng là $a\text{ giây}$, hãy tìm khoảng giá trị mà $a$ có thể nhận được.
	
	






## Dạng 2. Xác định sai số tương đối của số gần đúng






	**Ví dụ 1.** Cho $a = 3{,}14$ là số gần đúng của $\overline{a} = \pi$. Biết $\Delta_a = |\pi - 3{,}14| < 0{,}01$. Đánh giá sai số tương đối của $a$.
	







	**Ví dụ 2.** Một bồn hoa hình tròn có bán kính $r = 0{,}8\text{ m}$. Bạn Ngân lấy giá trị gần đúng $\pi \approx 3{,}1$ được diện tích $S_1$. Bạn Ánh lấy $\pi \approx 3{,}14$ được diện tích $S_2$. So sánh sai số tuyệt đối $\Delta_{S_1}$ và $\Delta_{S_2}$. Bạn nào cho kết quả chính xác hơn?
	







	**Ví dụ 3.** Một tờ giấy A4 có chiều dài $29{,}7\text{ cm}$ và chiều rộng $21\text{ cm}$. Tính độ dài đường chéo tờ giấy và xác định độ chính xác của kết quả khi làm tròn đến hàng phần mười.
	






## Dạng 3. Xác định số quy tròn của số gần đúng với độ chính xác cho trước






	**Ví dụ 1.** Quy tròn số $3{,}141$ đến hàng phần trăm rồi tính sai số tuyệt đối của số quy tròn.
	







	**Ví dụ 2.** 
	
		
-  Làm tròn số $2395{,}3$ đến hàng chục, số $18{,}693$ đến hàng phần trăm và số đúng $d \in [5{,}5; 6{,}5)$ đến hàng đơn vị. Đánh giá sai số tuyệt đối của phép làm tròn số đúng $d$.
		
-  Cho số gần đúng $a = 2{,}53$ với độ chính xác $d = 0{,}01$. Số đúng $\overline{a}$ thuộc đoạn nào? Nếu làm tròn số $a$ thì nên làm tròn đến hàng nào? Vì sao?
	
	







	**Ví dụ 3.** Cho số gần đúng $a = 581\,268$ với độ chính xác $d = 200$. Hãy viết số quy tròn của số $a$.
	







	**Ví dụ 4.** Viết số quy tròn của mỗi số sau với độ chính xác $d$:
	
		
-  $2\,841\,331$ với $d = 400$;
		
-  $4{,}1463$ với $d = 0{,}01$;
		
-  $1{,}4142135$ với $d = 0{,}001$.
	
	






## Dạng 4. Sử dụng máy tính cầm tay để tính toán với số gần đúng






	**Ví dụ 1.** Sử dụng máy tính cầm tay, tính $3^7 \cdot \sqrt{14}$ (trong kết quả lấy bốn chữ số ở phần thập phân).
	







	**Ví dụ 2.** Dùng máy tính cầm tay, tính kết quả của phép tính $\sqrt[3]{15} : 5 - 2$ (trong kết quả lấy hai chữ số ở phần thập phân).
	







	**Ví dụ 3.** Gọi $P$ là chu vi của đường tròn bán kính $1\text{ cm}$. Hãy tìm giá trị gần đúng của $P$ (trong kết quả lấy hai chữ số ở phần thập phân).
	







# III. BÀI TẬP VẬN DỤNG





## PHẦN I. CÂU HỎI TRẮC NGHIỆM


*\small (Mỗi câu học sinh chỉ chọn một phương án trả lời đúng)*
\setcounter{ex}{0}

% Câu 1



	Cho $a$ là số gần đúng của số đúng $\overline{a}$. Khi đó $\Delta_a = |\overline{a} - a|$ được gọi là
	

@@TAB@@**A.** số quy tròn của $\overline{a@@TAB@@**B.** sai số tương đối của số gần đúng $a$@@TAB@@**C.** sai số tuyệt đối của số gần đúng $a$@@TAB@@**D.** số quy tròn của $a$





% Câu 2



	Cho số $a$ là số gần đúng của số $\overline{a}$. Mệnh đề nào sau đây là mệnh đề đúng?
	

@@TAB@@**A.** $a > \overline{a@@TAB@@**B.** $a < \overline{a@@TAB@@**C.** $|\overline{a@@TAB@@**D.** $-a < \overline{a





% Câu 3



	Cho số $a$ là số gần đúng của $\overline{a}$ với độ chính xác $d$. Mệnh đề nào sau đây là mệnh đề đúng?
	

@@TAB@@**A.** $\overline{a@@TAB@@**B.** $\overline{a@@TAB@@**C.** $\overline{a@@TAB@@**D.** $\overline{a





% Câu 4



	Kết quả làm tròn số $b = 500\sqrt{7}$ đến chữ số thập phân thứ hai là
	

@@TAB@@**A.** $b \approx 132{,@@TAB@@**B.** $b \approx 1322{,@@TAB@@**C.** $b \approx 1322{,@@TAB@@**D.** $b \approx 1322{,





% Câu 5



	Kết quả làm tròn của số $c = 76\,324\,753{,}3695$ đến hàng nghìn là
	

@@TAB@@**A.** $c \approx 76\,324\,000$@@TAB@@**B.** $c \approx 76\,325\,000$@@TAB@@**C.** $c \approx 76\,324\,753{,@@TAB@@**D.** $c \approx 76\,324\,753{,





% Câu 6



	Viết số quy tròn của số gần đúng $a = 505\,360{,}996$ biết $\overline{a} = 505\,360{,}996 \pm 100$.
	

@@TAB@@**A.** $a \approx 505$@@TAB@@**B.** $a \approx 5054$@@TAB@@**C.** $a \approx 505\,400$@@TAB@@**D.** $a \approx 505\,000$





% Câu 7



	Viết số quy tròn số gần đúng $b = 3257{,}6254$ với độ chính xác $d = 0{,}01$.
	

@@TAB@@**A.** $b \approx 3257{,@@TAB@@**B.** $b \approx 3257{,@@TAB@@**C.** $b \approx 3257{,@@TAB@@**D.** $b \approx 3257{,





% Câu 8



	Cho giá trị gần đúng của số $\pi$ là $x = 3{,}141592653589$ với độ chính xác $10^{-10}$. Hãy viết số quy tròn của $x$.
	

@@TAB@@**A.** $x \approx 3{,@@TAB@@**B.** $x \approx 3{,@@TAB@@**C.** $x \approx 3{,@@TAB@@**D.** $x \approx 3{,





% Câu 9



	Cho $\overline{a} = 1{,}7059 \pm 0{,}001$, kết quả làm tròn số gần đúng $a = 1{,}7059$ là
	

@@TAB@@**A.** $1{,@@TAB@@**B.** $1{,@@TAB@@**C.** $1{,@@TAB@@**D.** $1{,





% Câu 10



	Cho $\overline{a} = 123\,564 \pm 100$. Kết quả làm tròn số gần đúng $x = 123\,564$ là
	

@@TAB@@**A.** $12360$@@TAB@@**B.** $123\,000$@@TAB@@**C.** $123\,570$@@TAB@@**D.** $124\,000$





% Câu 11



	Số gần đúng $a = 173{,}4592$ có sai số tuyệt đối không vượt quá $0{,}01$. Số quy tròn của $a$ là
	

@@TAB@@**A.** $173{,@@TAB@@**B.** $173{,@@TAB@@**C.** $173{,@@TAB@@**D.** $173$





% Câu 12



	Trong các số dưới đây, giá trị gần đúng của $\sqrt{30} - 5$ với sai số tuyệt đối bé nhất là
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,





% Câu 13



	Nếu lấy $3{,}14$ làm giá trị gần đúng cho số $\pi$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,





% Câu 14



	Nếu lấy $3{,}1416$ làm giá trị gần đúng cho $\pi$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,





% Câu 15



	Cho giá trị gần đúng của $\dfrac{8}{17}$ là $0{,}47$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,





% Câu 16



	Cho giá trị gần đúng của $\dfrac{3}{7}$ là $0{,}429$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,





% Câu 17



	Một vật có thể tích $V = 180{,}37\text{ cm}^3 \pm 0{,}05\text{ cm}^3$. Nếu lấy $180{,}37\text{ cm}^3$ làm giá trị gần đúng cho $V$ thì sai số tương đối của giá trị gần đúng đó không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,





% Câu 18



	Số $\overline{a}$ được cho bởi giá trị gần đúng $a = 5{,}7824$ với sai số tương đối không vượt quá $0{,}05\%$. Khi đó, sai số tuyệt đối của $a$ không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,





% Câu 19



	Cho $\overline{a} = \dfrac{1}{1 + x}$ ($0 < x < 1$). Giả sử ta lấy $a = 1 - x$ làm giá trị gần đúng của $\overline{a}$. Khi đó, sai số tương đối của $a$ theo $x$ bằng
	

@@TAB@@**A.** $\dfrac{x^2@@TAB@@**B.** 1 - x^2@@TAB@@**C.** $\dfrac{x@@TAB@@**D.** 1 - x





% Câu 20



	Các nhà toán học cổ đại Trung Quốc đã dùng phân số $\dfrac{22}{7}$ để xấp xỉ số $\pi$. Hãy đánh giá sai số tuyệt đối $\Delta$ của giá trị gần đúng này, biết $3{,}1415 < \pi < 3{,}1416$.
	

@@TAB@@**A.** $\Delta < 0{,@@TAB@@**B.** $\Delta < 0{,@@TAB@@**C.** $\Delta < 0{,@@TAB@@**D.** $\Delta < 0{,





% Câu 21



	Hình chữ nhật có các cạnh là $x = 2\text{ m} \pm 1\text{ cm}$ và $y = 5\text{ m} \pm 2\text{ cm}$. Diện tích của hình chữ nhật và sai số tương đối của giá trị đó là
	

@@TAB@@**A.** $10\text{ m@@TAB@@**B.** ,@@TAB@@**C.** $10\text{ m@@TAB@@**D.** ,








## PHẦN II. CÂU HỎI TỰ LUẬN


*\small (Học sinh trình bày chi tiết lời giải các bài toán sau)*
\setcounter{ex}{0}

% Bài 1



	**Bài 1.** Một bao gạo ghi thông tin khối lượng là $5 \pm 0{,}2\text{ kg}$.
	
		
-  Xác định khối lượng đúng, khối lượng gần đúng và độ chính xác của bao gạo.
		
-  Khối lượng thực của bao gạo nằm trong đoạn nào?
	
	




% Bài 2



	**Bài 2.** Một phép đo đường kính nhân tế bào cho kết quả là $5 \pm 0{,}3\ \mu\text{m}$. Đường kính thực của nhân tế bào thuộc đoạn nào?
	




% Bài 3



	**Bài 3.** Chiều dài một cái cầu là $\ell = 1745{,}25\text{ m} \pm 0{,}01\text{ m}$.
	
		
-  Xác định chiều dài đúng, chiều dài gần đúng và độ chính xác của cái cầu.
		
-  Chiều dài thực của cái cầu nằm trong đoạn nào?
	
	




% Bài 4



	**Bài 4.** Biết $\sqrt{7} = 2{,}6457513...$
	
		
-  Làm tròn kết quả đến phần mười và ước lượng sai số tuyệt đối.
		
-  Làm tròn kết quả đến phần nghìn và ước lượng sai số tuyệt đối.
	
	




% Bài 5



	**Bài 5.** Ở Babylon, một tấm đất sét có niên đại khoảng $1900 - 1600$ trước Công nguyên đã ghi lại ước lượng số $\pi$ bằng $\dfrac{25}{8} = 3{,}1250$. Hãy ước lượng sai số tuyệt đối và sai số tương đối của giá trị gần đúng này, biết $3{,}141 < \pi < 3{,}142$.
	




% Bài 6



	**Bài 6.** Cho số gần đúng $a = 6547$ với độ chính xác $d = 100$. Hãy viết số quy tròn của số $a$ và ước lượng sai số tương đối của số quy tròn đó.
	




% Bài 7



	**Bài 7.** Cho số gần đúng $a = 23\,748\,023$ với độ chính xác $d = 101$. Hãy viết số quy tròn của số $a$ và ước lượng sai số tương đối của số quy tròn đó.
	




% Bài 8



	**Bài 8.** Cho biết $\sqrt{3} = 1{,}7320508...$ Hãy quy tròn $\sqrt{3}$ đến hàng phần trăm và ước lượng sai số tương đối.
	




% Bài 9



	**Bài 9.** Cho $\overline{a} = \dfrac{1}{1 + x}$ ($0 < x < 1$). Giả sử ta lấy $a = 1 - x$ làm giá trị gần đúng của $\overline{a}$. Hãy tính sai số tương đối của $a$ theo $x$.
	




% Bài 10



	**Bài 10.** Làm tròn các số sau đến chữ số hàng chục:
	
		
			
-  $199$
			
-  $999$
			
-  $9999$
			
-  $2683$
			
-  $1099$
			
-  $12345$
			
-  $123456$
			
-  $43781$
			
-  $454995$
			
-  $14350$
			
-  $99999$
			
-  $987698$
			
-  $3400065$
			
-  $1000587$
			
-  $987654$
			
-  $28051989$
			
-  $2602283$
			
-  $123{,}45$
			
-  $12345{,}67$
			
-  $98765{,}432$
		
	
	




% Bài 11



	**Bài 11.** Làm tròn các số sau đến chữ số hàng trăm:
	
		
			
-  $199$
			
-  $999$
			
-  $9999$
			
-  $1099$
			
-  $2683$
			
-  $12345$
			
-  $43781$
			
-  $14350$
			
-  $1234567$
			
-  $454995$
			
-  $99999$
			
-  $987698$
			
-  $3400065$
			
-  $987654$
			
-  $260283$
			
-  $23456{,}7$
			
-  $12345{,}678$
			
-  $8765{,}432$
			
-  $9999{,}99$
		
	
	




% Bài 12



	**Bài 12.** Làm tròn các số sau đến chữ số hàng nghìn:
	
		
			
-  $12\,345$
			
-  $43\,781$
			
-  $28\,634$
			
-  $21\,999$
			
-  $22\,999$
			
-  $9999$
			
-  $12\,099$
			
-  $454\,995$
			
-  $14\,350$
			
-  $99\,999$
			
-  $987\,698$
			
-  $3\,400\,065$
			
-  $1\,000\,587$
			
-  $987\,654$
			
-  $260\,283$
			
-  $23456{,}7$
			
-  $1\,234\,567$
			
-  $12345{,}678$
			
-  $8765{,}432$
			
-  $9999{,}99$
		
	
	




% Bài 13



	**Bài 13.** Làm tròn các số sau đến hàng phần mười:
	
		
			
-  $10{,}00905$
			
-  $60{,}991$
			
-  $999{,}994$
			
-  $10{,}0456$
			
-  $23{,}0009$
			
-  $99{,}999$
			
-  $90{,}0909$
			
-  $9876{,}1$
			
-  $1234{,}56$
			
-  $98765{,}43$
		
	
	




% Bài 14



	**Bài 14.** Làm tròn các số sau đến hàng phần trăm:
	
		
			
-  $3{,}0468$
			
-  $12{,}3475$
			
-  $0{,}31069$
			
-  $12{,}516$
			
-  $0{,}999$
			
-  $7{,}923$
			
-  $17{,}418$
			
-  $79{,}1364$
			
-  $50{,}401$
			
-  $0{,}155$
			
-  $60{,}996$
			
-  $12{,}349$
			
-  $2{,}9999$
			
-  $123{,}456$
			
-  $98{,}7654$
		
	
	




% Bài 15



	**Bài 15.** Viết số quy tròn của mỗi số sau với độ chính xác $d$:
	
		
-  $1\,234\,567$ với $d = 400$.
		
-  $8{,}7654$ với $d = 0{,}01$.
		
-  $28{,}4156$ với $d = 0{,}001$.
		
-  $1{,}7320508...$ với $d = 0{,}0001$.
	
	




% Bài 16



	**Bài 16.** Hãy viết số quy tròn của:
	
		
-  $a$ biết $\overline{a} = 1\,951\,890 \pm 200$.
		
-  $b$ biết $\overline{b} = 1{,}236 \pm 0{,}002$.
		
-  $c$ biết $\overline{c} = 3{,}1463 \pm 0{,}002$.
	
	




% Bài 17



	**Bài 17.** Chiều dài một cái cầu là $\ell = 1745{,}25\text{ m} \pm 0{,}01\text{ m}$. Hãy viết số quy tròn của số gần đúng $1745{,}25$.
	




% Bài 18



	**Bài 18.** Sử dụng máy tính bỏ túi tính gần đúng các số sau (kết quả lấy 4 chữ số thập phân):
	
		
			
-  $3^7 \cdot \sqrt{14}$
			
-  $\sqrt[3]{15 \cdot 12^4}$
			
-  $\sqrt[3]{15 \cdot 14^4}$
		
	
	




% Bài 19



	**Bài 19.** Thực hiện các phép tính sau trên máy tính cầm tay (trong kết quả lấy 4 chữ số ở phần thập phân):
	
		
			
-  $4^6 \cdot \sqrt{0{,}1}$
			
-  $\sqrt[8]{2{,}1^{18} + 1} - \sqrt{2{,}1^{12} + 1}$
			
-  $\dfrac{1{,}5^3}{\sqrt[3]{6{,}8}}$
		
	
	





---

<p align='center'>**--------- HẾT ---------**</p>
