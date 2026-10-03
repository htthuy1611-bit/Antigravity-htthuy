import os
import sys
import subprocess
import docx
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

sys.path.append(os.path.dirname(__file__))
from bao_thang_core import (
    create_answer_box_table,
    format_doc_paragraph,
    insert_header_and_code,
    insert_section_header
)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
HINH_ANH_0102 = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", "Bao_Thang_3", "0102")
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
pandoc_exe = os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")

OUTPUT_DE_0102 = os.path.join(SAN_PHAM_DIR, "de-khao-sat-toan-12-nam-2026-2027-truong-thpt-bao-thang-3-lao-cai_De_0102.docx")
OUTPUT_HDG_0102 = os.path.join(SAN_PHAM_DIR, "de-khao-sat-toan-12-nam-2026-2027-truong-thpt-bao-thang-3-lao-cai_HDG_0102.docx")

# =========================================================================
# 1. TEX MÃ ĐỀ 0102 - ĐỀ BÀI HỌC SINH
# =========================================================================
tex_de_0102 = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage[top=1.6cm,bottom=1.6cm,left=2.0cm,right=1.5cm]{geometry}

\begin{document}

@@DOCUMENT_HEADER@@

@@SECTION_1_HEADER@@

% Câu 1 (BBT)
\textbf{Câu 1.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây.

@@CENTER_IMAGE_c1_bbt@@

Khoảng nào sau đây là một khoảng đồng biến của hàm số?

@@TAB@@\textbf{A.} $(-\infty; -2)$.@@TAB@@\textbf{B.} $(-2; 1)$.@@TAB@@\textbf{C.} $(-2; +\infty)$.@@TAB@@\textbf{D.} $(-\infty; 1)$.

% Câu 2
\textbf{Câu 2.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = 3(x + 1)(x - 3)$ với mọi $x \in \mathbb{R}$. Điểm cực tiểu của hàm số đã cho là

@@TAB@@\textbf{A.} $x = -1$.@@TAB@@\textbf{B.} $x = 0$.@@TAB@@\textbf{C.} $x = 9$.@@TAB@@\textbf{D.} $x = 3$.

% Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{2x - 3}{x + 2}$. Đường tiệm cận đứng của đồ thị là

@@TAB@@\textbf{A.} $x = 2$.@@TAB@@\textbf{B.} $x = -2$.@@TAB@@\textbf{C.} $y = 2$.@@TAB@@\textbf{D.} $y = -2$.

% Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{3x + 1}{x - 2}$. Đường tiệm cận ngang của đồ thị là

@@TAB@@\textbf{A.} $y = -2$.@@TAB@@\textbf{B.} $x = 3$.@@TAB@@\textbf{C.} $y = 3$.@@TAB@@\textbf{D.} $y = 1$.

% Câu 5
\textbf{Câu 5.} Cho hàm số $y = x - 1 + \dfrac{2}{x - 1}$. Phương trình đường tiệm cận xiên của đồ thị hàm số là

@@TAB@@\textbf{A.} $y = x + 1$.@@TAB@@\textbf{B.} $y = -x + 1$.@@TAB@@\textbf{C.} $x = 1$.@@TAB@@\textbf{D.} $y = x - 1$.

% Câu 6
\textbf{Câu 6.} Đồ thị hàm số $y = 2 + \dfrac{4}{x - 1}$ có tâm đối xứng là

@@TAB@@\textbf{A.} $I(1; 2)$.@@TAB@@\textbf{B.} $I(2; 1)$.@@TAB@@\textbf{C.} $I(-1; 2)$.@@TAB@@\textbf{D.} $I(1; -2)$.

% Câu 7
\textbf{Câu 7.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x + 2)(x - 1)^2(x - 3)$ với mọi $x \in \mathbb{R}$. Số điểm cực trị của hàm số là

@@TAB@@\textbf{A.} $2$.@@TAB@@\textbf{B.} $1$.@@TAB@@\textbf{C.} $3$.@@TAB@@\textbf{D.} $4$.

% Câu 8
\textbf{Câu 8.} Cho hàm số $y = x + 2 - \dfrac{1}{x + 1}$. Giao điểm hai đường tiệm cận của đồ thị hàm số là

@@TAB@@\textbf{A.} $I(1; 3)$.@@TAB@@\textbf{B.} $I(-1; -2)$.@@TAB@@\textbf{C.} $I(1; -1)$.@@TAB@@\textbf{D.} $I(-1; 1)$.

% Câu 9
\textbf{Câu 9.} Cho hàm số $y = f(x) = x^3 - 3x$. Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số có đúng một điểm cực trị.

@@TAB@@\textbf{B.} Hàm số có cực đại tại $x = -1$ và cực tiểu tại $x = 1$.

@@TAB@@\textbf{C.} Hàm số nghịch biến trên $(-\infty; -1)$.

@@TAB@@\textbf{D.} Tâm đối xứng của đồ thị là $I(1; 0)$.

% Câu 10 (BBT)
\textbf{Câu 10.} Cho hàm số phân thức $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_c10_hinh@@

Hàm số nào dưới đây có bảng biến thiên đã cho?

@@TAB@@\textbf{A.} $y = \dfrac{2x - 5}{x - 1}$.@@TAB@@\textbf{B.} $y = \dfrac{x + 1}{x - 1}$.@@TAB@@\textbf{C.} $y = \dfrac{2x + 1}{x - 1}$.@@TAB@@\textbf{D.} $y = \dfrac{2x + 1}{x + 1}$.

% Câu 11 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_C11@@

\textbf{Câu 11.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Hàm số nào dưới đây có đồ thị như hình đã cho?

@@TAB@@\textbf{A.} $y = -x^3 + 3x$.@@TAB@@\textbf{B.} $y = x^3 - 3x$.

@@TAB@@\textbf{C.} $y = x^3 + 3x$.@@TAB@@\textbf{D.} $y = x^3 - 3x + 1$.

@@END_SIDE_BY_SIDE_C11@@

% Câu 12 (BBT)
\textbf{Câu 12.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây.

@@CENTER_IMAGE_c12_bbt@@

Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số nghịch biến trên $(-\infty; -1)$.

@@TAB@@\textbf{B.} Hàm số có cực trị tại $x = -1$.

@@TAB@@\textbf{C.} Hàm số đồng biến trên từng khoảng $(-\infty; -1)$ và $(-1; +\infty)$.

@@TAB@@\textbf{D.} Đồ thị không có tiệm cận ngang.

@@SECTION_2_HEADER@@

% Phần 2 Câu 1 (BBT)
\textbf{Câu 1.} Cho hàm số $y = f(x) = x^3 - 3x^2 + 2$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $f'(x) = 3x(x - 2)$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên khoảng $(0; 2)$.

@@TAB@@\textbf{c)} Hàm số đạt cực đại tại $x = 2$.

@@TAB@@\textbf{d)} Bảng biến thiên dưới đây là bảng biến thiên của hàm số đã cho.

@@CENTER_IMAGE_p2_c1_bbt@@

% Phần 2 Câu 2
\textbf{Câu 2.} Cho hàm số $y = \dfrac{x + 3}{x - 1}$ có đạo hàm $y' = -\dfrac{4}{(x - 1)^2}$ với mọi $x \ne 1$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định là $\mathbb{R} \setminus \{1\}$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên khoảng $(1; +\infty)$.

@@TAB@@\textbf{c)} Đồ thị nhận điểm $I(1; 1)$ làm tâm đối xứng.

@@TAB@@\textbf{d)} Hai đường thẳng $y = x$ và $y = -x + 2$ là hai trục đối xứng của đồ thị.

% Phần 2 Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{(x - 2)^2 + 1}{x - 2}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đồ thị có tiệm cận đứng $x = 2$.

@@TAB@@\textbf{b)} Đồ thị có tiệm cận xiên $y = x + 2$.

@@TAB@@\textbf{c)} Hàm số có đúng hai điểm cực trị.

@@TAB@@\textbf{d)} Hàm số nghịch biến trên khoảng $(1; 3)$.

% Phần 2 Câu 4 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_P2C4@@

\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2 - 2x + 2}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $y' = \dfrac{x(x - 2)}{(x - 1)^2}$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên khoảng $(0; 1)$.

@@TAB@@\textbf{c)} Đồ thị có tiệm cận xiên $y = x + 1$.

@@TAB@@\textbf{d)} Hình bên là đồ thị của hàm số đã cho.

@@END_SIDE_BY_SIDE_P2C4@@

@@SECTION_3_HEADER@@

% Phần 3 Câu 1
\textbf{Câu 1.} Cho hàm số $y = f(x) = x^3 + 3x^2 - 24x + 1$. Tính tổng các giá trị của $x$ tại đó hàm số đạt cực trị.

@@ANSWER_BOX_1@@

% Phần 3 Câu 2
\textbf{Câu 2.} Cho hàm số $y = \dfrac{3x - 2}{x + 1}$. Gọi $I(a; b)$ là giao điểm hai đường tiệm cận. Tính $ab$.

@@ANSWER_BOX_2@@

% Phần 3 Câu 3 (BBT)
\textbf{Câu 3.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_p3_c3_bbt@@

Tính hiệu giữa giá trị cực đại và giá trị cực tiểu của hàm số.

@@ANSWER_BOX_3@@

% Phần 3 Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2 + 2x + 5}{x + 1}$. Tính hoành độ giao điểm của hai đường tiệm cận của đồ thị.

@@ANSWER_BOX_4@@

% Phần 3 Câu 5
\textbf{Câu 5.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x - 2)^2(x + 1)(x - 4)$ với mọi $x \in \mathbb{R}$. Hàm số có bao nhiêu điểm cực trị?

@@ANSWER_BOX_5@@

% Phần 3 Câu 6
\textbf{Câu 6.} Cho hàm số $y = \dfrac{mx + 3}{2x - 1}$ có tiệm cận ngang $y = 2$. Tính $m$.

@@ANSWER_BOX_6@@

\vspace{0.4cm}
\begin{center}
\textbf{------ HẾT ------}
\end{center}

\end{document}
"""

# =========================================================================
# 2. TEX MÃ ĐỀ 0102 - HƯỚNG DẪN GIẢI CHI TIẾT
# =========================================================================
tex_hdg_0102 = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage[top=1.6cm,bottom=1.6cm,left=2.0cm,right=1.5cm]{geometry}

\begin{document}

@@DOCUMENT_HEADER@@

@@SECTION_1_HEADER@@

% Câu 1
\textbf{Câu 1.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây.

@@CENTER_IMAGE_c1_bbt@@

Khoảng nào sau đây là một khoảng đồng biến của hàm số?

@@TAB@@\textbf{A.} $(-\infty; -2)$.@@TAB@@\textbf{B.} $(-2; 1)$.@@TAB@@\textbf{C.} $(-2; +\infty)$.@@TAB@@\textbf{D.} $(-\infty; 1)$.

\textbf{Lời giải.} Theo bảng biến thiên, đạo hàm $f'(x) > 0$ trên $(-\infty; -2)$ và $(1; +\infty)$. Do đó hàm số đồng biến trên $(-\infty; -2)$.

\textbf{==> Chọn đáp án A.}

% Câu 2
\textbf{Câu 2.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = 3(x + 1)(x - 3)$ với mọi $x \in \mathbb{R}$. Điểm cực tiểu của hàm số đã cho là

@@TAB@@\textbf{A.} $x = -1$.@@TAB@@\textbf{B.} $x = 0$.@@TAB@@\textbf{C.} $x = 9$.@@TAB@@\textbf{D.} $x = 3$.

\textbf{Lời giải.} $f'(x) = 0 \iff x = -1$ hoặc $x = 3$. Qua $x = 3$, $f'(x)$ đổi dấu từ âm sang dương nên $x = 3$ là điểm cực tiểu của hàm số.

\textbf{==> Chọn đáp án D.}

% Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{2x - 3}{x + 2}$. Đường tiệm cận đứng của đồ thị là

@@TAB@@\textbf{A.} $x = 2$.@@TAB@@\textbf{B.} $x = -2$.@@TAB@@\textbf{C.} $y = 2$.@@TAB@@\textbf{D.} $y = -2$.

\textbf{Lời giải.} Nghiệm của mẫu số là $x = -2$, do đó đường tiệm cận đứng là $x = -2$.

\textbf{==> Chọn đáp án B.}

% Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{3x + 1}{x - 2}$. Đường tiệm cận ngang của đồ thị là

@@TAB@@\textbf{A.} $y = -2$.@@TAB@@\textbf{B.} $x = 3$.@@TAB@@\textbf{C.} $y = 3$.@@TAB@@\textbf{D.} $y = 1$.

\textbf{Lời giải.} $\lim_{x \to \pm \infty} \dfrac{3x + 1}{x - 2} = 3 \implies$ đường tiệm cận ngang là $y = 3$.

\textbf{==> Chọn đáp án C.}

% Câu 5
\textbf{Câu 5.} Cho hàm số $y = x - 1 + \dfrac{2}{x - 1}$. Phương trình đường tiệm cận xiên của đồ thị hàm số là

@@TAB@@\textbf{A.} $y = x + 1$.@@TAB@@\textbf{B.} $y = -x + 1$.@@TAB@@\textbf{C.} $x = 1$.@@TAB@@\textbf{D.} $y = x - 1$.

\textbf{Lời giải.} Vì $\lim_{x \to \pm \infty} \left[ y - (x - 1) \right] = \lim_{x \to \pm \infty} \dfrac{2}{x - 1} = 0 \implies$ tiệm cận xiên là $y = x - 1$.

\textbf{==> Chọn đáp án D.}

% Câu 6
\textbf{Câu 6.} Đồ thị hàm số $y = 2 + \dfrac{4}{x - 1}$ có tâm đối xứng là

@@TAB@@\textbf{A.} $I(1; 2)$.@@TAB@@\textbf{B.} $I(2; 1)$.@@TAB@@\textbf{C.} $I(-1; 2)$.@@TAB@@\textbf{D.} $I(1; -2)$.

\textbf{Lời giải.} Giao điểm hai đường tiệm cận $x = 1$ và $y = 2$ là điểm $I(1; 2)$, đây là tâm đối xứng của hyperbol.

\textbf{==> Chọn đáp án A.}

% Câu 7
\textbf{Câu 7.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x + 2)(x - 1)^2(x - 3)$ với mọi $x \in \mathbb{R}$. Số điểm cực trị của hàm số là

@@TAB@@\textbf{A.} $2$.@@TAB@@\textbf{B.} $1$.@@TAB@@\textbf{C.} $3$.@@TAB@@\textbf{D.} $4$.

\textbf{Lời giải.} $f'(x)$ đổi dấu khi qua các nghiệm bội lẻ $x = -2$ và $x = 3$. Không đổi dấu qua nghiệm bội chẵn $x = 1$. Vậy hàm số có 2 điểm cực trị.

\textbf{==> Chọn đáp án A.}

% Câu 8
\textbf{Câu 8.} Cho hàm số $y = x + 2 - \dfrac{1}{x + 1}$. Giao điểm hai đường tiệm cận của đồ thị hàm số là

@@TAB@@\textbf{A.} $I(1; 3)$.@@TAB@@\textbf{B.} $I(-1; -2)$.@@TAB@@\textbf{C.} $I(1; -1)$.@@TAB@@\textbf{D.} $I(-1; 1)$.

\textbf{Lời giải.} Tiệm cận đứng $x = -1$, tiệm cận xiên $y = x + 2$. Thay $x = -1 \implies y = 1$. Giao điểm là $I(-1; 1)$.

\textbf{==> Chọn đáp án D.}

% Câu 9
\textbf{Câu 9.} Cho hàm số $y = f(x) = x^3 - 3x$. Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số có đúng một điểm cực trị.

@@TAB@@\textbf{B.} Hàm số có cực đại tại $x = -1$ và cực tiểu tại $x = 1$.

@@TAB@@\textbf{C.} Hàm số nghịch biến trên $(-\infty; -1)$.

@@TAB@@\textbf{D.} Tâm đối xứng của đồ thị là $I(1; 0)$.

\textbf{Lời giải.} Đạo hàm $y' = 3x^2 - 3 = 0 \iff x = \pm 1$. Đạo hàm đổi dấu từ $+$ sang $-$ qua $x = -1$ (cực đại) và từ $-$ sang $+$ qua $x = 1$ (cực tiểu).

\textbf{==> Chọn đáp án B.}

% Câu 10
\textbf{Câu 10.} Cho hàm số phân thức $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_c10_hinh@@

Hàm số nào dưới đây có bảng biến thiên đã cho?

@@TAB@@\textbf{A.} $y = \dfrac{2x - 5}{x - 1}$.@@TAB@@\textbf{B.} $y = \dfrac{x + 1}{x - 1}$.@@TAB@@\textbf{C.} $y = \dfrac{2x + 1}{x - 1}$.@@TAB@@\textbf{D.} $y = \dfrac{2x + 1}{x + 1}$.

\textbf{Lời giải.} Tiệm cận đứng $x = 1$, tiệm cận ngang $y = 2$. Hàm số nghịch biến nên $y' < 0$. Xét $y = \dfrac{2x - 5}{x - 1} \implies y' = \dfrac{2(-1) - (-5)}{(x - 1)^2} = \dfrac{3}{(x - 1)^2} > 0$. Còn với BBT mang dấu $-$ ta có $ad - bc < 0$, đáp án phù hợp là $y = \dfrac{2x - 5}{x - 1}$.

\textbf{==> Chọn đáp án A.}

% Câu 11
@@START_SIDE_BY_SIDE_C11@@

\textbf{Câu 11.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Hàm số nào dưới đây có đồ thị như hình đã cho?

@@TAB@@\textbf{A.} $y = -x^3 + 3x$.@@TAB@@\textbf{B.} $y = x^3 - 3x$.

@@TAB@@\textbf{C.} $y = x^3 + 3x$.@@TAB@@\textbf{D.} $y = x^3 - 3x + 1$.

\textbf{Lời giải.} Nhánh ngoài cùng bên phải đi lên nên hệ số $a > 0$. Đồ thị đi qua gốc tọa độ $O(0; 0)$ và có điểm cực trị $(-1; 2)$ và $(1; -2)$. Vậy hàm số là $y = x^3 - 3x$.

\textbf{==> Chọn đáp án B.}

@@END_SIDE_BY_SIDE_C11@@

% Câu 12
\textbf{Câu 12.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây.

@@CENTER_IMAGE_c12_bbt@@

Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số nghịch biến trên $(-\infty; -1)$.

@@TAB@@\textbf{B.} Hàm số có cực trị tại $x = -1$.

@@TAB@@\textbf{C.} Hàm số đồng biến trên từng khoảng $(-\infty; -1)$ và $(-1; +\infty)$.

@@TAB@@\textbf{D.} Đồ thị không có tiệm cận ngang.

\textbf{Lời giải.} Theo bảng biến thiên, đạo hàm luôn mang dấu dương $+$ trên $(-\infty; -1)$ và $(-1; +\infty)$. Do đó hàm số đồng biến trên từng khoảng $(-\infty; -1)$ và $(-1; +\infty)$.

\textbf{==> Chọn đáp án C.}

@@SECTION_2_HEADER@@

% Phần 2 Câu 1
\textbf{Câu 1.} Cho hàm số $y = f(x) = x^3 - 3x^2 + 2$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $f'(x) = 3x(x - 2)$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên khoảng $(0; 2)$.

@@TAB@@\textbf{c)} Hàm số đạt cực đại tại $x = 2$.

@@TAB@@\textbf{d)} Bảng biến thiên dưới đây là bảng biến thiên của hàm số đã cho.

@@CENTER_IMAGE_p2_c1_bbt@@

\textbf{Lời giải.}

- Ý a) Đúng: $f'(x) = 3x^2 - 6x = 3x(x - 2)$.

- Ý b) Đúng: $f'(x) < 0 \iff x \in (0; 2)$.

- Ý c) Sai: Hàm số đạt cực đại tại $x = 0$ và đạt cực tiểu tại $x = 2$.

- Ý d) Sai: Tại $x = 2$, giá trị cực tiểu là $f(2) = 2^3 - 3(2)^2 + 2 = -2$, nhưng mũi tên ở bảng biến thiên không khớp dấu.

\textbf{==> Đáp án: a) Đúng | b) Đúng | c) Sai | d) Sai.}

% Phần 2 Câu 2
\textbf{Câu 2.} Cho hàm số $y = \dfrac{x + 3}{x - 1}$ có đạo hàm $y' = -\dfrac{4}{(x - 1)^2}$ với mọi $x \ne 1$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định là $\mathbb{R} \setminus \{1\}$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên khoảng $(1; +\infty)$.

@@TAB@@\textbf{c)} Đồ thị nhận điểm $I(1; 1)$ làm tâm đối xứng.

@@TAB@@\textbf{d)} Hai đường thẳng $y = x$ và $y = -x + 2$ là hai trục đối xứng của đồ thị.

\textbf{Lời giải.}

- Ý a) Đúng: Mẫu số khác 0 khi $x \ne 1$.

- Ý b) Sai: $y' < 0$ nên hàm số nghịch biến trên $(1; +\infty)$.

- Ý c) Đúng: Giao điểm hai tiệm cận là $I(1; 1)$, đây là tâm đối xứng.

- Ý d) Đúng: Hai trục đối xứng có phương trình $y - 1 = \pm(x - 1) \implies y = x$ và $y = -x + 2$.

\textbf{==> Đáp án: a) Đúng | b) Sai | c) Đúng | d) Đúng.}

% Phần 2 Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{(x - 2)^2 + 1}{x - 2}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đồ thị có tiệm cận đứng $x = 2$.

@@TAB@@\textbf{b)} Đồ thị có tiệm cận xiên $y = x + 2$.

@@TAB@@\textbf{c)} Hàm số có đúng hai điểm cực trị.

@@TAB@@\textbf{d)} Hàm số nghịch biến trên khoảng $(1; 3)$.

\textbf{Lời giải.}

- Ý a) Đúng: Mẫu triệt tiêu tại $x = 2$.

- Ý b) Sai: $y = x - 2 + \dfrac{1}{x - 2} \implies$ tiệm cận xiên là $y = x - 2$.

- Ý c) Đúng: $y' = 1 - \dfrac{1}{(x - 2)^2} = 0 \iff x = 1$ hoặc $x = 3$.

- Ý d) Đúng: Hàm số nghịch biến trên $(1; 2)$ và $(2; 3)$.

\textbf{==> Đáp án: a) Đúng | b) Sai | c) Đúng | d) Đúng.}

% Phần 2 Câu 4
@@START_SIDE_BY_SIDE_P2C4@@

\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2 - 2x + 2}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $y' = \dfrac{x(x - 2)}{(x - 1)^2}$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên khoảng $(0; 1)$.

@@TAB@@\textbf{c)} Đồ thị có tiệm cận xiên $y = x + 1$.

@@TAB@@\textbf{d)} Hình bên là đồ thị của hàm số đã cho.

\textbf{Lời giải.}

- Ý a) Đúng: Đạo hàm chuẩn $y' = \dfrac{(2x - 2)(x - 1) - (x^2 - 2x + 2)}{(x - 1)^2} = \dfrac{x^2 - 2x}{(x - 1)^2} = \dfrac{x(x - 2)}{(x - 1)^2}$.

- Ý b) Sai: $x \in (0; 1) \implies x > 0, x - 2 < 0 \implies y' < 0$ (nghịch biến), đúng quy tắc.

- Ý c) Sai: $y = x - 1 + \dfrac{1}{x - 1} \implies$ tiệm cận xiên là $y = x - 1$.

- Ý d) Đúng: Đồ thị hàm số phân thức bậc hai trên bậc nhất với tiệm cận đứng $x = 1$.

\textbf{==> Đáp án: a) Đúng | b) Sai | c) Sai | d) Đúng.}

@@END_SIDE_BY_SIDE_P2C4@@

@@SECTION_3_HEADER@@

% Phần 3 Câu 1
\textbf{Câu 1.} Cho hàm số $y = f(x) = x^3 + 3x^2 - 24x + 1$. Tính tổng các giá trị của $x$ tại đó hàm số đạt cực trị.

\textbf{Lời giải.} Đạo hàm $f'(x) = 3x^2 + 6x - 24 = 3(x^2 + 2x - 8) = 0 \iff x = 2$ hoặc $x = -4$. Tổng các điểm cực trị là $2 + (-4) = -2$.

\textbf{==> Đáp án: -2.}

% Phần 3 Câu 2
\textbf{Câu 2.} Cho hàm số $y = \dfrac{3x - 2}{x + 1}$. Gọi $I(a; b)$ là giao điểm hai đường tiệm cận. Tính $ab$.

\textbf{Lời giải.} Tiệm cận đứng $x = -1 \implies a = -1$. Tiệm cận ngang $y = 3 \implies b = 3$. Tích $ab = (-1) \cdot 3 = -3$.

\textbf{==> Đáp án: -3.}

% Phần 3 Câu 3
\textbf{Câu 3.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_p3_c3_bbt@@

Tính hiệu giữa giá trị cực đại và giá trị cực tiểu của hàm số.

\textbf{Lời giải.} Giá trị cực đại là $y_{CĐ} = 5$, giá trị cực tiểu là $y_{CT} = -4$. Hiệu cần tìm là $5 - (-4) = 9$.

\textbf{==> Đáp án: 9.}

% Phần 3 Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2 + 2x + 5}{x + 1}$. Tính hoành độ giao điểm của hai đường tiệm cận của đồ thị.

\textbf{Lời giải.} Đường tiệm cận đứng là $x = -1$. Mọi điểm nằm trên đường tiệm cận đứng đều có hoành độ bằng $-1$. Do đó giao điểm của hai tiệm cận có hoành độ là $-1$.

\textbf{==> Đáp án: -1.}

% Phần 3 Câu 5
\textbf{Câu 5.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x - 2)^2(x + 1)(x - 4)$ với mọi $x \in \mathbb{R}$. Hàm số có bao nhiêu điểm cực trị?

\textbf{Lời giải.} $f'(x)$ đổi dấu qua hai nghiệm đơn $x = -1$ và $x = 4$. Nghiệm $x = 2$ là nghiệm bội chẵn nên $f'(x)$ không đổi dấu. Vậy hàm số có 2 điểm cực trị.

\textbf{==> Đáp án: 2.}

% Phần 3 Câu 6
\textbf{Câu 6.} Cho hàm số $y = \dfrac{mx + 3}{2x - 1}$ có tiệm cận ngang $y = 2$. Tính $m$.

\textbf{Lời giải.} Tiệm cận ngang của đồ thị là $y = \dfrac{m}{2}$. Theo đề bài ta có $\dfrac{m}{2} = 2 \implies m = 4$.

\textbf{==> Đáp án: 4.}

\vspace{0.4cm}
\begin{center}
\textbf{------ HẾT ------}
\end{center}

\end{document}
"""

def build_0102_doc(tex_str, output_path, is_solution=False):
    temp_tex = os.path.join(CURRENT_DIR, f"temp_0102_{'hdg' if is_solution else 'de'}.tex")
    temp_docx = os.path.join(CURRENT_DIR, f"temp_0102_{'hdg' if is_solution else 'de'}.docx")
    
    with open(temp_tex, "w", encoding="utf-8") as f:
        f.write(tex_str)
        
    print(f"[*] Đang xuất bản: {os.path.basename(output_path)}...")
    subprocess.run([pandoc_exe, temp_tex, "-o", temp_docx], check=True)
    
    doc = docx.Document(temp_docx)
    
    for s in doc.sections:
        s.top_margin = Cm(1.6)
        s.bottom_margin = Cm(1.6)
        s.left_margin = Cm(2.0)
        s.right_margin = Cm(1.5)
        s.page_width = Cm(21.0)
        s.page_height = Cm(29.7)
        
        footer = s.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_p.text = ""
        r_l = f_p.add_run("Lớp Toán Cô Thúy  •  SĐT: 0935.322.328  •  50/2C Phạm Thị Liên                                   ")
        r_l.font.name = "Times New Roman"
        r_l.font.size = Pt(9.5)
        r_l.italic = True
        r_l.font.color.rgb = RGBColor(100, 100, 100)
        
        r_r = f_p.add_run("Trang Mã đề 0102")
        r_r.font.name = "Times New Roman"
        r_r.font.size = Pt(9.5)
        r_r.italic = True
        r_r.font.color.rgb = RGBColor(80, 80, 80)
        
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.font.color.rgb = RGBColor(0, 0, 0)
    
    for p in list(doc.paragraphs):
        if "@@DOCUMENT_HEADER@@" in p.text:
            insert_header_and_code(doc, p, "0102", is_solution)
        elif "@@SECTION_1_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn.", "Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.")
        elif "@@SECTION_2_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN II. Câu trắc nghiệm đúng sai.", "Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")
        elif "@@SECTION_3_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN III. Câu trắc nghiệm yêu cầu trả lời ngắn.", "Thí sinh trả lời từ câu 1 đến câu 6.")
            
    # Side-by-side
    sbs_configs = [
        ("C11", "c11_hinh.png", 5.0),
        ("P2C4", "p2_c4_hinh.png", 4.8),
    ]
    for tag, img_name, img_w in sbs_configs:
        start_tag = f"@@START_SIDE_BY_SIDE_{tag}@@"
        end_tag = f"@@END_SIDE_BY_SIDE_{tag}@@"
        start_p, end_p, inner_ps = None, None, []
        found = False
        for p in doc.paragraphs:
            if start_tag in p.text:
                start_p = p; found = True; continue
            if end_tag in p.text:
                end_p = p; found = False; continue
            if found:
                inner_ps.append(p)
                
        if start_p and end_p:
            tbl = doc.add_table(rows=1, cols=2)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            
            tblPr = tbl._tbl.tblPr
            for look in tblPr.findall(qn('w:tblLook')): tblPr.remove(look)
            tblLook = parse_xml(r'<w:tblLook %s w:val="0000" w:firstRow="0" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/>' % nsdecls('w'))
            for b in tblPr.findall(qn('w:tblBorders')): tblPr.remove(b)
            tblBorders = parse_xml(
                r'<w:tblBorders %s>'
                r'<w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/>'
                r'<w:insideH w:val="none"/><w:insideV w:val="none"/>'
                r'</w:tblBorders>' % nsdecls('w')
            )
            tblPr.append(tblBorders)
            tblPr.append(tblLook)
            
            cell_0 = tbl.rows[0].cells[0]
            cell_1 = tbl.rows[0].cells[1]
            cell_0.width = Cm(11.8)
            cell_1.width = Cm(5.7)
            cell_0.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell_1.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            for c in [cell_0, cell_1]:
                tcPr = c._tc.get_or_add_tcPr()
                for b in tcPr.findall(qn('w:tcBorders')): tcPr.remove(b)
                tcPr.append(parse_xml(
                    r'<w:tcBorders %s><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/></w:tcBorders>' % nsdecls('w')
                ))
                
            start_p._p.addprevious(tbl._tbl)
            cell_0._tc.remove(cell_0.paragraphs[0]._p)
            for p in inner_ps:
                cell_0._tc.append(p._p)
                
            img_path = os.path.join(HINH_ANH_0102, img_name)
            cell_1_p = cell_1.paragraphs[0]
            cell_1_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cell_1_p.paragraph_format.space_before = Pt(0)
            cell_1_p.paragraph_format.space_after = Pt(0)
            if os.path.exists(img_path):
                cell_1_p.add_run().add_picture(img_path, width=Cm(img_w))
                
            start_p._p.getparent().remove(start_p._p)
            end_p._p.getparent().remove(end_p._p)
            
    # Images & Boxes
    for p in list(doc.paragraphs):
        for img_tag in ["c1_bbt", "c10_hinh", "c12_bbt", "p2_c1_bbt", "p3_c3_bbt"]:
            token = f"@@CENTER_IMAGE_{img_tag}@@"
            if token in p.text:
                img_path = os.path.join(HINH_ANH_0102, f"{img_tag}.png")
                p.text = ""
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                if os.path.exists(img_path):
                    p.add_run().add_picture(img_path, width=Cm(9.5))
                break
                
        if not is_solution:
            for num in range(1, 7):
                tag = f"@@ANSWER_BOX_{num}@@"
                if tag in p.text:
                    box_tbl = create_answer_box_table(doc)
                    p._p.addprevious(box_tbl._tbl)
                    p._p.getparent().remove(p._p)
                    break
                    
    for p in list(doc.paragraphs):
        format_doc_paragraph(p, inside_table_cell=False)
        if is_solution:
            p_text = p.text.strip()
            if "==> Chọn đáp án" in p_text or "==> Đáp án:" in p_text:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(8)
                for r in p.runs:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(192, 0, 0)
                    
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in list(cell.paragraphs):
                    format_doc_paragraph(p, inside_table_cell=True)
                    if is_solution:
                        p_text = p.text.strip()
                        if "==> Chọn đáp án" in p_text or "==> Đáp án:" in p_text:
                            for r in p.runs:
                                r.font.bold = True
                                r.font.color.rgb = RGBColor(192, 0, 0)
                                
    for s in doc.styles:
        if s.type == docx.enum.style.WD_STYLE_TYPE.TABLE:
            for child in list(s._element):
                if child.tag.endswith('tblStylePr'):
                    s._element.remove(child)
                    
    settings = doc.settings.element
    compat = parse_xml(
        r'<w:compat %s><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat>' % nsdecls('w')
    )
    settings.append(compat)
    
    doc.save(output_path)
    print(f"[THÀNH CÔNG] Đã xuất bản: {output_path}")
    if os.path.exists(temp_tex): os.remove(temp_tex)
    if os.path.exists(temp_docx): os.remove(temp_docx)

if __name__ == "__main__":
    print("=== TIẾN HÀNH XUẤT BẢN MÃ ĐỀ 0102 (ĐỀ BÀI + LỜI GIẢI CHI TIẾT) ===")
    build_0102_doc(tex_de_0102, OUTPUT_DE_0102, is_solution=False)
    build_0102_doc(tex_hdg_0102, OUTPUT_HDG_0102, is_solution=True)
