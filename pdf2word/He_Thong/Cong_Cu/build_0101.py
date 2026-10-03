import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
import subprocess
import docx
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

sys.path.append(os.path.dirname(__file__))
from bao_thang_core import (
    create_answer_box_table,
    format_doc_paragraph,
    insert_header_and_code,
    insert_section_header
)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
HINH_ANH_0101 = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", "Bao_Thang_3", "0101")
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
pandoc_exe = os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")

OUTPUT_DE_0101 = os.path.join(SAN_PHAM_DIR, "de-khao-sat-toan-12-nam-2026-2027-truong-thpt-bao-thang-3-lao-cai_De_0101.docx")
OUTPUT_HDG_0101 = os.path.join(SAN_PHAM_DIR, "de-khao-sat-toan-12-nam-2026-2027-truong-thpt-bao-thang-3-lao-cai_HDG_0101.docx")

# =========================================================================
# 1. NỘI DUNG TEX MÃ ĐỀ 0101 - BẢN ĐỀ BÀI HỌC SINH
# =========================================================================
tex_de_0101 = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage[top=1.6cm,bottom=1.6cm,left=2.0cm,right=1.5cm]{geometry}

\begin{document}

@@DOCUMENT_HEADER@@

@@SECTION_1_HEADER@@

% Câu 1 (BBT)
\textbf{Câu 1.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c1_bbt@@

Giá trị cực đại của hàm số là

@@TAB@@\textbf{A.} $-1$.@@TAB@@\textbf{B.} $1$.@@TAB@@\textbf{C.} $4$.@@TAB@@\textbf{D.} $0$.

% Câu 2 (BBT)
\textbf{Câu 2.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c2_bbt@@

Điểm cực tiểu của hàm số đã cho là

@@TAB@@\textbf{A.} $x = 0$.@@TAB@@\textbf{B.} $x = 1$.@@TAB@@\textbf{C.} $x = 2$.@@TAB@@\textbf{D.} $x = 3$.

% Câu 3 (Side-by-side đồ thị phân thức)
@@START_SIDE_BY_SIDE_C3@@

\textbf{Câu 3.} Cho hàm số phân thức $y = \dfrac{ax^2 + bx + c}{px + q}$ ($a \ne 0, p \ne 0$, đa thức tử không chia hết cho đa thức mẫu) có đồ thị như hình bên. Đường tiệm cận xiên của đồ thị hàm số đã cho có phương trình là

@@TAB@@\textbf{A.} $y = x - 1$.@@TAB@@\textbf{B.} $y = -x + 1$.

@@TAB@@\textbf{C.} $y = x + 1$.@@TAB@@\textbf{D.} $y = 2$.

@@END_SIDE_BY_SIDE_C3@@

% Câu 4 (Side-by-side đồ thị nhất biến)
@@START_SIDE_BY_SIDE_C4@@

\textbf{Câu 4.} Cho hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có đồ thị như hình bên. Đường tiệm cận đứng của đồ thị hàm số đã cho có phương trình là

@@TAB@@\textbf{A.} $y = -1$.@@TAB@@\textbf{B.} $y = 1$.

@@TAB@@\textbf{C.} $x = 1$.@@TAB@@\textbf{D.} $x = -1$.

@@END_SIDE_BY_SIDE_C4@@

% Câu 5 (Side-by-side đồ thị bậc 3)
@@START_SIDE_BY_SIDE_C5@@

\textbf{Câu 5.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I(0; 1)$.@@TAB@@\textbf{B.} $I(1; 1)$.

@@TAB@@\textbf{C.} $I(1; 0)$.@@TAB@@\textbf{D.} $I(2; -1)$.

@@END_SIDE_BY_SIDE_C5@@

% Câu 6 (Side-by-side đồ thị nhất biến)
@@START_SIDE_BY_SIDE_C6@@

\textbf{Câu 6.} Cho hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có đồ thị như hình bên. Hàm số nào dưới đây có đồ thị như hình vẽ?

@@TAB@@\textbf{A.} $y = \dfrac{x + 1}{x + 2}$.@@TAB@@\textbf{B.} $y = \dfrac{x - 5}{x - 2}$.

@@TAB@@\textbf{C.} $y = \dfrac{x + 1}{x - 2}$.@@TAB@@\textbf{D.} $y = \dfrac{-x + 1}{x - 2}$.

@@END_SIDE_BY_SIDE_C6@@

% Câu 7 (Side-by-side đồ thị bậc 3)
@@START_SIDE_BY_SIDE_C7@@

\textbf{Câu 7.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Số điểm cực trị của hàm số là

@@TAB@@\textbf{A.} $0$.@@TAB@@\textbf{B.} $1$.@@TAB@@\textbf{C.} $2$.@@TAB@@\textbf{D.} $3$.

@@END_SIDE_BY_SIDE_C7@@

% Câu 8 (BBT nhất biến)
\textbf{Câu 8.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c8_bbt@@

Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số đồng biến trên khoảng $(-\infty; 2)$.

@@TAB@@\textbf{B.} Hàm số nghịch biến trên từng khoảng $(-\infty; 2)$ và $(2; +\infty)$.

@@TAB@@\textbf{C.} Hàm số đồng biến trên khoảng $(2; +\infty)$.

@@TAB@@\textbf{D.} Hàm số nghịch biến trên $(-\infty; +\infty)$.

% Câu 9 (BBT)
\textbf{Câu 9.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c9_bbt@@

Khoảng nào sau đây là một khoảng nghịch biến của hàm số?

@@TAB@@\textbf{A.} $(-\infty; 1)$.@@TAB@@\textbf{B.} $(1; 3)$.@@TAB@@\textbf{C.} $(1; 2)$.@@TAB@@\textbf{D.} $(3; +\infty)$.

% Câu 10 (Side-by-side đồ thị bậc 3)
@@START_SIDE_BY_SIDE_C10@@

\textbf{Câu 10.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Điểm cực tiểu của hàm số đã cho là

@@TAB@@\textbf{A.} $x = -1$.@@TAB@@\textbf{B.} $x = 0$.

@@TAB@@\textbf{C.} $x = 1$.@@TAB@@\textbf{D.} $x = 2$.

@@END_SIDE_BY_SIDE_C10@@

% Câu 11 (Side-by-side đồ thị nhất biến)
@@START_SIDE_BY_SIDE_C11@@

\textbf{Câu 11.} Cho hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có đồ thị như hình bên. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I(1; 2)$.@@TAB@@\textbf{B.} $I(2; 1)$.

@@TAB@@\textbf{C.} $I(-1; 2)$.@@TAB@@\textbf{D.} $I(2; -1)$.

@@END_SIDE_BY_SIDE_C11@@

% Câu 12 (Side-by-side đồ thị phân thức)
@@START_SIDE_BY_SIDE_C12@@

\textbf{Câu 12.} Cho hàm số phân thức $y = \dfrac{ax^2 + bx + c}{px + q}$ ($a \ne 0, p \ne 0$, đa thức tử không chia hết cho đa thức mẫu) có đồ thị như hình bên. Đường tiệm cận xiên $d$ của đồ thị có phương trình là

@@TAB@@\textbf{A.} $y = x + 1$.@@TAB@@\textbf{B.} $y = x - 1$.

@@TAB@@\textbf{C.} $y = -x - 1$.@@TAB@@\textbf{D.} $y = -1$.

@@END_SIDE_BY_SIDE_C12@@

@@SECTION_2_HEADER@@

% Phần 2 Câu 1 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_P2C1@@

\textbf{Câu 1.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên, trong đó điểm $I(0; 2)$ được đánh dấu. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Hàm số đồng biến trên khoảng $(-1; 1)$.

@@TAB@@\textbf{b)} Hàm số đạt cực đại tại điểm $x = -1$.

@@TAB@@\textbf{c)} Giá trị cực tiểu của hàm số bằng $0$.

@@TAB@@\textbf{d)} Điểm $I(0; 2)$ là tâm đối xứng của đồ thị.

@@END_SIDE_BY_SIDE_P2C1@@

% Phần 2 Câu 2 (3 hình)
\textbf{Câu 2.} Cho các biểu diễn như dưới đây. Trong đó, Hình 1 và bảng biến thiên lần lượt là đồ thị và bảng biến thiên của hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$); Hình 2 là đồ thị của hàm số $y = \dfrac{mx^2 + nx + p}{qx + r}$ ($mq \ne 0$, đa thức tử không chia hết cho đa thức mẫu).

@@CENTER_IMAGE_p2_c2_hinh_all@@

Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Ở Hình 1, đường tiệm cận đứng của đồ thị là $x = 1$.

@@TAB@@\textbf{b)} Ở Hình 1, cả $d_1$ và $d_2$ đều là trục đối xứng của đồ thị.

@@TAB@@\textbf{c)} Bảng biến thiên cho thấy hàm số nghịch biến trên từng khoảng $(-\infty; 1)$ và $(1; +\infty)$.

@@TAB@@\textbf{d)} Ở Hình 2, đường tiệm cận xiên $d$ có phương trình $y = x - 1$.

% Phần 2 Câu 3
\textbf{Câu 3.} Cho hàm số $y = f(x) = x^3 - 3x + 1$ có đạo hàm $f'(x) = 3(x + 1)(x - 1)$ với mọi $x \in \mathbb{R}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định của hàm số là $\mathbb{R}$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên từng khoảng $(-\infty; -1)$ và $(1; +\infty)$.

@@TAB@@\textbf{c)} Hàm số đạt cực tiểu tại $x = -1$.

@@TAB@@\textbf{d)} Giá trị cực tiểu của hàm số bằng $-1$.

% Phần 2 Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định của hàm số là $\mathbb{R} \setminus \{1\}$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên từng khoảng $(0; 1)$ và $(1; 2)$.

@@TAB@@\textbf{c)} Hàm số đạt cực tiểu tại $x = 0$.

@@TAB@@\textbf{d)} Đồ thị hàm số có đường tiệm cận xiên $y = x + 1$.

@@SECTION_3_HEADER@@

% Phần 3 Câu 1
\textbf{Câu 1.} Cho hàm số $y = f(x) = x^3 - 6x^2 + 9x + 1$ có đạo hàm $f'(x) = 3(x - 1)(x - 3)$ với mọi $x \in \mathbb{R}$. Tìm điểm cực đại của hàm số đã cho.

@@ANSWER_BOX_1@@

% Phần 3 Câu 2
\textbf{Câu 2.} Cho hàm số $y = g(x) = -x^3 + 3x + 2$ có đạo hàm $g'(x) = 3(1 - x^2)$ với mọi $x \in \mathbb{R}$. Giá trị cực đại của hàm số bằng bao nhiêu?

@@ANSWER_BOX_2@@

% Phần 3 Câu 3
\textbf{Câu 3.} Cho hàm số $y = f(x) = \dfrac{2x + 1}{x - 1}$ có đạo hàm $f'(x) = \dfrac{-3}{(x - 1)^2}$ với mọi $x \ne 1$. Trong hai khoảng $(-\infty; 1)$ và $(1; +\infty)$, hàm số nghịch biến trên bao nhiêu khoảng?

@@ANSWER_BOX_3@@

% Phần 3 Câu 4
\textbf{Câu 4.} Cho hàm số $y = f(x) = \dfrac{x^2}{x + 1}$ có đạo hàm $f'(x) = \dfrac{x(x + 2)}{(x + 1)^2}$ với mọi $x \ne -1$. Giá trị cực đại của hàm số bằng bao nhiêu?

@@ANSWER_BOX_4@@

% Phần 3 Câu 5
\textbf{Câu 5.} Cho hàm số $y = f(x) = x^3 - 3x^2 + 1$. Gọi $M$ và $m$ lần lượt là giá trị cực đại và giá trị cực tiểu của hàm số. Tính $M + m$.

@@ANSWER_BOX_5@@

% Phần 3 Câu 6
\textbf{Câu 6.} Cho hai hàm số $y = g(x) = \dfrac{2x + 1}{x - 1}$ và $y = h(x) = \dfrac{x^2 - x - 1}{x - 2}$. Gọi $a$ là tung độ tiệm cận ngang của đồ thị hàm số $g$, $b$ là hệ số tự do của tiệm cận xiên $y = x + b$ của đồ thị hàm số $h$. Tính $a + b$.

@@ANSWER_BOX_6@@

\vspace{0.4cm}
\begin{center}
\textbf{------ HẾT ------}
\end{center}

\end{document}
"""

# =========================================================================
# 2. NỘI DUNG TEX MÃ ĐỀ 0101 - BẢN HƯỚNG DẪN GIẢI CHI TIẾT
# =========================================================================
tex_hdg_0101 = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage[top=1.6cm,bottom=1.6cm,left=2.0cm,right=1.5cm]{geometry}

\begin{document}

@@DOCUMENT_HEADER@@

@@SECTION_1_HEADER@@

% Câu 1
\textbf{Câu 1.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c1_bbt@@

Giá trị cực đại của hàm số là

@@TAB@@\textbf{A.} $-1$.@@TAB@@\textbf{B.} $1$.@@TAB@@\textbf{C.} $4$.@@TAB@@\textbf{D.} $0$.

\textbf{Lời giải.} Theo bảng biến thiên, tại $x = -1$ hàm số đạt giá trị cực đại bằng $4$.

\textbf{==> Chọn đáp án C.}

% Câu 2
\textbf{Câu 2.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c2_bbt@@

Điểm cực tiểu của hàm số đã cho là

@@TAB@@\textbf{A.} $x = 0$.@@TAB@@\textbf{B.} $x = 1$.@@TAB@@\textbf{C.} $x = 2$.@@TAB@@\textbf{D.} $x = 3$.

\textbf{Lời giải.} Theo bảng biến thiên, hàm số đạt cực tiểu tại $x = 2$.

\textbf{==> Chọn đáp án C.}

% Câu 3
@@START_SIDE_BY_SIDE_C3@@

\textbf{Câu 3.} Cho hàm số phân thức $y = \dfrac{ax^2 + bx + c}{px + q}$ ($a \ne 0, p \ne 0$, đa thức tử không chia hết cho đa thức mẫu) có đồ thị như hình bên. Đường tiệm cận xiên của đồ thị hàm số đã cho có phương trình là

@@TAB@@\textbf{A.} $y = x - 1$.@@TAB@@\textbf{B.} $y = -x + 1$.

@@TAB@@\textbf{C.} $y = x + 1$.@@TAB@@\textbf{D.} $y = 2$.

\textbf{Lời giải.} Theo hình vẽ, đường thẳng nét đứt xiên đi qua $(-1; 0)$ và $(0; 1)$, nên có phương trình $y = x + 1$.

\textbf{==> Chọn đáp án C.}

@@END_SIDE_BY_SIDE_C3@@

% Câu 4
@@START_SIDE_BY_SIDE_C4@@

\textbf{Câu 4.} Cho hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có đồ thị như hình bên. Đường tiệm cận đứng của đồ thị hàm số đã cho có phương trình là

@@TAB@@\textbf{A.} $y = -1$.@@TAB@@\textbf{B.} $y = 1$.

@@TAB@@\textbf{C.} $x = 1$.@@TAB@@\textbf{D.} $x = -1$.

\textbf{Lời giải.} Theo hình vẽ, đường thẳng đứng mà hai nhánh đồ thị tiến sát là $x = -1$.

\textbf{==> Chọn đáp án D.}

@@END_SIDE_BY_SIDE_C4@@

% Câu 5
@@START_SIDE_BY_SIDE_C5@@

\textbf{Câu 5.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I(0; 1)$.@@TAB@@\textbf{B.} $I(1; 1)$.

@@TAB@@\textbf{C.} $I(1; 0)$.@@TAB@@\textbf{D.} $I(2; -1)$.

\textbf{Lời giải.} Trên hình vẽ, điểm uốn và tâm đối xứng của đồ thị là $I(1; 1)$.

\textbf{==> Chọn đáp án B.}

@@END_SIDE_BY_SIDE_C5@@

% Câu 6
@@START_SIDE_BY_SIDE_C6@@

\textbf{Câu 6.} Cho hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có đồ thị như hình bên. Hàm số nào dưới đây có đồ thị như hình vẽ?

@@TAB@@\textbf{A.} $y = \dfrac{x + 1}{x + 2}$.@@TAB@@\textbf{B.} $y = \dfrac{x - 5}{x - 2}$.

@@TAB@@\textbf{C.} $y = \dfrac{x + 1}{x - 2}$.@@TAB@@\textbf{D.} $y = \dfrac{-x + 1}{x - 2}$.

\textbf{Lời giải.} Đồ thị có tiệm cận đứng $x = 2$, tiệm cận ngang $y = 1$; nhánh bên phải nằm phía trên đường tiệm cận ngang. Do đó hàm số phù hợp là $y = 1 + \dfrac{3}{x - 2} = \dfrac{x + 1}{x - 2}$.

\textbf{==> Chọn đáp án C.}

@@END_SIDE_BY_SIDE_C6@@

% Câu 7
@@START_SIDE_BY_SIDE_C7@@

\textbf{Câu 7.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Số điểm cực trị của hàm số là

@@TAB@@\textbf{A.} $0$.@@TAB@@\textbf{B.} $1$.@@TAB@@\textbf{C.} $2$.@@TAB@@\textbf{D.} $3$.

\textbf{Lời giải.} Đồ thị hàm số có một điểm cực đại và một điểm cực tiểu. Vậy hàm số có 2 điểm cực trị.

\textbf{==> Chọn đáp án C.}

@@END_SIDE_BY_SIDE_C7@@

% Câu 8
\textbf{Câu 8.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c8_bbt@@

Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số đồng biến trên khoảng $(-\infty; 2)$.

@@TAB@@\textbf{B.} Hàm số nghịch biến trên từng khoảng $(-\infty; 2)$ và $(2; +\infty)$.

@@TAB@@\textbf{C.} Hàm số đồng biến trên khoảng $(2; +\infty)$.

@@TAB@@\textbf{D.} Hàm số nghịch biến trên $(-\infty; +\infty)$.

\textbf{Lời giải.} Dựa vào bảng biến thiên, đạo hàm $f'(x) < 0$ trên $(-\infty; 2)$ và $(2; +\infty)$. Vậy hàm số nghịch biến trên từng khoảng $(-\infty; 2)$ và $(2; +\infty)$.

\textbf{==> Chọn đáp án B.}

% Câu 9
\textbf{Câu 9.} Cho hàm số $y = f(x)$ có bảng biến thiên như sau:

@@CENTER_IMAGE_c9_bbt@@

Khoảng nào sau đây là một khoảng nghịch biến của hàm số?

@@TAB@@\textbf{A.} $(-\infty; 1)$.@@TAB@@\textbf{B.} $(1; 3)$.@@TAB@@\textbf{C.} $(1; 2)$.@@TAB@@\textbf{D.} $(3; +\infty)$.

\textbf{Lời giải.} Dựa vào bảng biến thiên, hàm số nghịch biến trên khoảng $(1; 2)$ và $(2; 3)$. Do đó $(1; 2)$ là một khoảng nghịch biến.

\textbf{==> Chọn đáp án C.}

% Câu 10
@@START_SIDE_BY_SIDE_C10@@

\textbf{Câu 10.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Điểm cực tiểu của hàm số đã cho là

@@TAB@@\textbf{A.} $x = -1$.@@TAB@@\textbf{B.} $x = 0$.

@@TAB@@\textbf{C.} $x = 1$.@@TAB@@\textbf{D.} $x = 2$.

\textbf{Lời giải.} Dựa vào đồ thị, hàm số đạt cực tiểu tại điểm $x = 1$ (với giá trị cực tiểu tương ứng là $y = -2$).

\textbf{==> Chọn đáp án C.}

@@END_SIDE_BY_SIDE_C10@@

% Câu 11
@@START_SIDE_BY_SIDE_C11@@

\textbf{Câu 11.} Cho hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$) có đồ thị như hình bên. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I(1; 2)$.@@TAB@@\textbf{B.} $I(2; 1)$.

@@TAB@@\textbf{C.} $I(-1; 2)$.@@TAB@@\textbf{D.} $I(2; -1)$.

\textbf{Lời giải.} Giao điểm của hai đường tiệm cận $x = -1$ và $y = 2$ là $I(-1; 2)$, đây là tâm đối xứng của đồ thị.

\textbf{==> Chọn đáp án C.}

@@END_SIDE_BY_SIDE_C11@@

% Câu 12
@@START_SIDE_BY_SIDE_C12@@

\textbf{Câu 12.} Cho hàm số phân thức $y = \dfrac{ax^2 + bx + c}{px + q}$ ($a \ne 0, p \ne 0$, đa thức tử không chia hết cho đa thức mẫu) có đồ thị như hình bên. Đường tiệm cận xiên $d$ của đồ thị có phương trình là

@@TAB@@\textbf{A.} $y = x + 1$.@@TAB@@\textbf{B.} $y = x - 1$.

@@TAB@@\textbf{C.} $y = -x - 1$.@@TAB@@\textbf{D.} $y = -1$.

\textbf{Lời giải.} Đường thẳng nét đứt $d$ có hệ số góc $k = 1$ và cắt trục tung tại điểm $(0; -1)$, nên phương trình đường tiệm cận xiên là $d\colon y = x - 1$.

\textbf{==> Chọn đáp án B.}

@@END_SIDE_BY_SIDE_C12@@

@@SECTION_2_HEADER@@

% Phần 2 Câu 1
@@START_SIDE_BY_SIDE_P2C1@@

\textbf{Câu 1.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên, trong đó điểm $I(0; 2)$ được đánh dấu. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Hàm số đồng biến trên khoảng $(-1; 1)$.

@@TAB@@\textbf{b)} Hàm số đạt cực đại tại điểm $x = -1$.

@@TAB@@\textbf{c)} Giá trị cực tiểu của hàm số bằng $0$.

@@TAB@@\textbf{d)} Điểm $I(0; 2)$ là tâm đối xứng của đồ thị.

\textbf{Lời giải.} 

- Ý a) Sai: Trên khoảng $(-1; 1)$, đồ thị đi xuống từ trái sang phải nên hàm số nghịch biến.

- Ý b) Đúng: Hàm số đạt cực đại tại $x = -1$ với giá trị cực đại $y = 4$.

- Ý c) Đúng: Điểm cực tiểu là $(1; 0)$ nên giá trị cực tiểu của hàm số bằng $0$.

- Ý d) Đúng: Điểm uốn $I(0; 2)$ chính là tâm đối xứng của đồ thị hàm số bậc ba.

\textbf{==> Đáp án: a) Sai | b) Đúng | c) Đúng | d) Đúng.}

@@END_SIDE_BY_SIDE_P2C1@@

% Phần 2 Câu 2
\textbf{Câu 2.} Cho các biểu diễn như dưới đây. Trong đó, Hình 1 và bảng biến thiên lần lượt là đồ thị và bảng biến thiên của hàm số $y = \dfrac{ax + b}{cx + d}$ ($ac \ne 0, ad - bc \ne 0$); Hình 2 là đồ thị của hàm số $y = \dfrac{mx^2 + nx + p}{qx + r}$ ($mq \ne 0$, đa thức tử không chia hết cho đa thức mẫu).

@@CENTER_IMAGE_p2_c2_hinh_all@@

Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Ở Hình 1, đường tiệm cận đứng của đồ thị là $x = 1$.

@@TAB@@\textbf{b)} Ở Hình 1, cả $d_1$ và $d_2$ đều là trục đối xứng của đồ thị.

@@TAB@@\textbf{c)} Bảng biến thiên cho thấy hàm số nghịch biến trên từng khoảng $(-\infty; 1)$ và $(1; +\infty)$.

@@TAB@@\textbf{d)} Ở Hình 2, đường tiệm cận xiên $d$ có phương trình $y = x - 1$.

\textbf{Lời giải.}

- Ý a) Đúng: Hình 1 có tiệm cận đứng là đường thẳng $x = 1$.

- Ý b) Đúng: Hai đường phân giác của các góc tạo bởi hai tiệm cận $d_1, d_2$ đều là các trục đối xứng của hyperbol.

- Ý c) Đúng: Dấu đạo hàm mang dấu âm trên cả $(-\infty; 1)$ và $(1; +\infty)$.

- Ý d) Sai: Đường thẳng $d$ đi qua $(-1; 0)$ và $(0; 1)$ nên có phương trình $y = x + 1$ (chứ không phải $y = x - 1$).

\textbf{==> Đáp án: a) Đúng | b) Đúng | c) Đúng | d) Sai.}

% Phần 2 Câu 3
\textbf{Câu 3.} Cho hàm số $y = f(x) = x^3 - 3x + 1$ có đạo hàm $f'(x) = 3(x + 1)(x - 1)$ với mọi $x \in \mathbb{R}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định của hàm số là $\mathbb{R}$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên từng khoảng $(-\infty; -1)$ và $(1; +\infty)$.

@@TAB@@\textbf{c)} Hàm số đạt cực tiểu tại $x = -1$.

@@TAB@@\textbf{d)} Giá trị cực tiểu của hàm số bằng $-1$.

\textbf{Lời giải.}

- Ý a) Đúng: Hàm đa thức xác định trên $\mathbb{R}$.

- Ý b) Đúng: $f'(x) > 0 \iff x \in (-\infty; -1) \cup (1; +\infty)$.

- Ý c) Sai: Đạo hàm đổi dấu từ $+$ sang $-$ qua $x = -1$ nên đây là điểm cực đại. Hàm số đạt cực tiểu tại $x = 1$.

- Ý d) Đúng: Giá trị cực tiểu là $f(1) = 1^3 - 3(1) + 1 = -1$.

\textbf{==> Đáp án: a) Đúng | b) Đúng | c) Sai | d) Đúng.}

% Phần 2 Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định của hàm số là $\mathbb{R} \setminus \{1\}$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên từng khoảng $(0; 1)$ và $(1; 2)$.

@@TAB@@\textbf{c)} Hàm số đạt cực tiểu tại $x = 0$.

@@TAB@@\textbf{d)} Đồ thị hàm số có đường tiệm cận xiên $y = x + 1$.

\textbf{Lời giải.}

- Ý a) Đúng: Mẫu số khác 0 khi $x \ne 1$.

- Ý b) Đúng: $y' = \dfrac{x^2 - 2x}{(x - 1)^2} = \dfrac{x(x - 2)}{(x - 1)^2} < 0 \iff x \in (0; 1) \cup (1; 2)$.

- Ý c) Sai: Đạo hàm đổi dấu từ $+$ sang $-$ qua $x = 0$ nên $x = 0$ là điểm cực đại.

- Ý d) Đúng: $y = \dfrac{x^2 - 1 + 1}{x - 1} = x + 1 + \dfrac{1}{x - 1} \implies$ tiệm cận xiên là $y = x + 1$.

\textbf{==> Đáp án: a) Đúng | b) Đúng | c) Sai | d) Đúng.}

@@SECTION_3_HEADER@@

% Phần 3 Câu 1
\textbf{Câu 1.} Cho hàm số $y = f(x) = x^3 - 6x^2 + 9x + 1$ có đạo hàm $f'(x) = 3(x - 1)(x - 3)$ với mọi $x \in \mathbb{R}$. Tìm điểm cực đại của hàm số đã cho.

\textbf{Lời giải.} Đạo hàm $f'(x) = 0 \iff x = 1$ hoặc $x = 3$. Qua điểm $x = 1$, $f'(x)$ đổi dấu từ dương sang âm nên điểm cực đại của hàm số là $x = 1$.

\textbf{==> Đáp án: 1.}

% Phần 3 Câu 2
\textbf{Câu 2.} Cho hàm số $y = g(x) = -x^3 + 3x + 2$ có đạo hàm $g'(x) = 3(1 - x^2)$ với mọi $x \in \mathbb{R}$. Giá trị cực đại của hàm số bằng bao nhiêu?

\textbf{Lời giải.} Đạo hàm $g'(x) = 0 \iff x = \pm 1$. Hàm số đổi dấu từ $+$ sang $-$ qua $x = 1$ nên đạt cực đại tại $x = 1$. Giá trị cực đại là $g(1) = -(1)^3 + 3(1) + 2 = 4$.

\textbf{==> Đáp án: 4.}

% Phần 3 Câu 3
\textbf{Câu 3.} Cho hàm số $y = f(x) = \dfrac{2x + 1}{x - 1}$ có đạo hàm $f'(x) = \dfrac{-3}{(x - 1)^2}$ với mọi $x \ne 1$. Trong hai khoảng $(-\infty; 1)$ và $(1; +\infty)$, hàm số nghịch biến trên bao nhiêu khoảng?

\textbf{Lời giải.} Vì $f'(x) = \dfrac{-3}{(x - 1)^2} < 0$ với mọi $x \ne 1$, nên hàm số nghịch biến trên cả hai khoảng $(-\infty; 1)$ và $(1; +\infty)$. Số khoảng nghịch biến là 2.

\textbf{==> Đáp án: 2.}

% Phần 3 Câu 4
\textbf{Câu 4.} Cho hàm số $y = f(x) = \dfrac{x^2}{x + 1}$ có đạo hàm $f'(x) = \dfrac{x(x + 2)}{(x + 1)^2}$ với mọi $x \ne -1$. Giá trị cực đại của hàm số bằng bao nhiêu?

\textbf{Lời giải.} Ta có $f'(x) = 0 \iff x = 0$ hoặc $x = -2$. Đạo hàm đổi dấu từ $+$ sang $-$ qua $x = -2$ nên hàm số đạt cực đại tại $x = -2$. Giá trị cực đại là $f(-2) = \dfrac{(-2)^2}{-2 + 1} = \dfrac{4}{-1} = -4$.

\textbf{==> Đáp án: -4.}

% Phần 3 Câu 5
\textbf{Câu 5.} Cho hàm số $y = f(x) = x^3 - 3x^2 + 1$. Gọi $M$ và $m$ lần lượt là giá trị cực đại và giá trị cực tiểu của hàm số. Tính $M + m$.

\textbf{Lời giải.} Ta có $f'(x) = 3x^2 - 6x = 3x(x - 2)$. $f'(x) = 0 \iff x = 0$ hoặc $x = 2$. Do đó $M = f(0) = 1$ và $m = f(2) = 2^3 - 3(2)^2 + 1 = -3$. Suy ra $M + m = 1 + (-3) = -2$.

\textbf{==> Đáp án: -2.}

% Phần 3 Câu 6
\textbf{Câu 6.} Cho hai hàm số $y = g(x) = \dfrac{2x + 1}{x - 1}$ và $y = h(x) = \dfrac{x^2 - x - 1}{x - 2}$. Gọi $a$ là tung độ tiệm cận ngang của đồ thị hàm số $g$, $b$ là hệ số tự do của tiệm cận xiên $y = x + b$ của đồ thị hàm số $h$. Tính $a + b$.

\textbf{Lời giải.} 

- Với đồ thị hàm số $g$, tiệm cận ngang là đường thẳng $y = 2 \implies a = 2$.

- Với đồ thị hàm số $h$, ta có $h(x) = \dfrac{x^2 - x - 1}{x - 2} = x + 1 + \dfrac{1}{x - 2} \implies$ tiệm cận xiên là $y = x + 1 \implies b = 1$.

- Vậy $a + b = 2 + 1 = 3$.

\textbf{==> Đáp án: 3.}

\vspace{0.4cm}
\begin{center}
\textbf{------ HẾT ------}
\end{center}

\end{document}
"""

def build_exam_document(tex_str, output_path, ma_de, is_solution=False):
    temp_tex = os.path.join(CURRENT_DIR, f"temp_build_{ma_de}_{'hdg' if is_solution else 'de'}.tex")
    temp_docx = os.path.join(CURRENT_DIR, f"temp_build_{ma_de}_{'hdg' if is_solution else 'de'}.docx")
    
    with open(temp_tex, "w", encoding="utf-8") as f:
        f.write(tex_str)
        
    print(f"[*] Đang chuyển đổi qua Pandoc: {os.path.basename(output_path)}...")
    subprocess.run([pandoc_exe, temp_tex, "-o", temp_docx], check=True)
    
    doc = docx.Document(temp_docx)
    
    # 1. Page Setup
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
        
        r_r = f_p.add_run(f"Trang Mã đề {ma_de}")
        r_r.font.name = "Times New Roman"
        r_r.font.size = Pt(9.5)
        r_r.italic = True
        r_r.font.color.rgb = RGBColor(80, 80, 80)
        
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.font.color.rgb = RGBColor(0, 0, 0)
    rPr = style.element.get_or_add_rPr()
    rFonts = parse_xml(r'<w:rFonts %s w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>' % nsdecls('w'))
    rPr.append(rFonts)
    
    # 2. Section and Header replacements
    for p in list(doc.paragraphs):
        if "@@DOCUMENT_HEADER@@" in p.text:
            insert_header_and_code(doc, p, ma_de, is_solution)
        elif "@@SECTION_1_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn.", "Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.")
        elif "@@SECTION_2_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN II. Câu trắc nghiệm đúng sai.", "Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")
        elif "@@SECTION_3_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN III. Câu trắc nghiệm yêu cầu trả lời ngắn.", "Thí sinh trả lời từ câu 1 đến câu 6.")
            
    # 3. Side-by-side tables
    sbs_configs = [
        ("C3", "c3_hinh.png", 5.2),
        ("C4", "c4_hinh.png", 5.2),
        ("C5", "c5_hinh.png", 5.0),
        ("C6", "c6_hinh.png", 5.0),
        ("C7", "c7_hinh.png", 5.0),
        ("C10", "c10_hinh.png", 5.0),
        ("C11", "c11_hinh.png", 5.0),
        ("C12", "c12_hinh.png", 5.0),
        ("P2C1", "p2_c1_hinh.png", 5.2),
    ]
    
    for tag, img_name, img_w in sbs_configs:
        start_tag = f"@@START_SIDE_BY_SIDE_{tag}@@"
        end_tag = f"@@END_SIDE_BY_SIDE_{tag}@@"
        
        start_p = None
        end_p = None
        inner_ps = []
        found = False
        
        for p in doc.paragraphs:
            if start_tag in p.text:
                start_p = p
                found = True
                continue
            if end_tag in p.text:
                end_p = p
                found = False
                continue
            if found:
                inner_ps.append(p)
                
        if start_p and end_p:
            tbl = doc.add_table(rows=1, cols=2)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            
            tblPr = tbl._tbl.tblPr
            for look in tblPr.findall(qn('w:tblLook')):
                tblPr.remove(look)
            tblLook = parse_xml(r'<w:tblLook %s w:val="0000" w:firstRow="0" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/>' % nsdecls('w'))
            for b in tblPr.findall(qn('w:tblBorders')):
                tblPr.remove(b)
            tblBorders = parse_xml(
                r'<w:tblBorders %s>'
                r'<w:top w:val="none"/>'
                r'<w:left w:val="none"/>'
                r'<w:bottom w:val="none"/>'
                r'<w:right w:val="none"/>'
                r'<w:insideH w:val="none"/>'
                r'<w:insideV w:val="none"/>'
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
                for b in tcPr.findall(qn('w:tcBorders')):
                    tcPr.remove(b)
                tcPr.append(parse_xml(
                    r'<w:tcBorders %s>'
                    r'<w:top w:val="none"/>'
                    r'<w:left w:val="none"/>'
                    r'<w:bottom w:val="none"/>'
                    r'<w:right w:val="none"/>'
                    r'</w:tcBorders>' % nsdecls('w')
                ))
                
            start_p._p.addprevious(tbl._tbl)
            cell_0._tc.remove(cell_0.paragraphs[0]._p)
            for p in inner_ps:
                cell_0._tc.append(p._p)
                
            img_path = os.path.join(HINH_ANH_0101, img_name)
            cell_1_p = cell_1.paragraphs[0]
            cell_1_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cell_1_p.paragraph_format.space_before = Pt(0)
            cell_1_p.paragraph_format.space_after = Pt(0)
            if os.path.exists(img_path):
                cell_1_p.add_run().add_picture(img_path, width=Cm(img_w))
                
            start_p._p.getparent().remove(start_p._p)
            end_p._p.getparent().remove(end_p._p)
            
    # 4. Insert Center Images & Answer boxes
    for p in list(doc.paragraphs):
        # BBT images
        for bbt_name in ["c1_bbt", "c2_bbt", "c8_bbt", "c9_bbt", "p2_c2_hinh_all"]:
            token = f"@@CENTER_IMAGE_{bbt_name}@@"
            if token in p.text:
                img_path = os.path.join(HINH_ANH_0101, f"{bbt_name}.png")
                p.text = ""
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                if os.path.exists(img_path):
                    w_cm = 16.0 if "hinh_all" in bbt_name else 9.5
                    p.add_run().add_picture(img_path, width=Cm(w_cm))
                break
                
        # Answer boxes for student test
        if not is_solution:
            for num in range(1, 7):
                tag = f"@@ANSWER_BOX_{num}@@"
                if tag in p.text:
                    box_tbl = create_answer_box_table(doc)
                    p._p.addprevious(box_tbl._tbl)
                    p._p.getparent().remove(p._p)
                    break

    # 5. Format Paragraphs & Tables
    for p in list(doc.paragraphs):
        format_doc_paragraph(p, inside_table_cell=False)
        # Highlight "Lời giải" and "==> Chọn đáp án" in solutions
        if is_solution:
            p_text = p.text.strip()
            if p_text.startswith("Lời giải."):
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(2)
            elif "==> Chọn đáp án" in p_text or "==> Đáp án:" in p_text:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(8)
                for r in p.runs:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(192, 0, 0) # Màu đỏ nổi bật đáp án đúng
                    
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
                                
    # Clean up tblStylePr
    for s in doc.styles:
        if s.type == docx.enum.style.WD_STYLE_TYPE.TABLE:
            for child in list(s._element):
                if child.tag.endswith('tblStylePr'):
                    s._element.remove(child)
                    
    settings = doc.settings.element
    compat = parse_xml(
        r'<w:compat %s>'
        r'<w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/>'
        r'</w:compat>' % nsdecls('w')
    )
    settings.append(compat)
    
    doc.save(output_path)
    print(f"[THÀNH CÔNG] Đã xuất bản: {output_path}")
    
    if os.path.exists(temp_tex):
        os.remove(temp_tex)
    if os.path.exists(temp_docx):
        os.remove(temp_docx)

if __name__ == "__main__":
    print("=== TIẾN HÀNH XUẤT BẢN MÃ ĐỀ 0101 (ĐỀ BÀI + LỜI GIẢI CHI TIẾT) ===")
    build_exam_document(tex_de_0101, OUTPUT_DE_0101, "0101", is_solution=False)
    build_exam_document(tex_hdg_0101, OUTPUT_HDG_0101, "0101", is_solution=True)
