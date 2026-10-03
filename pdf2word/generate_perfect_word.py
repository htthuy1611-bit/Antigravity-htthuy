import os
import sys
import subprocess

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

tex_content = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage[top=2cm,bottom=2cm,left=2cm,right=2cm]{geometry}

\begin{document}

\noindent
\begin{tabular}{@{}p{0.48\textwidth}p{0.48\textwidth}@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA ĐÁNH GIÁ THƯỜNG XUYÊN} \\
\textbf{THÀNH PHỐ HỒ CHÍ MINH} & \textbf{NĂM HỌC: 2026--2027} \\
\textbf{TRƯỜNG THCS--THPT NGUYỄN KHUYẾN} & \textbf{MÔN: TOÁN -- KHỐI LỚP: 12} \\
\textbf{TRƯỜNG TH--THCS--THPT LÊ THÁNH TÔNG} & \textit{Thời gian làm bài: 90 phút}
\end{tabular}

\begin{center}
\textbf{\large MÃ ĐỀ THI 2009}
\end{center}

\vspace{0.3cm}
\noindent\textbf{\large PHẦN 1. Câu trắc nghiệm 4 phương án}

\vspace{0.2cm}
\textbf{Câu 1.} Cho hàm số $y = f(x)$ có đạo hàm trên $\mathbb{R}$ thỏa $f'(x) < 0$, $\forall x \in (1; 2)$ và $f'(x) > 0$, $\forall x \in (2; 3)$. Phát biểu nào sau đây là đúng?

\noindent
\begin{tabular}{@{}p{0.48\textwidth}p{0.48\textwidth}@{}}
\textbf{A.} Hàm số $y = f(x)$ đồng biến trên cả hai khoảng $(1; 2)$ và $(2; 3)$. &
\textbf{B.} Hàm số $y = f(x)$ nghịch biến trên cả hai khoảng $(1; 2)$ và $(2; 3)$. \\
\textbf{C.} Hàm số $y = f(x)$ đồng biến trên khoảng $(1; 2)$ và nghịch biến trên khoảng $(2; 3)$. &
\textbf{D.} Hàm số $y = f(x)$ nghịch biến trên khoảng $(1; 2)$ và đồng biến trên khoảng $(2; 3)$.
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 2.} Giá trị cực đại của hàm số $f(x) = 2x^3 - 9x^2 - 24x + 1$ là

\noindent
\begin{tabular}{@{}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}@{}}
\textbf{A.} $-1$ & \textbf{B.} $14$ & \textbf{C.} $4$ & \textbf{D.} $-111$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 3.} Cho lăng trụ $ABC.A'B'C'$. Khẳng định nào sau đây đúng?

\noindent
\begin{tabular}{@{}p{0.48\textwidth}p{0.48\textwidth}@{}}
\textbf{A.} $\overrightarrow{BA} + \overrightarrow{A'C'} = \overrightarrow{BC}$ &
\textbf{B.} $\overrightarrow{BA} + \overrightarrow{A'C'} = \overrightarrow{BC'}$ \\
\textbf{C.} $\overrightarrow{BA} + \overrightarrow{A'C'} = \overrightarrow{C'B}$ &
\textbf{D.} $\overrightarrow{BA} + \overrightarrow{A'C'} = \overrightarrow{B'C}$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 4.}
\begin{tabular}{@{}p{0.65\textwidth}p{0.32\textwidth}@{}}
Hàm số $y = f(x)$ xác định trên đoạn $[-1; 6]$ và có đồ thị như hình bên. Hàm số đã cho nghịch biến trên khoảng nào sau đây?
\vspace{0.2cm}

\begin{tabular}{@{}p{0.48\linewidth}p{0.48\linewidth}@{}}
\textbf{A.} $(-1; 2)$ & \textbf{B.} $(0; 2)$ \\
\textbf{C.} $(2; 6)$ & \textbf{D.} $(-2; 0)$
\end{tabular}
&
\includegraphics[width=0.3\textwidth]{fig_cau4.png}
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 5.} Cho tứ diện $ABCD$. Lấy $G$ là trọng tâm của tam giác $ABC$. Phát biểu nào sau đây là sai?

\noindent
\begin{tabular}{@{}p{0.48\textwidth}p{0.48\textwidth}@{}}
\textbf{A.} $\overrightarrow{GA} + \overrightarrow{GB} + \overrightarrow{GC} = \overrightarrow{0}$ &
\textbf{B.} $\overrightarrow{GA} + \overrightarrow{GB} + \overrightarrow{GC} + \overrightarrow{GD} = \overrightarrow{0}$ \\
\textbf{C.} $\overrightarrow{GD} - \overrightarrow{GA} = \overrightarrow{AD}$ &
\textbf{D.} $\overrightarrow{DA} + \overrightarrow{DB} + \overrightarrow{DC} = 3\overrightarrow{DG}$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 6.} Một chiếc hộp hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $12\text{ cm}$, mặt trên $A'B'C'D'$ không nắp. Có một con kiến ở đỉnh $A$ bên ngoài hộp và một miếng mồi của kiến tại điểm $O$ là tâm đáy $ABCD$ ở bên trong hộp. Quãng đường ngắn nhất mà con kiến tìm đến miếng mồi (làm tròn đến hai chữ số thập phân) là

\noindent
\begin{tabular}{@{}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}@{}}
\textbf{A.} $32{,}49\text{ cm}$ & \textbf{B.} $36{,}29\text{ cm}$ & \textbf{C.} $12\text{ cm}$ & \textbf{D.} $30{,}59\text{ cm}$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 7.} Giá trị nhỏ nhất của hàm số $f(x) = x^4 - 8x^2 + a$, ($a \in \mathbb{R}$) trên đoạn $[-1; 3]$ bằng

\noindent
\begin{tabular}{@{}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}@{}}
\textbf{A.} $-6$ & \textbf{B.} $a$ & \textbf{C.} $-16 + a$ & \textbf{D.} $9 + a$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 8.}
\begin{tabular}{@{}p{0.65\textwidth}p{0.32\textwidth}@{}}
Hàm số $y = f(x)$ xác định trên đoạn $[-1; 5]$ và có đồ thị như hình bên. Tập giá trị của hàm số $y = f(x)$ trên đoạn $[-1; 5]$ là
\vspace{0.2cm}

\begin{tabular}{@{}p{0.48\linewidth}p{0.48\linewidth}@{}}
\textbf{A.} $[-1; 5]$ & \textbf{B.} $[1; 3]$ \\
\textbf{C.} $[-1; 3]$ & \textbf{D.} $[1; 5]$
\end{tabular}
&
\includegraphics[width=0.3\textwidth]{fig_cau8.png}
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 9.} Mỗi ngày bác Bình đều đi bộ để rèn luyện sức khoẻ. Quãng đường đi bộ mỗi ngày (đơn vị: $\text{km}$) của bác Bình trong 20 ngày được thống kê lại ở bảng sau:

\begin{center}
\begin{tabular}{|l|c|c|c|c|c|}
\hline
\textbf{Quãng đường} & $[2{,}7; 3{,}0)$ & $[3{,}0; 3{,}3)$ & $[3{,}3; 3{,}6)$ & $[3{,}6; 3{,}9)$ & $[3{,}9; 4{,}2)$ \\
\hline
\textbf{Số ngày} & $3$ & $6$ & $5$ & $4$ & $2$ \\
\hline
\end{tabular}
\end{center}

Khoảng biến thiên của mẫu số liệu ghép nhóm trên bằng

\noindent
\begin{tabular}{@{}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}@{}}
\textbf{A.} $1{,}2$ & \textbf{B.} $0{,}362$ & \textbf{C.} $3{,}39$ & \textbf{D.} $1{,}5$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 10.} Trong không gian $Oxyz$, cho hai điểm $A(1; 1; 2)$ và $B(3; 1; 0)$. Trung điểm của đoạn thẳng $AB$ có toạ độ là

\noindent
\begin{tabular}{@{}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}@{}}
\textbf{A.} $(2; 1; 1)$ & \textbf{B.} $(4; 2; 2)$ & \textbf{C.} $(2; 0; -2)$ & \textbf{D.} $(1; 0; -1)$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 11.} Đường tiệm cận xiên của đồ thị hàm số $y = \dfrac{x^2 + 2x - 2}{x - 2}$ là

\noindent
\begin{tabular}{@{}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}@{}}
\textbf{A.} $y = -x + 3$ & \textbf{B.} $y = x + 3$ & \textbf{C.} $y = x - 3$ & \textbf{D.} $y = x + 4$
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 12.} Trong không gian $Oxyz$, cho điểm $A(-3; 1; -4)$, $B(1; -5; 2)$. Đường thẳng $AB$ cắt mặt phẳng $(Oxy)$ tại điểm

\noindent
\begin{tabular}{@{}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}p{0.24\textwidth}@{}}
\textbf{A.} $M\left(-\dfrac{1}{3}; -3; 0\right)$ & \textbf{B.} $N\left(\dfrac{1}{3}; 3; 0\right)$ & \textbf{C.} $P(0; 3; 1)$ & \textbf{D.} $Q(-3; 1; 0)$
\end{tabular}

\vspace{0.6cm}
\noindent\textbf{\large PHẦN 2. Câu trắc nghiệm đúng sai}

\vspace{0.2cm}
\textbf{Câu 1.} Hàm số $y = f(x)$ liên tục trên $\mathbb{R}$ và có bảng biến thiên như sau:

\begin{center}
\includegraphics[width=0.7\textwidth]{fig_bbt.png}
\end{center}

\begin{enumerate}[label=\alph*)]
\item Đồ thị hàm số đã cho có hai đường tiệm cận ngang.
\item Giá trị nhỏ nhất của hàm số trên $(-\infty; +\infty)$ bằng $8$.
\item Hàm số đồng biến trên $(8; 38)$.
\item Giá trị lớn nhất của hàm số trên $\mathbb{R}$ bằng $142$.
\end{enumerate}

\vspace{0.3cm}
\textbf{Câu 2.}
\begin{tabular}{@{}p{0.68\textwidth}p{0.3\textwidth}@{}}
Xét tam giác $ABC$ có $AC = 2AB$ và $BC = 10\text{ cm}$. Trên cạnh $AC$ lấy điểm $D$ sao cho $AD = \dfrac{1}{4}AC$, trên cạnh $AB$ lấy điểm $E$ sao cho $AE = \dfrac{1}{4}AB$, trên cạnh $AD$ lấy điểm $F$ sao cho $AF = \dfrac{1}{4}AD$ và tiếp tục lấy các điểm $G, H, I, J\dots$ (vô hạn lần) theo quy luật đó. Xét tính đúng sai các mệnh đề sau:
&
\includegraphics[width=0.28\textwidth]{fig_tamgiac.png}
\end{tabular}

\begin{enumerate}[label=\alph*)]
\item $\dfrac{AB}{AC} = \dfrac{AD}{AB}$.
\item Tam giác $ABD$ đồng dạng với tam giác $ABC$.
\item $BD = 5\text{ cm}$; $DE = 3\text{ cm}$.
\item Độ dài đường gấp khúc $CBDEFGH\dots$ bằng $20\text{ cm}$.
\end{enumerate}

\vspace{0.3cm}
\textbf{Câu 3.}
\begin{tabular}{@{}p{0.65\textwidth}p{0.32\textwidth}@{}}
Hình vẽ bên mô tả vị trí của máy bay vào thời điểm 9h30 phút. Biết các đơn vị trên hình tính theo đơn vị $\text{km}$. Trong các khẳng định sau đây, khẳng định nào đúng, khẳng định nào sai?
&
\includegraphics[width=0.3\textwidth]{fig_maybay.png}
\end{tabular}

\begin{enumerate}[label=\alph*)]
\item Máy bay đang ở độ cao $9\text{ km}$.
\item Tọa độ của máy bay $(300; 150; 9)$.
\item Phi công để máy bay ở chế độ tự động với vận tốc theo hướng đông là $750\text{ km/h}$, độ cao không đổi. Biết rằng gió thổi theo hướng đông với vận tốc $10\text{ m/s}$. Giả sử vận tốc và hướng gió không đổi thì lúc 10h30 phút máy bay ở tọa độ $(150; 1086; 9)$.
\item Sau khi bay đến vị trí lúc 10h30 thì máy bay bay theo hướng ngược lại với vận tốc $800\text{ km/h}$ với độ cao không đổi, biết lúc đó trời lặng gió thì lúc 11h máy bay ở tọa độ $(686; 150; 9)$.
\end{enumerate}

\vspace{0.3cm}
\textbf{Câu 4.} Khảo sát chiều cao của 20 học sinh nam lớp 12A của một trường THPT X, người ta được kết quả thống kê trong bảng sau:

\begin{center}
\begin{tabular}{|l|c|c|c|c|c|}
\hline
\textbf{Chiều cao (cm)} & $[160; 165)$ & $[165; 170)$ & $[170; 175)$ & $[175; 180)$ & $[180; 185)$ \\
\hline
\textbf{Số học sinh} & $3$ & $5$ & $7$ & $4$ & $1$ \\
\hline
\end{tabular}
\end{center}

\begin{enumerate}[label=\alph*)]
\item Gọi $x_1; x_2; \dots; x_{20}$ là mẫu số liệu gốc gồm chiều cao của 20 học sinh trên được xếp theo thứ tự không giảm. Khi đó, $x_3 \in [165; 170)$ và $x_9 \in [170; 175)$.
\item Tứ phân vị thứ ba của mẫu số liệu ghép nhóm đã cho bằng $175$.
\item Khoảng tứ phân vị của mẫu số liệu ghép nhóm đã cho là $\Delta Q = Q_3 - Q_1 = 8{,}5$.
\item Chọn ngẫu nhiên một học sinh trong nhóm khảo sát nói trên, xác suất chọn được học sinh có chiều cao từ $175\text{ cm}$ trở lên bằng $0{,}25$.
\end{enumerate}

\vspace{0.6cm}
\noindent\textbf{\large PHẦN 3. Câu trắc nghiệm trả lời ngắn}

\vspace{0.2cm}
\textbf{Câu 1.} Một doanh nghiệp dự kiến sản xuất không quá $2000$ sản phẩm cùng loại. Giả sử rằng doanh thu của doanh nghiệp khi sản xuất $x$ sản phẩm ($x \in \mathbb{N}$; $0 \leqslant x \leqslant 2000$) là $R(x) = 16x - 0{,}005x^2$ (triệu đồng) và doanh nghiệp phải nộp một khoản thuế là $5\%$ của doanh thu $R(x)$. Chi phí để sản xuất mỗi sản phẩm là bốn triệu đồng. Lợi nhuận của doanh nghiệp (khi sản xuất $x$ sản phẩm) được tính theo công thức: Lợi nhuận bằng doanh thu trừ đi thuế và chi phí. Doanh nghiệp phải sản xuất bao nhiêu sản phẩm để thu được lợi nhuận lớn nhất?

\vspace{0.1cm}
\noindent\textbf{KQ:} \fbox{\phantom{\rule{2.5cm}{0.5cm}}}

\vspace{0.3cm}
\textbf{Câu 2.}
\begin{tabular}{@{}p{0.65\textwidth}p{0.32\textwidth}@{}}
Một bác Shipper giao hàng xuất phát từ kho $A$ để lấy hàng và đi giao tất cả các con đường sau đó lại trở về kho $A$ để trả lại những hàng hóa mà khách hàng chưa nhận. Con đường có sơ đồ và thời gian giao hàng (phút) trên mỗi con đường được mô tả trong hình bên. Thời gian ngắn nhất để bác Shipper hoàn thành công việc trên là bao nhiêu phút?

\vspace{0.2cm}
\textbf{KQ:} \fbox{\phantom{\rule{2.5cm}{0.5cm}}}
&
\includegraphics[width=0.32\textwidth]{fig_shipper.png}
\end{tabular}

\vspace{0.3cm}
\textbf{Câu 3.} Trong không gian $Oxyz$, cho tam giác $ABC$ có $A(-4; -1; 2)$, $B(3; 5; -6)$ và $C(a; b; c)$. Biết trung điểm cạnh $AC$ thuộc trục tung, trung điểm cạnh $BC$ thuộc mặt phẳng $(Oxz)$. Tính $T = 2a + b - c$.

\vspace{0.1cm}
\noindent\textbf{KQ:} \fbox{\phantom{\rule{2.5cm}{0.5cm}}}

\vspace{0.3cm}
\textbf{Câu 4.} Cho tập hợp $X = \{1; 2; 3; 4; 5; 6; 7; 8\}$. Gọi $S$ là tập hợp tất cả các số tự nhiên có 4 chữ số được lập từ các chữ số thuộc tập $X$. Chọn ngẫu nhiên một số từ tập hợp $S$. Xác suất để chọn được một số chia hết cho 3 bằng $\dfrac{a}{b}$ (với $a, b \in \mathbb{N}^*$, $\dfrac{a}{b}$ là phân số tối giản). Tính $T = a + b$.

\vspace{0.1cm}
\noindent\textbf{KQ:} \fbox{\phantom{\rule{2.5cm}{0.5cm}}}

\vspace{0.3cm}
\textbf{Câu 5.} Một quần thể vi khuẩn được nuôi cấy trong phòng thí nghiệm. Nồng độ dinh dưỡng $S$ (đơn vị: $\text{mg/}\ell$) thay đổi theo thời gian $t$ giờ ($t \geqslant 0$) được mô hình hóa bởi hàm số: $S(t) = \dfrac{10t + 5}{t + 1}$. Biết tốc độ sinh trưởng $V$ của vi khuẩn phụ thuộc vào nồng độ dinh dưỡng theo hàm số $V(S) = \dfrac{5S}{S + 2}$. Khi thời gian $t$ kéo dài, tốc độ sinh trưởng $V$ tăng dần và ổn định quanh một ngưỡng $K$ nhất định. Hỏi sau bao nhiêu phút thì tốc độ sinh trưởng của vi khuẩn đạt $90\%$ ngưỡng $K$?

\vspace{0.1cm}
\noindent\textbf{KQ:} \fbox{\phantom{\rule{2.5cm}{0.5cm}}}

\vspace{0.3cm}
\textbf{Câu 6.} Trong không gian với hệ trục tọa độ $Oxyz$, mặt phẳng $(P)\colon bcx + acy + abz - abc = 0$ qua điểm $M(2; 4; 8)$ và cắt các tia $Ox, Oy, Oz$ lần lượt tại $A, B, C$ sao cho $OA = 2OB = 4OC$. Tính $T = a + b + c$.

\vspace{0.1cm}
\noindent\textbf{KQ:} \fbox{\phantom{\rule{2.5cm}{0.5cm}}}

\end{document}
"""

with open("De_Thi_2009_pandoc.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

pandoc_exe = os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")
cmd = [pandoc_exe, "De_Thi_2009_pandoc.tex", "-o", "De_Thi_2009.docx"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
if res.returncode == 0:
    print("[THÀNH CÔNG] Đã tạo file Word hoàn hảo: De_Thi_2009.docx")
else:
    print("[LỖI PANDOC]:", res.stderr)
