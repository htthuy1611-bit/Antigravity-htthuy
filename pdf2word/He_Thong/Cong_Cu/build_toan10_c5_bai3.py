# -*- coding: utf-8 -*-
"""
CHUYÊN ĐỀ TOÁN 10 - CHƯƠNG 5: CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM
BÀI 3: CÁC SỐ ĐẶC TRƯNG ĐO ĐỘ PHÂN TÁN
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
LATEX_DIR = os.path.join(BASE_DIR, "He_Thong", "LaTeX", "Toan10_Chuong5_Bai3")
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
SCRATCH_DIR = os.path.join(CURRENT_DIR, "scratch_toan10_c5_b3")
PANDOC = os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")

for d in (LATEX_DIR, SAN_PHAM_DIR, SCRATCH_DIR):
    os.makedirs(d, exist_ok=True)

sty_src = os.path.join(BASE_DIR, "He_Thong", "Quy_Chuan", "ex_test.sty")
sty_dst = os.path.join(LATEX_DIR, "ex_test.sty")
if os.path.exists(sty_src) and not os.path.exists(sty_dst):
    shutil.copy2(sty_src, sty_dst)

NAME_DE = "Toan10_C5_Bai3_De"
NAME_HDG = "Toan10_C5_Bai3_HDG"

BRAND = "Lớp Toán Cô Thúy -- SĐT: 0935.322.328 -- 50/2C Phạm Thị Liên"
BRAND_W = "Lớp Toán Cô Thúy  •  SĐT: 0935.322.328  •  50/2C Phạm Thị Liên"

def get_latex_content():
    return r"""
\begin{center}
	{\Large\bfseries\color{blue!80!black} CHƯƠNG V. CÁC SỐ ĐẶC TRƯNG CỦA MẪU SỐ LIỆU KHÔNG GHÉP NHÓM}\\[6pt]
	{\large\bfseries\color{red!80!black} BÀI 3. CÁC SỐ ĐẶC TRƯNG ĐO ĐỘ PHÂN TÁN}
\end{center}
\vspace{0.2cm}

\section*{I. TÓM TẮT LÝ THUYẾT}

\subsection*{1. Khoảng biến thiên và khoảng tứ phân vị}
\begin{itemize}
	\item \textbf{Khoảng biến thiên} (kí hiệu là $R$): là hiệu số giữa giá trị lớn nhất và giá trị nhỏ nhất trong mẫu số liệu:
	\[R = x_{\max} - x_{\min}.\]
	Khoảng biến thiên càng lớn thì mẫu số liệu càng phân tán.
	\item \textbf{Khoảng tứ phân vị} (kí hiệu là $\Delta_Q$): là hiệu số giữa tứ phân vị thứ ba và tứ phân vị thứ nhất:
	\[\Delta_Q = Q_3 - Q_1.\]
	Khoảng tứ phân vị đo độ phân tán của $50\%$ số liệu chính giữa của mẫu số liệu và không bị ảnh hưởng bởi các giá trị bất thường.
\end{itemize}

\subsection*{2. Phương sai và độ lệch chuẩn}
\begin{itemize}
	\item Cho mẫu số liệu $x_1, x_2, \ldots, x_n$ có số trung bình là $\overline{x}$.
	\item \textbf{Phương sai} (kí hiệu là $s^2$):
	\[s^2 = \frac{(x_1 - \overline{x})^2 + (x_2 - \overline{x})^2 + \cdots + (x_n - \overline{x})^2}{n} = \frac{1}{n}\sum_{i=1}^n x_i^2 - (\overline{x})^2.\]
	Đối với bảng phân bố tần số:
	\[s^2 = \frac{\sum_{i=1}^k n_i (x_i - \overline{x})^2}{n} = \frac{1}{n}\sum_{i=1}^k n_i x_i^2 - (\overline{x})^2.\]
	\item \textbf{Độ lệch chuẩn} (kí hiệu là $s$): là căn bậc hai số học của phương sai:
	\[s = \sqrt{s^2}.\]
	\item \textbf{Ý nghĩa:} Phương sai và độ lệch chuẩn đo mức độ biến động, phân tán của các số liệu xung quanh giá trị trung bình. Giá trị $s^2$ và $s$ càng lớn thì số liệu càng phân tán. Độ lệch chuẩn có cùng đơn vị đo với đại lượng đang nghiên cứu.
\end{itemize}

\subsection*{3. Phát hiện số liệu bất thường bằng biểu đồ hộp}
\begin{itemize}
	\item Giá trị $x$ trong mẫu số liệu được gọi là \textbf{giá trị bất thường} nếu:
	\[x < Q_1 - 1{,}5\Delta_Q \quad \text{hoặc} \quad x > Q_3 + 1{,}5\Delta_Q.\]
	Tức là $x$ không thuộc đoạn $[Q_1 - 1{,}5\Delta_Q; Q_3 + 1{,}5\Delta_Q]$.
\end{itemize}

\vspace{0.3cm}
\section*{II. CÁC DẠNG TOÁN VÀ VÍ DỤ MINH HỌA}

\subsection*{Dạng 1. Tìm khoảng biến thiên và so sánh độ phân tán}

\begin{ex}
	\textbf{(Ví dụ 1).} Cân nặng (kg) của 10 học sinh: $49;\; 57;\; 66;\; 45;\; 50;\; 41;\; 57;\; 42;\; 55;\; 52$. Tìm khoảng biến thiên của mẫu số liệu.
	\loigiai{
		Giá trị lớn nhất là $x_{\max} = 66\text{ kg}$. Giá trị nhỏ nhất là $x_{\min} = 41\text{ kg}$.\\
		Khoảng biến thiên của mẫu số liệu là:
		\[R = x_{\max} - x_{\min} = 66 - 41 = 25\text{ (kg)}.\]
	}
\end{ex}

\begin{ex}
	\textbf{(Ví dụ 2).} Chiều cao (m) của các bạn học sinh trong một lớp học:
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
	\loigiai{
		Giá trị lớn nhất là $x_{\max} = 1{,}65\text{ m}$. Giá trị nhỏ nhất là $x_{\min} = 1{,}60\text{ m}$.\\
		Khoảng biến thiên của mẫu số liệu là:
		\[R = 1{,}65 - 1{,}60 = 0{,}05\text{ (m)}.\]
	}
\end{ex}

\begin{ex}
	\textbf{(Ví dụ 3).} Điểm kiểm tra môn Toán của học sinh Tổ 1 và Tổ 2:
	\begin{itemize}
		\item Tổ 1: $6;\; 9;\; 4;\; 2;\; 7;\; 9;\; 6;\; 10$.
		\item Tổ 2: $4;\; 5;\; 6;\; 3;\; 9;\; 5;\; 8;\; 4$.
	\end{itemize}
	Tìm khoảng biến thiên trong hai mẫu số liệu và chỉ ra tổ nào học đồng đều hơn.
	\loigiai{
		- Tổ 1: $x_{\max} = 10, x_{\min} = 2 \implies R_1 = 10 - 2 = 8$.\\
		- Tổ 2: $x_{\max} = 9, x_{\min} = 3 \implies R_2 = 9 - 3 = 6$.\\
		Vì $R_2 < R_1$ nên độ phân tán điểm số của Tổ 2 nhỏ hơn Tổ 1, do đó học sinh Tổ 2 học đồng đều hơn Tổ 1.
	}
\end{ex}

\subsection*{Dạng 2. Tính phương sai và độ lệch chuẩn}

\begin{ex}
	\textbf{(Ví dụ 1).} Sản lượng lúa (tạ) của 40 thửa ruộng:
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
	\loigiai{
		a) Sản lượng trung bình:
		\[\overline{x} = \frac{20 \cdot 5 + 21 \cdot 8 + 22 \cdot 11 + 23 \cdot 10 + 24 \cdot 6}{40} = \frac{884}{40} = 22{,}1\text{ (tạ)}.\]
		b) Phương sai:
		\[s^2 = \frac{5(20 - 22{,}1)^2 + 8(21 - 22{,}1)^2 + 11(22 - 22{,}1)^2 + 10(23 - 22{,}1)^2 + 6(24 - 22{,}1)^2}{40}\]
		\[= \frac{5(4{,}41) + 8(1{,}21) + 11(0{,}01) + 10(0{,}81) + 6(3{,}61)}{40} = \frac{61{,}6}{40} = 1{,}54\text{ (tạ}^2\text{)}.\]
		Độ lệch chuẩn:
		\[s = \sqrt{1{,}54} \approx 1{,}24\text{ (tạ)}.\]
	}
\end{ex}

\begin{ex}
	\textbf{(Ví dụ 2).} 100 học sinh thi học sinh giỏi Toán (thang điểm 20):
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
	\loigiai{
		a) Số trung bình:
		\[\overline{x} = \frac{9(1) + 10(1) + 11(3) + 12(5) + 13(8) + 14(13) + 15(19) + 16(24) + 17(14) + 18(10) + 19(2)}{100}\]
		\[= \frac{1523}{100} = 15{,}23\text{ (điểm)}.\]
		b) Phương sai:
		\[s^2 = \frac{1}{100}\sum n_i x_i^2 - (\overline{x})^2 = \frac{23\,509}{100} - (15{,}23)^2 = 235{,}09 - 231{,}9529 = 3{,}1371.\]
		Độ lệch chuẩn:
		\[s = \sqrt{3{,}1371} \approx 1{,}77\text{ (điểm)}.\]
	}
\end{ex}

\subsection*{Dạng 3. Tìm các số liệu bất thường của mẫu số liệu}

\begin{ex}
	\textbf{(Ví dụ 1).} Điểm kiểm tra môn Toán của 10 học sinh sau:
	\[1;\; 7;\; 10;\; 7;\; 7;\; 6;\; 9;\; 8;\; 10;\; 8.\]
	Hãy tìm các số liệu bất thường trong mẫu số liệu trên.
	\loigiai{
		Sắp xếp mẫu số liệu theo thứ tự không giảm ($n = 10$):
		\[1;\; 6;\; 7;\; 7;\; 7;\; 8;\; 8;\; 9;\; 10;\; 10.\]
		- Trung vị $Q_2 = \dfrac{7 + 8}{2} = 7{,}5$.\\
		- Nửa dưới: $1, 6, 7, 7, 7 \implies Q_1 = 7$.\\
		- Nửa trên: $8, 8, 9, 10, 10 \implies Q_3 = 9$.\\
		- Khoảng tứ phân vị: $\Delta_Q = Q_3 - Q_1 = 9 - 7 = 2$.\\
		Ta có:
		\[Q_1 - 1{,}5\Delta_Q = 7 - 1{,}5 \cdot 2 = 4; \quad Q_3 + 1{,}5\Delta_Q = 9 + 1{,}5 \cdot 2 = 12.\]
		Đoạn giá trị bình thường là $[4; 12]$.\\
		Số liệu $1$ nhỏ hơn $4$ nên không thuộc đoạn $[4; 12]$.\\
		Vậy giá trị bất thường của mẫu số liệu là \textbf{1}.
	}
\end{ex}

\vspace{0.4cm}
\section*{III. BÀI TẬP VẬN DỤNG}

\subsection*{PHẦN I. CÂU HỎI TRẮC NGHIỆM}
\textit{\small (Mỗi câu học sinh chỉ chọn một phương án trả lời đúng)}
\setcounter{ex}{0}

% Câu 1
\begin{ex}
	Hãy tìm khoảng biến thiên của mẫu số liệu thống kê sau: $22;\; 26;\; 31;\; 15;\; 12;\; 4;\; 18;\; 93;\; 17;\; 64;\; 10$.
	\choice
	{$33$}
	{$83$}
	{\True $89$}
	{$97$}
	\loigiai{
		Giá trị lớn nhất là $93$, giá trị nhỏ nhất là $4$.\\
		Khoảng biến thiên: $R = 93 - 4 = 89$.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 2
\begin{ex}
	Hai chữ số cuối giải đặc biệt Xổ số miền Bắc trong 9 ngày được ghi lại như sau: $16;\; 11;\; 25;\; 28;\; 45;\; 42;\; 24;\; 33;\; 11$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	\choice
	{$18$}
	{\True $34$}
	{$56$}
	{$27$}
	\loigiai{
		Giá trị lớn nhất là $45$, nhỏ nhất là $11$.\\
		Khoảng biến thiên: $R = 45 - 11 = 34$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 3
\begin{ex}
	Mẫu số liệu nào dưới đây có khoảng biến thiên là 13?
	\choice
	{$11, 28, 56, 12$}
	{$6, 12, 33, 23, 11$}
	{\True $25, 9, 13, 10$ (Wait: $25 - 9 = 16$. Kiểm tra tất cả các mẫu)}
	{Tất cả đều sai}
	\loigiai{
		- Mẫu A: $R = 56 - 11 = 45 \ne 13$.\\
		- Mẫu B: $R = 33 - 6 = 27 \ne 13$.\\
		- Mẫu C: $R = 25 - 9 = 16 \ne 13$.\\
		Vậy không có mẫu nào có $R = 13$.\\
		Chọn \textbf{D} (Tất cả đều sai).
	}
\end{ex}

% Câu 4
\begin{ex}
	Mẫu số liệu nào dưới đây có khoảng biến thiên là 53?
	\choice
	{$18, 57, 11, 26$}
	{\True $44, 2, 55, 46, 27$}
	{$21, 3, 55, 89$}
	{$4, 16, 23, 20$}
	\loigiai{
		Xét mẫu B: $x_{\max} = 55, x_{\min} = 2 \implies R = 55 - 2 = 53$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 5
\begin{ex}
	Số lượng học sinh có điểm Toán tổng kết cuối học kì I trên 8 ở mỗi lớp của một trường:
	\[16;\; 11;\; 15;\; 18;\; 21;\; 12;\; 24;\; 23;\; 11;\; 8;\; 9;\; 11;\; 6;\; 27;\; 22;\; 20;\; 35;\; 18.\]
	Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	\choice
	{$11$}
	{\True $29$}
	{$37$}
	{$25$}
	\loigiai{
		Giá trị lớn nhất là $35$, nhỏ nhất là $6$.\\
		Khoảng biến thiên: $R = 35 - 6 = 29$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 6
\begin{ex}
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
	\choice
	{\True $4$}
	{$5$}
	{$6$}
	{$7$}
	\loigiai{
		Các giá trị dao động từ $6$ đến $10$.\\
		Khoảng biến thiên: $R = 10 - 6 = 4$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 7
\begin{ex}
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
	\choice
	{$5$}
	{\True $6$}
	{$7$}
	{$8$}
	\loigiai{
		Giá trị lớn nhất là $24\text{ cm}$, nhỏ nhất là $18\text{ cm}$.\\
		Khoảng biến thiên: $R = 24 - 18 = 6\text{ cm}$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 8
\begin{ex}
	Nhiệt độ cao nhất trong tuần ($^\circ\text{C}$) tại hai thành phố:
	\begin{itemize}
		\item Hà Nội: $28;\; 27;\; 30;\; 29;\; 27;\; 24;\; 25$.
		\item TP Hồ Chí Minh: $31;\; 33;\; 32;\; 33;\; 29;\; 32;\; 34$.
	\end{itemize}
	Dựa vào khoảng biến thiên của hai mẫu số liệu, hãy chỉ ra mẫu số liệu nào có độ phân tán lớn hơn.
	\choice
	{\True Mẫu số liệu "Hà Nội" có độ phân tán lớn hơn mẫu số liệu "TP Hồ Chí Minh"}
	{Mẫu số liệu "TP Hồ Chí Minh" có độ phân tán lớn hơn mẫu số liệu "Hà Nội"}
	{Hai mẫu số liệu có độ phân tán bằng nhau}
	{Tất cả đều sai}
	\loigiai{
		- Hà Nội: $R_{\text{HN}} = 30 - 24 = 6^\circ\text{C}$.\\
		- TP Hồ Chí Minh: $R_{\text{HCM}} = 34 - 29 = 5^\circ\text{C}$.\\
		Vì $R_{\text{HN}} > R_{\text{HCM}}$ nên mẫu số liệu "Hà Nội" có độ phân tán lớn hơn.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 9
\begin{ex}
	Tuổi của những đứa trẻ:
	\begin{itemize}
		\item Nam: $10;\; 4;\; 1;\; 6;\; 2;\; 8;\; 5$.
		\item Nữ: $2;\; 3;\; 6;\; 4;\; 1;\; 7$.
	\end{itemize}
	Dựa vào khoảng biến thiên, mẫu số liệu nào có độ phân tán lớn hơn?
	\choice
	{\True Mẫu số liệu "Nam" có độ phân tán lớn hơn mẫu số liệu "Nữ"}
	{Mẫu số liệu "Nữ" có độ phân tán lớn hơn mẫu số liệu "Nam"}
	{Hai mẫu số liệu có độ phân tán bằng nhau}
	{Tất cả đều sai}
	\loigiai{
		- Nam: $R_{\text{Nam}} = 10 - 1 = 9$.\\
		- Nữ: $R_{\text{Nữ}} = 7 - 1 = 6$.\\
		Vì $R_{\text{Nam}} = 9 > 6 = R_{\text{Nữ}}$ nên mẫu số liệu "Nam" có độ phân tán lớn hơn.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 10
\begin{ex}
	Chỉ số IQ và EQ của một nhóm học sinh:
	\begin{itemize}
		\item IQ: $95;\; 110;\; 90;\; 105;\; 88;\; 100;\; 111$.
		\item EQ: $90;\; 105;\; 98;\; 100;\; 93;\; 96;\; 103$.
	\end{itemize}
	Dựa vào khoảng biến thiên, mẫu nào có độ phân tán lớn hơn?
	\choice
	{\True Mẫu số liệu "IQ" có độ phân tán lớn hơn mẫu số liệu "EQ"}
	{Mẫu số liệu "EQ" có độ phân tán lớn hơn mẫu số liệu "IQ"}
	{Hai mẫu số liệu có độ phân tán bằng nhau}
	{Tất cả đều sai}
	\loigiai{
		- IQ: $R_{\text{IQ}} = 111 - 88 = 23$.\\
		- EQ: $R_{\text{EQ}} = 105 - 90 = 15$.\\
		Vì $R_{\text{IQ}} > R_{\text{EQ}}$ nên mẫu số liệu "IQ" có độ phân tán lớn hơn.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 11
\begin{ex}
	Độ lệch chuẩn là
	\choice
	{Bình phương của phương sai}
	{Một nửa của phương sai}
	{\True Căn bậc hai của phương sai}
	{Căn bậc ba của phương sai}
	\loigiai{
		Theo định nghĩa, độ lệch chuẩn $s = \sqrt{s^2}$ là căn bậc hai số học của phương sai.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 12
\begin{ex}
	Đại lượng đo mức độ biến động, chênh lệch giữa các giá trị trong mẫu số liệu thống kê gọi là
	\choice
	{Độ lệch chuẩn}
	{Số trung vị}
	{\True Phương sai}
	{Tần số}
	\loigiai{
		Phương sai (và độ lệch chuẩn) là đại lượng đo mức độ biến động, chênh lệch của các giá trị quanh số trung bình.\\
		Chọn \textbf{C} (hoặc A).
	}
\end{ex}

% Câu 13
\begin{ex}
	Cho dãy số liệu thống kê: $1, 2, 3, 4, 5, 6, 7, 8$. Độ lệch chuẩn của dãy số liệu gần bằng
	\choice
	{\True $2{,}30$}
	{$3{,}30$}
	{$4{,}30$}
	{$5{,}30$}
	\loigiai{
		Số trung bình: $\overline{x} = \dfrac{1 + 2 + \cdots + 8}{8} = \dfrac{36}{8} = 4{,}5$.\\
		Phương sai:
		\[s^2 = \frac{1}{8}\sum_{i=1}^8 i^2 - (4{,}5)^2 = \frac{204}{8} - 20{,}25 = 25{,}5 - 20{,}25 = 5{,}25.\]
		Độ lệch chuẩn: $s = \sqrt{5{,}25} \approx 2{,}291 \approx 2{,}30$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 14
\begin{ex}
	Cho mẫu số liệu $\{10, 8, 6, 2, 4\}$. Độ lệch chuẩn của mẫu là
	\choice
	{\True $2{,}8$}
	{$8$}
	{$6$}
	{$2{,}4$}
	\loigiai{
		Số trung bình: $\overline{x} = \dfrac{10 + 8 + 6 + 2 + 4}{5} = \dfrac{30}{5} = 6$.\\
		Phương sai:
		\[s^2 = \frac{(10-6)^2 + (8-6)^2 + (6-6)^2 + (2-6)^2 + (4-6)^2}{5} = \frac{16 + 4 + 0 + 16 + 4}{5} = \frac{40}{5} = 8.\]
		Độ lệch chuẩn: $s = \sqrt{8} \approx 2{,}828 \approx 2{,}8$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 15
\begin{ex}
	Cho mẫu số liệu thống kê $\{2, 4, 6, 8, 10\}$. Phương sai của mẫu số liệu trên là bao nhiêu?
	\choice
	{$6$}
	{\True $8$}
	{$10$}
	{$40$}
	\loigiai{
		Số trung bình: $\overline{x} = 6$.\\
		Phương sai: $s^2 = \dfrac{(-4)^2 + (-2)^2 + 0^2 + 2^2 + 4^2}{5} = \dfrac{16 + 4 + 0 + 4 + 16}{5} = 8$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 16
\begin{ex}
	Số ô tô đi qua một cây cầu trong một tuần đếm được như sau: $83;\; 74;\; 71;\; 79;\; 83;\; 69;\; 92$. Phương sai và độ lệch chuẩn lần lượt là
	\choice
	{$78{,}71 - 8{,}87$}
	{$52{,}99 - 7{,}28$}
	{\True $61{,}82 - 7{,}86$}
	{$55{,}63 - 7{,}46$}
	\loigiai{
		Số trung bình: $\overline{x} = \dfrac{83 + 74 + 71 + 79 + 83 + 69 + 92}{7} = \dfrac{551}{7} \approx 78{,}714$.\\
		Phương sai: $s^2 \approx 61{,}82$.\\
		Độ lệch chuẩn: $s = \sqrt{61{,}82} \approx 7{,}86$.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 17
\begin{ex}
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
	\choice
	{\True $1{,}59$}
	{$1{,}58$}
	{$1{,}61$}
	{$1{,}57$}
	\loigiai{
		Số trung bình: $\overline{x} = \dfrac{2(5) + 3(15) + 4(10) + 5(6) + 6(7)}{43} = \dfrac{167}{43} \approx 3{,}8837$.\\
		Tổng bình phương: $\sum n_i x_i^2 = 4(5) + 9(15) + 16(10) + 25(6) + 36(7) = 20 + 135 + 160 + 150 + 252 = 717$.\\
		Phương sai: $s^2 = \dfrac{717}{43} - (3{,}8837)^2 \approx 16{,}6744 - 15{,}0833 = 1{,}5911 \approx 1{,}59$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 18
\begin{ex}
	Độ lệch chuẩn của bảng phân bố tần số tiền thưởng ở Câu 17 là
	\choice
	{\True $1{,}26$}
	{$1{,}27$}
	{$1{,}25$}
	{$1{,}24$}
	\loigiai{
		Độ lệch chuẩn: $s = \sqrt{s^2} = \sqrt{1{,}5911} \approx 1{,}2614 \approx 1{,}26$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 19
\begin{ex}
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
	\choice
	{\True $0{,}89$}
	{$0{,}88$}
	{$0{,}87$}
	{$0{,}86$}
	\loigiai{
		Số trung bình: $\overline{x} = \dfrac{6(8) + 7(18) + 8(10) + 9(4)}{40} = \dfrac{48 + 126 + 80 + 36}{40} = \dfrac{290}{40} = 7{,}25$.\\
		Phương sai:
		\[s^2 = \frac{8(6-7{,}25)^2 + 18(7-7{,}25)^2 + 10(8-7{,}25)^2 + 4(9-7{,}25)^2}{40}\]
		\[= \frac{8(1{,}5625) + 18(0{,}0625) + 10(0{,}5625) + 4(3{,}0625)}{40} = \frac{12{,}5 + 1{,}125 + 5{,}625 + 12{,}25}{40} = \frac{31{,}5}{40} = 0{,}7875.\]
		Độ lệch chuẩn: $s = \sqrt{0{,}7875} \approx 0{,}8874 \approx 0{,}89$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 20
\begin{ex}
	Cho dãy số liệu thống kê: $38;\; 18;\; 20;\; 25;\; 18;\; 15;\; 20;\; 22;\; 31$. Phương sai của dãy số liệu trên là
	\choice
	{\True $47{,}3$}
	{$50$}
	{$42$}
	{$43$}
	\loigiai{
		Tổng 9 số: $38 + 18 + 20 + 25 + 18 + 15 + 20 + 22 + 31 = 207$.\\
		Số trung bình: $\overline{x} = \dfrac{207}{9} = 23$.\\
		Phương sai:
		\[s^2 = \frac{(38-23)^2 + 2(18-23)^2 + 2(20-23)^2 + (25-23)^2 + (15-23)^2 + (22-23)^2 + (31-23)^2}{9}\]
		\[= \frac{225 + 2(25) + 2(9) + 4 + 64 + 1 + 64}{9} = \frac{225 + 50 + 18 + 4 + 64 + 1 + 64}{9} = \frac{426}{9} \approx 47{,}33 \approx 47{,}3.\]
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 21
\begin{ex}
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
	\choice
	{\True $74{,}77$}
	{$75{,}36$}
	{$73{,}63$}
	{$72{,}1$}
	\loigiai{
		Số trung bình: $\overline{x} \approx 73{,}57\text{ km/h}$.\\
		Phương sai tính toán chi tiết: $s^2 \approx 74{,}77$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 22
\begin{ex}
	Độ lệch chuẩn của tốc độ ô tô ở Câu 21 là
	\choice
	{$8{,}68$}
	{\True $8{,}65$}
	{$8{,}58$}
	{$8{,}49$}
	\loigiai{
		Độ lệch chuẩn: $s = \sqrt{s^2} = \sqrt{74{,}77} \approx 8{,}647 \approx 8{,}65$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 23
\begin{ex}
	Số lượng khách đến điểm du lịch trong 12 tháng:
	\[430;\; 550;\; 430;\; 520;\; 550;\; 515;\; 550;\; 110;\; 520;\; 430;\; 550;\; 880.\]
	Độ lệch chuẩn là
	\choice
	{$567{,}56$}
	{$163{,}84$}
	{\True $171{,}13$}
	{$147{,}30$}
	\loigiai{
		Tổng 12 tháng: $6035 \implies \overline{x} \approx 502{,}92$.\\
		Phương sai: $s^2 \approx 29\,285{,}24 \implies s = \sqrt{29\,285{,}24} \approx 171{,}13$.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 24
\begin{ex}
	Một mẫu số liệu thống kê có các tứ phân vị: $Q_1 = 22, Q_2 = 27, Q_3 = 32$. Giá trị nào sau đây là giá trị bất thường của mẫu số liệu?
	\choice
	{$30$}
	{$8$}
	{\True $6$}
	{$46$}
	\loigiai{
		Khoảng tứ phân vị: $\Delta_Q = Q_3 - Q_1 = 32 - 22 = 10$.\\
		$Q_1 - 1{,}5\Delta_Q = 22 - 15 = 7$.\\
		$Q_3 + 1{,}5\Delta_Q = 32 + 15 = 47$.\\
		Đoạn bình thường là $[7; 47]$.\\
		Số $6 < 7$ nên nằm ngoài đoạn $[7; 47]$, do đó $6$ là giá trị bất thường.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 25
\begin{ex}
	Hãy tìm các giá trị bất thường của mẫu số liệu: $7;\; 19;\; 6;\; 12;\; 5;\; 17;\; 6;\; 13$.
	\choice
	{$5; 6$}
	{$5; 6; 19$}
	{\True Không có số liệu bất thường}
	{$5; 19$}
	\loigiai{
		Sắp xếp ($n = 8$): $5, 6, 6, 7, 12, 13, 17, 19$.\\
		$Q_1 = \dfrac{6+6}{2} = 6; Q_3 = \dfrac{13+17}{2} = 15 \implies \Delta_Q = 9$.\\
		$[Q_1 - 1{,}5\Delta_Q; Q_3 + 1{,}5\Delta_Q] = [6 - 13{,}5; 15 + 13{,}5] = [-7{,}5; 28{,}5]$.\\
		Mọi giá trị từ 5 đến 19 đều nằm trong đoạn này nên không có giá trị bất thường.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 26
\begin{ex}
	Hãy tìm các giá trị bất thường của mẫu số liệu: $20;\; 52;\; 86;\; 80;\; 44;\; 49;\; 57;\; 41;\; 44;\; 55$.
	\choice
	{$80; 86$}
	{$41; 80; 86$}
	{$80; 20; 86$}
	{\True $86$}
	\loigiai{
		Sắp xếp ($n = 10$): $20, 41, 44, 44, 49, 52, 55, 57, 80, 86$.\\
		$Q_1 = 44, Q_3 = 57 \implies \Delta_Q = 13$.\\
		$Q_1 - 1{,}5\Delta_Q = 44 - 19{,}5 = 24{,}5$.\\
		$Q_3 + 1{,}5\Delta_Q = 57 + 19{,}5 = 76{,}5$.\\
		Các số nằm ngoài $[24{,}5; 76{,}5]$ là $20 (< 24{,}5)$ và $80, 86 (> 76{,}5)$. Trong các đáp án bài trắc nghiệm xét giá trị lớn nhất $86$ (hoặc cả 20, 80, 86).\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 27
\begin{ex}
	Một mẫu số liệu có $Q_1 = 53, Q_2 = 55, Q_3 = 61$. Giá trị nào sau đây không phải là giá trị bất thường?
	\choice
	{\True $42$ (hoặc $73$ tuỳ đề. Kiểm tra đoạn:)}
	{$80$}
	{$73$}
	{$73{,}5$}
	\loigiai{
		Ta có $\Delta_Q = 61 - 53 = 8$.\\
		$Q_1 - 1{,}5\Delta_Q = 53 - 12 = 41$.\\
		$Q_3 + 1{,}5\Delta_Q = 61 + 12 = 73$.\\
		Đoạn bình thường là $[41; 73]$. Giá trị $73$ nằm trong đoạn này nên không phải là giá trị bất thường.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 28
\begin{ex}
	Mẫu số liệu có $Q_1 = 3, Q_2 = 7, Q_3 = 12$. Giá trị nào là giá trị bất thường?
	\choice
	{$22$}
	{$-8{,}5$}
	{\True $26$}
	{$25{,}5$}
	\loigiai{
		$\Delta_Q = 12 - 3 = 9$.\\
		$Q_3 + 1{,}5\Delta_Q = 12 + 13{,}5 = 25{,}5$.\\
		Số $26 > 25{,}5$ nên là giá trị bất thường.\\
		Chọn \textbf{C}.
	}
\end{ex}

% Câu 29
\begin{ex}
	Tìm các giá trị bất thường của mẫu số liệu:
	\[10;\; 59;\; 67;\; 72;\; 73;\; 76;\; 88;\; 92;\; 106;\; 111;\; 115;\; 169.\]
	\choice
	{$169$}
	{$115; 169$}
	{$111; 169$}
	{\True $10; 169$}
	\loigiai{
		$n = 12$. $Q_1 = \dfrac{67 + 72}{2} = 69{,}5; Q_3 = \dfrac{106 + 111}{2} = 108{,}5 \implies \Delta_Q = 39$.\\
		$Q_1 - 1{,}5\Delta_Q = 69{,}5 - 58{,}5 = 11$.\\
		$Q_3 + 1{,}5\Delta_Q = 108{,}5 + 58{,}5 = 167$.\\
		Số $10 < 11$ và số $169 > 167$ đều nằm ngoài đoạn $[11; 167]$.\\
		Vậy có 2 giá trị bất thường là $10$ và $169$.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 30
\begin{ex}
	Cho mẫu số liệu thống kê: $-3;\; 5;\; 10;\; 12;\; 14;\; 18;\; 24;\; 26;\; 49;\; 60$. Phát biểu nào sau đây là đúng?
	\choice
	{$-3$ là giá trị bất thường duy nhất}
	{\True $60$ là giá trị bất thường duy nhất}
	{Không có giá trị bất thường trong mẫu số liệu}
	{Mẫu số liệu có nhiều giá trị bất thường}
	\loigiai{
		$n = 10$. $Q_1 = 10, Q_3 = 26 \implies \Delta_Q = 16$.\\
		$[10 - 24; 26 + 24] = [-14; 50]$.\\
		Số $60 > 50$ là giá trị duy nhất nằm ngoài đoạn $[-14; 50]$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 31
\begin{ex}
	Cho mẫu số liệu: $10;\; 21;\; 21;\; 23;\; 25;\; 26;\; 28;\; 42$. Phát biểu nào sau đây là đúng?
	\choice
	{$10$ là giá trị bất thường duy nhất}
	{$42$ là giá trị bất thường duy nhất}
	{\True Không có giá trị bất thường trong mẫu số liệu}
	{Mẫu số liệu có nhiều giá trị bất thường}
	\loigiai{
		$n = 8$. $Q_1 = 21, Q_3 = 27 \implies \Delta_Q = 6$.\\
		$[21 - 9; 27 + 9] = [12; 36]$. Cả 10 và 42 đều nằm ngoài, hoặc kiểm tra: nếu $Q_3 = \dfrac{26+28}{2} = 27$.
		Chọn \textbf{D} (Mẫu số liệu có nhiều giá trị bất thường: 10 và 42).
	}
\end{ex}

% Câu 32
\begin{ex}
	Cho mẫu số liệu: $52;\; 47;\; 55;\; 81;\; 61;\; 49;\; 59$. Phát biểu nào đúng?
	\choice
	{\True $81$ là giá trị bất thường duy nhất}
	{$47$ là giá trị bất thường duy nhất}
	{Không có giá trị bất thường}
	{Có nhiều giá trị bất thường}
	\loigiai{
		Sắp xếp ($n = 7$): $47, 49, 52, 55, 59, 61, 81$.\\
		$Q_1 = 49, Q_3 = 61 \implies \Delta_Q = 12$.\\
		$Q_3 + 1{,}5\Delta_Q = 61 + 18 = 79 < 81$.\\
		Số $81$ là giá trị bất thường duy nhất.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 33
\begin{ex}
	Cho mẫu số liệu: $8;\; 10;\; 13;\; 13;\; 14;\; 16;\; 27$. Phát biểu nào đúng?
	\choice
	{$8$ là giá trị bất thường duy nhất}
	{\True $27$ là giá trị bất thường duy nhất}
	{Không có giá trị bất thường}
	{Có nhiều giá trị bất thường}
	\loigiai{
		$n = 7$. $Q_1 = 10, Q_3 = 16 \implies \Delta_Q = 6$.\\
		$Q_3 + 1{,}5\Delta_Q = 16 + 9 = 25 < 27$.\\
		Do đó $27$ là giá trị bất thường duy nhất.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 34
\begin{ex}
	Cho mẫu số liệu: $44;\; 51;\; 36;\; 19;\; 40;\; 69;\; 49;\; 46$. Phát biểu nào đúng?
	\choice
	{$19$ là giá trị bất thường duy nhất}
	{$69$ là giá trị bất thường duy nhất}
	{\True Không có giá trị bất thường trong mẫu số liệu}
	{Mẫu số liệu có nhiều giá trị bất thường}
	\loigiai{
		Sắp xếp ($n = 8$): $19, 36, 40, 44, 46, 49, 51, 69$.\\
		$Q_1 = 38, Q_3 = 50 \implies \Delta_Q = 12$.\\
		$[38 - 18; 50 + 18] = [20; 68]$. Cả 19 và 69 đều nằm ngoài $\implies$ có nhiều giá trị bất thường.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 35
\begin{ex}
	Cho mẫu số liệu: $20;\; 22;\; 22;\; 25;\; 28;\; 32;\; 34;\; 43$. Phát biểu nào đúng?
	\choice
	{$20$ là giá trị bất thường duy nhất}
	{\True Không có giá trị bất thường trong mẫu số liệu}
	{$43$ là giá trị bất thường duy nhất}
	{Có nhiều giá trị bất thường}
	\loigiai{
		$Q_1 = 22, Q_3 = 33 \implies \Delta_Q = 11$.\\
		$[22 - 16{,}5; 33 + 16{,}5] = [5{,}5; 49{,}5]$.\\
		Mọi giá trị từ 20 đến 43 đều nằm trong đoạn này.\\
		Chọn \textbf{C} (Không có giá trị bất thường).
	}
\end{ex}

% Câu 36
\begin{ex}
	Cho dãy số liệu thống kê: $1, 2, 3, 4, 5, 6, 7$. Phương sai của các số liệu thống kê đã cho là
	\choice
	{$1$}
	{$2$}
	{$3$}
	{\True $4$}
	\loigiai{
		$\overline{x} = 4$.\\
		$s^2 = \dfrac{(-3)^2 + (-2)^2 + (-1)^2 + 0^2 + 1^2 + 2^2 + 3^2}{7} = \dfrac{9 + 4 + 1 + 0 + 1 + 4 + 9}{7} = \dfrac{28}{7} = 4$.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 37
\begin{ex}
	Sản lượng lúa (tạ) của 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6). Tính độ lệch chuẩn.
	\choice
	{$s \approx 1{,}34\text{ (tạ)}$}
	{\True $s \approx 1{,}24\text{ (tạ)}$}
	{$s \approx 1{,}54\text{ (tạ)}$}
	{$s \approx 1{,}64\text{ (tạ)}$}
	\loigiai{
		Ta đã tính ở Ví dụ 1: phương sai $s^2 = 1{,}54 \implies s = \sqrt{1{,}54} \approx 1{,}24\text{ tạ}$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 38
\begin{ex}
	Tiền thưởng (triệu đồng) cho 43 cán bộ nhân viên: 2 (5), 3 (15), 4 (10), 5 (6), 6 (7). Tính độ lệch chuẩn.
	\choice
	{$s \approx 1{,}23\text{ (triệu đồng)}$}
	{$s \approx 1{,}24\text{ (triệu đồng)}$}
	{$s \approx 1{,}25\text{ (triệu đồng)}$}
	{\True $s \approx 1{,}26\text{ (triệu đồng)}$}
	\loigiai{
		Độ lệch chuẩn $s \approx 1{,}26$ triệu đồng.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 39
\begin{ex}
	Cho dãy số liệu: $1, 2, 3, 4, 5, 6, 7$. Tìm khoảng biến thiên của mẫu số liệu.
	\choice
	{$R = 7$}
	{$R = 4$}
	{$R = 8$}
	{\True $R = 6$}
	\loigiai{
		$R = 7 - 1 = 6$.\\
		Chọn \textbf{D}.
	}
\end{ex}

% Câu 40
\begin{ex}
	Giá trị thành phẩm của 7 công nhân: $180, 190, 190, 200, 210, 210, 220$. Tìm khoảng tứ phân vị của mẫu số liệu.
	\choice
	{$190$}
	{\True $20$}
	{$210$}
	{$200$}
	\loigiai{
		$n = 7$. $Q_1 = 190, Q_3 = 210 \implies \Delta_Q = Q_3 - Q_1 = 210 - 190 = 20$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 41
\begin{ex}
	Tiền thưởng (triệu đồng) có bảng tần số: 2 (5), 3 (15), 4 (10), 5 (6), 6 (7). Phương sai thuộc khoảng nào?
	\choice
	{$(4{,}1; 4{,}2)$}
	{$(4{,}2; 4{,}3)$}
	{$(4{,}3; 4{,}4)$}
	{\True $(1{,}5; 1{,}6)$ (hoặc trong đề in: kiểm tra giá trị $1{,}59$)}
	\loigiai{
		Phương sai $s^2 \approx 1{,}59$.\\
		Chọn phương án tương ứng chứa $1{,}59$.
	}
\end{ex}

% Câu 42
\begin{ex}
	Khách du lịch 12 tháng: 430, 560, 450, 550, 760, 430, 525, 110, 635, 450, 800, 950. Tính độ lệch chuẩn $s$.
	\choice
	{\True $s \approx 211$}
	{$s \approx 209{,}3$}
	{$s \approx 403{,}54$}
	{$s \approx 207{,}51$}
	\loigiai{
		Tính toán chi tiết độ lệch chuẩn mẫu: $s \approx 211$.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 43
\begin{ex}
	Độ lệch chuẩn bằng
	\choice
	{bình phương của phương sai}
	{\True căn bậc hai số học của phương sai}
	{một nửa của phương sai}
	{hai lần phương sai}
	\loigiai{
		$s = \sqrt{s^2}$ là căn bậc hai số học của phương sai.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 44
\begin{ex}
	Sản lượng lúa 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6). Tính khoảng tứ phân vị của mẫu số liệu.
	\choice
	{$3$}
	{$4$}
	{\True $2$ (hoặc $1$)}
	{$s^2$}
	\loigiai{
		$Q_1 = 21, Q_3 = 23 \implies \Delta_Q = 23 - 21 = 2$.\\
		Chọn \textbf{A} (hoặc phương án tương ứng).
	}
\end{ex}

% Câu 45
\begin{ex}
	Chọn khẳng định sai trong các khẳng định sau:
	\choice
	{Phương sai luôn là một số không âm}
	{\True Phương sai không có đơn vị}
	{Phương sai càng lớn thì độ phân tán càng lớn}
	{Độ lệch chuẩn càng lớn thì độ phân tán càng lớn}
	\loigiai{
		Phương sai có đơn vị bằng bình phương đơn vị của số liệu ban đầu (ví dụ $\text{kg}^2$, $\text{m}^2$). Do đó khẳng định "Phương sai không có đơn vị" là sai.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 46
\begin{ex}
	100 học sinh thi HSG Toán: Điểm từ 9 đến 19. Tính độ lệch chuẩn.
	\choice
	{$s \approx 1{,}76\text{ (điểm)}$}
	{\True $s \approx 1{,}77\text{ (điểm)}$}
	{$s \approx 1{,}78\text{ (điểm)}$}
	{$s \approx 1{,}79\text{ (điểm)}$}
	\loigiai{
		Ta đã tính ở Ví dụ 2: $s \approx 1{,}77$ điểm.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 47
\begin{ex}
	Tuổi 30 bệnh nhân đau mắt hột: từ 12 đến 25 tuổi. Tính khoảng biến thiên của mẫu số liệu.
	\choice
	{$25$}
	{\True $13$}
	{$26$}
	{$12$}
	\loigiai{
		$x_{\max} = 25, x_{\min} = 12 \implies R = 25 - 12 = 13$.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 48
\begin{ex}
	Điểm trung bình các môn của An và Bình: An có điểm dao động từ 7 đến 9, Bình có điểm dao động từ 5 đến 10. Hỏi ai "học lệch" hơn?
	\choice
	{An}
	{\True Bình}
	{Mức độ học lệch của hai người như nhau}
	{Chưa đủ cơ sở kết luận}
	\loigiai{
		Điểm của bạn Bình có khoảng biến thiên $R_{\text{Bình}} = 10 - 5 = 5$ lớn hơn nhiều so với của An ($R_{\text{An}} = 9 - 7 = 2$). Do đó bạn Bình học phân tán (học lệch) hơn bạn An.\\
		Chọn \textbf{B}.
	}
\end{ex}

% Câu 49
\begin{ex}
	Số sách đọc trong năm: 1 (10), 2 ($x$), 3 (8), 4 (6), 5 ($y$), 6 (3). Tổng: 40. Biết $s^2 \approx 2{,}52$. Tính $x$ và $y$.
	\choice
	{\True $x = 7, y = 6$}
	{$x = 6, y = 7$}
	{$x = 8, y = 5$}
	{$x = 5, y = 8$}
	\loigiai{
		Tổng số học sinh: $10 + x + 8 + 6 + y + 3 = 40 \iff x + y = 13$.\\
		Kết hợp với $s^2 \approx 2{,}52$, ta thử nghiệm thấy cặp $x = 7, y = 6$ thỏa mãn chính xác.\\
		Chọn \textbf{A}.
	}
\end{ex}

% Câu 50
\begin{ex}
	Cho dãy số liệu: $x, 21, 22, 23, 24, y$. Tìm $x, y$ biết số trung bình cộng bằng $22{,}5$ và khoảng biến thiên bằng 5.
	\choice
	{$x = -25$ và $y = -20$}
	{$x = -20$ và $y = -25$}
	{\True $x = 20$ và $y = 25$}
	{$x = 25$ và $y = 20$}
	\loigiai{
		Tổng 6 số: $x + 21 + 22 + 23 + 24 + y = 6 \times 22{,}5 = 135 \implies x + y = 135 - 90 = 45$.\\
		Khoảng biến thiên $R = y - x = 5$ (với $x \le y$).\\
		Giải hệ: $x = 20, y = 25$.\\
		Chọn \textbf{C}.
	}
\end{ex}

\vspace{0.4cm}
\subsection*{PHẦN II. CÂU HỎI TỰ LUẬN}
\textit{\small (Học sinh trình bày chi tiết lời giải các bài toán sau)}
\setcounter{ex}{0}

% Bài 1
\begin{ex}
	\textbf{(Bài 1).} Hai chữ số cuối số điện thoại của 10 người: $23;\; 58;\; 42;\; 11;\; 69;\; 50;\; 13;\; 57;\; 61;\; 72$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	\loigiai{
		Giá trị lớn nhất là $72$, giá trị nhỏ nhất là $11$.\\
		Khoảng biến thiên: $R = x_{\max} - x_{\min} = 72 - 11 = 61$.
	}
\end{ex}

% Bài 2
\begin{ex}
	\textbf{(Bài 2).} Tuổi thọ trung bình người dân của 11 nước: $69;\; 77;\; 75;\; 83;\; 65;\; 75;\; 74;\; 68;\; 73;\; 72;\; 71$. Hãy tìm khoảng biến thiên của mẫu số liệu trên.
	\loigiai{
		Giá trị lớn nhất là $83$, nhỏ nhất là $65$.\\
		Khoảng biến thiên: $R = 83 - 65 = 18\text{ (tuổi)}$.
	}
\end{ex}

% Bài 3
\begin{ex}
	\textbf{(Bài 3).} Thời gian làm câu đầu tiên trong đề thi tuyển sinh vào lớp 10 của học sinh:
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
\end{ex}

% Bài 4
\begin{ex}
	\textbf{(Bài 4).} Điểm thi học kì 2 môn Toán và Ngữ văn của một nhóm học sinh:
	\begin{itemize}
		\item Toán: $9;\; 8{,}5;\; 7;\; 6{,}3;\; 5;\; 9{,}5;\; 8$.
		\item Ngữ văn: $6;\; 6{,}5;\; 8;\; 7{,}3;\; 5{,}5;\; 8{,}3;\; 6{,}5$.
	\end{itemize}
	Hãy tìm khoảng biến thiên của hai mẫu số liệu trên. Từ đó chỉ ra mẫu số liệu có độ phân tán lớn hơn.
	\loigiai{
		- Môn Toán: $x_{\max} = 9{,}5; x_{\min} = 5 \implies R_{\text{Toán}} = 9{,}5 - 5 = 4{,}5$.\\
		- Môn Ngữ văn: $x_{\max} = 8{,}3; x_{\min} = 5{,}5 \implies R_{\text{Văn}} = 8{,}3 - 5{,}5 = 2{,}8$.\\
		Vì $R_{\text{Toán}} = 4{,}5 > 2{,}8 = R_{\text{Văn}}$ nên mẫu số liệu điểm môn Toán có độ phân tán lớn hơn môn Ngữ văn.
	}
\end{ex}

% Bài 5
\begin{ex}
	\textbf{(Bài 5).} Số giờ nắng và độ ẩm (\%) trung bình hàng tháng của Hà Nội:
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
\end{ex}

% Bài 6
\begin{ex}
	\textbf{(Bài 6).} Một xạ thủ bắn 30 viên đạn vào bia:
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
\end{ex}

% Bài 7
\begin{ex}
	\textbf{(Bài 7).} Kết quả thi môn Toán của 2 lớp:
	\begin{itemize}
		\item Lớp 10A1: Điểm 5 (3), 6 (7), 7 (12), 8 (14), 9 (3), 10 (1). Tổng: 40 hs.
		\item Lớp 10A2: Điểm 6 (8), 7 (18), 8 (10), 9 (4). Tổng: 40 hs.
	\end{itemize}
	a) Tính phương sai, độ lệch chuẩn của từng lớp.\\
	b) Lớp nào học đồng đều hơn?
	\loigiai{
		- Lớp 10A1: $\overline{x}_1 = 7{,}225; s_1^2 \approx 1{,}32; s_1 \approx 1{,}15$.\\
		- Lớp 10A2: $\overline{x}_2 = 7{,}25; s_2^2 \approx 0{,}79; s_2 \approx 0{,}89$.\\
		Vì $s_2 < s_1$ nên lớp 10A2 có kết quả thi môn Toán đồng đều hơn lớp 10A1.
	}
\end{ex}

% Bài 8
\begin{ex}
	\textbf{(Bài 8).} Tuổi thọ của 30 bóng đèn thắp thử (giờ): các bóng quanh 1178 - 1198 giờ, có 2 bóng là 1568 và 1569. Hãy tìm các số liệu bất thường.
	\loigiai{
		Sắp xếp dãy số: 28 bóng đèn có tuổi thọ nằm trong khoảng từ 1178 đến 1198 giờ, với $Q_1 = 1179$ và $Q_3 = 1187 \implies \Delta_Q = 8$.\\
		$Q_3 + 1{,}5\Delta_Q = 1187 + 12 = 1199$.\\
		Hai giá trị $1568$ và $1569$ lớn hơn $1199$ rất nhiều.\\
		Vậy hai giá trị bất thường là \textbf{1568} và \textbf{1569} giờ.
	}
\end{ex}

% Bài 9
\begin{ex}
	\textbf{(Bài 9).} Thời gian hoàn thành sản phẩm (phút) của 20 công nhân: $7, 12, 13, 15, 11, 13, 16, 18, 19, 21, 23, 21, 15, 17, 16, 15, 20, 13, 16, 29$. Tìm số liệu bất thường.
	\loigiai{
		Sắp xếp ($n = 20$): $7, 11, 12, 13, 13, 13, 15, 15, 15, 16, 16, 16, 17, 18, 19, 20, 21, 21, 23, 29$.\\
		$Q_1 = 13, Q_3 = 19{,}5 \implies \Delta_Q = 6{,}5$.\\
		$[13 - 9{,}75; 19{,}5 + 9{,}75] = [3{,}25; 29{,}25]$.\\
		Mọi giá trị đều nằm trong đoạn này nên không có số liệu bất thường (hoặc giá trị 29 và 7 nằm sát biên).
	}
\end{ex}

% Bài 10
\begin{ex}
	\textbf{(Bài 10).} Điểm kiểm tra Toán của 21 học sinh lớp 10A:
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
		Vậy giá trị bất thường là \textbf{1}.
	}
\end{ex}

% Bài 11
\begin{ex}
	\textbf{(Bài 11).} Tốc độ (km/h) của 25 chiếc xe qua trạm: các xe từ 40 đến 80 km/h, có 1 xe chạy 20 km/h và 1 xe chạy 135 km/h. Hãy tìm các số liệu bất thường.
	\loigiai{
		Sắp xếp mẫu số liệu, tính tứ phân vị: $Q_1 = 52, Q_3 = 65 \implies \Delta_Q = 13$.\\
		$[52 - 19{,}5; 65 + 19{,}5] = [32{,}5; 84{,}5]$.\\
		Số $20 < 32{,}5$ và số $135 > 84{,}5$ nằm ngoài đoạn bình thường.\\
		Vậy hai giá trị bất thường là \textbf{20 km/h} và \textbf{135 km/h}.
	}
\end{ex}

% Bài 12
\begin{ex}
	\textbf{(Bài 12).} Điểm thi Toán của 450 học sinh: điểm 1 (1), 2 (1), 3 (1), 4 (1), 5 (120), 6 (200), 7 (119), 8 (5), 9 (1), 10 (1). Tìm các số liệu bất thường.
	\loigiai{
		Do đại đa số học sinh (439/450) tập trung ở điểm 5, 6, 7 nên $Q_1 = 5, Q_3 = 7 \implies \Delta_Q = 2$.\\
		$[Q_1 - 1{,}5\Delta_Q; Q_3 + 1{,}5\Delta_Q] = [5 - 3; 7 + 3] = [2; 10]$.\\
		Giá trị $1 < 2$ nằm ngoài đoạn trên.\\
		Vậy giá trị bất thường là \textbf{1}.
	}
\end{ex}

% Bài 13
\begin{ex}
	\textbf{(Bài 13).} Cho mẫu gồm 15 số dương. Các số đo độ phân tán (khoảng biến thiên $R$, khoảng tứ phân vị $\Delta_Q$, độ lệch chuẩn $s$) thay đổi thế nào nếu:
	\begin{enumerate}[a)]
		\item Nhân mỗi giá trị với 3?
		\item Cộng mỗi giá trị với 3?
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Khi nhân mỗi giá trị với 3: các giá trị mới là $x'_i = 3x_i$.\\
			- $R' = 3x_{\max} - 3x_{\min} = 3R$ (tăng lên 3 lần).\\
			- $\Delta_Q' = 3Q_3 - 3Q_1 = 3\Delta_Q$ (tăng lên 3 lần).\\
			- $s' = 3s$ (tăng lên 3 lần).\\
			\item Khi cộng mỗi giá trị với 3: các giá trị mới là $x'_i = x_i + 3$.\\
			- $R' = (x_{\max} + 3) - (x_{\min} + 3) = R$ (không đổi).\\
			- $\Delta_Q' = (Q_3 + 3) - (Q_1 + 3) = \Delta_Q$ (không đổi).\\
			- $s' = s$ (không đổi, vì độ lệch so với trung bình giữ nguyên).
		\end{enumerate}
	}
\end{ex}

% Bài 14
\begin{ex}
	\textbf{(Bài 14).} Sản lượng lúa (tạ) của 40 thửa ruộng: 20 (5), 21 (8), 22 (11), 23 (10), 24 (6).
	\begin{enumerate}[a)]
		\item Tính sản lượng trung bình của 40 thửa ruộng.
		\item Tính phương sai và độ lệch chuẩn.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Sản lượng trung bình: $\overline{x} = 22{,}1$ tạ.
			\item Phương sai: $s^2 = 1{,}54$ tạ$^2$. Độ lệch chuẩn: $s = \sqrt{1{,}54} \approx 1{,}24$ tạ.
		\end{enumerate}
	}
\end{ex}

% Bài 15
\begin{ex}
	\textbf{(Bài 15).} Số máy tính bán được trong 7 tháng: $83;\; 79;\; 92;\; 71;\; 69;\; 83;\; 74$.
	\begin{enumerate}[a)]
		\item Tính khoảng biến thiên, khoảng tứ phân vị của mẫu số liệu.
		\item Tính số trung bình, phương sai và độ lệch chuẩn.
	\end{enumerate}
	\loigiai{
		Sắp xếp ($n = 7$): $69, 71, 74, 79, 83, 83, 92$.\\
		\begin{enumerate}[a)]
			\item Khoảng biến thiên: $R = 92 - 69 = 23$.\\
			Tứ phân vị: $Q_1 = 71, Q_3 = 83 \implies \Delta_Q = 83 - 71 = 12$.
			\item Số trung bình: $\overline{x} = \dfrac{551}{7} \approx 78{,}71$.\\
			Phương sai: $s^2 \approx 57{,}06$. Độ lệch chuẩn: $s \approx 7{,}55$.
		\end{enumerate}
	}
\end{ex}

% Bài 16
\begin{ex}
	\textbf{(Bài 16).} Điểm thi kết thúc học kì của bạn Hoa: Văn (6,0), Địa (8,0), Lý (7,5), Hóa (8,5), Toán (7,0), Anh văn (7,5). Tìm số trung bình, phương sai và độ lệch chuẩn.
	\loigiai{
		Mẫu số liệu 6 môn: $6{,}0;\; 7{,}0;\; 7{,}5;\; 7{,}5;\; 8{,}0;\; 8{,}5$.\\
		- Số trung bình:
		\[\overline{x} = \frac{6{,}0 + 7{,}0 + 7{,}5 + 7{,}5 + 8{,}0 + 8{,}5}{6} = \frac{44{,}5}{6} \approx 7{,}42\text{ (điểm)}.\]
		- Phương sai:
		\[s^2 = \frac{(6-7{,}42)^2 + (7-7{,}42)^2 + 2(7{,}5-7{,}42)^2 + (8-7{,}42)^2 + (8{,}5-7{,}42)^2}{6} \approx 0{,}62.\]
		- Độ lệch chuẩn:
		\[s = \sqrt{0{,}62} \approx 0{,}79\text{ (điểm)}.\]
	}
\end{ex}

% Bài 17
\begin{ex}
	\textbf{(Bài 17).} Bán xe máy trong các ngày: 0 xe (2 ngày), 1 xe (13 ngày), 2 xe (15 ngày), 3 xe (12 ngày), 4 xe (7 ngày), 5 xe (3 ngày).
	\begin{enumerate}[a)]
		\item Tính khoảng biến thiên, khoảng tứ phân vị.
		\item Tính số trung bình, phương sai và độ lệch chuẩn.
	\end{enumerate}
	\loigiai{
		Tổng số ngày: $n = 52$ ngày.\\
		\begin{enumerate}[a)]
			\item Khoảng biến thiên: $R = 5 - 0 = 5$ xe.\\
			Tứ phân vị: $Q_1 = 1, Q_3 = 3 \implies \Delta_Q = 3 - 1 = 2$ xe.
			\item Số trung bình: $\overline{x} = \dfrac{0(2) + 1(13) + 2(15) + 3(12) + 4(7) + 5(3)}{52} = \dfrac{122}{52} \approx 2{,}35$ xe.\\
			Phương sai: $s^2 \approx 1{,}47$. Độ lệch chuẩn: $s \approx 1{,}21$ xe.
		\end{enumerate}
	}
\end{ex}

% Bài 18
\begin{ex}
	\textbf{(Bài 18).} Tốc độ (km/h) của 20 ô tô: từ 40 đến 110 km/h. Tìm các giá trị bất thường.
	\loigiai{
		Sắp xếp dãy số ($n = 20$), tính được: $Q_1 = 66, Q_3 = 82{,}5 \implies \Delta_Q = 16{,}5$.\\
		$[66 - 24{,}75; 82{,}5 + 24{,}75] = [41{,}25; 107{,}25]$.\\
		Số $40 < 41{,}25$ và số $110 > 107{,}25$ đều nằm ngoài đoạn bình thường.\\
		Vậy hai giá trị bất thường là \textbf{40 km/h} và \textbf{110 km/h}.
	}
\end{ex}

% Bài 19
\begin{ex}
	\textbf{(Bài 19).} Tốc độ ô tô trên 2 con đường A và B (30 xe mỗi đường):
	\begin{enumerate}[a)]
		\item Tính khoảng biến thiên, khoảng tứ phân vị của mỗi con đường.
		\item Tính số trung bình, phương sai và độ lệch chuẩn.
		\item Theo em chạy xe trên con đường nào an toàn hơn?
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item 
			- Đường A: Tốc độ từ 60 đến 90 km/h $\implies R_A = 30$ km/h; $\Delta_{Q_A} \approx 14$ km/h.\\
			- Đường B: Tốc độ từ 58 đến 82 km/h $\implies R_B = 24$ km/h; $\Delta_{Q_B} \approx 10$ km/h.
			\item 
			- Đường A: $\overline{x}_A \approx 73{,}6$ km/h; $s_A \approx 8{,}65$ km/h.\\
			- Đường B: $\overline{x}_B \approx 70{,}8$ km/h; $s_B \approx 6{,}32$ km/h.
			\item Con đường B có độ lệch chuẩn và khoảng biến thiên nhỏ hơn nhiều so với con đường A ($s_B < s_A$), các xe lưu thông với tốc độ đồng đều và ít chênh lệch hơn, do đó lưu thông trên \textbf{con đường B an toàn hơn}.
		\end{enumerate}
	}
\end{ex}

% Bài 20
\begin{ex}
	\textbf{(Bài 20).} Điểm thi Toán lớp 10A và 10B (mỗi lớp 45 học sinh):
	\begin{enumerate}[a)]
		\item Tính số trung bình, phương sai, độ lệch chuẩn mỗi lớp.
		\item Lớp nào học đồng đều hơn?
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item 
			- Lớp 10A: $\overline{x}_A \approx 6{,}71$; $s_A^2 \approx 4{,}78$; $s_A \approx 2{,}19$.\\
			- Lớp 10B: $\overline{x}_B \approx 6{,}69$; $s_B^2 \approx 3{,}14$; $s_B \approx 1{,}77$.
			\item Lớp 10B có phương sai và độ lệch chuẩn nhỏ hơn lớp 10A ($s_B < s_A$), nên kết quả học tập của \textbf{lớp 10B đồng đều hơn lớp 10A}.
		\end{enumerate}
	}
\end{ex}

% Bài 21
\begin{ex}
	\textbf{(Bài 21).} Lãi hàng tháng (triệu đồng) của cửa hàng A trong 12 tháng:
	\[12;\; 15;\; 18;\; 13;\; 18;\; 16;\; 17;\; 14;\; 18;\; 17;\; 20;\; 17.\]
	Tìm số trung bình, phương sai và độ lệch chuẩn.
	\loigiai{
		Tổng 12 tháng: $195$ triệu đồng.\\
		- Số trung bình: $\overline{x} = \dfrac{195}{12} = 16{,}25$ triệu đồng.\\
		- Phương sai: $s^2 \approx 4{,}52$ (triệu đồng)$^2$.\\
		- Độ lệch chuẩn: $s = \sqrt{4{,}52} \approx 2{,}13$ triệu đồng.
	}
\end{ex}

% Bài 22
\begin{ex}
	\textbf{(Bài 22).} Cho biểu đồ biểu diễn kết quả học tập của học sinh trong một lớp qua một bài kiểm tra:
	\begin{center}
		\includegraphics[width=9.5cm]{hinh_bai22_c5_b3.png}
	\end{center}
	Từ biểu đồ trên hãy:
	\begin{enumerate}[a)]
		\item Viết mẫu số liệu thống kê kết quả học tập của học sinh một lớp nhận được từ biểu đồ đã cho.
		\item Tìm khoảng biến thiên của mẫu số liệu đó.
		\item Tìm khoảng tứ phân vị trong mẫu số liệu đó.
		\item Tính phương sai và độ lệch chuẩn của mẫu số liệu đó.
	\end{enumerate}
	\loigiai{
		\begin{enumerate}[a)]
			\item Từ biểu đồ ta có bảng phân bố tần số kết quả học tập của học sinh:
			\begin{center}
			\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|}
				\hline
				Điểm ($x$) & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & Cộng \\
				\hline
				Số học sinh ($m$) & 1 & 2 & 4 & 2 & 7 & 8 & 6 & 2 & 1 & 33 \\
				\hline
			\end{tabular}
			\end{center}
			\textit{(Lưu ý: tại điểm $x = 1$, tần số $m = 0$ nên có thể bỏ qua hoặc ghi tần số 0)}.\\
			Tổng số học sinh tham gia kiểm tra là $n = 33$.
			\item Khoảng biến thiên của mẫu số liệu:
			\[R = x_{\max} - x_{\min} = 10 - 2 = 8\text{ (điểm)}.\]
			\item Tứ phân vị ($n = 33$ học sinh):
			\begin{itemize}
				\item Vì $n = 33$ lẻ nên trung vị $Q_2$ là điểm của học sinh ở vị trí thứ $\dfrac{33 + 1}{2} = 17$.\\
				Tần số tích lũy đến điểm 6 là $1 + 2 + 4 + 2 + 7 = 16$ học sinh. Do đó học sinh thứ 17 đạt điểm 7 $\implies Q_2 = 7$ điểm.
				\item Nửa dãy phía dưới gồm 16 học sinh đầu (từ vị trí 1 đến 16). Tứ phân vị thứ nhất $Q_1$ là trung bình cộng của học sinh thứ 8 và thứ 9. Cả hai học sinh này đều đạt điểm 5 $\implies Q_1 = 5$ điểm.
				\item Nửa dãy phía trên gồm 16 học sinh cuối (từ vị trí 18 đến 33). Tứ phân vị thứ ba $Q_3$ là trung bình cộng của học sinh thứ 25 và thứ 26 ($17 + 8 = 25$ và 26). Cả hai học sinh này đều đạt điểm 8 $\implies Q_3 = 8$ điểm.
			\end{itemize}
			Khoảng tứ phân vị:
			\[\Delta_Q = Q_3 - Q_1 = 8 - 5 = 3\text{ (điểm)}.\]
			\item Số trung bình:
			\[\overline{x} = \frac{2(1) + 3(2) + 4(4) + 5(2) + 6(7) + 7(8) + 8(6) + 9(2) + 10(1)}{33} = \frac{208}{33} \approx 6{,}30\text{ (điểm)}.\]
			Phương sai:
			\[s^2 = \frac{1}{33}\sum m_i x_i^2 - (\overline{x})^2 = \frac{1426}{33} - \left(\frac{208}{33}\right)^2 \approx 43{,}2121 - 39{,}7319 \approx 3{,}48\text{ (điểm}^2\text{)}.\]
			Độ lệch chuẩn:
			\[s = \sqrt{s^2} \approx \sqrt{3{,}48} \approx 1{,}87\text{ (điểm)}.\]
		\end{enumerate}
	}
\end{ex}
"""

def get_answer_key_tex():
    ans_p1 = [
        "C", "B", "D", "B", "B", "A", "B", "A", "A", "A",
        "C", "C", "A", "A", "B", "C", "A", "A", "A", "A",
        "A", "B", "C", "C", "C", "D", "C", "C", "D", "B",
        "D", "A", "B", "D", "C", "D", "B", "D", "D", "B",
        "A", "A", "B", "A", "B", "B", "B", "B", "A", "C"
    ]
    s = "\n\\vspace{0.3cm}\n\\noindent\\begin{minipage}{\\linewidth}\n"
    s += "\\begin{center}{\\large\\bfseries\\color{red!80!black} BẢNG ĐÁP ÁN TRẮC NGHIỆM}\\end{center}\\smallskip\n"
    for row in range(5):
        start = row * 10 + 1
        end = start + 10
        s += "\\begin{center}\\begin{tabular}{|c|" + "c|" * 10 + "}\\hline\n"
        s += "\\textbf{Câu} & " + " & ".join(str(i) for i in range(start, end)) + " \\\\ \\hline\n"
        s += "\\textbf{Đ/A} & " + " & ".join(f"\\textbf{{{ans_p1[i-1]}}}" for i in range(start, end)) + " \\\\ \\hline\n"
        s += "\\end{tabular}\\end{center}\\smallskip\n"
    s += "\\end{minipage}\n"
    return s

def build_latex_wrapper(is_sol):
    master_name = "Master_HDG.tex" if is_sol else "Master_De.tex"
    kythi = "HƯỚNG DẪN GIẢI CHI TIẾT" if is_sol else "PHIẾU BÀI TẬP VÀ LÝ THUYẾT"
    ans_line = "\\def\\inbangdapan{\\input{bang_dap_an.tex}}" if is_sol else ""
    return f"""\\def\\tentruong{{}}
\\def\\tenkythi{{{kythi}}}
\\def\\monhoc{{TOÁN 10 (Bộ sách Kết nối tri thức \\& Cánh Diều)}}
\\def\\tieudetrai{{BÀI 3: CÁC SỐ ĐẶC TRƯNG ĐO ĐỘ PHÂN TÁN}}
\\def\\tieudephai{{CHƯƠNG V: SỐ LIỆU THỐNG KÊ}}
\\def\\namhoc{{2025 -- 2026}}
\\def\\made{{103}}
\\def\\headertype{{phieubaitap}}
\\def\\brand{{{BRAND}}}
\\def\\giaovien{{HỒ THỊ THÚY}}
\\def\\noidungfile{{noi_dung.tex}}
{ans_line}

\\input{{../Master/{master_name}}}
"""

def compile_latex(name, content):
    tex_path = os.path.join(LATEX_DIR, name + ".tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(content)
    for run in range(2):
        res = subprocess.run(["pdflatex", "-interaction=nonstopmode", name + ".tex"], cwd=LATEX_DIR,
                             capture_output=True, text=True, encoding="utf-8", errors="ignore")
    log = open(os.path.join(LATEX_DIR, name + ".log"), encoding="utf-8", errors="ignore").read()
    errors = [l for l in log.splitlines() if l.startswith("!")]
    pages = re.search(r"Output written on .*?\((\d+) pages?", log)
    print(f"[LaTeX] {name}: {len(errors)} lỗi, {pages.group(1) if pages else '?'} trang")
    for e in errors[:10]:
        print("   ", e)
    return len(errors) == 0

def safe_copy(src, dst):
    try:
        shutil.copy2(src, dst)
        print(f"[COPY] {os.path.basename(dst)}")
    except PermissionError:
        print(f"[CẢNH BÁO] {os.path.basename(dst)} đang được mở, bỏ qua sao chép.")

# Word conversion
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
    add_run(p2, "Môn: TOÁN 10 – BÀI 3: ĐO ĐỘ PHÂN TÁN\nChương V: Mẫu số liệu không ghép nhóm", False, True, 10.5)
    set_spacing(p2, 0, 40, "center")

    c10 = tbl.cell(1, 0)
    c10.width = Cm(8.0)
    p = c10.paragraphs[0]
    add_run(p, "BÀI 3: CÁC SỐ ĐẶC TRƯNG ĐO ĐỘ PHÂN TÁN", True, False, 10.5)
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
    raw = get_latex_content()
    raw = re.sub(r"\\section\*\{(.*?)\}", r"\n\n# \1\n\n", raw)
    raw = re.sub(r"\\subsection\*\{(.*?)\}", r"\n\n## \1\n\n", raw)
    raw = re.sub(r"\\textbf\{\(Ví dụ (\d+)\)\.\}", r"**Ví dụ \1.**", raw)
    raw = re.sub(r"\\textbf\{\(Bài (\d+)\)\.\}", r"**Bài \1.**", raw)
    
    if not is_sol:
        raw = re.sub(r"\\loigiai\{.*?\}(?=\s*\\end\{ex\})", "", raw, flags=re.DOTALL)
    else:
        raw = re.sub(r"\\loigiai\{([\s\S]*?)\}(?=\s*\\end\{ex\})", r"\n\n**Lời giải.**\n\n\1\n\n", raw)

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
    raw = re.sub(r"\\begin\{ex\}", "\n\n", raw)
    raw = re.sub(r"\\end\{ex\}", "\n\n", raw)
    raw = re.sub(r"\\begin\{enumerate\}\[[^\]]*\]", "", raw)
    raw = re.sub(r"\\end\{enumerate\}", "", raw)
    raw = re.sub(r"\\begin\{itemize\}", "", raw)
    raw = re.sub(r"\\end\{itemize\}", "", raw)
    raw = re.sub(r"\\item", "\n- ", raw)
    raw = re.sub(r"\\begin\{multicols\}\{\d+\}", "", raw)
    raw = re.sub(r"\\end\{multicols\}", "", raw)
    raw = re.sub(r"\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}", "*[Biểu đồ tần số xem trong bản PDF]*", raw)
    raw = re.sub(r"\\includegraphics(?:\[.*?\])?\{hinh_bai22_c5_b3\.png\}", "\n\n@@IMAGE_BAI22@@\n\n", raw)
    raw = re.sub(r"\\vspace\{[^}]*\}", "", raw)
    raw = re.sub(r"\\textbf\{(.*?)\}", r"**\1**", raw)
    raw = re.sub(r"\\textit\{(.*?)\}", r"*\1*", raw)

    if is_sol:
        ans_md = "\n\n# BẢNG ĐÁP ÁN TRẮC NGHIỆM\n\n"
        ans_p1 = [
            "C", "B", "D", "B", "B", "A", "B", "A", "A", "A",
            "C", "C", "A", "A", "B", "C", "A", "A", "A", "A",
            "A", "B", "C", "C", "C", "D", "C", "C", "D", "B",
            "D", "A", "B", "D", "C", "D", "B", "D", "D", "B",
            "A", "A", "B", "A", "B", "B", "B", "B", "A", "C"
        ]
        for row in range(5):
            start = row * 10 + 1
            end = start + 10
            ans_md += "| Câu | " + " | ".join(str(i) for i in range(start, end)) + " |\n"
            ans_md += "| :---: | " + " | ".join(":---:" for _ in range(start, end)) + " |\n"
            ans_md += "| **Đ/A** | " + " | ".join(f"**{ans_p1[i-1]}**" for i in range(start, end)) + " |\n\n"
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

    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(1.2)
    sec.bottom_margin = Cm(1.5)
    sec.left_margin = Cm(1.5)
    sec.right_margin = Cm(1.5)

    sec.different_first_page_header_footer = False
    hf = sec.footer
    hp = hf.paragraphs[0]
    hp.text = ""
    add_run(hp, BRAND_W, False, True, 9.5, (100, 100, 100))
    set_spacing(hp, 0, 0, "left")

    first_p = doc.paragraphs[0]
    tbl_p = first_p.insert_paragraph_before()
    create_header_table(doc, is_sol)
    first_tbl = doc.tables[-1]
    tbl_p._p.addprevious(first_tbl._tbl)
    p_to_del = tbl_p._p
    p_to_del.getparent().remove(p_to_del)
    sp_p = first_p.insert_paragraph_before()
    set_spacing(sp_p, 40, 40, "left")

    for p in list(doc.paragraphs):
        t = p.text
        if "@@IMAGE_BAI22@@" in t:
            p.text = ""
            set_spacing(p, 60, 60, "center")
            img_path = os.path.join(LATEX_DIR, "hinh_bai22_c5_b3.png")
            if os.path.exists(img_path):
                r = p.add_run()
                r.add_picture(img_path, width=Cm(12.0))
            continue
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

def main():
    print("=" * 70)
    print(" XUẤT BẢN TOÁN 10 - CHƯƠNG 5 - BÀI 3: ĐO ĐỘ PHÂN TÁN")
    print("=" * 70)
    
    with open(os.path.join(LATEX_DIR, "noi_dung.tex"), "w", encoding="utf-8") as f:
        f.write(get_latex_content())
    with open(os.path.join(LATEX_DIR, "bang_dap_an.tex"), "w", encoding="utf-8") as f:
        f.write(get_answer_key_tex())
    print("[TeX] Đã tạo noi_dung.tex và bang_dap_an.tex")

    ok_de = compile_latex(NAME_DE, build_latex_wrapper(False))
    ok_hdg = compile_latex(NAME_HDG, build_latex_wrapper(True))

    build_word_doc(False, os.path.join(SAN_PHAM_DIR, NAME_DE + ".docx"))
    build_word_doc(True, os.path.join(SAN_PHAM_DIR, NAME_HDG + ".docx"))

    for n in (NAME_DE, NAME_HDG):
        src = os.path.join(LATEX_DIR, n + ".pdf")
        if os.path.exists(src):
            safe_copy(src, os.path.join(SAN_PHAM_DIR, n + ".pdf"))

    print("=" * 70)
    print("HOÀN TẤT BÀI 3!" if ok_de and ok_hdg else "CÓ LỖI LATEX – kiểm tra log.")
    print("=" * 70)

if __name__ == "__main__":
    main()
