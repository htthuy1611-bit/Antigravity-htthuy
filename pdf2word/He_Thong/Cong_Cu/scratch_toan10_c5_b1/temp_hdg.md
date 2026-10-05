
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





**Ví dụ 1.** 
	Đỉnh Everest được mệnh danh là "nóc nhà của thế giới" với nhiều con số từng công bố như: $8848\text{ m}$; $8848{,}13\text{ m}$; $8844{,}43\text{ m}$; $8850\text{ m}$. Hãy giải thích tại sao các con số này đều là số gần đúng.
	

**Lời giải.**


		Chiều cao của đỉnh Everest là một đại lượng vật lí biến đổi liên tục theo thời gian (do lớp băng tuyết dày mỏng theo mùa, do sự dịch chuyển của mảng kiến tạo Trái Đất) và kết quả đo đạc phụ thuộc vào công nghệ, thiết bị đo tại từng thời điểm. Do đó, các con số được công bố đều chỉ là các giá trị xấp xỉ chiều cao thực tế tại thời điểm đo, tức là các **số gần đúng**.
	}






**Ví dụ 2.** 
	Xác định các thông tin sau là số đúng hay số gần đúng:
	
		
-  Bán kính đường Xích Đạo của Trái Đất là $6\,378\text{ km}$.
		
-  Khoảng cách từ Mặt Trăng đến Trái Đất là $384\,400\text{ km}$.
		
-  $1\text{ m} = 100\text{ cm}$.
	
	\loigiai{
		
			
-  "Bán kính đường Xích Đạo của Trái Đất là $6\,378\text{ km}$" là **số gần đúng** vì bề mặt Trái Đất không phải là hình cầu hoàn hảo và giá trị đo đạc luôn có sai số.
			
-  "Khoảng cách từ Mặt Trăng đến Trái Đất là $384\,400\text{ km}$" là **số gần đúng** vì quỹ đạo Mặt Trăng là hình elip nên khoảng cách thay đổi liên tục.
			
-  "$1\text{ m} = 100\text{ cm}$" là **số đúng** vì đây là định nghĩa quy ước chuẩn trong hệ đo lường quốc tế SI.
		
	}






**Ví dụ 3.** 
	Gọi $d$ là độ dài đường chéo của hình vuông có cạnh bằng 1. Trong hai số $\sqrt{2}$ và $1{,}41$, số nào là số đúng, số nào là số gần đúng của $d$?
	\loigiai{
		Theo định lí Pythagore, độ dài đường chéo của hình vuông cạnh 1 là $d = \sqrt{1^2 + 1^2} = \sqrt{2}$.\\
		- Số $\sqrt{2}$ là **số đúng** biểu diễn độ dài chính xác của đường chéo.\\
		- Số $1{,}41$ là **số gần đúng** của $\sqrt{2}$ (vì $\sqrt{2} = 1{,}41421356...$).
	}






**Ví dụ 4.** 
	Giả sử khối lượng đúng của một hộp kẹo là $0{,}85\text{ kg}$. Hai bạn Bình và An cân hộp kẹo này và ghi nhận kết quả lần lượt là $0{,}8\text{ kg}$ và $1\text{ kg}$.
	
		
-  Tìm sai số tuyệt đối của kết quả cân của mỗi bạn.
		
-  Kết quả cân của bạn nào chính xác hơn? Vì sao?
	
	\loigiai{
		
			
-  Sai số tuyệt đối của kết quả cân của bạn Bình:
			\[\Delta_{\text{Bình}} = |0{,}85 - 0{,}8| = 0{,}05\text{ kg}.\]
			Sai số tuyệt đối của kết quả cân của bạn An:
			\[\Delta_{\text{An}} = |0{,}85 - 1| = 0{,}15\text{ kg}.\]
			
-  Vì $\Delta_{\text{Bình}} = 0{,}05\text{ kg} < 0{,}15\text{ kg} = \Delta_{\text{An}}$ nên kết quả cân của bạn Bình chính xác hơn kết quả của bạn An.
		
	}






**Ví dụ 5.** 
	Người ta dùng một đồng hồ bấm giờ có độ chia nhỏ nhất là $0{,}1\text{ giây}$ để đo thời gian hoàn thành cự li bơi của một vận động viên và được kết quả là $27{,}2\text{ giây}$.
	
		
-  Tìm độ chính xác $d$ của phép đo.
		
-  Nếu thời gian đúng là $a\text{ giây}$, hãy tìm khoảng giá trị mà $a$ có thể nhận được.
	
	\loigiai{
		
			
-  Sai số dụng cụ thông thường không vượt quá một độ chia nhỏ nhất (hoặc nửa độ chia nhỏ nhất). Theo quy ước thông thường trong đo lường, độ chính xác của phép đo lấy bằng độ chia nhỏ nhất: $d = 0{,}1\text{ s}$ (hoặc lấy bằng nửa độ chia: $d = 0{,}05\text{ s}$).
			
-  Nếu lấy $d = 0{,}1\text{ s}$ thì thời gian đúng $a$ thỏa mãn:
			\[27{,}2 - 0{,}1 \le a \le 27{,}2 + 0{,}1 \iff 27{,}1 \le a \le 27{,}3\text{ (giây)}.\]
			Nếu lấy $d = 0{,}05\text{ s}$ (nửa độ chia) thì $27{,}15 \le a \le 27{,}25\text{ (giây)}$.
		
	}






## Dạng 2. Xác định sai số tương đối của số gần đúng





**Ví dụ 6.** 
	Cho $a = 3{,}14$ là số gần đúng của $\overline{a} = \pi$. Biết $\Delta_a = |\pi - 3{,}14| < 0{,}01$. Đánh giá sai số tương đối của $a$.
	\loigiai{
		Ta có độ chính xác $d = 0{,}01$. Sai số tương đối của số gần đúng $a = 3{,}14$ thỏa mãn:
		\[\delta_a = \frac{\Delta_a}{|a|} \le \frac{d}{|a|} = \frac{0{,}01}{3{,}14} \approx 0{,}00318 = 0{,}318\%.\]
	}






**Ví dụ 7.** 
	Một bồn hoa hình tròn có bán kính $r = 0{,}8\text{ m}$. Bạn Ngân lấy giá trị gần đúng $\pi \approx 3{,}1$ được diện tích $S_1$. Bạn Ánh lấy $\pi \approx 3{,}14$ được diện tích $S_2$. So sánh sai số tuyệt đối $\Delta_{S_1}$ và $\Delta_{S_2}$. Bạn nào cho kết quả chính xác hơn?
	\loigiai{
		Diện tích đúng của bồn hoa là $S = \pi r^2 = \pi \cdot (0{,}8)^2 = 0{,}64\pi\text{ m}^2$.\\
		- Kết quả của bạn Ngân: $S_1 = 3{,}1 \cdot 0{,}64 = 1{,}984\text{ m}^2$. Sai số tuyệt đối:
		\[\Delta_{S_1} = |S - S_1| = 0{,}64 \cdot |\pi - 3{,}1| \approx 0{,}64 \cdot 0{,}04159 = 0{,}0266\text{ m}^2.\]
		- Kết quả của bạn Ánh: $S_2 = 3{,}14 \cdot 0{,}64 = 2{,}0096\text{ m}^2$. Sai số tuyệt đối:
		\[\Delta_{S_2} = |S - S_2| = 0{,}64 \cdot |\pi - 3{,}14| \approx 0{,}64 \cdot 0{,}00159 = 0{,}0010\text{ m}^2.\]
		Vì $\Delta_{S_2} < \Delta_{S_1}$ nên bạn Ánh cho kết quả chính xác hơn bạn Ngân.
	}






**Ví dụ 8.** 
	Một tờ giấy A4 có chiều dài $29{,}7\text{ cm}$ và chiều rộng $21\text{ cm}$. Tính độ dài đường chéo tờ giấy và xác định độ chính xác của kết quả khi làm tròn đến hàng phần mười.
	\loigiai{
		Độ dài đúng của đường chéo là:
		\[d = \sqrt{29{,}7^2 + 21^2} = \sqrt{882{,}09 + 441} = \sqrt{1323{,}09} \approx 36{,}3743\text{ cm}.\]
		Làm tròn đến hàng phần mười ta được số gần đúng là $36{,}4\text{ cm}$.\\
		Sai số tuyệt đối của phép làm tròn không vượt quá nửa đơn vị hàng làm tròn: $\Delta \le 0{,}05\text{ cm}$.\\
		Vậy độ chính xác của kết quả làm tròn là $d = 0{,}05\text{ cm}$.
	}






## Dạng 3. Xác định số quy tròn của số gần đúng với độ chính xác cho trước





**Ví dụ 9.** 
	Quy tròn số $3{,}141$ đến hàng phần trăm rồi tính sai số tuyệt đối của số quy tròn.
	\loigiai{
		Chữ số hàng phần trăm là $4$, chữ số ngay bên phải là $1 < 5$ nên ta giữ nguyên chữ số hàng phần trăm và bỏ chữ số sau đó.\\
		Số quy tròn là $3{,}14$.\\
		Sai số tuyệt đối của số quy tròn:
		\[\Delta = |3{,}141 - 3{,}14| = 0{,}001.\]
	}






**Ví dụ 10.** 
	
		
-  Làm tròn số $2395{,}3$ đến hàng chục, số $18{,}693$ đến hàng phần trăm và số đúng $d \in [5{,}5; 6{,}5)$ đến hàng đơn vị. Đánh giá sai số tuyệt đối của phép làm tròn số đúng $d$.
		
-  Cho số gần đúng $a = 2{,}53$ với độ chính xác $d = 0{,}01$. Số đúng $\overline{a}$ thuộc đoạn nào? Nếu làm tròn số $a$ thì nên làm tròn đến hàng nào? Vì sao?
	
	\loigiai{
		
			
-  Làm tròn $2395{,}3$ đến hàng chục: vì chữ số hàng đơn vị là $5$ nên tăng hàng chục thêm 1 đơn vị $\implies 2400$.\\
			Làm tròn $18{,}693$ đến hàng phần trăm: chữ số hàng phần nghìn là $3 < 5$ nên giữ nguyên $\implies 18{,}69$.\\
			Với mọi số đúng $d \in [5{,}5; 6{,}5)$, khi làm tròn đến hàng đơn vị ta đều được kết quả là $6$ (vì phần thập phân luôn $\ge 0{,}5$ và $< 1{,}5$). Sai số tuyệt đối của phép làm tròn này thỏa mãn:
			\[\Delta = |d - 6| \le 0{,}5.\]
			
-  Vì $\overline{a} = 2{,}53 \pm 0{,}01$ nên số đúng $\overline{a}$ thuộc đoạn:
			\[[2{,}53 - 0{,}01; 2{,}53 + 0{,}01] = [2{,}52; 2{,}54].\]
			Độ chính xác $d = 0{,}01$ ở hàng phần trăm, do đó chữ số hàng phần trăm trong số gần đúng chưa đáng tin cậy. Vì vậy, ta nên làm tròn số $a$ đến **hàng phần mười** (hàng cao hơn hàng của $d$ một bậc). Khi đó số quy tròn là $2{,}5$.
		
	}






**Ví dụ 11.** 
	Cho số gần đúng $a = 581\,268$ với độ chính xác $d = 200$. Hãy viết số quy tròn của số $a$.
	\loigiai{
		Độ chính xác $d = 200$ thỏa mãn $100 \le d < 1000$, tức là hàng của độ chính xác là hàng trăm. Do đó ta làm tròn số $a$ đến **hàng nghìn**.\\
		Chữ số hàng nghìn là $1$, chữ số ngay sau nó (hàng trăm) là $2 < 5$ nên giữ nguyên.\\
		Vậy số quy tròn của $a$ là $581\,000$.
	}






**Ví dụ 12.** 
	Viết số quy tròn của mỗi số sau với độ chính xác $d$:
	
		
-  $2\,841\,331$ với $d = 400$;
		
-  $4{,}1463$ với $d = 0{,}01$;
		
-  $1{,}4142135$ với $d = 0{,}001$.
	
	\loigiai{
		
			
-  Với $d = 400$ ($100 \le d < 1000$, hàng trăm), ta làm tròn đến hàng nghìn. Chữ số hàng trăm là $3 < 5$ nên số quy tròn là $2\,841\,000$.
			
-  Với $d = 0{,}01$ (hàng phần trăm), ta làm tròn đến hàng phần mười. Chữ số hàng phần trăm là $4 < 5$ nên số quy tròn là $4{,}1$.
			
-  Với $d = 0{,}001$ (hàng phần nghìn), ta làm tròn đến hàng phần trăm. Chữ số hàng phần nghìn là $4 < 5$ nên số quy tròn là $1{,}41$.
		
	}






## Dạng 4. Sử dụng máy tính cầm tay để tính toán với số gần đúng





**Ví dụ 13.** 
	Sử dụng máy tính cầm tay, tính $3^7 \cdot \sqrt{14}$ (trong kết quả lấy bốn chữ số ở phần thập phân).
	\loigiai{
		Nhập vào máy tính biểu thức $3^7 \times \sqrt{14}$ ta được kết quả hiển thị xấp xỉ:\\
		$3^7 \cdot \sqrt{14} = 2187 \cdot \sqrt{14} \approx 8182{,}806847...$\\
		Lấy bốn chữ số ở phần thập phân (làm tròn đến hàng phần chục nghìn): kết quả là **$8182{,**8068$}.
	}






**Ví dụ 14.** 
	Dùng máy tính cầm tay, tính kết quả của phép tính $\sqrt[3]{15} : 5 - 2$ (trong kết quả lấy hai chữ số ở phần thập phân).
	\loigiai{
		Thực hiện bấm máy tính biểu thức $\sqrt[3]{15} \div 5 - 2$:\\
		Ta có $\sqrt[3]{15} \approx 2{,}466212 \implies \dfrac{\sqrt[3]{15}}{5} \approx 0{,}493242$.\\
		Do đó $\sqrt[3]{15} : 5 - 2 \approx 0{,}493242 - 2 = -1{,}506757...$\\
		Làm tròn đến hai chữ số ở phần thập phân (chữ số thứ ba là $6 \ge 5$): kết quả là **$-1{,**51$}.
	}






**Ví dụ 15.** 
	Gọi $P$ là chu vi của đường tròn bán kính $1\text{ cm}$. Hãy tìm giá trị gần đúng của $P$ (trong kết quả lấy hai chữ số ở phần thập phân).
	\loigiai{
		Chu vi đường tròn bán kính $R = 1\text{ cm}$ là $P = 2\pi R = 2\pi\text{ cm}$.\\
		Sử dụng máy tính bấm $2 \times \pi$ ta được $P \approx 6{,}283185...$\\
		Lấy hai chữ số ở phần thập phân: kết quả là **$6{,**28\text{ cm}$}.
	}







# III. BÀI TẬP VẬN DỤNG





## PHẦN I. CÂU HỎI TRẮC NGHIỆM


*\small (Mỗi câu học sinh chỉ chọn một phương án trả lời đúng)*
\setcounter{ex}{0}


**Câu 1.** 
	Cho $a$ là số gần đúng của số đúng $\overline{a}$. Khi đó $\Delta_a = |\overline{a} - a|$ được gọi là
	

@@TAB@@**A.** số quy tròn của $\overline{a@@TAB@@**B.** sai số tương đối của số gần đúng $a$@@TAB@@@@CHON@@**C.** sai số tuyệt đối của số gần đúng $a$@@CHON@@@@TAB@@**D.** số quy tròn của $a$

\loigiai{
		Theo định nghĩa, sai số tuyệt đối của số gần đúng $a$ là $\Delta_a = |\overline{a} - a|$.\\
		Chọn **C**.
	







**Câu 2.** 
	Cho số $a$ là số gần đúng của số $\overline{a}$. Mệnh đề nào sau đây là mệnh đề đúng?
	

@@TAB@@**A.** $a > \overline{a@@TAB@@**B.** $a < \overline{a@@TAB@@@@CHON@@**C.** $|\overline{a@@CHON@@@@TAB@@**D.** $-a < \overline{a






**Câu 3.** 
	Cho số $a$ là số gần đúng của $\overline{a}$ với độ chính xác $d$. Mệnh đề nào sau đây là mệnh đề đúng?
	

@@TAB@@**A.** $\overline{a@@TAB@@**B.** $\overline{a@@TAB@@**C.** $\overline{a@@TAB@@@@CHON@@**D.** $\overline{a@@CHON@@






**Câu 4.** 
	Kết quả làm tròn số $b = 500\sqrt{7}$ đến chữ số thập phân thứ hai là
	

@@TAB@@**A.** $b \approx 132{,@@TAB@@@@CHON@@**B.** $b \approx 1322{,@@CHON@@@@TAB@@**C.** $b \approx 1322{,@@TAB@@**D.** $b \approx 1322{,






**Câu 5.** 
	Kết quả làm tròn của số $c = 76\,324\,753{,}3695$ đến hàng nghìn là
	

@@TAB@@**A.** $c \approx 76\,324\,000$@@TAB@@@@CHON@@**B.** $c \approx 76\,325\,000$@@CHON@@@@TAB@@**C.** $c \approx 76\,324\,753{,@@TAB@@**D.** $c \approx 76\,324\,753{,






**Câu 6.** 
	Viết số quy tròn của số gần đúng $a = 505\,360{,}996$ biết $\overline{a} = 505\,360{,}996 \pm 100$.
	

@@TAB@@**A.** $a \approx 505$@@TAB@@**B.** $a \approx 5054$@@TAB@@**C.** $a \approx 505\,400$@@TAB@@@@CHON@@**D.** $a \approx 505\,000$@@CHON@@






**Câu 7.** 
	Viết số quy tròn số gần đúng $b = 3257{,}6254$ với độ chính xác $d = 0{,}01$.
	

@@TAB@@**A.** $b \approx 3257{,@@TAB@@**B.** $b \approx 3257{,@@TAB@@@@CHON@@**C.** $b \approx 3257{,@@CHON@@@@TAB@@**D.** $b \approx 3257{,






**Câu 8.** 
	Cho giá trị gần đúng của số $\pi$ là $x = 3{,}141592653589$ với độ chính xác $10^{-10}$. Hãy viết số quy tròn của $x$.
	

@@TAB@@@@CHON@@**A.** $x \approx 3{,@@CHON@@@@TAB@@**B.** $x \approx 3{,@@TAB@@**C.** $x \approx 3{,@@TAB@@**D.** $x \approx 3{,






**Câu 9.** 
	Cho $\overline{a} = 1{,}7059 \pm 0{,}001$, kết quả làm tròn số gần đúng $a = 1{,}7059$ là
	

@@TAB@@@@CHON@@**A.** $1{,@@CHON@@@@TAB@@**B.** $1{,@@TAB@@**C.** $1{,@@TAB@@**D.** $1{,






**Câu 10.** 
	Cho $\overline{a} = 123\,564 \pm 100$. Kết quả làm tròn số gần đúng $x = 123\,564$ là
	

@@TAB@@**A.** $12360$@@TAB@@**B.** $123\,000$@@TAB@@**C.** $123\,570$@@TAB@@@@CHON@@**D.** $124\,000$@@CHON@@






**Câu 11.** 
	Số gần đúng $a = 173{,}4592$ có sai số tuyệt đối không vượt quá $0{,}01$. Số quy tròn của $a$ là
	

@@TAB@@**A.** $173{,@@TAB@@**B.** $173{,@@TAB@@@@CHON@@**C.** $173{,@@CHON@@@@TAB@@**D.** $173$






**Câu 12.** 
	Trong các số dưới đây, giá trị gần đúng của $\sqrt{30} - 5$ với sai số tuyệt đối bé nhất là
	

@@TAB@@**A.** $0{,@@TAB@@@@CHON@@**B.** $0{,@@CHON@@@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,






**Câu 13.** 
	Nếu lấy $3{,}14$ làm giá trị gần đúng cho số $\pi$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@@@CHON@@**A.** $0{,@@CHON@@@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,






**Câu 14.** 
	Nếu lấy $3{,}1416$ làm giá trị gần đúng cho $\pi$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@**B.** $0{,@@TAB@@@@CHON@@**C.** $0{,@@CHON@@@@TAB@@**D.** $0{,






**Câu 15.** 
	Cho giá trị gần đúng của $\dfrac{8}{17}$ là $0{,}47$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@@@CHON@@**A.** $0{,@@CHON@@@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,






**Câu 16.** 
	Cho giá trị gần đúng của $\dfrac{3}{7}$ là $0{,}429$ thì sai số tuyệt đối không vượt quá
	

@@TAB@@**A.** $0{,@@TAB@@@@CHON@@**B.** $0{,@@CHON@@@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,






**Câu 17.** 
	Một vật có thể tích $V = 180{,}37\text{ cm}^3 \pm 0{,}05\text{ cm}^3$. Nếu lấy $180{,}37\text{ cm}^3$ làm giá trị gần đúng cho $V$ thì sai số tương đối của giá trị gần đúng đó không vượt quá
	

@@TAB@@@@CHON@@**A.** $0{,@@CHON@@@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,






**Câu 18.** 
	Số $\overline{a}$ được cho bởi giá trị gần đúng $a = 5{,}7824$ với sai số tương đối không vượt quá $0{,}05\%$. Khi đó, sai số tuyệt đối của $a$ không vượt quá
	

@@TAB@@@@CHON@@**A.** $0{,@@CHON@@@@TAB@@**B.** $0{,@@TAB@@**C.** $0{,@@TAB@@**D.** $0{,






**Câu 19.** 
	Cho $\overline{a} = \dfrac{1}{1 + x}$ ($0 < x < 1$). Giả sử ta lấy $a = 1 - x$ làm giá trị gần đúng của $\overline{a}$. Khi đó, sai số tương đối của $a$ theo $x$ bằng
	

@@TAB@@@@CHON@@**A.** $\dfrac{x^2@@CHON@@@@TAB@@**B.** 1 - x^2@@TAB@@**C.** $\dfrac{x@@TAB@@**D.** 1 - x






**Câu 20.** 
	Các nhà toán học cổ đại Trung Quốc đã dùng phân số $\dfrac{22}{7}$ để xấp xỉ số $\pi$. Hãy đánh giá sai số tuyệt đối $\Delta$ của giá trị gần đúng này, biết $3{,}1415 < \pi < 3{,}1416$.
	

@@TAB@@**A.** $\Delta < 0{,@@TAB@@@@CHON@@**B.** $\Delta < 0{,@@CHON@@@@TAB@@**C.** $\Delta < 0{,@@TAB@@**D.** $\Delta < 0{,






**Câu 21.** 
	Hình chữ nhật có các cạnh là $x = 2\text{ m} \pm 1\text{ cm}$ và $y = 5\text{ m} \pm 2\text{ cm}$. Diện tích của hình chữ nhật và sai số tương đối của giá trị đó là
	

@@TAB@@@@CHON@@**A.** $10\text{ m@@CHON@@@@TAB@@**B.** ,@@TAB@@**C.** $10\text{ m@@TAB@@**D.** ,








## PHẦN II. CÂU HỎI TỰ LUẬN


*\small (Học sinh trình bày chi tiết lời giải các bài toán sau)*


**Bài 1.** 
	Một bao gạo ghi thông tin khối lượng là $5 \pm 0{,}2\text{ kg}$.
	
		
-  Xác định khối lượng đúng, khối lượng gần đúng và độ chính xác của bao gạo.
		
-  Khối lượng thực của bao gạo nằm trong đoạn nào?
	
	\loigiai{
		
			
-  Kí hiệu $\overline{m}$ là khối lượng đúng (thực) của bao gạo.\\
			Khối lượng gần đúng là $m = 5\text{ kg}$.\\
			Độ chính xác của phép đo là $d = 0{,}2\text{ kg}$.
			
-  Khối lượng thực $\overline{m}$ của bao gạo nằm trong đoạn:
			\[[5 - 0{,}2; 5 + 0{,}2] = [4{,}8; 5{,}2]\text{ (kg)}.\]
		
	}





**Bài 2.** 
	Một phép đo đường kính nhân tế bào cho kết quả là $5 \pm 0{,}3\ \mu\text{m}$. Đường kính thực của nhân tế bào thuộc đoạn nào?
	\loigiai{
		Gọi $\overline{D}$ là đường kính thực của nhân tế bào.\\
		Theo giả thiết, đường kính gần đúng là $D = 5\ \mu\text{m}$ với độ chính xác $d = 0{,}3\ \mu\text{m}$.\\
		Do đó, đường kính thực của nhân tế bào thuộc đoạn:
		\[[5 - 0{,}3; 5 + 0{,}3] = [4{,}7; 5{,}3]\ (\mu\text{m}).\]
	}





**Bài 3.** 
	Chiều dài một cái cầu là $\ell = 1745{,}25\text{ m} \pm 0{,}01\text{ m}$.
	
		
-  Xác định chiều dài đúng, chiều dài gần đúng và độ chính xác của cái cầu.
		
-  Chiều dài thực của cái cầu nằm trong đoạn nào?
	
	\loigiai{
		
			
-  Chiều dài đúng của cái cầu được kí hiệu là $\overline{\ell}$.\\
			Chiều dài gần đúng là $\ell = 1745{,}25\text{ m}$.\\
			Độ chính xác là $d = 0{,}01\text{ m}$.
			
-  Chiều dài thực của cái cầu nằm trong đoạn:
			\[[1745{,}25 - 0{,}01; 1745{,}25 + 0{,}01] = [1745{,}24; 1745{,}26]\text{ (m)}.\]
		
	}





**Bài 4.** 
	Biết $\sqrt{7} = 2{,}6457513...$
	
		
-  Làm tròn kết quả đến phần mười và ước lượng sai số tuyệt đối.
		
-  Làm tròn kết quả đến phần nghìn và ước lượng sai số tuyệt đối.
	
	\loigiai{
		
			
-  Làm tròn đến hàng phần mười (chữ số thập phân thứ nhất):\\
			Chữ số hàng phần mười là $6$, chữ số kế tiếp là $4 < 5$ nên số quy tròn là $2{,}6$.\\
			Ước lượng sai số tuyệt đối:
			\[\Delta = |\sqrt{7} - 2{,}6| \approx |2{,}6457513 - 2{,}6| = 0{,}0457513 < 0{,}05.\]
			
-  Làm tròn đến hàng phần nghìn (chữ số thập phân thứ ba):\\
			Chữ số hàng phần nghìn là $5$, chữ số kế tiếp là $7 \ge 5$ nên số quy tròn là $2{,}646$.\\
			Ước lượng sai số tuyệt đối:
			\[\Delta = |\sqrt{7} - 2{,}646| \approx |2{,}6457513 - 2{,}646| = 0{,}0002487 < 0{,}0005.\]
		
	}





**Bài 5.** 
	Ở Babylon, một tấm đất sét có niên đại khoảng $1900 - 1600$ trước Công nguyên đã ghi lại ước lượng số $\pi$ bằng $\dfrac{25}{8} = 3{,}1250$. Hãy ước lượng sai số tuyệt đối và sai số tương đối của giá trị gần đúng này, biết $3{,}141 < \pi < 3{,}142$.
	\loigiai{
		Ta có số gần đúng $a = 3{,}1250 < \pi$.\\
		Sai số tuyệt đối là $\Delta = |\pi - 3{,}1250| = \pi - 3{,}1250$.\\
		Vì $3{,}141 < \pi < 3{,}142$ nên:
		\[3{,}141 - 3{,}1250 < \Delta < 3{,}142 - 3{,}1250 \iff 0{,}0160 < \Delta < 0{,}0170.\]
		Do đó sai số tuyệt đối được ước lượng là $\Delta < 0{,}0170$.\\
		Sai số tương đối của giá trị gần đúng thỏa mãn:
		\[\delta = \frac{\Delta}{|a|} < \frac{0{,}0170}{3{,}1250} = 0{,}00544 = 0{,}544\%.\]
	}





**Bài 6.** 
	Cho số gần đúng $a = 6547$ với độ chính xác $d = 100$. Hãy viết số quy tròn của số $a$ và ước lượng sai số tương đối của số quy tròn đó.
	\loigiai{
		Vì độ chính xác $d = 100$ là hàng trăm nên ta quy tròn số $a$ đến **hàng nghìn**.\\
		Chữ số hàng nghìn là $6$, chữ số ngay bên phải là $5 \ge 5$ nên tăng lên 1 đơn vị:\\
		Số quy tròn là $a^* = 7000$.\\
		Sai số tuyệt đối của số quy tròn $a^*$ đối với số đúng $\overline{a}$:\\
		Ta có $|\overline{a} - 6547| \le 100$ và $|7000 - 6547| = 453$, suy ra:
		\[\Delta_{a^*} = |\overline{a} - 7000| \le |\overline{a} - 6547| + |6547 - 7000| \le 100 + 453 = 553.\]
		Ước lượng sai số tương đối của số quy tròn:
		\[\delta_{a^*} = \frac{\Delta_{a^*}}{|a^*|} \le \frac{553}{7000} \approx 0{,}079 = 7{,}9\%.\]
	}





**Bài 7.** 
	Cho số gần đúng $a = 23\,748\,023$ với độ chính xác $d = 101$. Hãy viết số quy tròn của số $a$ và ước lượng sai số tương đối của số quy tròn đó.
	\loigiai{
		Vì $100 \le d = 101 < 1000$ nên hàng của độ chính xác là hàng trăm. Do đó ta quy tròn số $a$ đến **hàng nghìn**.\\
		Chữ số hàng nghìn là $8$, chữ số hàng trăm là $0 < 5$ nên giữ nguyên chữ số hàng nghìn:\\
		Số quy tròn là $a^* = 23\,748\,000$.\\
		Sai số tuyệt đối của số quy tròn:\\
		\[\Delta_{a^*} \le |\overline{a} - a| + |a - a^*| \le 101 + |23\,748\,023 - 23\,748\,000| = 101 + 23 = 124.\]
		Ước lượng sai số tương đối của số quy tròn:
		\[\delta_{a^*} \le \frac{124}{23\,748\,000} \approx 5{,}22 \times 10^{-6} \approx 0{,}000522\%.\]
	}





**Bài 8.** 
	Cho biết $\sqrt{3} = 1{,}7320508...$ Hãy quy tròn $\sqrt{3}$ đến hàng phần trăm và ước lượng sai số tương đối.
	\loigiai{
		Làm tròn $\sqrt{3}$ đến hàng phần trăm (chữ số thập phân thứ hai):\\
		Chữ số hàng phần trăm là $3$, chữ số kế tiếp là $2 < 5$ nên số quy tròn là $1{,}73$.\\
		Sai số tuyệt đối của phép quy tròn:
		\[\Delta = |\sqrt{3} - 1{,}73| \approx |1{,}7320508 - 1{,}73| = 0{,}0020508 < 0{,}005.\]
		Sai số tương đối:
		\[\delta = \frac{\Delta}{1{,}73} < \frac{0{,}005}{1{,}73} \approx 0{,}00289 = 0{,}289\%.\]
	}





**Bài 9.** 
	Cho $\overline{a} = \dfrac{1}{1 + x}$ ($0 < x < 1$). Giả sử ta lấy $a = 1 - x$ làm giá trị gần đúng của $\overline{a}$. Hãy tính sai số tương đối của $a$ theo $x$.
	\loigiai{
		Sai số tuyệt đối:
		\[\Delta_a = |\overline{a} - a| = \left|\frac{1}{1 + x} - (1 - x)\right| = \left|\frac{1 - (1 - x^2)}{1 + x}\right| = \frac{x^2}{1 + x}\text{ (do $0 < x < 1$)}.\]
		Sai số tương đối:
		\[\delta_a = \frac{\Delta_a}{|a|} = \frac{\dfrac{x^2}{1 + x}}{1 - x} = \frac{x^2}{(1 + x)(1 - x)} = \frac{x^2}{1 - x^2}.\]
	}





**Bài 10.** 
	Làm tròn các số sau đến chữ số hàng chục:
	
		
			
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
		
	
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng đơn vị (ngay bên phải hàng chục): nếu $< 5$ thì giữ nguyên hàng chục, nếu $\ge 5$ thì tăng hàng chục thêm 1 đơn vị, các chữ số sau hàng chục thay bằng $0$ (bỏ phần thập phân):
		
		
			
-  a) $199 \approx 200$.
			
-  b) $999 \approx 1000$.
			
-  c) $9999 \approx 10\,000$.
			
-  d) $2683 \approx 2680$.
			
-  e) $1099 \approx 1100$.
			
-  f) $12345 \approx 12\,350$.
			
-  g) $123456 \approx 123\,460$.
			
-  h) $43781 \approx 43\,780$.
			
-  i) $454995 \approx 455\,000$.
			
-  j) $14350 \approx 14\,350$.
			
-  k) $99999 \approx 100\,000$.
			
-  l) $987698 \approx 987\,700$.
			
-  m) $3400065 \approx 3\,400\,070$.
			
-  n) $1000587 \approx 1\,000\,590$.
			
-  o) $987654 \approx 987\,650$.
			
-  p) $28051989 \approx 28\,051\,990$.
			
-  q) $2602283 \approx 2\,602\,280$.
			
-  r) $123{,}45 \approx 120$.
			
-  s) $12345{,}67 \approx 12\,350$.
			
-  t) $98765{,}432 \approx 98\,770$.
		
		
	}





**Bài 11.** 
	Làm tròn các số sau đến chữ số hàng trăm:
	
		
			
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
		
	
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng chục (ngay bên phải hàng trăm):
		
		
			
-  a) $199 \approx 200$.
			
-  b) $999 \approx 1000$.
			
-  c) $9999 \approx 10\,000$.
			
-  d) $1099 \approx 1100$.
			
-  e) $2683 \approx 2700$.
			
-  f) $12345 \approx 12\,300$.
			
-  g) $43781 \approx 43\,800$.
			
-  h) $14350 \approx 14\,400$.
			
-  i) $1234567 \approx 1\,234\,600$.
			
-  j) $454995 \approx 455\,000$.
			
-  k) $99999 \approx 100\,000$.
			
-  l) $987698 \approx 987\,700$.
			
-  m) $3400065 \approx 3\,400\,100$.
			
-  n) $987654 \approx 987\,700$.
			
-  o) $260283 \approx 260\,300$.
			
-  p) $23456{,}7 \approx 23\,500$.
			
-  q) $12345{,}678 \approx 12\,300$.
			
-  r) $8765{,}432 \approx 8800$.
			
-  s) $9999{,}99 \approx 10\,000$.
		
		
	}





**Bài 12.** 
	Làm tròn các số sau đến chữ số hàng nghìn:
	
		
			
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
		
	
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng trăm (ngay bên phải hàng nghìn):
		
		
			
-  a) $12\,345 \approx 12\,000$.
			
-  b) $43\,781 \approx 44\,000$.
			
-  c) $28\,634 \approx 29\,000$.
			
-  d) $21\,999 \approx 22\,000$.
			
-  e) $22\,999 \approx 23\,000$.
			
-  f) $9999 \approx 10\,000$.
			
-  g) $12\,099 \approx 12\,000$.
			
-  h) $454\,995 \approx 455\,000$.
			
-  i) $14\,350 \approx 14\,000$.
			
-  j) $99\,999 \approx 100\,000$.
			
-  k) $987\,698 \approx 988\,000$.
			
-  l) $3\,400\,065 \approx 3\,400\,000$.
			
-  m) $1\,000\,587 \approx 1\,001\,000$.
			
-  n) $987\,654 \approx 988\,000$.
			
-  o) $260\,283 \approx 260\,000$.
			
-  p) $23456{,}7 \approx 23\,000$.
			
-  q) $1\,234\,567 \approx 1\,235\,000$.
			
-  r) $12345{,}678 \approx 12\,000$.
			
-  s) $8765{,}432 \approx 9000$.
			
-  t) $9999{,}99 \approx 10\,000$.
		
		
	}





**Bài 13.** 
	Làm tròn các số sau đến hàng phần mười:
	
		
			
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
		
	
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng phần trăm:
		
		
			
-  a) $10{,}00905 \approx 10{,}0$.
			
-  b) $60{,}991 \approx 61{,}0$.
			
-  c) $999{,}994 \approx 1000{,}0$.
			
-  d) $10{,}0456 \approx 10{,}0$.
			
-  e) $23{,}0009 \approx 23{,}0$.
			
-  f) $99{,}999 \approx 100{,}0$.
			
-  g) $90{,}0909 \approx 90{,}1$.
			
-  h) $9876{,}1 \approx 9876{,}1$.
			
-  i) $1234{,}56 \approx 1234{,}6$.
			
-  j) $98765{,}43 \approx 98765{,}4$.
		
		
	}





**Bài 14.** 
	Làm tròn các số sau đến hàng phần trăm:
	
		
			
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
		
	
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng phần nghìn:
		
		
			
-  a) $3{,}0468 \approx 3{,}05$.
			
-  b) $12{,}3475 \approx 12{,}35$.
			
-  c) $0{,}31069 \approx 0{,}31$.
			
-  d) $12{,}516 \approx 12{,}52$.
			
-  e) $0{,}999 \approx 1{,}00$.
			
-  f) $7{,}923 \approx 7{,}92$.
			
-  g) $17{,}418 \approx 17{,}42$.
			
-  h) $79{,}1364 \approx 79{,}14$.
			
-  i) $50{,}401 \approx 50{,}40$.
			
-  j) $0{,}155 \approx 0{,}16$.
			
-  k) $60{,}996 \approx 61{,}00$.
			
-  l) $12{,}349 \approx 12{,}35$.
			
-  m) $2{,}9999 \approx 3{,}00$.
			
-  n) $123{,}456 \approx 123{,}46$.
			
-  o) $98{,}7654 \approx 98{,}77$.
		
		
	}





**Bài 15.** 
	Viết số quy tròn của mỗi số sau với độ chính xác $d$:
	
		
-  $1\,234\,567$ với $d = 400$.
		
-  $8{,}7654$ với $d = 0{,}01$.
		
-  $28{,}4156$ với $d = 0{,}001$.
		
-  $1{,}7320508...$ với $d = 0{,}0001$.
	
	\loigiai{
		
			
-  Vì $100 \le d = 400 < 1000$ (hàng trăm), ta làm tròn đến hàng nghìn:\\
			Chữ số hàng trăm là $5 \ge 5 \implies$ số quy tròn là $1\,235\,000$.
			
-  Vì $d = 0{,}01$ (hàng phần trăm), ta làm tròn đến hàng phần mười:\\
			Chữ số hàng phần trăm là $6 \ge 5 \implies$ số quy tròn là $8{,}8$.
			
-  Vì $d = 0{,}001$ (hàng phần nghìn), ta làm tròn đến hàng phần trăm:\\
			Chữ số hàng phần nghìn là $5 \ge 5 \implies$ số quy tròn là $28{,}42$.
			
-  Vì $d = 0{,}0001$ (hàng phần chục nghìn), ta làm tròn đến hàng phần nghìn:\\
			Chữ số hàng phần chục nghìn là $0 < 5 \implies$ số quy tròn là $1{,}732$.
		
	}





**Bài 16.** 
	Hãy viết số quy tròn của:
	
		
-  $a$ biết $\overline{a} = 1\,951\,890 \pm 200$.
		
-  $b$ biết $\overline{b} = 1{,}236 \pm 0{,}002$.
		
-  $c$ biết $\overline{c} = 3{,}1463 \pm 0{,}002$.
	
	\loigiai{
		
			
-  Độ chính xác $d = 200$ (hàng trăm), ta quy tròn $a$ đến hàng nghìn:\\
			Chữ số hàng trăm là $8 \ge 5 \implies$ số quy tròn là $1\,952\,000$.
			
-  Độ chính xác $d = 0{,}002$ (hàng phần nghìn), ta quy tròn $b$ đến hàng phần trăm:\\
			Chữ số hàng phần nghìn là $6 \ge 5 \implies$ số quy tròn là $1{,}24$.
			
-  Độ chính xác $d = 0{,}002$ (hàng phần nghìn), ta quy tròn $c$ đến hàng phần trăm:\\
			Chữ số hàng phần nghìn là $6 \ge 5 \implies$ số quy tròn là $3{,}15$.
		
	}





**Bài 17.** 
	Chiều dài một cái cầu là $\ell = 1745{,}25\text{ m} \pm 0{,}01\text{ m}$. Hãy viết số quy tròn của số gần đúng $1745{,}25$.
	\loigiai{
		Độ chính xác $d = 0{,}01\text{ m}$ ở hàng phần trăm, do đó ta quy tròn số gần đúng $\ell = 1745{,}25$ đến **hàng phần mười**.\\
		Chữ số hàng phần mười là $2$, chữ số ngay sau nó là $5 \ge 5$ nên cộng thêm 1 đơn vị vào hàng phần mười:\\
		Số quy tròn là **$1745{,**3\text{ m}$}.
	}





**Bài 18.** 
	Sử dụng máy tính bỏ túi tính gần đúng các số sau (kết quả lấy 4 chữ số thập phân):
	
		
			
-  $3^7 \cdot \sqrt{14}$
			
-  $\sqrt[3]{15 \cdot 12^4}$
			
-  $\sqrt[3]{15 \cdot 14^4}$
		
	
	\loigiai{
		
			
-  $3^7 \cdot \sqrt{14} = 2187 \cdot \sqrt{14} \approx 8182{,}806847... \implies \mathbf{8182{,}8068}$.
			
-  $\sqrt[3]{15 \cdot 12^4} = \sqrt[3]{15 \cdot 20736} = \sqrt[3]{311040} \approx 67{,}754877... \implies \mathbf{67{,}7549}$.
			
-  $\sqrt[3]{15 \cdot 14^4} = \sqrt[3]{15 \cdot 38416} = \sqrt[3]{576240} \approx 83{,}214777... \implies \mathbf{83{,}2148}$.
		
	}





**Bài 19.** 
	Thực hiện các phép tính sau trên máy tính cầm tay (trong kết quả lấy 4 chữ số ở phần thập phân):
	
		
			
-  $4^6 \cdot \sqrt{0{,}1}$
			
-  $\sqrt[8]{2{,}1^{18} + 1} - \sqrt{2{,}1^{12} + 1}$
			
-  $\dfrac{1{,}5^3}{\sqrt[3]{6{,}8}}$
		
	
	\loigiai{
		
			
-  $4^6 \cdot \sqrt{0{,}1} = 4096 \cdot \sqrt{0{,}1} \approx 1295{,}27140... \implies \mathbf{1295{,}2714}$.
			
-  Ta có $2{,}1^{18} + 1 \approx 63261{,}744 \implies \sqrt[8]{2{,}1^{18} + 1} \approx 3{,}998939$.\\
			Và $2{,}1^{12} + 1 \approx 7355{,}8275 \implies \sqrt{2{,}1^{12} + 1} \approx 85{,}766121$.\\
			Do đó: $\sqrt[8]{2{,}1^{18} + 1} - \sqrt{2{,}1^{12} + 1} \approx 3{,}998939 - 85{,}766121 = -81{,}76718... \implies \mathbf{-81{,}7672}$.
			
-  $\dfrac{1{,}5^3}{\sqrt[3]{6{,}8}} = \dfrac{3{,}375}{\sqrt[3]{6{,}8}} \approx \dfrac{3{,}375}{1{,}894536} \approx 1{,}781439... \implies \mathbf{1{,}7814}$.
		
	}





# BẢNG ĐÁP ÁN TRẮC NGHIỆM

| Câu | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Đ/A** | **C** | **C** | **D** | **B** | **B** | **D** | **C** | **A** | **A** | **D** | **C** |

| Câu | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Đ/A** | **B** | **A** | **C** | **A** | **B** | **A** | **A** | **A** | **B** | **A** |



---

<p align='center'>**--------- HẾT ---------**</p>
