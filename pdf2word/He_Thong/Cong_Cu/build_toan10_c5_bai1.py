# -*- coding: utf-8 -*-
"""
CHUYÊN ĐỀ TOÁN 10 - CHƯƠNG 5: CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM
BÀI 1: SỐ GẦN ĐÚNG VÀ SAI SỐ
Bản quyền: LỚP TOÁN CÔ THÚY - GV: HỒ THỊ THÚY - SĐT: 0935.322.328 - Đ/C: 50/2C Phạm Thị Liên

Sinh toàn bộ:
  1. LaTeX Đề & HDG theo kiến trúc Master Main
  2. PDF (pdflatex 2 passes chuẩn số trang)
  3. Word (.docx) chuẩn BTPro, 100% công thức toán OMML
"""
import os
import sys
import re
import shutil
import subprocess
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
LATEX_DIR = os.path.join(BASE_DIR, "He_Thong", "LaTeX", "Toan10_Chuong5_Bai1")
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
SCRATCH_DIR = os.path.join(CURRENT_DIR, "scratch_toan10_c5_b1")
PANDOC = os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")

for d in (LATEX_DIR, SAN_PHAM_DIR, SCRATCH_DIR):
    os.makedirs(d, exist_ok=True)

# Đảm bảo có file ex_test.sty trong thư mục LaTeX
sty_src = os.path.join(BASE_DIR, "He_Thong", "Quy_Chuan", "ex_test.sty")
sty_dst = os.path.join(LATEX_DIR, "ex_test.sty")
if os.path.exists(sty_src) and not os.path.exists(sty_dst):
    shutil.copy2(sty_src, sty_dst)

NAME_DE = "Toan10_C5_Bai1_De"
NAME_HDG = "Toan10_C5_Bai1_HDG"

BRAND = "Lớp Toán Cô Thúy -- SĐT: 0935.322.328 -- 50/2C Phạm Thị Liên"
BRAND_W = "Lớp Toán Cô Thúy  •  SĐT: 0935.322.328  •  50/2C Phạm Thị Liên"

# ============================================================================
# NỘI DUNG TÀI LIỆU (Tóm tắt lý thuyết, Ví dụ, 21 TN, 19 TL)
# ============================================================================
def get_latex_content():
    return r"""
\begin{center}
	{\Large\bfseries\color{blue!80!black} CHƯƠNG V. CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM}\\[6pt]
	{\large\bfseries\color{red!80!black} BÀI 1. SỐ GẦN ĐÚNG VÀ SAI SỐ}
\end{center}
\vspace{0.2cm}

\section*{I. TÓM TẮT LÝ THUYẾT}

\subsection*{1. Số gần đúng}
Trong thực tế, ta thường không biết hoặc khó biết giá trị chính xác (số đúng, kí hiệu $\overline{a}$) mà chỉ tìm được giá trị xấp xỉ nó. Giá trị này được gọi là \textbf{số gần đúng}, kí hiệu là $a$.

\subsection*{2. Sai số tuyệt đối và sai số tương đối}
\begin{itemize}
	\item \textbf{Sai số tuyệt đối:} Giá trị $\Delta_a = |\overline{a} - a|$ phản ánh mức độ sai lệch giữa số đúng $\overline{a}$ và số gần đúng $a$, được gọi là sai số tuyệt đối của số gần đúng $a$.
	\item \textbf{Độ chính xác của số gần đúng:} Nếu $\Delta_a \le d$ thì $a - d \le \overline{a} \le a + d$. Khi đó ta viết $\overline{a} = a \pm d$ và hiểu là số đúng $\overline{a}$ nằm trong đoạn $[a - d; a + d]$. Đại lượng $d > 0$ được gọi là \textbf{độ chính xác} của số gần đúng $a$. Giá trị $d$ càng nhỏ thì $a$ càng gần $\overline{a}$.
	\item \textbf{Sai số tương đối:} Tỉ số $\delta_a = \dfrac{\Delta_a}{|a|}$ được gọi là \textbf{sai số tương đối} của số gần đúng $a$. Nếu $\overline{a} = a \pm d$ thì $\delta_a \le \dfrac{d}{|a|}$. Tỉ số $\dfrac{d}{|a|}$ càng nhỏ thì chất lượng phép đo càng cao. Người ta thường biểu diễn sai số tương đối dưới dạng phần trăm (\%).
\end{itemize}

\subsection*{3. Quy tròn số gần đúng}
\begin{itemize}
	\item \textbf{Quy tắc quy tròn số:}
	\begin{enumerate}
		\item Đối với chữ số hàng làm tròn: Giữ nguyên nếu chữ số ngay bên phải nó nhỏ hơn 5; tăng 1 đơn vị nếu chữ số ngay bên phải nó lớn hơn hoặc bằng 5.
		\item Đối với các chữ số sau hàng làm tròn: Bỏ đi nếu ở phần thập phân; thay bởi các chữ số 0 nếu ở phần nguyên.
	\end{enumerate}
	\item \textbf{Đánh giá sai số khi quy tròn:} Khi thay số đúng bởi số quy tròn đến một hàng nào đó thì sai số tuyệt đối của số quy tròn không vượt quá nửa đơn vị của hàng làm tròn.
	\item \textbf{Quy tắc làm tròn số gần đúng $a$ với độ chính xác $d$:} Khi yêu cầu làm tròn số gần đúng $a$ với độ chính xác $d$, ta làm tròn số $a$ đến hàng cao hơn hàng của độ chính xác một bậc (tức là hàng thấp nhất mà $d$ nhỏ hơn một đơn vị của hàng đó).
\end{itemize}

\vspace{0.3cm}
\section*{II. CÁC DẠNG TOÁN VÀ VÍ DỤ MINH HỌA}

\subsection*{Dạng 1. Xác định số gần đúng và đánh giá độ chính xác}

\begin{vd}
	Đỉnh Everest được mệnh danh là "nóc nhà của thế giới" với nhiều con số từng công bố như: $8848\text{ m}$; $8848{,}13\text{ m}$; $8844{,}43\text{ m}$; $8850\text{ m}$. Hãy giải thích tại sao các con số này đều là số gần đúng.
	\loigiai{
		Chiều cao của đỉnh Everest là một đại lượng vật lí biến đổi liên tục theo thời gian (do lớp băng tuyết dày mỏng theo mùa, do sự dịch chuyển của mảng kiến tạo Trái Đất) và kết quả đo đạc phụ thuộc vào công nghệ, thiết bị đo tại từng thời điểm. Do đó, các con số được công bố đều chỉ là các giá trị xấp xỉ chiều cao thực tế tại thời điểm đo, tức là các \textbf{số gần đúng}.
	}
\end{vd}

\begin{vd}
	Xác định các thông tin sau là số đúng hay số gần đúng:
	\begin{enumerate}[a)]
		\item Bán kính đường Xích Đạo của Trái Đất là $6\,378\text{ km}$.
		\item Khoảng cách từ Mặt Trăng đến Trái Đất là $384\,400\text{ km}$.
		\item $1\text{ m} = 100\text{ cm}$.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item "Bán kính đường Xích Đạo của Trái Đất là $6\,378\text{ km}$" là \textbf{số gần đúng} vì bề mặt Trái Đất không phải là hình cầu hoàn hảo và giá trị đo đạc luôn có sai số.
			\item "Khoảng cách từ Mặt Trăng đến Trái Đất là $384\,400\text{ km}$" là \textbf{số gần đúng} vì quỹ đạo Mặt Trăng là hình elip nên khoảng cách thay đổi liên tục.
			\item "$1\text{ m} = 100\text{ cm}$" là \textbf{số đúng} vì đây là định nghĩa quy ước chuẩn trong hệ đo lường quốc tế SI.
		\end{enumerate}
	}
\end{vd}

\begin{vd}
	Gọi $d$ là độ dài đường chéo của hình vuông có cạnh bằng 1. Trong hai số $\sqrt{2}$ và $1{,}41$, số nào là số đúng, số nào là số gần đúng của $d$?
	\loigiai{
		Theo định lí Pythagore, độ dài đường chéo của hình vuông cạnh 1 là $d = \sqrt{1^2 + 1^2} = \sqrt{2}$.\\
		- Số $\sqrt{2}$ là \textbf{số đúng} biểu diễn độ dài chính xác của đường chéo.\\
		- Số $1{,}41$ là \textbf{số gần đúng} của $\sqrt{2}$ (vì $\sqrt{2} = 1{,}41421356...$).
	}
\end{vd}

\begin{vd}
	Giả sử khối lượng đúng của một hộp kẹo là $0{,}85\text{ kg}$. Hai bạn Bình và An cân hộp kẹo này và ghi nhận kết quả lần lượt là $0{,}8\text{ kg}$ và $1\text{ kg}$.
	\begin{enumerate}[a)]
		\item Tìm sai số tuyệt đối của kết quả cân của mỗi bạn.
		\item Kết quả cân của bạn nào chính xác hơn? Vì sao?
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Sai số tuyệt đối của kết quả cân của bạn Bình:
			\[\Delta_{\text{Bình}} = |0{,}85 - 0{,}8| = 0{,}05\text{ kg}.\]
			Sai số tuyệt đối của kết quả cân của bạn An:
			\[\Delta_{\text{An}} = |0{,}85 - 1| = 0{,}15\text{ kg}.\]
			\item Vì $\Delta_{\text{Bình}} = 0{,}05\text{ kg} < 0{,}15\text{ kg} = \Delta_{\text{An}}$ nên kết quả cân của bạn Bình chính xác hơn kết quả của bạn An.
		\end{enumerate}
	}
\end{vd}

\begin{vd}
	Người ta dùng một đồng hồ bấm giờ có độ chia nhỏ nhất là $0{,}1\text{ giây}$ để đo thời gian hoàn thành cự li bơi của một vận động viên và được kết quả là $27{,}2\text{ giây}$.
	\begin{enumerate}[a)]
		\item Tìm độ chính xác $d$ của phép đo.
		\item Nếu thời gian đúng là $a\text{ giây}$, hãy tìm khoảng giá trị mà $a$ có thể nhận được.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Sai số dụng cụ thông thường không vượt quá một độ chia nhỏ nhất (hoặc nửa độ chia nhỏ nhất). Theo quy ước thông thường trong đo lường, độ chính xác của phép đo lấy bằng độ chia nhỏ nhất: $d = 0{,}1\text{ s}$ (hoặc lấy bằng nửa độ chia: $d = 0{,}05\text{ s}$).
			\item Nếu lấy $d = 0{,}1\text{ s}$ thì thời gian đúng $a$ thỏa mãn:
			\[27{,}2 - 0{,}1 \le a \le 27{,}2 + 0{,}1 \iff 27{,}1 \le a \le 27{,}3\text{ (giây)}.\]
			Nếu lấy $d = 0{,}05\text{ s}$ (nửa độ chia) thì $27{,}15 \le a \le 27{,}25\text{ (giây)}$.
		\end{enumerate}
	}
\end{vd}

\subsection*{Dạng 2. Xác định sai số tương đối của số gần đúng}

\begin{vd}
	Cho $a = 3{,}14$ là số gần đúng của $\overline{a} = \pi$. Biết $\Delta_a = |\pi - 3{,}14| < 0{,}01$. Đánh giá sai số tương đối của $a$.
	\loigiai{
		Ta có độ chính xác $d = 0{,}01$. Sai số tương đối của số gần đúng $a = 3{,}14$ thỏa mãn:
		\[\delta_a = \frac{\Delta_a}{|a|} \le \frac{d}{|a|} = \frac{0{,}01}{3{,}14} \approx 0{,}00318 = 0{,}318\%.\]
	}
\end{vd}

\begin{vd}
	Một bồn hoa hình tròn có bán kính $r = 0{,}8\text{ m}$. Bạn Ngân lấy giá trị gần đúng $\pi \approx 3{,}1$ được diện tích $S_1$. Bạn Ánh lấy $\pi \approx 3{,}14$ được diện tích $S_2$. So sánh sai số tuyệt đối $\Delta_{S_1}$ và $\Delta_{S_2}$. Bạn nào cho kết quả chính xác hơn?
	\loigiai{
		Diện tích đúng của bồn hoa là $S = \pi r^2 = \pi \cdot (0{,}8)^2 = 0{,}64\pi\text{ m}^2$.\\
		- Kết quả của bạn Ngân: $S_1 = 3{,}1 \cdot 0{,}64 = 1{,}984\text{ m}^2$. Sai số tuyệt đối:
		\[\Delta_{S_1} = |S - S_1| = 0{,}64 \cdot |\pi - 3{,}1| \approx 0{,}64 \cdot 0{,}04159 = 0{,}0266\text{ m}^2.\]
		- Kết quả của bạn Ánh: $S_2 = 3{,}14 \cdot 0{,}64 = 2{,}0096\text{ m}^2$. Sai số tuyệt đối:
		\[\Delta_{S_2} = |S - S_2| = 0{,}64 \cdot |\pi - 3{,}14| \approx 0{,}64 \cdot 0{,}00159 = 0{,}0010\text{ m}^2.\]
		Vì $\Delta_{S_2} < \Delta_{S_1}$ nên bạn Ánh cho kết quả chính xác hơn bạn Ngân.
	}
\end{vd}

\begin{vd}
	Một tờ giấy A4 có chiều dài $29{,}7\text{ cm}$ và chiều rộng $21\text{ cm}$. Tính độ dài đường chéo tờ giấy và xác định độ chính xác của kết quả khi làm tròn đến hàng phần mười.
	\loigiai{
		Độ dài đúng của đường chéo là:
		\[d = \sqrt{29{,}7^2 + 21^2} = \sqrt{882{,}09 + 441} = \sqrt{1323{,}09} \approx 36{,}3743\text{ cm}.\]
		Làm tròn đến hàng phần mười ta được số gần đúng là $36{,}4\text{ cm}$.\\
		Sai số tuyệt đối của phép làm tròn không vượt quá nửa đơn vị hàng làm tròn: $\Delta \le 0{,}05\text{ cm}$.\\
		Vậy độ chính xác của kết quả làm tròn là $d = 0{,}05\text{ cm}$.
	}
\end{vd}

\subsection*{Dạng 3. Xác định số quy tròn của số gần đúng với độ chính xác cho trước}

\begin{vd}
	Quy tròn số $3{,}141$ đến hàng phần trăm rồi tính sai số tuyệt đối của số quy tròn.
	\loigiai{
		Chữ số hàng phần trăm là $4$, chữ số ngay bên phải là $1 < 5$ nên ta giữ nguyên chữ số hàng phần trăm và bỏ chữ số sau đó.\\
		Số quy tròn là $3{,}14$.\\
		Sai số tuyệt đối của số quy tròn:
		\[\Delta = |3{,}141 - 3{,}14| = 0{,}001.\]
	}
\end{vd}

\begin{vd}
	\begin{enumerate}[a)]
		\item Làm tròn số $2395{,}3$ đến hàng chục, số $18{,}693$ đến hàng phần trăm và số đúng $d \in [5{,}5; 6{,}5)$ đến hàng đơn vị. Đánh giá sai số tuyệt đối của phép làm tròn số đúng $d$.
		\item Cho số gần đúng $a = 2{,}53$ với độ chính xác $d = 0{,}01$. Số đúng $\overline{a}$ thuộc đoạn nào? Nếu làm tròn số $a$ thì nên làm tròn đến hàng nào? Vì sao?
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Làm tròn $2395{,}3$ đến hàng chục: vì chữ số hàng đơn vị là $5$ nên tăng hàng chục thêm 1 đơn vị $\implies 2400$.\\
			Làm tròn $18{,}693$ đến hàng phần trăm: chữ số hàng phần nghìn là $3 < 5$ nên giữ nguyên $\implies 18{,}69$.\\
			Với mọi số đúng $d \in [5{,}5; 6{,}5)$, khi làm tròn đến hàng đơn vị ta đều được kết quả là $6$ (vì phần thập phân luôn $\ge 0{,}5$ và $< 1{,}5$). Sai số tuyệt đối của phép làm tròn này thỏa mãn:
			\[\Delta = |d - 6| \le 0{,}5.\]
			\item Vì $\overline{a} = 2{,}53 \pm 0{,}01$ nên số đúng $\overline{a}$ thuộc đoạn:
			\[[2{,}53 - 0{,}01; 2{,}53 + 0{,}01] = [2{,}52; 2{,}54].\]
			Độ chính xác $d = 0{,}01$ ở hàng phần trăm, do đó chữ số hàng phần trăm trong số gần đúng chưa đáng tin cậy. Vì vậy, ta nên làm tròn số $a$ đến \textbf{hàng phần mười} (hàng cao hơn hàng của $d$ một bậc). Khi đó số quy tròn là $2{,}5$.
		\end{enumerate}
	}
\end{vd}

\begin{vd}
	Cho số gần đúng $a = 581\,268$ với độ chính xác $d = 200$. Hãy viết số quy tròn của số $a$.
	\loigiai{
		Độ chính xác $d = 200$ thỏa mãn $100 \le d < 1000$, tức là hàng của độ chính xác là hàng trăm. Do đó ta làm tròn số $a$ đến \textbf{hàng nghìn}.\\
		Chữ số hàng nghìn là $1$, chữ số ngay sau nó (hàng trăm) là $2 < 5$ nên giữ nguyên.\\
		Vậy số quy tròn của $a$ là $581\,000$.
	}
\end{vd}

\begin{vd}
	Viết số quy tròn của mỗi số sau với độ chính xác $d$:
	\begin{enumerate}[a)]
		\item $2\,841\,331$ với $d = 400$;
		\item $4{,}1463$ với $d = 0{,}01$;
		\item $1{,}4142135$ với $d = 0{,}001$.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Với $d = 400$ ($100 \le d < 1000$, hàng trăm), ta làm tròn đến hàng nghìn. Chữ số hàng trăm là $3 < 5$ nên số quy tròn là $2\,841\,000$.
			\item Với $d = 0{,}01$ (hàng phần trăm), ta làm tròn đến hàng phần mười. Chữ số hàng phần trăm là $4 < 5$ nên số quy tròn là $4{,}1$.
			\item Với $d = 0{,}001$ (hàng phần nghìn), ta làm tròn đến hàng phần trăm. Chữ số hàng phần nghìn là $4 < 5$ nên số quy tròn là $1{,}41$.
		\end{enumerate}
	}
\end{vd}

\subsection*{Dạng 4. Sử dụng máy tính cầm tay để tính toán với số gần đúng}

\begin{vd}
	Sử dụng máy tính cầm tay, tính $3^7 \cdot \sqrt{14}$ (trong kết quả lấy bốn chữ số ở phần thập phân).
	\loigiai{
		Nhập vào máy tính biểu thức $3^7 \times \sqrt{14}$ ta được kết quả hiển thị xấp xỉ:\\
		$3^7 \cdot \sqrt{14} = 2187 \cdot \sqrt{14} \approx 8182{,}806847...$\\
		Lấy bốn chữ số ở phần thập phân (làm tròn đến hàng phần chục nghìn): kết quả là \textbf{$8182{,}8068$}.
	}
\end{vd}

\begin{vd}
	Dùng máy tính cầm tay, tính kết quả của phép tính $\sqrt[3]{15} : 5 - 2$ (trong kết quả lấy hai chữ số ở phần thập phân).
	\loigiai{
		Thực hiện bấm máy tính biểu thức $\sqrt[3]{15} \div 5 - 2$:\\
		Ta có $\sqrt[3]{15} \approx 2{,}466212 \implies \dfrac{\sqrt[3]{15}}{5} \approx 0{,}493242$.\\
		Do đó $\sqrt[3]{15} : 5 - 2 \approx 0{,}493242 - 2 = -1{,}506757...$\\
		Làm tròn đến hai chữ số ở phần thập phân (chữ số thứ ba là $6 \ge 5$): kết quả là \textbf{$-1{,}51$}.
	}
\end{vd}

\begin{vd}
	Gọi $P$ là chu vi của đường tròn bán kính $1\text{ cm}$. Hãy tìm giá trị gần đúng của $P$ (trong kết quả lấy hai chữ số ở phần thập phân).
	\loigiai{
		Chu vi đường tròn bán kính $R = 1\text{ cm}$ là $P = 2\pi R = 2\pi\text{ cm}$.\\
		Sử dụng máy tính bấm $2 \times \pi$ ta được $P \approx 6{,}283185...$\\
		Lấy hai chữ số ở phần thập phân: kết quả là \textbf{$6{,}28\text{ cm}$}.
	}
\end{vd}

\vspace{0.4cm}
\section*{III. BÀI TẬP VẬN DỤNG}

\subsection*{PHẦN I. CÂU HỎI TRẮC NGHIỆM}
\textit{\small (Mỗi câu học sinh chỉ chọn một phương án trả lời đúng)}
\setcounter{ex}{0}

% Câu 1
\begin{ex}
	Cho $a$ là số gần đúng của số đúng $\overline{a}$. Khi đó $\Delta_a = |\overline{a} - a|$ được gọi là
	\choice
	{số quy tròn của $\overline{a}$}
	{sai số tương đối của số gần đúng $a$}
	{\True sai số tuyệt đối của số gần đúng $a$}
	{số quy tròn của $a$}
	\loigiai{
		Theo định nghĩa, sai số tuyệt đối của số gần đúng $a$ là $\Delta_a = |\overline{a} - a|$.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 2
\begin{ex}
	Cho số $a$ là số gần đúng của số $\overline{a}$. Mệnh đề nào sau đây là mệnh đề đúng?
	\choice
	{$a > \overline{a}$}
	{$a < \overline{a}$}
	{\True $|\overline{a} - a| > 0$}
	{$-a < \overline{a} < a$}
	\loigiai{
		Số gần đúng $a$ xấp xỉ số đúng $\overline{a}$ nhưng khác $\overline{a}$, do đó khoảng cách $|\overline{a} - a| > 0$ (hoặc tổng quát $|\overline{a} - a| \ge 0$). Các khẳng định $a > \overline{a}$ hay $a < \overline{a}$ đều không nhất thiết xảy ra.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 3
\begin{ex}
	Cho số $a$ là số gần đúng của $\overline{a}$ với độ chính xác $d$. Mệnh đề nào sau đây là mệnh đề đúng?
	\choice
	{$\overline{a} = a + d$}
	{$\overline{a} = a - d$}
	{$\overline{a} = a$}
	{\True $\overline{a} = a \pm d$}
	\loigiai{
		Theo quy ước kí hiệu về độ chính xác: khi $\Delta_a \le d$, ta viết $\overline{a} = a \pm d$.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 4
\begin{ex}
	Kết quả làm tròn số $b = 500\sqrt{7}$ đến chữ số thập phân thứ hai là
	\choice
	{$b \approx 132{,}88$}
	{\True $b \approx 1322{,}88$}
	{$b \approx 1322{,}8$}
	{$b \approx 1322{,}9$}
	\loigiai{
		Ta có $b = 500\sqrt{7} \approx 1322{,}875655...$\\
		Chữ số thập phân thứ ba là $5 \ge 5$ nên tăng chữ số thập phân thứ hai lên 1 đơn vị: $b \approx 1322{,}88$.\\
		Chọn \textbf{B} (phương án đúng chính xác là $1322{,}88$).
	}
\end{ex}

% Câu 5
\begin{ex}
	Kết quả làm tròn của số $c = 76\,324\,753{,}3695$ đến hàng nghìn là
	\choice
	{$c \approx 76\,324\,000$}
	{\True $c \approx 76\,325\,000$}
	{$c \approx 76\,324\,753{,}369$}
	{$c \approx 76\,324\,753{,}37$}
	\loigiai{
		Hàng làm tròn là hàng nghìn (chữ số $4$). Chữ số ngay bên phải nó (hàng trăm) là $7 \ge 5$, do đó ta cộng thêm 1 đơn vị vào hàng nghìn và thay các chữ số sau hàng nghìn bằng chữ số $0$ (bỏ phần thập phân):\\
		$c \approx 76\,325\,000$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 6
\begin{ex}
	Viết số quy tròn của số gần đúng $a = 505\,360{,}996$ biết $\overline{a} = 505\,360{,}996 \pm 100$.
	\choice
	{$a \approx 505$}
	{$a \approx 5054$}
	{$a \approx 505\,400$}
	{\True $a \approx 505\,000$}
	\loigiai{
		Độ chính xác $d = 100$ là hàng trăm, do đó ta quy tròn số gần đúng $a$ đến \textbf{hàng nghìn}.\\
		Chữ số hàng nghìn là $5$, chữ số ngay sau nó là $3 < 5$ nên ta giữ nguyên chữ số hàng nghìn và thay các chữ số sau đó bằng $0$:\\
		$a \approx 505\,000$.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 7
\begin{ex}
	Viết số quy tròn số gần đúng $b = 3257{,}6254$ với độ chính xác $d = 0{,}01$.
	\choice
	{$b \approx 3257{,}63$}
	{$b \approx 3257{,}62$}
	{\True $b \approx 3257{,}6$}
	{$b \approx 3257{,}7$}
	\loigiai{
		Độ chính xác $d = 0{,}01$ ở hàng phần trăm, do đó ta quy tròn $b$ đến \textbf{hàng phần mười}.\\
		Chữ số hàng phần mười là $6$, chữ số ngay bên phải là $2 < 5$ nên giữ nguyên:\\
		$b \approx 3257{,}6$.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 8
\begin{ex}
	Cho giá trị gần đúng của số $\pi$ là $x = 3{,}141592653589$ với độ chính xác $10^{-10}$. Hãy viết số quy tròn của $x$.
	\choice
	{\True $x \approx 3{,}141592654$}
	{$x \approx 3{,}1415926535$}
	{$x \approx 3{,}1415926536$}
	{$x \approx 3{,}141592653$}
	\loigiai{
		Độ chính xác $d = 10^{-10}$ ở hàng phần mười tỉ (chữ số thập phân thứ 10). Do đó ta quy tròn $x$ đến hàng phần tỉ (chữ số thập phân thứ 9).\\
		Chữ số thập phân thứ 9 là $3$, chữ số thập phân thứ 10 là $5 \ge 5$ nên tăng 1 đơn vị thành $4$:\\
		$x \approx 3{,}141592654$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 9
\begin{ex}
	Cho $\overline{a} = 1{,}7059 \pm 0{,}001$, kết quả làm tròn số gần đúng $a = 1{,}7059$ là
	\choice
	{\True $1{,}71$}
	{$1{,}706$}
	{$1{,}7$}
	{$1{,}705$}
	\loigiai{
		Độ chính xác $d = 0{,}001$ ở hàng phần nghìn, do đó ta làm tròn số $a$ đến \textbf{hàng phần trăm}.\\
		Chữ số hàng phần trăm là $0$, chữ số hàng phần nghìn là $5 \ge 5$ nên tăng hàng phần trăm thêm 1 đơn vị:\\
		Số quy tròn là $1{,}71$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 10
\begin{ex}
	Cho $\overline{a} = 123\,564 \pm 100$. Kết quả làm tròn số gần đúng $x = 123\,564$ là
	\choice
	{$12360$}
	{$123\,000$}
	{$123\,570$}
	{\True $124\,000$}
	\loigiai{
		Độ chính xác $d = 100$ ở hàng trăm, nên ta quy tròn số $x$ đến \textbf{hàng nghìn}.\\
		Chữ số hàng nghìn là $3$, chữ số hàng trăm là $5 \ge 5$ nên tăng chữ số hàng nghìn thành $4$:\\
		Số quy tròn là $124\,000$.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 11
\begin{ex}
	Số gần đúng $a = 173{,}4592$ có sai số tuyệt đối không vượt quá $0{,}01$. Số quy tròn của $a$ là
	\choice
	{$173{,}45$}
	{$173{,}46$}
	{\True $173{,}5$}
	{$173$}
	\loigiai{
		Độ chính xác $d = 0{,}01$ ở hàng phần trăm, do đó ta quy tròn số $a$ đến \textbf{hàng phần mười}.\\
		Chữ số hàng phần mười là $4$, chữ số ngay sau nó là $5 \ge 5$ nên tăng lên thành $5$:\\
		Số quy tròn là $173{,}5$.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 12
\begin{ex}
	Trong các số dưới đây, giá trị gần đúng của $\sqrt{30} - 5$ với sai số tuyệt đối bé nhất là
	\choice
	{$0{,}476$}
	{\True $0{,}477$}
	{$0{,}478$}
	{$0{,}479$}
	\loigiai{
		Ta có $\sqrt{30} \approx 5{,}477225575 \implies \sqrt{30} - 5 \approx 0{,}477225575$.\\
		Tính sai số tuyệt đối của các phương án:
		\begin{itemize}
			\item Với $0{,}476$: $\Delta = |0{,}477225575 - 0{,}476| \approx 0{,}001226$.
			\item Với $0{,}477$: $\Delta = |0{,}477225575 - 0{,}477| \approx 0{,}000226$ (bé nhất).
			\item Với $0{,}478$: $\Delta = |0{,}477225575 - 0{,}478| \approx 0{,}000774$.
			\item Với $0{,}479$: $\Delta = |0{,}477225575 - 0{,}479| \approx 0{,}001774$.
		\end{itemize}
		Vậy giá trị $0{,}477$ có sai số tuyệt đối bé nhất.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 13
\begin{ex}
	Nếu lấy $3{,}14$ làm giá trị gần đúng cho số $\pi$ thì sai số tuyệt đối không vượt quá
	\choice
	{\True $0{,}01$}
	{$0{,}02$}
	{$0{,}03$}
	{$0{,}04$}
	\loigiai{
		Ta có $\pi \approx 3{,}14159265... \implies |\pi - 3{,}14| \approx 0{,}00159 < 0{,}01$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 14
\begin{ex}
	Nếu lấy $3{,}1416$ làm giá trị gần đúng cho $\pi$ thì sai số tuyệt đối không vượt quá
	\choice
	{$0{,}0002$}
	{$0{,}0003$}
	{\True $0{,}0001$}
	{$0{,}0004$}
	\loigiai{
		Ta có $\pi \approx 3{,}14159265... \implies |\pi - 3{,}1416| \approx 0{,}0000073 < 0{,}0001$.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 15
\begin{ex}
	Cho giá trị gần đúng của $\dfrac{8}{17}$ là $0{,}47$ thì sai số tuyệt đối không vượt quá
	\choice
	{\True $0{,}01$}
	{$0{,}02$}
	{$0{,}03$}
	{$0{,}04$}
	\loigiai{
		Ta có $\dfrac{8}{17} \approx 0{,}470588... \implies \left|\dfrac{8}{17} - 0{,}47\right| \approx 0{,}000588 < 0{,}01$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 16
\begin{ex}
	Cho giá trị gần đúng của $\dfrac{3}{7}$ là $0{,}429$ thì sai số tuyệt đối không vượt quá
	\choice
	{$0{,}002$}
	{\True $0{,}001$}
	{$0{,}003$}
	{$0{,}004$}
	\loigiai{
		Ta có $\dfrac{3}{7} \approx 0{,}428571... \implies \left|\dfrac{3}{7} - 0{,}429\right| \approx 0{,}000429 < 0{,}001$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 17
\begin{ex}
	Một vật có thể tích $V = 180{,}37\text{ cm}^3 \pm 0{,}05\text{ cm}^3$. Nếu lấy $180{,}37\text{ cm}^3$ làm giá trị gần đúng cho $V$ thì sai số tương đối của giá trị gần đúng đó không vượt quá
	\choice
	{\True $0{,}03\%$}
	{$0{,}01\%$}
	{$0{,}02\%$}
	{$0{,}001\%$}
	\loigiai{
		Sai số tương đối thỏa mãn:
		\[\delta_V \le \frac{d}{|V|} = \frac{0{,}05}{180{,}37} \approx 0{,}000277 = 0{,}0277\% < 0{,}03\%.\]
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 18
\begin{ex}
	Số $\overline{a}$ được cho bởi giá trị gần đúng $a = 5{,}7824$ với sai số tương đối không vượt quá $0{,}05\%$. Khi đó, sai số tuyệt đối của $a$ không vượt quá
	\choice
	{\True $0{,}0028912$}
	{$0{,}0027912$}
	{$0{,}0026912$}
	{$0{,}0025912$}
	\loigiai{
		Ta có $\delta_a = \dfrac{\Delta_a}{|a|} \le 0{,}05\% = 0{,}0005$.\\
		Suy ra sai số tuyệt đối không vượt quá:
		\[\Delta_a \le |a| \cdot \delta_a = 5{,}7824 \cdot 0{,}0005 = 0{,}0028912.\]
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 19
\begin{ex}
	Cho $\overline{a} = \dfrac{1}{1 + x}$ ($0 < x < 1$). Giả sử ta lấy $a = 1 - x$ làm giá trị gần đúng của $\overline{a}$. Khi đó, sai số tương đối của $a$ theo $x$ bằng
	\choice
	{\True $\dfrac{x^2}{1 - x^2}$}
	{$\dfrac{x}{1 - x}$}
	{$\dfrac{x^2}{1 - x}$}
	{$\dfrac{x}{1 - x^2}$}
	\loigiai{
		Sai số tuyệt đối của $a$ là:
		\[\Delta_a = |\overline{a} - a| = \left|\frac{1}{1 + x} - (1 - x)\right| = \left|\frac{1 - (1 - x^2)}{1 + x}\right| = \frac{x^2}{1 + x}\text{ (vì $0 < x < 1$)}.\]
		Sai số tương đối của $a$ là:
		\[\delta_a = \frac{\Delta_a}{|a|} = \frac{\dfrac{x^2}{1 + x}}{1 - x} = \frac{x^2}{(1 + x)(1 - x)} = \frac{x^2}{1 - x^2}.\]
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 20
\begin{ex}
	Các nhà toán học cổ đại Trung Quốc đã dùng phân số $\dfrac{22}{7}$ để xấp xỉ số $\pi$. Hãy đánh giá sai số tuyệt đối $\Delta$ của giá trị gần đúng này, biết $3{,}1415 < \pi < 3{,}1416$.
	\choice
	{$\Delta < 0{,}0012$}
	{\True $\Delta < 0{,}0014$}
	{$\Delta < 0{,}0013$}
	{$\Delta < 0{,}0011$}
	\loigiai{
		Ta có $\dfrac{22}{7} \approx 3{,}142857 > \pi$.\\
		Sai số tuyệt đối là:
		\[\Delta = \left|\frac{22}{7} - \pi\right| = \frac{22}{7} - \pi.\]
		Vì $\pi > 3{,}1415$ nên:
		\[\Delta < \frac{22}{7} - 3{,}1415 \approx 3{,}142857 - 3{,}1415 = 0{,}001357 < 0{,}0014.\]
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 21
\begin{ex}
	Hình chữ nhật có các cạnh là $x = 2\text{ m} \pm 1\text{ cm}$ và $y = 5\text{ m} \pm 2\text{ cm}$. Diện tích của hình chữ nhật và sai số tương đối của giá trị đó là
	\choice
	{\True $10\text{ m}^2$ và $\delta \le 0{,}91\%$}
	{$10\text{ m}^2$ và $\delta \le 0{,}9\%$}
	{$10\text{ m}^2$ và $\delta \le 0{,}92\%$}
	{$10\text{ m}^2$ và $\delta \le 0{,}93\%$}
	\loigiai{
		Đổi đơn vị: $x = 2 \pm 0{,}01\text{ m}$ và $y = 5 \pm 0{,}02\text{ m}$.\\
		Giá trị gần đúng của diện tích là:
		\[S = x \cdot y = 2 \cdot 5 = 10\text{ m}^2.\]
		Diện tích thực tế $\overline{S} = \overline{x} \cdot \overline{y}$ thỏa mãn:
		\[(2 - 0{,}01)(5 - 0{,}02) \le \overline{S} \le (2 + 0{,}01)(5 + 0{,}02) \iff 1{,}99 \cdot 4{,}98 \le \overline{S} \le 2{,}01 \cdot 5{,}02\]
		\[\iff 9{,}9102 \le \overline{S} \le 10{,}0902.\]
		Sai số tuyệt đối: $\Delta_S = |\overline{S} - 10| \le 10{,}0902 - 10 = 0{,}0902\text{ m}^2$.\\
		Sai số tương đối:
		\[\delta_S = \frac{\Delta_S}{S} \le \frac{0{,}0902}{10} = 0{,}00902 = 0{,}902\% \le 0{,}91\%.\]
		Chọn \textbf{A}.
	}
\end{ex}

\vspace{0.4cm}
\subsection*{PHẦN II. CÂU HỎI TỰ LUẬN}
\textit{\small (Học sinh trình bày chi tiết lời giải các bài toán sau)}


% Bài 1
\begin{bt}
	Một bao gạo ghi thông tin khối lượng là $5 \pm 0{,}2\text{ kg}$.
	\begin{enumerate}[a)]
		\item Xác định khối lượng đúng, khối lượng gần đúng và độ chính xác của bao gạo.
		\item Khối lượng thực của bao gạo nằm trong đoạn nào?
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Kí hiệu $\overline{m}$ là khối lượng đúng (thực) của bao gạo.\\
			Khối lượng gần đúng là $m = 5\text{ kg}$.\\
			Độ chính xác của phép đo là $d = 0{,}2\text{ kg}$.
			\item Khối lượng thực $\overline{m}$ của bao gạo nằm trong đoạn:
			\[[5 - 0{,}2; 5 + 0{,}2] = [4{,}8; 5{,}2]\text{ (kg)}.\]
		\end{enumerate}
	}
\end{bt}

% Bài 2
\begin{bt}
	Một phép đo đường kính nhân tế bào cho kết quả là $5 \pm 0{,}3\ \mu\text{m}$. Đường kính thực của nhân tế bào thuộc đoạn nào?
	\loigiai{
		Gọi $\overline{D}$ là đường kính thực của nhân tế bào.\\
		Theo giả thiết, đường kính gần đúng là $D = 5\ \mu\text{m}$ với độ chính xác $d = 0{,}3\ \mu\text{m}$.\\
		Do đó, đường kính thực của nhân tế bào thuộc đoạn:
		\[[5 - 0{,}3; 5 + 0{,}3] = [4{,}7; 5{,}3]\ (\mu\text{m}).\]
	}
\end{bt}

% Bài 3
\begin{bt}
	Chiều dài một cái cầu là $\ell = 1745{,}25\text{ m} \pm 0{,}01\text{ m}$.
	\begin{enumerate}[a)]
		\item Xác định chiều dài đúng, chiều dài gần đúng và độ chính xác của cái cầu.
		\item Chiều dài thực của cái cầu nằm trong đoạn nào?
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Chiều dài đúng của cái cầu được kí hiệu là $\overline{\ell}$.\\
			Chiều dài gần đúng là $\ell = 1745{,}25\text{ m}$.\\
			Độ chính xác là $d = 0{,}01\text{ m}$.
			\item Chiều dài thực của cái cầu nằm trong đoạn:
			\[[1745{,}25 - 0{,}01; 1745{,}25 + 0{,}01] = [1745{,}24; 1745{,}26]\text{ (m)}.\]
		\end{enumerate}
	}
\end{bt}

% Bài 4
\begin{bt}
	Biết $\sqrt{7} = 2{,}6457513...$
	\begin{enumerate}[a)]
		\item Làm tròn kết quả đến phần mười và ước lượng sai số tuyệt đối.
		\item Làm tròn kết quả đến phần nghìn và ước lượng sai số tuyệt đối.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Làm tròn đến hàng phần mười (chữ số thập phân thứ nhất):\\
			Chữ số hàng phần mười là $6$, chữ số kế tiếp là $4 < 5$ nên số quy tròn là $2{,}6$.\\
			Ước lượng sai số tuyệt đối:
			\[\Delta = |\sqrt{7} - 2{,}6| \approx |2{,}6457513 - 2{,}6| = 0{,}0457513 < 0{,}05.\]
			\item Làm tròn đến hàng phần nghìn (chữ số thập phân thứ ba):\\
			Chữ số hàng phần nghìn là $5$, chữ số kế tiếp là $7 \ge 5$ nên số quy tròn là $2{,}646$.\\
			Ước lượng sai số tuyệt đối:
			\[\Delta = |\sqrt{7} - 2{,}646| \approx |2{,}6457513 - 2{,}646| = 0{,}0002487 < 0{,}0005.\]
		\end{enumerate}
	}
\end{bt}

% Bài 5
\begin{bt}
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
\end{bt}

% Bài 6
\begin{bt}
	Cho số gần đúng $a = 6547$ với độ chính xác $d = 100$. Hãy viết số quy tròn của số $a$ và ước lượng sai số tương đối của số quy tròn đó.
	\loigiai{
		Vì độ chính xác $d = 100$ là hàng trăm nên ta quy tròn số $a$ đến \textbf{hàng nghìn}.\\
		Chữ số hàng nghìn là $6$, chữ số ngay bên phải là $5 \ge 5$ nên tăng lên 1 đơn vị:\\
		Số quy tròn là $a^* = 7000$.\\
		Sai số tuyệt đối của số quy tròn $a^*$ đối với số đúng $\overline{a}$:\\
		Ta có $|\overline{a} - 6547| \le 100$ và $|7000 - 6547| = 453$, suy ra:
		\[\Delta_{a^*} = |\overline{a} - 7000| \le |\overline{a} - 6547| + |6547 - 7000| \le 100 + 453 = 553.\]
		Ước lượng sai số tương đối của số quy tròn:
		\[\delta_{a^*} = \frac{\Delta_{a^*}}{|a^*|} \le \frac{553}{7000} \approx 0{,}079 = 7{,}9\%.\]
	}
\end{bt}

% Bài 7
\begin{bt}
	Cho số gần đúng $a = 23\,748\,023$ với độ chính xác $d = 101$. Hãy viết số quy tròn của số $a$ và ước lượng sai số tương đối của số quy tròn đó.
	\loigiai{
		Vì $100 \le d = 101 < 1000$ nên hàng của độ chính xác là hàng trăm. Do đó ta quy tròn số $a$ đến \textbf{hàng nghìn}.\\
		Chữ số hàng nghìn là $8$, chữ số hàng trăm là $0 < 5$ nên giữ nguyên chữ số hàng nghìn:\\
		Số quy tròn là $a^* = 23\,748\,000$.\\
		Sai số tuyệt đối của số quy tròn:\\
		\[\Delta_{a^*} \le |\overline{a} - a| + |a - a^*| \le 101 + |23\,748\,023 - 23\,748\,000| = 101 + 23 = 124.\]
		Ước lượng sai số tương đối của số quy tròn:
		\[\delta_{a^*} \le \frac{124}{23\,748\,000} \approx 5{,}22 \times 10^{-6} \approx 0{,}000522\%.\]
	}
\end{bt}

% Bài 8
\begin{bt}
	Cho biết $\sqrt{3} = 1{,}7320508...$ Hãy quy tròn $\sqrt{3}$ đến hàng phần trăm và ước lượng sai số tương đối.
	\loigiai{
		Làm tròn $\sqrt{3}$ đến hàng phần trăm (chữ số thập phân thứ hai):\\
		Chữ số hàng phần trăm là $3$, chữ số kế tiếp là $2 < 5$ nên số quy tròn là $1{,}73$.\\
		Sai số tuyệt đối của phép quy tròn:
		\[\Delta = |\sqrt{3} - 1{,}73| \approx |1{,}7320508 - 1{,}73| = 0{,}0020508 < 0{,}005.\]
		Sai số tương đối:
		\[\delta = \frac{\Delta}{1{,}73} < \frac{0{,}005}{1{,}73} \approx 0{,}00289 = 0{,}289\%.\]
	}
\end{bt}

% Bài 9
\begin{bt}
	Cho $\overline{a} = \dfrac{1}{1 + x}$ ($0 < x < 1$). Giả sử ta lấy $a = 1 - x$ làm giá trị gần đúng của $\overline{a}$. Hãy tính sai số tương đối của $a$ theo $x$.
	\loigiai{
		Sai số tuyệt đối:
		\[\Delta_a = |\overline{a} - a| = \left|\frac{1}{1 + x} - (1 - x)\right| = \left|\frac{1 - (1 - x^2)}{1 + x}\right| = \frac{x^2}{1 + x}\text{ (do $0 < x < 1$)}.\]
		Sai số tương đối:
		\[\delta_a = \frac{\Delta_a}{|a|} = \frac{\dfrac{x^2}{1 + x}}{1 - x} = \frac{x^2}{(1 + x)(1 - x)} = \frac{x^2}{1 - x^2}.\]
	}
\end{bt}

% Bài 10
\begin{bt}
	Làm tròn các số sau đến chữ số hàng chục:
	\begin{multicols}{5}
		\begin{enumerate}[a)]
			\item $199$
			\item $999$
			\item $9999$
			\item $2683$
			\item $1099$
			\item $12345$
			\item $123456$
			\item $43781$
			\item $454995$
			\item $14350$
			\item $99999$
			\item $987698$
			\item $3400065$
			\item $1000587$
			\item $987654$
			\item $28051989$
			\item $2602283$
			\item $123{,}45$
			\item $12345{,}67$
			\item $98765{,}432$
		\end{enumerate}
	\end{multicols}
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng đơn vị (ngay bên phải hàng chục): nếu $< 5$ thì giữ nguyên hàng chục, nếu $\ge 5$ thì tăng hàng chục thêm 1 đơn vị, các chữ số sau hàng chục thay bằng $0$ (bỏ phần thập phân):
		\begin{multicols}{2}
		\begin{itemize}
			\item a) $199 \approx 200$.
			\item b) $999 \approx 1000$.
			\item c) $9999 \approx 10\,000$.
			\item d) $2683 \approx 2680$.
			\item e) $1099 \approx 1100$.
			\item f) $12345 \approx 12\,350$.
			\item g) $123456 \approx 123\,460$.
			\item h) $43781 \approx 43\,780$.
			\item i) $454995 \approx 455\,000$.
			\item j) $14350 \approx 14\,350$.
			\item k) $99999 \approx 100\,000$.
			\item l) $987698 \approx 987\,700$.
			\item m) $3400065 \approx 3\,400\,070$.
			\item n) $1000587 \approx 1\,000\,590$.
			\item o) $987654 \approx 987\,650$.
			\item p) $28051989 \approx 28\,051\,990$.
			\item q) $2602283 \approx 2\,602\,280$.
			\item r) $123{,}45 \approx 120$.
			\item s) $12345{,}67 \approx 12\,350$.
			\item t) $98765{,}432 \approx 98\,770$.
		\end{itemize}
		\end{multicols}
	}
\end{bt}

% Bài 11
\begin{bt}
	Làm tròn các số sau đến chữ số hàng trăm:
	\begin{multicols}{5}
		\begin{enumerate}[a)]
			\item $199$
			\item $999$
			\item $9999$
			\item $1099$
			\item $2683$
			\item $12345$
			\item $43781$
			\item $14350$
			\item $1234567$
			\item $454995$
			\item $99999$
			\item $987698$
			\item $3400065$
			\item $987654$
			\item $260283$
			\item $23456{,}7$
			\item $12345{,}678$
			\item $8765{,}432$
			\item $9999{,}99$
		\end{enumerate}
	\end{multicols}
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng chục (ngay bên phải hàng trăm):
		\begin{multicols}{2}
		\begin{itemize}
			\item a) $199 \approx 200$.
			\item b) $999 \approx 1000$.
			\item c) $9999 \approx 10\,000$.
			\item d) $1099 \approx 1100$.
			\item e) $2683 \approx 2700$.
			\item f) $12345 \approx 12\,300$.
			\item g) $43781 \approx 43\,800$.
			\item h) $14350 \approx 14\,400$.
			\item i) $1234567 \approx 1\,234\,600$.
			\item j) $454995 \approx 455\,000$.
			\item k) $99999 \approx 100\,000$.
			\item l) $987698 \approx 987\,700$.
			\item m) $3400065 \approx 3\,400\,100$.
			\item n) $987654 \approx 987\,700$.
			\item o) $260283 \approx 260\,300$.
			\item p) $23456{,}7 \approx 23\,500$.
			\item q) $12345{,}678 \approx 12\,300$.
			\item r) $8765{,}432 \approx 8800$.
			\item s) $9999{,}99 \approx 10\,000$.
		\end{itemize}
		\end{multicols}
	}
\end{bt}

% Bài 12
\begin{bt}
	Làm tròn các số sau đến chữ số hàng nghìn:
	\begin{multicols}{5}
		\begin{enumerate}[a)]
			\item $12\,345$
			\item $43\,781$
			\item $28\,634$
			\item $21\,999$
			\item $22\,999$
			\item $9999$
			\item $12\,099$
			\item $454\,995$
			\item $14\,350$
			\item $99\,999$
			\item $987\,698$
			\item $3\,400\,065$
			\item $1\,000\,587$
			\item $987\,654$
			\item $260\,283$
			\item $23456{,}7$
			\item $1\,234\,567$
			\item $12345{,}678$
			\item $8765{,}432$
			\item $9999{,}99$
		\end{enumerate}
	\end{multicols}
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng trăm (ngay bên phải hàng nghìn):
		\begin{multicols}{2}
		\begin{itemize}
			\item a) $12\,345 \approx 12\,000$.
			\item b) $43\,781 \approx 44\,000$.
			\item c) $28\,634 \approx 29\,000$.
			\item d) $21\,999 \approx 22\,000$.
			\item e) $22\,999 \approx 23\,000$.
			\item f) $9999 \approx 10\,000$.
			\item g) $12\,099 \approx 12\,000$.
			\item h) $454\,995 \approx 455\,000$.
			\item i) $14\,350 \approx 14\,000$.
			\item j) $99\,999 \approx 100\,000$.
			\item k) $987\,698 \approx 988\,000$.
			\item l) $3\,400\,065 \approx 3\,400\,000$.
			\item m) $1\,000\,587 \approx 1\,001\,000$.
			\item n) $987\,654 \approx 988\,000$.
			\item o) $260\,283 \approx 260\,000$.
			\item p) $23456{,}7 \approx 23\,000$.
			\item q) $1\,234\,567 \approx 1\,235\,000$.
			\item r) $12345{,}678 \approx 12\,000$.
			\item s) $8765{,}432 \approx 9000$.
			\item t) $9999{,}99 \approx 10\,000$.
		\end{itemize}
		\end{multicols}
	}
\end{bt}

% Bài 13
\begin{bt}
	Làm tròn các số sau đến hàng phần mười:
	\begin{multicols}{5}
		\begin{enumerate}[a)]
			\item $10{,}00905$
			\item $60{,}991$
			\item $999{,}994$
			\item $10{,}0456$
			\item $23{,}0009$
			\item $99{,}999$
			\item $90{,}0909$
			\item $9876{,}1$
			\item $1234{,}56$
			\item $98765{,}43$
		\end{enumerate}
	\end{multicols}
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng phần trăm:
		\begin{multicols}{2}
		\begin{itemize}
			\item a) $10{,}00905 \approx 10{,}0$.
			\item b) $60{,}991 \approx 61{,}0$.
			\item c) $999{,}994 \approx 1000{,}0$.
			\item d) $10{,}0456 \approx 10{,}0$.
			\item e) $23{,}0009 \approx 23{,}0$.
			\item f) $99{,}999 \approx 100{,}0$.
			\item g) $90{,}0909 \approx 90{,}1$.
			\item h) $9876{,}1 \approx 9876{,}1$.
			\item i) $1234{,}56 \approx 1234{,}6$.
			\item j) $98765{,}43 \approx 98765{,}4$.
		\end{itemize}
		\end{multicols}
	}
\end{bt}

% Bài 14
\begin{bt}
	Làm tròn các số sau đến hàng phần trăm:
	\begin{multicols}{5}
		\begin{enumerate}[a)]
			\item $3{,}0468$
			\item $12{,}3475$
			\item $0{,}31069$
			\item $12{,}516$
			\item $0{,}999$
			\item $7{,}923$
			\item $17{,}418$
			\item $79{,}1364$
			\item $50{,}401$
			\item $0{,}155$
			\item $60{,}996$
			\item $12{,}349$
			\item $2{,}9999$
			\item $123{,}456$
			\item $98{,}7654$
		\end{enumerate}
	\end{multicols}
	\loigiai{
		Quy tắc: Nhìn vào chữ số hàng phần nghìn:
		\begin{multicols}{2}
		\begin{itemize}
			\item a) $3{,}0468 \approx 3{,}05$.
			\item b) $12{,}3475 \approx 12{,}35$.
			\item c) $0{,}31069 \approx 0{,}31$.
			\item d) $12{,}516 \approx 12{,}52$.
			\item e) $0{,}999 \approx 1{,}00$.
			\item f) $7{,}923 \approx 7{,}92$.
			\item g) $17{,}418 \approx 17{,}42$.
			\item h) $79{,}1364 \approx 79{,}14$.
			\item i) $50{,}401 \approx 50{,}40$.
			\item j) $0{,}155 \approx 0{,}16$.
			\item k) $60{,}996 \approx 61{,}00$.
			\item l) $12{,}349 \approx 12{,}35$.
			\item m) $2{,}9999 \approx 3{,}00$.
			\item n) $123{,}456 \approx 123{,}46$.
			\item o) $98{,}7654 \approx 98{,}77$.
		\end{itemize}
		\end{multicols}
	}
\end{bt}

% Bài 15
\begin{bt}
	Viết số quy tròn của mỗi số sau với độ chính xác $d$:
	\begin{enumerate}[a)]
		\item $1\,234\,567$ với $d = 400$.
		\item $8{,}7654$ với $d = 0{,}01$.
		\item $28{,}4156$ với $d = 0{,}001$.
		\item $1{,}7320508...$ với $d = 0{,}0001$.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Vì $100 \le d = 400 < 1000$ (hàng trăm), ta làm tròn đến hàng nghìn:\\
			Chữ số hàng trăm là $5 \ge 5 \implies$ số quy tròn là $1\,235\,000$.
			\item Vì $d = 0{,}01$ (hàng phần trăm), ta làm tròn đến hàng phần mười:\\
			Chữ số hàng phần trăm là $6 \ge 5 \implies$ số quy tròn là $8{,}8$.
			\item Vì $d = 0{,}001$ (hàng phần nghìn), ta làm tròn đến hàng phần trăm:\\
			Chữ số hàng phần nghìn là $5 \ge 5 \implies$ số quy tròn là $28{,}42$.
			\item Vì $d = 0{,}0001$ (hàng phần chục nghìn), ta làm tròn đến hàng phần nghìn:\\
			Chữ số hàng phần chục nghìn là $0 < 5 \implies$ số quy tròn là $1{,}732$.
		\end{enumerate}
	}
\end{bt}

% Bài 16
\begin{bt}
	Hãy viết số quy tròn của:
	\begin{enumerate}[a)]
		\item $a$ biết $\overline{a} = 1\,951\,890 \pm 200$.
		\item $b$ biết $\overline{b} = 1{,}236 \pm 0{,}002$.
		\item $c$ biết $\overline{c} = 3{,}1463 \pm 0{,}002$.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Độ chính xác $d = 200$ (hàng trăm), ta quy tròn $a$ đến hàng nghìn:\\
			Chữ số hàng trăm là $8 \ge 5 \implies$ số quy tròn là $1\,952\,000$.
			\item Độ chính xác $d = 0{,}002$ (hàng phần nghìn), ta quy tròn $b$ đến hàng phần trăm:\\
			Chữ số hàng phần nghìn là $6 \ge 5 \implies$ số quy tròn là $1{,}24$.
			\item Độ chính xác $d = 0{,}002$ (hàng phần nghìn), ta quy tròn $c$ đến hàng phần trăm:\\
			Chữ số hàng phần nghìn là $6 \ge 5 \implies$ số quy tròn là $3{,}15$.
		\end{enumerate}
	}
\end{bt}

% Bài 17
\begin{bt}
	Chiều dài một cái cầu là $\ell = 1745{,}25\text{ m} \pm 0{,}01\text{ m}$. Hãy viết số quy tròn của số gần đúng $1745{,}25$.
	\loigiai{
		Độ chính xác $d = 0{,}01\text{ m}$ ở hàng phần trăm, do đó ta quy tròn số gần đúng $\ell = 1745{,}25$ đến \textbf{hàng phần mười}.\\
		Chữ số hàng phần mười là $2$, chữ số ngay sau nó là $5 \ge 5$ nên cộng thêm 1 đơn vị vào hàng phần mười:\\
		Số quy tròn là \textbf{$1745{,}3\text{ m}$}.
	}
\end{bt}

% Bài 18
\begin{bt}
	Sử dụng máy tính bỏ túi tính gần đúng các số sau (kết quả lấy 4 chữ số thập phân):
	\begin{multicols}{3}
		\begin{enumerate}[a)]
			\item $3^7 \cdot \sqrt{14}$
			\item $\sqrt[3]{15 \cdot 12^4}$
			\item $\sqrt[3]{15 \cdot 14^4}$
		\end{enumerate}
	\end{multicols}
	\loigiai{
		\begin{enumerate}[a)]
			\item $3^7 \cdot \sqrt{14} = 2187 \cdot \sqrt{14} \approx 8182{,}806847... \implies \mathbf{8182{,}8068}$.
			\item $\sqrt[3]{15 \cdot 12^4} = \sqrt[3]{15 \cdot 20736} = \sqrt[3]{311040} \approx 67{,}754877... \implies \mathbf{67{,}7549}$.
			\item $\sqrt[3]{15 \cdot 14^4} = \sqrt[3]{15 \cdot 38416} = \sqrt[3]{576240} \approx 83{,}214777... \implies \mathbf{83{,}2148}$.
		\end{enumerate}
	}
\end{bt}

% Bài 19
\begin{bt}
	Thực hiện các phép tính sau trên máy tính cầm tay (trong kết quả lấy 4 chữ số ở phần thập phân):
	\begin{multicols}{3}
		\begin{enumerate}[a)]
			\item $4^6 \cdot \sqrt{0{,}1}$
			\item $\sqrt[8]{2{,}1^{18} + 1} - \sqrt{2{,}1^{12} + 1}$
			\item $\dfrac{1{,}5^3}{\sqrt[3]{6{,}8}}$
		\end{enumerate}
	\end{multicols}
	\loigiai{
		\begin{enumerate}[a)]
			\item $4^6 \cdot \sqrt{0{,}1} = 4096 \cdot \sqrt{0{,}1} \approx 1295{,}27140... \implies \mathbf{1295{,}2714}$.
			\item Ta có $2{,}1^{18} + 1 \approx 63261{,}744 \implies \sqrt[8]{2{,}1^{18} + 1} \approx 3{,}998939$.\\
			Và $2{,}1^{12} + 1 \approx 7355{,}8275 \implies \sqrt{2{,}1^{12} + 1} \approx 85{,}766121$.\\
			Do đó: $\sqrt[8]{2{,}1^{18} + 1} - \sqrt{2{,}1^{12} + 1} \approx 3{,}998939 - 85{,}766121 = -81{,}76718... \implies \mathbf{-81{,}7672}$.
			\item $\dfrac{1{,}5^3}{\sqrt[3]{6{,}8}} = \dfrac{3{,}375}{\sqrt[3]{6{,}8}} \approx \dfrac{3{,}375}{1{,}894536} \approx 1{,}781439... \implies \mathbf{1{,}7814}$.
		\end{enumerate}
	}
\end{bt}
"""

def get_answer_key_tex():
    # Bảng đáp án trắc nghiệm 21 câu
    ans_p1 = [
        "C", "C", "D", "B", "B", "D", "C", "A", "A", "D",
        "C", "B", "A", "C", "A", "B", "A", "A", "A", "B", "A"
    ]
    s = "\n\\vspace{0.3cm}\n\\noindent\\begin{minipage}{\\linewidth}\n"
    s += "\\begin{center}{\\large\\bfseries\\color{red!80!black} BẢNG ĐÁP ÁN TRẮC NGHIỆM}\\end{center}\\smallskip\n"
    s += "\\begin{center}\\begin{tabular}{|c|" + "c|" * 11 + "}\\hline\n"
    s += "\\textbf{Câu} & " + " & ".join(str(i) for i in range(1, 12)) + " \\\\ \\hline\n"
    s += "\\textbf{Đ/A} & " + " & ".join(f"\\textbf{{{ans_p1[i-1]}}}" for i in range(1, 12)) + " \\\\ \\hline\n"
    s += "\\end{tabular}\\end{center}\\smallskip\n"
    s += "\\begin{center}\\begin{tabular}{|c|" + "c|" * 10 + "}\\hline\n"
    s += "\\textbf{Câu} & " + " & ".join(str(i) for i in range(12, 22)) + " \\\\ \\hline\n"
    s += "\\textbf{Đ/A} & " + " & ".join(f"\\textbf{{{ans_p1[i-1]}}}" for i in range(12, 22)) + " \\\\ \\hline\n"
    s += "\\end{tabular}\\end{center}\n\\end{minipage}\n"
    return s

def build_latex_wrapper(is_sol):
    master_name = "Master_HDG.tex" if is_sol else "Master_De.tex"
    kythi = "HƯỚNG DẪN GIẢI CHI TIẾT" if is_sol else "PHIẾU BÀI TẬP VÀ LÝ THUYẾT"
    ans_line = "\\def\\inbangdapan{\\input{bang_dap_an.tex}}" if is_sol else ""
    return f"""\\def\\tentruong{{}}
\\def\\tenkythi{{{kythi}}}
\\def\\monhoc{{TOÁN 10 (Bộ sách Kết nối tri thức \\& Cánh Diều)}}
\\def\\tieudetrai{{BÀI 1: SỐ GẦN ĐÚNG VÀ SAI SỐ}}
\\def\\tieudephai{{CHƯƠNG V: SỐ LIỆU THỐNG KÊ}}
\\def\\namhoc{{2025 -- 2026}}
\\def\\made{{101}}
\\def\\headertype{{phieubaitap}}
\\def\\brand{{{BRAND}}}
\\def\\giaovien{{HỒ THỊ THÚY}}
\\def\\noidungfile{{noi_dung.tex}}
{ans_line}

\\input{{../Master/{master_name}}}
"""

def compile_latex(name, content):
    target_pdf = os.path.join(LATEX_DIR, name + ".pdf")
    is_locked = False
    if os.path.exists(target_pdf):
        try:
            with open(target_pdf, "r+b"):
                pass
        except PermissionError:
            is_locked = True

    job_name = name if not is_locked else name + "_moi"
    tex_path = os.path.join(LATEX_DIR, job_name + ".tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(content)
    for run in range(2):
        res = subprocess.run(["pdflatex", "-interaction=nonstopmode", job_name + ".tex"], cwd=LATEX_DIR,
                             capture_output=True, text=True, encoding="utf-8", errors="ignore")
    log = open(os.path.join(LATEX_DIR, job_name + ".log"), encoding="utf-8", errors="ignore").read()
    errors = [l for l in log.splitlines() if l.startswith("!")]
    pages = re.search(r"Output written on .*?\((\d+) pages?", log)
    print(f"[LaTeX] {job_name}: {len(errors)} lỗi, {pages.group(1) if pages else '?'} trang")
    for e in errors[:10]:
        print("   ", e)
    if is_locked and len(errors) == 0:
        print(f"[CẢNH BÁO] {name}.pdf đang mở -> đã biên dịch thành công ra {job_name}.pdf")
        safe_copy(os.path.join(LATEX_DIR, job_name + ".pdf"), os.path.join(SAN_PHAM_DIR, job_name + ".pdf"))
    return len(errors) == 0

def safe_copy(src, dst):
    try:
        shutil.copy2(src, dst)
        print(f"[COPY] {os.path.basename(dst)}")
    except PermissionError:
        print(f"[CẢNH BÁO] {os.path.basename(dst)} đang được mở, bỏ qua sao chép.")

# ============================================================================
# XUẤT BẢN WORD (.DOCX) CHUẨN BTPRO
# ============================================================================
def set_spacing(p, before_pt10=0, after_pt10=0, align="left", line_rule="auto"):
    pPr = p._p.get_or_add_pPr()
    sp = parse_xml(r'<w:spacing %s w:before="%d" w:after="%d" w:line="240" w:lineRule="%s"/>'
                   % (nsdecls('w'), before_pt10, after_pt10, line_rule))
    pPr.append(sp)
    if align == "center":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "right":
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    elif align == "both":
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    else:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT

def add_run(p, text, bold=False, italic=False, size=11, color=None):
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    r.font.name = "Times New Roman"
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor(*color)
    return r

def create_header_table(doc, is_sol):
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for row in tbl.rows:
        for cell in row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = parse_xml(r'<w:tcBorders %s><w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/><w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/><w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/><w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/></w:tcBorders>' % nsdecls('w'))
            tcPr.append(tcBorders)

    c00 = tbl.cell(0, 0)
    c00.width = Cm(8.0)
    p = c00.paragraphs[0]
    add_run(p, "LỚP TOÁN CÔ THÚY", True, False, 11.5, (0, 32, 96))
    set_spacing(p, 40, 20, "center")
    p2 = c00.add_paragraph()
    add_run(p2, "SĐT: 0935.322.328\nĐịa chỉ: 50/2C Phạm Thị Liên", False, False, 10.5)
    set_spacing(p2, 0, 40, "center")

    c01 = tbl.cell(0, 1)
    c01.width = Cm(10.0)
    p = c01.paragraphs[0]
    title_text = "HƯỚNG DẪN GIẢI CHI TIẾT" if is_sol else "PHIẾU BÀI TẬP VÀ LÝ THUYẾT"
    add_run(p, title_text, True, False, 12, (192, 0, 0))
    set_spacing(p, 40, 20, "center")
    p2 = c01.add_paragraph()
    add_run(p2, "Môn: TOÁN 10 – BÀI 1: SỐ GẦN ĐÚNG VÀ SAI SỐ\nChương V: Mẫu số liệu không ghép nhóm", False, True, 10.5)
    set_spacing(p2, 0, 40, "center")

    c10 = tbl.cell(1, 0)
    c10.width = Cm(8.0)
    p = c10.paragraphs[0]
    add_run(p, "BÀI 1: SỐ GẦN ĐÚNG VÀ SAI SỐ", True, False, 10.5)
    set_spacing(p, 30, 30, "center")

    c11 = tbl.cell(1, 1)
    c11.width = Cm(10.0)
    p = c11.paragraphs[0]
    if is_sol:
        add_run(p, "Giáo viên: HỒ THỊ THÚY", True, False, 10.5)
    else:
        add_run(p, "Họ và tên: .............................................................", False, False, 10)
    set_spacing(p, 30, 30, "center")

def convert_latex_to_word_md(is_sol):
    # Lấy nội dung LaTeX đã có, chuyển đổi sang Markdown thân thiện với Pandoc
    raw = get_latex_content()
    
    # Xử lý các khối
    # Tiêu đề
    raw = re.sub(r"\\section\*\{(.*?)\}", r"\n\n# \1\n\n", raw)
    raw = re.sub(r"\\subsection\*\{(.*?)\}", r"\n\n## \1\n\n", raw)
    
    # Ẩn hoặc hiện lời giải
    if not is_sol:
        raw = re.sub(r"\\loigiai\{.*?\}(?=\s*\\end\{ex\})", "", raw, flags=re.DOTALL)
    else:
        raw = re.sub(r"\\loigiai\{([\s\S]*?)\}(?=\s*\\end\{ex\})", r"\n\n**Lời giải.**\n\n\1\n\n", raw)

    # Chuyển choice của ex_test
    def choice_repl(m):
        choices = re.findall(r"\{([\s\S]*?)\}", m.group(1))
        letters = "ABCD"
        out = ["\n"]
        for i, c in enumerate(choices[:4]):
            c_clean = c.replace(r"\True", "").strip()
            is_true = r"\True" in c and is_sol
            mark = "@@CHON@@" if is_true else ""
            out.append(f"{mark}**{letters[i]}.** {c_clean}{mark}")
        return "\n\n@@TAB@@" + "@@TAB@@".join(out[1:]) + "\n\n"

    raw = re.sub(r"\\choice([\s\S]*?)(?=\\loigiai|\\end\{ex\})", choice_repl, raw)
    raw = re.sub(r"(?m)^\s*%.*$\n?", "", raw)

    vd_c = [0]
    def vd_fn(m):
        vd_c[0] += 1
        return f"\n\n**Ví dụ {vd_c[0]}.** "
    raw = re.sub(r"\\begin\{vd\}", vd_fn, raw)
    raw = re.sub(r"\\end\{vd\}", "\n\n", raw)

    ex_c = [0]
    def ex_fn(m):
        ex_c[0] += 1
        return f"\n\n**Câu {ex_c[0]}.** "
    raw = re.sub(r"\\begin\{ex\}", ex_fn, raw)
    raw = re.sub(r"\\end\{ex\}", "\n\n", raw)

    bt_c = [0]
    def bt_fn(m):
        bt_c[0] += 1
        return f"\n\n**Bài {bt_c[0]}.** "
    raw = re.sub(r"\\begin\{bt\}", bt_fn, raw)
    raw = re.sub(r"\\end\{bt\}", "\n\n", raw)
    raw = re.sub(r"\\begin\{enumerate\}\[[^\]]*\]", "", raw)
    raw = re.sub(r"\\end\{enumerate\}", "", raw)
    raw = re.sub(r"\\begin\{itemize\}", "", raw)
    raw = re.sub(r"\\end\{itemize\}", "", raw)
    raw = re.sub(r"\\item", "\n- ", raw)
    raw = re.sub(r"\\begin\{multicols\}\{\d+\}", "", raw)
    raw = re.sub(r"\\end\{multicols\}", "", raw)
    raw = re.sub(r"\\vspace\{[^}]*\}", "", raw)
    raw = re.sub(r"\\textbf\{(.*?)\}", r"**\1**", raw)
    raw = re.sub(r"\\textit\{(.*?)\}", r"*\1*", raw)

    # Thêm bảng đáp án vào bản HDG
    if is_sol:
        ans_md = "\n\n# BẢNG ĐÁP ÁN TRẮC NGHIỆM\n\n"
        ans_p1 = [
            "C", "C", "D", "B", "B", "D", "C", "A", "A", "D",
            "C", "B", "A", "C", "A", "B", "A", "A", "A", "B", "A"
        ]
        ans_md += "| Câu | " + " | ".join(str(i) for i in range(1, 12)) + " |\n"
        ans_md += "| :---: | " + " | ".join(":---:" for _ in range(1, 12)) + " |\n"
        ans_md += "| **Đ/A** | " + " | ".join(f"**{ans_p1[i-1]}**" for i in range(1, 12)) + " |\n\n"
        ans_md += "| Câu | " + " | ".join(str(i) for i in range(12, 22)) + " |\n"
        ans_md += "| :---: | " + " | ".join(":---:" for _ in range(12, 22)) + " |\n"
        ans_md += "| **Đ/A** | " + " | ".join(f"**{ans_p1[i-1]}**" for i in range(12, 22)) + " |\n\n"
        raw += ans_md

    raw += "\n\n---\n\n<p align='center'>**--------- HẾT ---------**</p>\n"
    return raw

def apply_tabs(p):
    text = p.text
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    parts = text.split("@@TAB@@")
    parts = [pt for pt in parts if pt != ""]
    pPr = p._p.get_or_add_pPr()
    tabs = OxmlElement('w:tabs')
    if len(parts) == 4:
        pos_list = [0, 4800, 9600, 14400]
    elif len(parts) == 2:
        pos_list = [0, 9600]
    else:
        pos_list = [0]
    for pos in pos_list[1:]:
        tab = parse_xml(r'<w:tab %s w:val="left" w:pos="%d"/>' % (nsdecls('w'), pos))
        tabs.append(tab)
    pPr.append(tabs)
    set_spacing(p, 40, 40, "left")
    for i, pt in enumerate(parts):
        if i > 0:
            p.add_run().add_tab()
        pt_clean = pt.strip()
        m = re.match(r"(\([A-D]\)|[A-D]\.)\s*(.*)", pt_clean)
        if m:
            add_run(p, m.group(1) + " ", True, False, 11)
            add_run(p, m.group(2), False, False, 11)
        else:
            add_run(p, pt_clean, False, False, 11)

def build_word_doc(is_sol, out_path):
    md = convert_latex_to_word_md(is_sol)
    tag = "hdg" if is_sol else "de"
    md_file = os.path.join(SCRATCH_DIR, f"temp_{tag}.md")
    tmp_docx = os.path.join(SCRATCH_DIR, f"temp_{tag}.docx")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md)

    cmd = [PANDOC, md_file, "-o", tmp_docx, "--from=markdown", "--to=docx"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"[LỖI PANDOC] {res.stderr}")
        return False

    doc = docx.Document(tmp_docx)

    # Cài đặt trang A4, lề chuẩn
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(1.2)
    sec.bottom_margin = Cm(1.5)
    sec.left_margin = Cm(1.5)
    sec.right_margin = Cm(1.5)

    # Cài đặt Footer bản quyền Cô Thúy
    sec.different_first_page_header_footer = False
    hf = sec.footer
    hp = hf.paragraphs[0]
    hp.text = ""
    add_run(hp, BRAND_W, False, True, 9.5, (100, 100, 100))
    set_spacing(hp, 0, 0, "left")

    # Bảng tiêu đề ở đầu tài liệu
    first_p = doc.paragraphs[0]
    tbl_p = first_p.insert_paragraph_before()
    create_header_table(doc, is_sol)
    first_tbl = doc.tables[-1]
    tbl_p._p.addprevious(first_tbl._tbl)
    p_to_del = tbl_p._p
    p_to_del.getparent().remove(p_to_del)
    sp_p = first_p.insert_paragraph_before()
    set_spacing(sp_p, 40, 40, "left")

    # Xử lý các đoạn văn và marker
    for p in list(doc.paragraphs):
        t = p.text
        if "@@TAB" in p._p.xml or "@@TAB" in t:
            apply_tabs(p)
            continue
        if "@@CHON@@" in t:
            p.text = t.replace("@@CHON@@", "")
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(192, 0, 0)
        if t.startswith("Lời giải.") or "**Lời giải.**" in t:
            for r in p.runs:
                if "Lời giải." in r.text:
                    r.bold = True
                    r.font.color.rgb = RGBColor(31, 73, 125)
        for r in p.runs:
            r.font.name = "Times New Roman"
            if r.font.size is None:
                r.font.size = Pt(11)

    # Đếm công thức OMML
    body_xml = doc.element.body.xml
    omml = body_xml.count("<m:oMath>") + body_xml.count("<m:oMath ")
    try:
        doc.save(out_path)
    except PermissionError:
        alt = out_path.replace(".docx", "_moi.docx")
        doc.save(alt)
        print(f"[CẢNH BÁO] {os.path.basename(out_path)} đang mở -> lưu {os.path.basename(alt)}")
        out_path = alt
    print(f"[Word] {os.path.basename(out_path)}: {omml} công thức OMML")
    return True

# ============================================================================
# HÀM CHÍNH THỰC THI
# ============================================================================
def main():
    print("=" * 70)
    print(" XUẤT BẢN TOÁN 10 - CHƯƠNG 5 - BÀI 1: SỐ GẦN ĐÚNG VÀ SAI SỐ")
    print("=" * 70)
    
    # 1. Ghi file nội dung TeX con và bảng đáp án
    with open(os.path.join(LATEX_DIR, "noi_dung.tex"), "w", encoding="utf-8") as f:
        f.write(get_latex_content())
    with open(os.path.join(LATEX_DIR, "bang_dap_an.tex"), "w", encoding="utf-8") as f:
        f.write(get_answer_key_tex())
    print("[TeX] Đã tạo noi_dung.tex và bang_dap_an.tex")

    # 2. Biên dịch LaTeX qua Master Main
    ok_de = compile_latex(NAME_DE, build_latex_wrapper(False))
    ok_hdg = compile_latex(NAME_HDG, build_latex_wrapper(True))

    # 3. Tạo file Word (.docx)
    build_word_doc(False, os.path.join(SAN_PHAM_DIR, NAME_DE + ".docx"))
    build_word_doc(True, os.path.join(SAN_PHAM_DIR, NAME_HDG + ".docx"))

    # 4. Sao chép PDF sang San_Pham
    for n in (NAME_DE, NAME_HDG):
        src = os.path.join(LATEX_DIR, n + ".pdf")
        if os.path.exists(src):
            safe_copy(src, os.path.join(SAN_PHAM_DIR, n + ".pdf"))

    print("=" * 70)
    print("HOÀN TẤT BÀI 1!" if ok_de and ok_hdg else "CÓ LỖI LATEX – kiểm tra log.")
    print("=" * 70)

if __name__ == "__main__":
    main()
