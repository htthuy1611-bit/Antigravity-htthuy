# -*- coding: utf-8 -*-
"""
Generator script for chapters/bai_03_sai_so_trang_01_30.tex
"""
import os, sys, re

def clean_math(text):
    if not text:
        return ""
    text = text.replace('◦C', r'$^\circ\text{C}$')
    text = text.replace('◦ C', r'$^\circ\text{C}$')
    text = text.replace('±', r'\pm ')
    text = text.replace('≈', r'\approx ')
    text = text.replace('≤', r'\le ')
    text = text.replace('≥', r'\ge ')
    text = text.replace('·', r'\cdot ')
    text = text.replace('Ω', r'\,\Omega')
    text = text.replace('µ', r'\mu ')
    text = text.replace('⃓⃓⃓', '|')
    text = text.replace('⃓⃓', '')
    text = text.replace('ℓ', r'\ell ')
    text = text.replace('–', '--')
    text = text.replace('“', '')
    text = text.replace('”', '')
    text = text.replace('Í ', r'\item ')
    # Normalize fractions like 1/2 or 0,01/2
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def get_theory_tex():
    return r'''\tieudebaihoc{CHƯƠNG 1: MỞ ĐẦU}{BÀI 3: SAI SỐ TRONG PHÉP ĐO. GHI KẾT QUẢ ĐO}{Trang 1 -- 30}

\section*{A. TÓM TẮT LÝ THUYẾT TRỌNG TÂM}

\subsection*{1. Phép đo các đại lượng vật lí -- Hệ đơn vị SI}

\subsubsection*{a) Định nghĩa phép đo một đại lượng vật lí}
Phép đo một đại lượng vật lí là phép so sánh nó với một đại lượng cùng loại được quy ước làm đơn vị.

\subsubsection*{b) Đơn vị đo}
\begin{itemize}
    \item Hệ đơn vị đo thông dụng hiện nay là hệ đơn vị quốc tế SI.
    \item Hệ SI quy định 7 đơn vị cơ bản:
\end{itemize}

\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|l|c||l|c|}
\hline
\textbf{Đại lượng} & \textbf{Đơn vị (Kí hiệu)} & \textbf{Đại lượng} & \textbf{Đơn vị (Kí hiệu)} \\
\hline
Độ dài & mét ($\text{m}$) & Cường độ dòng điện & ampe ($\text{A}$) \\
Thời gian & giây ($\text{s}$) & Cường độ sáng & candela ($\text{cd}$) \\
Khối lượng & kilôgam ($\text{kg}$) & Lượng chất & mol ($\text{mol}$) \\
Nhiệt độ & kelvin ($\text{K}$) & & \\
\hline
\end{tabular}
\end{center}
Ngoài 7 đơn vị cơ bản, các đơn vị còn lại được gọi là \textbf{đơn vị dẫn xuất} (ví dụ: vận tốc có đơn vị $\text{m/s}$, gia tốc có đơn vị $\text{m/s}^2$, lực có đơn vị $\text{N}$, điện áp có đơn vị $\text{V}$,\dots).

\subsubsection*{c) Kí hiệu bội số và ước số của đơn vị đo}
Khi số đo của một đại lượng là một bội số hoặc ước số thập phân của 10, ta có thể sử dụng kí hiệu (tiếp đầu ngữ) ngay trước đơn vị để phần số đo được trình bày ngắn gọn.
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c||c|c|c|}
\hline
\textbf{Kí hiệu} & \textbf{Tên đọc} & \textbf{Hệ số} & \textbf{Kí hiệu} & \textbf{Tên đọc} & \textbf{Hệ số} \\
\hline
$\text{T}$ & tera & $10^{12}$ & $\text{d}$ & deci & $10^{-1}$ \\
$\text{G}$ & giga & $10^9$    & $\text{c}$ & centi & $10^{-2}$ \\
$\text{M}$ & mega & $10^6$    & $\text{m}$ & mili & $10^{-3}$ \\
$\text{k}$ & kilo & $10^3$    & $\mu$      & micro & $10^{-6}$ \\
$\text{h}$ & hecto & $10^2$   & $\text{n}$ & nano & $10^{-9}$ \\
$\text{da}$ & deka & $10^1$   & $\text{p}$ & pico & $10^{-12}$ \\
\hline
\end{tabular}
\end{center}

\subsubsection*{d) Các phương pháp đo một đại lượng vật lí}
\begin{itemize}
    \item \textbf{Phép đo trực tiếp:} Đo trực tiếp một đại lượng bằng dụng cụ đo, kết quả được đọc trực tiếp trên dụng cụ đo (ví dụ: dùng thước đo chiều dài, dùng cân đo khối lượng, dùng đồng hồ đo thời gian,\dots).
    \item \textbf{Phép đo gián tiếp:} Đo một đại lượng không trực tiếp mà thông qua công thức liên hệ với các đại lượng có thể đo trực tiếp (ví dụ: đo khối lượng riêng $D = \frac{m}{V}$, đo tốc độ $v = \frac{s}{t}$, đo gia tốc rơi tự do $g = \frac{2h}{t^2}$,\dots).
\end{itemize}

\subsubsection*{e) Số chữ số có nghĩa trong kết quả đo}
Số chữ số có nghĩa là tất cả những chữ số tính từ trái sang phải kể từ chữ số khác 0 đầu tiên.
\begin{itemize}
    \item $13{,}1 \longrightarrow$ có 3 chữ số có nghĩa.
    \item $13{,}10 \longrightarrow$ có 4 chữ số có nghĩa.
    \item $1{,}30 \cdot 10^3 \longrightarrow$ có 3 chữ số có nghĩa.
    \item $0{,}3109 \longrightarrow$ có 4 chữ số có nghĩa.
    \item $0{,}0314 \longrightarrow$ có 3 chữ số có nghĩa.
\end{itemize}

\subsection*{2. Sai số phép đo}

\subsubsection*{a) Phân loại sai số}
\begin{itemize}
    \item \textbf{Sai số hệ thống:}
    \begin{itemize}
        \item Khi sử dụng dụng cụ đo để đo các đại lượng vật lí luôn có sự sai lệch do đặc điểm và cấu tạo của dụng cụ gây ra. Sự sai lệch này gọi là sai số dụng cụ hoặc sai số hệ thống.
        \item Sai số hệ thống có nguyên nhân khách quan (do giới hạn cấu tạo của dụng cụ), hoặc nguyên nhân chủ quan do người đo hiệu chỉnh vạch số 0 ban đầu chưa chuẩn (cần phải loại bỏ trước khi đo).
    \end{itemize}
    \item \textbf{Sai số ngẫu nhiên:}
    \begin{itemize}
        \item Khi lặp lại các phép đo nhiều lần, ta thu được các giá trị khác nhau mà sự sai lệch không có nguyên nhân rõ ràng và ổn định. Đó là sai số ngẫu nhiên (do thao tác không đều, điều kiện thí nghiệm biến thiên, hạn chế phản xạ giác quan,\dots).
        \item Để giảm thiểu sai số ngẫu nhiên, ta thực hiện phép đo nhiều lần và lấy giá trị trung bình cộng.
    \end{itemize}
\end{itemize}

\begin{tcolorbox}[colback=yellow!5,colframe=orange!80!black,arc=2mm,boxrule=0.8pt]
\textbf{CHÚ Ý VỀ SAI SỐ DỤNG CỤ ($\Delta A_{\text{dc}}$):}\\
Sai số gây bởi dụng cụ thường được quy ước lấy bằng một độ chia nhỏ nhất (ĐCNN) hoặc nửa độ chia nhỏ nhất trên dụng cụ đo (ví dụ: thước có ĐCNN là $1\text{ mm}$ thì sai số dụng cụ lấy là $0{,}5\text{ mm}$ hoặc $1\text{ mm}$), hoặc lấy theo thông số cấp chính xác ghi sẵn trên dụng cụ do nhà sản xuất quy định.
\end{tcolorbox}

\subsubsection*{b) Cách xác định sai số phép đo trực tiếp}
Giả sử tiến hành đo $n$ lần cùng một đại lượng $A$, thu được các giá trị $A_1, A_2, \dots, A_n$:
\begin{itemize}
    \item \textbf{Giá trị trung bình:}
    \[
    \bar{A} = \frac{A_1 + A_2 + \dots + A_n}{n}
    \]
    \item \textbf{Sai số tuyệt đối của từng lần đo:}
    \[
    \Delta A_1 = |\bar{A} - A_1|;\quad \Delta A_2 = |\bar{A} - A_2|;\quad \dots;\quad \Delta A_n = |\bar{A} - A_n|
    \]
    \item \textbf{Sai số tuyệt đối trung bình (sai số ngẫu nhiên):}
    \[
    \overline{\Delta A} = \frac{\Delta A_1 + \Delta A_2 + \dots + \Delta A_n}{n}
    \]
    \item \textbf{Sai số tuyệt đối của phép đo:} là tổng của sai số ngẫu nhiên và sai số dụng cụ:
    \[
    \Delta A = \overline{\Delta A} + \Delta A_{\text{dc}}
    \]
    \item \textbf{Sai số tỉ đối:} là tỉ số phần trăm giữa sai số tuyệt đối và giá trị trung bình, đặc trưng cho mức độ chính xác của phép đo:
    \[
    \delta A = \frac{\Delta A}{\bar{A}} \cdot 100\%
    \]
\end{itemize}

\subsubsection*{c) Cách xác định sai số phép đo gián tiếp}
Cho các đại lượng đo trực tiếp: $X = \bar{X} \pm \Delta X$; $Y = \bar{Y} \pm \Delta Y$; $Z = \bar{Z} \pm \Delta Z$.
\begin{itemize}
    \item \textbf{Quy tắc tổng và hiệu:} Sai số tuyệt đối của một tổng hay hiệu bằng tổng các sai số tuyệt đối của các số hạng.
    \[
    A = 2X + 3Y - 4Z \implies
    \begin{cases}
    \bar{A} = 2\bar{X} + 3\bar{Y} - 4\bar{Z} \\
    \Delta A = 2\Delta X + 3\Delta Y + 4\Delta Z
    \end{cases}
    \]
    \item \textbf{Quy tắc tích và thương:} Sai số tỉ đối của một tích hay thương bằng tổng các sai số tỉ đối của các thừa số (số mũ lũy thừa nhân ra trước sai số tỉ đối tương ứng).
    \[
    A = 3 \cdot \frac{X \cdot Y^\alpha}{Z^\beta} \implies
    \begin{cases}
    \bar{A} = 3 \cdot \frac{\bar{X} \cdot \bar{Y}^\alpha}{\bar{Z}^\beta} \\
    \delta A = \delta X + \alpha \cdot \delta Y + \beta \cdot \delta Z
    \end{cases}
    \]
\end{itemize}

\subsubsection*{d) Cách ghi kết quả đo}
Kết quả đo đại lượng $A$ được ghi dưới dạng:
\[
A = \bar{A} \pm \Delta A \quad\text{hoặc}\quad (\bar{A} - \Delta A) \le A \le (\bar{A} + \Delta A)
\]
\textbf{Quy tắc biểu diễn chữ số:}
\begin{itemize}
    \item Sai số tuyệt đối $\Delta A$ thường được viết đến tối đa 1 hoặc 2 chữ số có nghĩa.
    \item Giá trị trung bình $\bar{A}$ được làm tròn đến bậc thập phân tương ứng với sai số tuyệt đối $\Delta A$.
    \item Nếu viết dạng lũy thừa $10^n$ thì cả giá trị trung bình $\bar{A}$ và sai số tuyệt đối $\Delta A$ đều phải viết chung cơ số lũy thừa $10^n$.
\end{itemize}

\noindent
\begin{minipage}[c]{0.62\linewidth}
\begin{tcolorbox}[colback=blue!2!white,colframe=blue!75!black,arc=2mm,boxrule=0.8pt]
\textbf{CHÚ Ý: PHƯƠNG PHÁP ĐỒ THỊ BIỂU DIỄN SAI SỐ}\\
Sai số và kết quả của phép đo có thể biểu diễn bằng đồ thị. Mỗi giá trị thực nghiệm đều có sai số: $\pm \Delta x$ và $\pm \Delta y$. Do đó trên mặt phẳng tọa độ, mỗi điểm thực nghiệm được biểu diễn bằng một điểm $M(x_M, y_M)$ nằm tại tâm của một hình chữ nhật có kích thước $2\Delta x \times 2\Delta y$, gọi là \textbf{ô bao sai số}.
\end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[c]{0.35\linewidth}
\centering
\begin{tikzpicture}[>=stealth, font=\footnotesize, scale=0.85]
    \draw[->] (0,0) -- (4,0) node[below] {$x$};
    \draw[->] (0,0) -- (0,3.5) node[left] {$y$};
    \node[below left] at (0,0) {$O$};
    \coordinate (M) at (2.2, 1.8);
    \draw[fill=blue!10, draw=blue!80, dashed] (1.6, 1.3) rectangle (2.8, 2.3);
    \fill[red] (M) circle (1.5pt) node[right=2pt] {$M(x_M, y_M)$};
    \draw[dotted] (2.2,0) -- (2.2,1.8) -- (0,1.8);
    \node[below] at (2.2,0) {$x_M$};
    \node[left] at (0,1.8) {$y_M$};
    \draw[<->] (1.6,0.95) -- (2.8,0.95) node[midway, below] {\scriptsize $2\Delta x$};
    \draw[<->] (3.0,1.3) -- (3.0,2.3) node[midway, right] {\scriptsize $2\Delta y$};
    \node[above, blue!80!black] at (2.2, 2.35) {\scriptsize Ô bao sai số};
\end{tikzpicture}
\end{minipage}
\vspace{0.3cm}
'''

print("Theory tex generated successfully")

def get_examples_tex():
    return r'''
\section*{B. CÁC VÍ DỤ MẪU MINH HỌA}

\begin{vd}
Dùng một thước có ĐCNN là $1\text{ mm}$ và một đồng hồ đo thời gian có ĐCNN $0{,}01\text{ s}$ để đo 5 lần quãng đường đi và thời gian chuyển động của một chiếc xe đồ chơi chạy bằng pin từ điểm $A$ đến điểm $B$.
\begin{center}
\includegraphics[width=0.6\linewidth]{figures/fig_p04_xe_do_choi.png}
\end{center}
\begin{enumerate}[a)]
    \item Nguyên nhân nào gây ra sự sai khác giữa các lần đo?
    \item Tính sai số tuyệt đối của phép đo $s, t$ và điền vào bảng. Lấy sai số dụng cụ bằng nửa độ chia nhỏ nhất của dụng cụ.
    \item Viết kết quả đo $s$ và $t$?
    \item Tính sai số tỉ đối của $s$ và $t$?
\end{enumerate}
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Lần đo} & $s\text{ (mm)}$ & $\Delta s\text{ (mm)}$ & $t\text{ (s)}$ & $\Delta t\text{ (s)}$ \\
\hline
1 & 649 & & 3,49 & \\
2 & 651 & & 3,51 & \\
3 & 654 & & 3,54 & \\
4 & 653 & & 3,53 & \\
5 & 650 & & 3,50 & \\
\hline
\textbf{Trung bình} & & & & \\
\hline
\end{tabular}
\end{center}
\loigiai{
\begin{enumerate}[a)]
    \item \textbf{Nguyên nhân gây ra sự sai khác giữa các lần đo:}
    \begin{itemize}
        \item Do đặc điểm cấu tạo của dụng cụ đo.
        \item Do điều kiện làm thí nghiệm chưa thật ổn định (bề mặt trượt, điện áp pin thay đổi nhẹ).
        \item Do phản xạ và thao tác khi bấm đồng hồ hoặc quan sát vạch đo của người thực hiện.
    \end{itemize}
    \item \textbf{Bảng số liệu kết quả đo sau khi tính toán:}
    \begin{center}
    \renewcommand{\arraystretch}{1.15}
    \begin{tabular}{|c|c|c|c|c|}
    \hline
    \textbf{Lần đo} & $s\text{ (mm)}$ & $\Delta s\text{ (mm)}$ & $t\text{ (s)}$ & $\Delta t\text{ (s)}$ \\
    \hline
    1 & 649 & 2,4 & 3,49 & 0,024 \\
    2 & 651 & 0,4 & 3,51 & 0,004 \\
    3 & 654 & 2,6 & 3,54 & 0,026 \\
    4 & 653 & 1,6 & 3,53 & 0,016 \\
    5 & 650 & 1,4 & 3,50 & 0,014 \\
    \hline
    \textbf{Trung bình} & $\bar{s} = 651{,}4$ & $\overline{\Delta s} = 1{,}68$ & $\bar{t} = 3{,}514$ & $\overline{\Delta t} = 0{,}0168$ \\
    \hline
    \end{tabular}
    \end{center}
    Ta có:
    \[
    \bar{s} = \frac{649 + 651 + 654 + 653 + 650}{5} = 651{,}4\text{ mm}
    \]
    \[
    \overline{\Delta s} = \frac{|651{,}4 - 649| + |651{,}4 - 651| + |651{,}4 - 654| + |651{,}4 - 653| + |651{,}4 - 650|}{5} = 1{,}68\text{ mm}
    \]
    \[
    \bar{t} = \frac{3{,}49 + 3{,}51 + 3{,}54 + 3{,}53 + 3{,}50}{5} = 3{,}514\text{ s}
    \]
    \[
    \overline{\Delta t} = \frac{|3{,}514 - 3{,}49| + |3{,}514 - 3{,}51| + |3{,}514 - 3{,}54| + |3{,}514 - 3{,}53| + |3{,}514 - 3{,}50|}{5} = 0{,}0168\text{ s}
    \]
    \item \textbf{Viết kết quả đo:}
    \begin{itemize}
        \item Sai số dụng cụ: $\Delta s_{\text{dc}} = \frac{1}{2} = 0{,}5\text{ mm}$; $\Delta t_{\text{dc}} = \frac{0{,}01}{2} = 0{,}005\text{ s}$.
        \item Sai số tuyệt đối toàn phần:
        \[
        \Delta s = \overline{\Delta s} + \Delta s_{\text{dc}} = 1{,}68 + 0{,}5 = 2{,}18\text{ mm} \approx 2{,}2\text{ mm (hoặc } 2\text{ mm)}
        \]
        \[
        \Delta t = \overline{\Delta t} + \Delta t_{\text{dc}} = 0{,}0168 + 0{,}005 = 0{,}0218\text{ s} \approx 0{,}022\text{ s (hoặc } 0{,}02\text{ s)}
        \]
        \item Kết quả đo:
        \[
        s = \bar{s} \pm \Delta s = 651{,}4 \pm 2{,}2\text{ mm} \quad (\text{hoặc } 651 \pm 2\text{ mm})
        \]
        \[
        t = \bar{t} \pm \Delta t = 3{,}514 \pm 0{,}022\text{ s} \quad (\text{hoặc } 3{,}51 \pm 0{,}02\text{ s})
        \]
    \end{itemize}
    \item \textbf{Tính sai số tỉ đối:}
    \[
    \delta s = \frac{\Delta s}{\bar{s}} \cdot 100\% = \frac{2{,}2}{651{,}4} \cdot 100\% \approx 0{,}34\% \quad (\text{hoặc } \frac{2}{651} \cdot 100\% \approx 0{,}31\%)
    \]
    \[
    \delta t = \frac{\Delta t}{\bar{t}} \cdot 100\% = \frac{0{,}022}{3{,}514} \cdot 100\% \approx 0{,}63\% \quad (\text{hoặc } \frac{0{,}02}{3{,}51} \cdot 100\% \approx 0{,}57\%)
    \]
\end{enumerate}
}
\end{vd}

\begin{vd}
Đường kính của một viên bi trong 5 lần đo bằng $2{,}620\text{ cm}$; $2{,}625\text{ cm}$; $2{,}630\text{ cm}$; $2{,}628\text{ cm}$ và $2{,}626\text{ cm}$. Đường kính trung bình của viên bi là
\choice
{\True $2{,}6258\text{ cm}$}
{$2{,}6271\text{ cm}$}
{$2{,}6251\text{ cm}$}
{$2{,}6249\text{ cm}$}
\loigiai{
Giá trị trung bình của đường kính viên bi:
\[
\bar{d} = \frac{2{,}620 + 2{,}625 + 2{,}630 + 2{,}628 + 2{,}626}{5} = \frac{13{,}129}{5} = 2{,}6258\text{ cm}
\]
Chọn đáp án \textbf{A}.
}
\end{vd}

\begin{vd}
Kết quả ba lần đo quãng đường chuyển động của viên bi từ $A$ đến $B$ lần lượt là $0{,}048\text{ m}$; $0{,}050\text{ m}$; $0{,}050\text{ m}$, quãng đường trung bình là $0{,}049\text{ m}$. Khi đó sai số tuyệt đối của quãng đường chuyển động của viên bi qua ba lần đo có giá trị lần lượt là
\choice
{\True $0{,}001\text{ m}$; $0{,}001\text{ m}$; $0{,}001\text{ m}$}
{$-0{,}001\text{ m}$; $0{,}001\text{ m}$; $0{,}001\text{ m}$}
{$0{,}001\text{ m}$; $-0{,}001\text{ m}$; $-0{,}001\text{ m}$}
{$0{,}001\text{ m}$; $0{,}000\text{ m}$; $0{,}002\text{ m}$}
\loigiai{
Sai số tuyệt đối của mỗi lần đo là trị tuyệt đối hiệu số giữa giá trị trung bình và giá trị đo:
\begin{itemize}
    \item $\Delta s_1 = |\bar{s} - s_1| = |0{,}049 - 0{,}048| = 0{,}001\text{ m}$.
    \item $\Delta s_2 = |\bar{s} - s_2| = |0{,}049 - 0{,}050| = 0{,}001\text{ m}$.
    \item $\Delta s_3 = |\bar{s} - s_3| = |0{,}049 - 0{,}050| = 0{,}001\text{ m}$.
\end{itemize}
Chọn đáp án \textbf{A}.
}
\end{vd}

\begin{vd}
Để xác định thời gian đi của bạn A trên quãng đường $s$, người ta sử dụng đồng hồ bấm giây, thu được bảng số liệu dưới đây:
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Lần đo} & 1 & 2 & 3 \\
\hline
\textbf{Thời gian (s)} & 35,20 & 36,15 & 35,75 \\
\hline
\end{tabular}
\end{center}
Coi tốc độ đi không đổi trong suốt quá trình chuyển động, sai số ngẫu nhiên trong phép đo này là bao nhiêu?
\choice
{$0{,}30\text{ s}$}
{$0{,}31\text{ s}$}
{$0{,}32\text{ s}$}
{\True $0{,}33\text{ s}$}
\loigiai{
Thời gian trung bình qua 3 lần đo:
\[
\bar{t} = \frac{35{,}20 + 36{,}15 + 35{,}75}{3} = \frac{107{,}10}{3} = 35{,}70\text{ s}
\]
Sai số tuyệt đối của từng lần đo:
\begin{itemize}
    \item $\Delta t_1 = |35{,}70 - 35{,}20| = 0{,}50\text{ s}$.
    \item $\Delta t_2 = |35{,}70 - 36{,}15| = 0{,}45\text{ s}$.
    \item $\Delta t_3 = |35{,}70 - 35{,}75| = 0{,}05\text{ s}$.
\end{itemize}
Sai số ngẫu nhiên (sai số tuyệt đối trung bình):
\[
\overline{\Delta t} = \frac{0{,}50 + 0{,}45 + 0{,}05}{3} = \frac{1{,}00}{3} \approx 0{,}33\text{ s}
\]
Chọn đáp án \textbf{D}.
}
\end{vd}

\begin{vd}
Dùng thước thẳng có giới hạn đo $20\text{ cm}$ và độ chia nhỏ nhất $0{,}5\text{ cm}$ để đo chiều dài chiếc bút máy. Lấy sai số dụng cụ bằng một nửa độ chia nhỏ nhất. Bỏ qua sai số ngẫu nhiên. Nếu chiếc bút có độ dài trung bình $15\text{ cm}$ thì phép đo này có sai số tuyệt đối và sai số tỉ đối là
\choice
{$0{,}5\text{ cm}$ và $2{,}5\%$}
{$0{,}5\text{ cm}$ và $1{,}7\%$}
{$0{,}25\text{ cm}$ và $2{,}5\%$}
{\True $0{,}25\text{ cm}$ và $1{,}7\%$}
\loigiai{
\begin{itemize}
    \item Sai số dụng cụ bằng một nửa ĐCNN: $\Delta \ell = \Delta \ell_{\text{dc}} = \frac{0{,}5}{2} = 0{,}25\text{ cm}$.
    \item Sai số tỉ đối của phép đo:
    \[
    \delta \ell = \frac{\Delta \ell}{\bar{\ell}} \cdot 100\% = \frac{0{,}25}{15} \cdot 100\% \approx 1{,}67\% \approx 1{,}7\%
    \]
\end{itemize}
Chọn đáp án \textbf{D}.
}
\end{vd}

\begin{vd}
Dùng thước kẹp có độ chia nhỏ nhất $0{,}1\text{ mm}$ để đo 5 lần đường kính $d$ của một trụ thép. Lấy sai số dụng cụ bằng một độ chia nhỏ nhất. Cho kết quả như trong bảng dưới. Hãy cho biết kết quả phép đo $d$.
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Lần đo} & 1 & 2 & 3 & 4 & 5 \\
\hline
$d\text{ (mm)}$ & 30,0 & 30,1 & 30,0 & 30,1 & 30,1 \\
\hline
\end{tabular}
\end{center}
\choice
{\True $d = (30{,}06 \pm 0{,}15)\text{ mm}$}
{$d = (30{,}1 \pm 0{,}15)\text{ mm}$}
{$d = (30 \pm 0{,}1)\text{ mm}$}
{$d = (30{,}00 \pm 0{,}15)\text{ mm}$}
\loigiai{
\begin{itemize}
    \item Giá trị trung bình của đường kính:
    \[
    \bar{d} = \frac{30{,}0 \cdot 2 + 30{,}1 \cdot 3}{5} = \frac{150{,}3}{5} = 30{,}06\text{ mm}
    \]
    \item Sai số ngẫu nhiên:
    \[
    \overline{\Delta d} = \frac{|30{,}06 - 30{,}0|\cdot 2 + |30{,}06 - 30{,}1|\cdot 3}{5} = \frac{0{,}06 \cdot 2 + 0{,}04 \cdot 3}{5} = 0{,}048\text{ mm}
    \]
    \item Sai số dụng cụ bằng 1 ĐCNN: $\Delta d_{\text{dc}} = 0{,}1\text{ mm}$.
    \item Sai số tuyệt đối toàn phần: $\Delta d = \overline{\Delta d} + \Delta d_{\text{dc}} = 0{,}048 + 0{,}1 = 0{,}148\text{ mm} \approx 0{,}15\text{ mm}$.
    \item Kết quả phép đo: $d = (30{,}06 \pm 0{,}15)\text{ mm}$.
\end{itemize}
Chọn đáp án \textbf{A}.
}
\end{vd}

\begin{vd}
Một học sinh dùng đồng hồ bấm giây để đo chu kì chuyển động tròn của một vật bằng cách đo thời gian vật quay hết một vòng. Năm lần đo cho kết quả thời gian vật quay hết một vòng lần lượt là $2{,}00\text{ s}$; $2{,}05\text{ s}$; $2{,}00\text{ s}$; $2{,}05\text{ s}$; $2{,}05\text{ s}$. Thang chia nhỏ nhất của đồng hồ là $0{,}01\text{ s}$. Lấy sai số dụng cụ là một độ chia nhỏ nhất. Kết quả của phép đo chu kì được biểu diễn bằng
\choice
{$T = 2{,}030 \pm 0{,}02\text{ s}$}
{$T = 2{,}030 \pm 0{,}024\text{ s}$}
{\True $T = 2{,}030 \pm 0{,}034\text{ s}$}
{$T = 2{,}03 \pm 0{,}03\text{ s}$}
\loigiai{
\begin{itemize}
    \item Giá trị trung bình của chu kì:
    \[
    \bar{T} = \frac{2{,}00 + 2{,}05 + 2{,}00 + 2{,}05 + 2{,}05}{5} = 2{,}03\text{ s}
    \]
    \item Sai số dụng cụ bằng 1 ĐCNN: $\Delta T_{\text{dc}} = 0{,}01\text{ s}$.
    \item Sai số ngẫu nhiên:
    \[
    \overline{\Delta T} = \frac{|2{,}00 - 2{,}03| \cdot 2 + |2{,}05 - 2{,}03| \cdot 3}{5} = \frac{0{,}03 \cdot 2 + 0{,}02 \cdot 3}{5} = 0{,}024\text{ s}
    \]
    \item Sai số tuyệt đối toàn phần: $\Delta T = \overline{\Delta T} + \Delta T_{\text{dc}} = 0{,}024 + 0{,}01 = 0{,}034\text{ s}$.
    \item Kết quả phép đo: $T = (2{,}030 \pm 0{,}034)\text{ s}$.
\end{itemize}
Chọn đáp án \textbf{C}.
}
\end{vd}

\begin{vd}
Nhiệt độ đầu và nhiệt độ cuối của một lượng nước được ghi bởi một người quan sát trên nhiệt kế là $(42{,}4 \pm 0{,}2)^\circ\text{C}$ và $(80{,}6 \pm 0{,}3)^\circ\text{C}$. Bỏ qua sai số dụng cụ, nhiệt độ của nước đã tăng
\choice
{$(39{,}2 \pm 0{,}5)^\circ\text{C}$}
{$(38{,}2 \pm 0{,}1)^\circ\text{C}$}
{\True $(38{,}2 \pm 0{,}5)^\circ\text{C}$}
{$(39{,}2 \pm 0{,}1)^\circ\text{C}$}
\loigiai{
\begin{itemize}
    \item Độ tăng nhiệt độ trung bình: $\Delta \bar{t} = t_2 - t_1 = 80{,}6 - 42{,}4 = 38{,}2^\circ\text{C}$.
    \item Áp dụng quy tắc sai số của một hiệu, sai số tuyệt đối bằng tổng các sai số tuyệt đối:
    \[
    \Delta (\Delta t) = \Delta t_1 + \Delta t_2 = 0{,}2 + 0{,}3 = 0{,}5^\circ\text{C}
    \]
    \item Kết quả độ tăng nhiệt độ: $\Delta t = (38{,}2 \pm 0{,}5)^\circ\text{C}$.
\end{itemize}
Chọn đáp án \textbf{C}.
}
\end{vd}

\begin{vd}
Điện trở của một dây dẫn bằng kim loại được xác định theo định luật Ohm $R = \frac{U}{I}$. Trong một mạch điện, hiệu điện thế $U$ giữa hai đầu điện trở đo được là $U = (8 \pm 0{,}4)\text{ V}$ và cường độ dòng điện qua điện trở là $I = (4 \pm 0{,}2)\text{ A}$. Giá trị của điện trở cùng sai số tỉ đối bằng
\choice
{$(2 \pm 5\%)\,\Omega$}
{$(2 \pm 7\%)\,\Omega$}
{\True $(2 \pm 10\%)\,\Omega$}
{$(2 \pm 28\%)\,\Omega$}
\loigiai{
\begin{itemize}
    \item Giá trị trung bình của điện trở: $\bar{R} = \frac{\bar{U}}{\bar{I}} = \frac{8}{4} = 2\,\Omega$.
    \item Sai số tỉ đối của một thương bằng tổng các sai số tỉ đối:
    \[
    \delta R = \delta U + \delta I = \frac{\Delta U}{\bar{U}} \cdot 100\% + \frac{\Delta I}{\bar{I}} \cdot 100\% = \frac{0{,}4}{8}\cdot 100\% + \frac{0{,}2}{4}\cdot 100\% = 5\% + 5\% = 10\%
    \]
    \item Kết quả ghi: $R = (2 \pm 10\%)\,\Omega$.
\end{itemize}
Chọn đáp án \textbf{C}.
}
\end{vd}
\vspace{0.3cm}
'''
