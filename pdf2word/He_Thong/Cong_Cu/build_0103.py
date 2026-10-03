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
HINH_ANH_0103 = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", "Bao_Thang_3", "0103")
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
pandoc_exe = os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")

OUTPUT_DE_0103 = os.path.join(SAN_PHAM_DIR, "de-khao-sat-toan-12-nam-2026-2027-truong-thpt-bao-thang-3-lao-cai_De_0103.docx")
OUTPUT_HDG_0103 = os.path.join(SAN_PHAM_DIR, "de-khao-sat-toan-12-nam-2026-2027-truong-thpt-bao-thang-3-lao-cai_HDG_0103.docx")

# =========================================================================
# 1. TEX MÃ ĐỀ 0103 - ĐỀ BÀI HỌC SINH
# =========================================================================
tex_de_0103 = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage[top=1.6cm,bottom=1.6cm,left=2.0cm,right=1.5cm]{geometry}

\begin{document}

@@DOCUMENT_HEADER@@

@@SECTION_1_HEADER@@

% Câu 1 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_C1@@

\textbf{Câu 1.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Hàm số nghịch biến trên khoảng nào sau đây?

@@TAB@@\textbf{A.} $(-\infty; -1)$.@@TAB@@\textbf{B.} $(1; +\infty)$.

@@TAB@@\textbf{C.} $(-1; 1)$.@@TAB@@\textbf{D.} $(-\infty; 1)$.

@@END_SIDE_BY_SIDE_C1@@

% Câu 2 (BBT)
\textbf{Câu 2.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_c2_bbt@@

Giá trị cực tiểu của hàm số là

@@TAB@@\textbf{A.} $-3$.@@TAB@@\textbf{B.} $-1$.@@TAB@@\textbf{C.} $2$.@@TAB@@\textbf{D.} $4$.

% Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{x - 4}{2x + 1}$. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I\left(-\dfrac{1}{2}; -\dfrac{1}{2}\right)$.@@TAB@@\textbf{B.} $I\left(\dfrac{1}{2}; -\dfrac{1}{2}\right)$.@@TAB@@\textbf{C.} $I(2; 1)$.@@TAB@@\textbf{D.} $I\left(-\dfrac{1}{2}; \dfrac{1}{2}\right)$.

% Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{2x + 5}{x + 1}$. Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số đồng biến trên từng khoảng xác định.

@@TAB@@\textbf{B.} Hàm số nghịch biến trên từng khoảng xác định.

@@TAB@@\textbf{C.} Hàm số có một điểm cực trị.

@@TAB@@\textbf{D.} Đồ thị không có tiệm cận ngang.

% Câu 5
\textbf{Câu 5.} Cho hàm số $y = x + \dfrac{1}{x}$. Phương trình đường tiệm cận xiên của đồ thị hàm số là

@@TAB@@\textbf{A.} $y = x$.@@TAB@@\textbf{B.} $y = x + 1$.@@TAB@@\textbf{C.} $y = x - 1$.@@TAB@@\textbf{D.} $x = 0$.

% Câu 6
\textbf{Câu 6.} Cho hàm số $y = x + 1 + \dfrac{2}{x + 1}$. Giao điểm hai đường tiệm cận của đồ thị hàm số là

@@TAB@@\textbf{A.} $I(1; 2)$.@@TAB@@\textbf{B.} $I(-1; 1)$.@@TAB@@\textbf{C.} $I(-1; 0)$.@@TAB@@\textbf{D.} $I(0; -1)$.

% Câu 7
\textbf{Câu 7.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = 3(x - 1)(x + 3)$ với mọi $x \in \mathbb{R}$. Điểm cực đại của hàm số đã cho là

@@TAB@@\textbf{A.} $x = 1$.@@TAB@@\textbf{B.} $x = -3$.@@TAB@@\textbf{C.} $x = 3$.@@TAB@@\textbf{D.} $x = -1$.

% Câu 8
\textbf{Câu 8.} Cho hàm số $y = f(x) = x^3 + 6x^2 + 9x$. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I(-1; 0)$.@@TAB@@\textbf{B.} $I(2; -2)$.@@TAB@@\textbf{C.} $I(-2; 0)$.@@TAB@@\textbf{D.} $I(-2; -2)$.

% Câu 9
\textbf{Câu 9.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x - 1)(x + 2)$ với mọi $x \in \mathbb{R}$. Số khoảng đồng biến của hàm số là

@@TAB@@\textbf{A.} $1$.@@TAB@@\textbf{B.} $3$.@@TAB@@\textbf{C.} $2$.@@TAB@@\textbf{D.} $4$.

% Câu 10 (BBT)
\textbf{Câu 10.} Cho hàm số $y = \dfrac{ax^2 + bx + c}{dx + e}$ ($ad \ne 0$), trong đó đa thức tử không chia hết cho đa thức mẫu. Bảng biến thiên của hàm số được cho như dưới đây:

@@CENTER_IMAGE_c10_bbt@@

Hàm số nào dưới đây có bảng biến thiên đã cho?

@@TAB@@\textbf{A.} $y = \dfrac{x^2 + 1}{x}$.@@TAB@@\textbf{B.} $y = \dfrac{x^2 - 1}{x}$.@@TAB@@\textbf{C.} $y = \dfrac{x^2 + 1}{x - 1}$.@@TAB@@\textbf{D.} $y = \dfrac{x^2 + 4}{x}$.

% Câu 11
\textbf{Câu 11.} Cho hàm số $y = x + 2 + \dfrac{3}{x - 2}$. Phương trình đường tiệm cận xiên của đồ thị hàm số là

@@TAB@@\textbf{A.} $x = 2$.@@TAB@@\textbf{B.} $y = 2$.@@TAB@@\textbf{C.} $y = x + 2$.@@TAB@@\textbf{D.} $y = x - 2$.

% Câu 12
\textbf{Câu 12.} Cho hàm số $y = f(x)$ xác định trên $\mathbb{R} \setminus \{-1\}$ và có đạo hàm $f'(x) = \dfrac{x(x + 2)}{(x + 1)^2}$. Điểm cực đại của hàm số đã cho là

@@TAB@@\textbf{A.} $x = -1$.@@TAB@@\textbf{B.} $x = 0$.@@TAB@@\textbf{C.} $x = 2$.@@TAB@@\textbf{D.} $x = -2$.

@@SECTION_2_HEADER@@

% Phần 2 Câu 1 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_P2C1@@

\textbf{Câu 1.} Cho hàm số $y = \dfrac{2x + 1}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $y' = -\dfrac{3}{(x - 1)^2}$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên khoảng $(1; +\infty)$.

@@TAB@@\textbf{c)} Đồ thị có tiệm cận ngang $y = 2$.

@@TAB@@\textbf{d)} Hình bên là đồ thị của hàm số đã cho.

@@END_SIDE_BY_SIDE_P2C1@@

% Phần 2 Câu 2 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_P2C2@@

\textbf{Câu 2.} Cho hàm số $y = \dfrac{ax^2 + bx + c}{dx + e}$ ($ad \ne 0$), trong đó đa thức tử không chia hết cho đa thức mẫu. Đồ thị của hàm số được cho như hình bên. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đồ thị có tiệm cận đứng $x = 1$.

@@TAB@@\textbf{b)} Đường tiệm cận xiên có phương trình $y = x + 2$.

@@TAB@@\textbf{c)} Đồ thị cắt trục tung tại điểm có tung độ bằng $2$.

@@TAB@@\textbf{d)} Hàm số nghịch biến trên toàn bộ $\mathbb{R}$.

@@END_SIDE_BY_SIDE_P2C2@@

% Phần 2 Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{(x - 2)^2}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định của hàm số là $\mathbb{R} \setminus \{1\}$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên khoảng $(-\infty; 0)$.

@@TAB@@\textbf{c)} Hàm số đạt cực tiểu tại $x = 0$.

@@TAB@@\textbf{d)} Đồ thị có tiệm cận xiên $y = x - 3$.

% Phần 2 Câu 4 (BBT)
\textbf{Câu 4.} Cho hàm số $y = f(x) = -x^3 + 3x + 1$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $f'(x) = 3(1 - x^2)$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên khoảng $(-1; 1)$.

@@TAB@@\textbf{c)} Giá trị cực tiểu của hàm số bằng $1$.

@@TAB@@\textbf{d)} Bảng biến thiên dưới đây là bảng biến thiên của hàm số đã cho.

@@CENTER_IMAGE_p2_c4_bbt@@

@@SECTION_3_HEADER@@

% Phần 3 Câu 1 (BBT)
\textbf{Câu 1.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_p3_c1_bbt@@

Hàm số có bao nhiêu điểm cực trị?

@@ANSWER_BOX_1@@

% Phần 3 Câu 2
\textbf{Câu 2.} Cho hàm số $y = f(x) = x^3 - 6x^2 + 9x + 1$. Tính hiệu giữa giá trị cực đại và giá trị cực tiểu của hàm số.

@@ANSWER_BOX_2@@

% Phần 3 Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{2x + 1}{x - 1}$. Gọi $I(a; b)$ là giao điểm hai đường tiệm cận. Tính $a + b$.

@@ANSWER_BOX_3@@

% Phần 3 Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2 - 1}{x - 2}$. Tính tung độ giao điểm của đường tiệm cận xiên của đồ thị với trục tung.

@@ANSWER_BOX_4@@

% Phần 3 Câu 5
\textbf{Câu 5.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x + 3)(x - 1)^2(x - 2)$ với mọi $x \in \mathbb{R}$. Tính tổng các giá trị của $x$ tại đó hàm số đạt cực trị.

@@ANSWER_BOX_5@@

% Phần 3 Câu 6
\textbf{Câu 6.} Cho hàm số $y = f(x) = x^3 - 3ax$, với $a > 0$. Biết hàm số đạt cực tiểu tại $x = 3$. Tính $a$.

@@ANSWER_BOX_6@@

\vspace{0.4cm}
\begin{center}
\textbf{------ HẾT ------}
\end{center}

\end{document}
"""

# =========================================================================
# 2. TEX MÃ ĐỀ 0103 - HƯỚNG DẪN GIẢI CHI TIẾT
# =========================================================================
tex_hdg_0103 = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage[top=1.6cm,bottom=1.6cm,left=2.0cm,right=1.5cm]{geometry}

\begin{document}

@@DOCUMENT_HEADER@@

@@SECTION_1_HEADER@@

% Câu 1 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_C1@@

\textbf{Câu 1.} Cho hàm số bậc ba $y = f(x)$ có đồ thị như hình bên. Hàm số nghịch biến trên khoảng nào sau đây?

@@TAB@@\textbf{A.} $(-\infty; -1)$.@@TAB@@\textbf{B.} $(1; +\infty)$.

@@TAB@@\textbf{C.} $(-1; 1)$.@@TAB@@\textbf{D.} $(-\infty; 1)$.

\textbf{Lời giải.} Dựa vào đồ thị hàm số, trên khoảng $(-1; 1)$ nét đồ thị đi xuống từ cực đại $(-1; 2)$ đến cực tiểu $(1; -2)$, do đó hàm số nghịch biến trên khoảng $(-1; 1)$.

\textbf{==> Chọn đáp án C.}

@@END_SIDE_BY_SIDE_C1@@

% Câu 2 (BBT)
\textbf{Câu 2.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_c2_bbt@@

Giá trị cực tiểu của hàm số là

@@TAB@@\textbf{A.} $-3$.@@TAB@@\textbf{B.} $-1$.@@TAB@@\textbf{C.} $2$.@@TAB@@\textbf{D.} $4$.

\textbf{Lời giải.} Từ bảng biến thiên, khi qua $x = -1$, đạo hàm $f'(x)$ đổi dấu từ âm sang dương nên hàm số đạt cực tiểu tại $x = -1$ và giá trị cực tiểu của hàm số là $y_{\text{CT}} = -3$.

\textbf{==> Chọn đáp án A.}

% Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{x - 4}{2x + 1}$. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I\left(-\dfrac{1}{2}; -\dfrac{1}{2}\right)$.@@TAB@@\textbf{B.} $I\left(\dfrac{1}{2}; -\dfrac{1}{2}\right)$.@@TAB@@\textbf{C.} $I(2; 1)$.@@TAB@@\textbf{D.} $I\left(-\dfrac{1}{2}; \dfrac{1}{2}\right)$.

\textbf{Lời giải.} Đồ thị hàm số phân thức bậc nhất trên bậc nhất có tiệm cận đứng $x = -\dfrac{1}{2}$ và tiệm cận ngang $y = \dfrac{1}{2}$. Tâm đối xứng của đồ thị là giao điểm hai tiệm cận: $I\left(-\dfrac{1}{2}; \dfrac{1}{2}\right)$.

\textbf{==> Chọn đáp án D.}

% Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{2x + 5}{x + 1}$. Khẳng định nào sau đây đúng?

@@TAB@@\textbf{A.} Hàm số đồng biến trên từng khoảng xác định.

@@TAB@@\textbf{B.} Hàm số nghịch biến trên từng khoảng xác định.

@@TAB@@\textbf{C.} Hàm số có một điểm cực trị.

@@TAB@@\textbf{D.} Đồ thị không có tiệm cận ngang.

\textbf{Lời giải.} Ta có $y' = \dfrac{-3}{(x + 1)^2} < 0, \; \forall x \ne -1$. Do đó hàm số nghịch biến trên từng khoảng xác định $(-\infty; -1)$ và $(-1; +\infty)$.

\textbf{==> Chọn đáp án B.}

% Câu 5
\textbf{Câu 5.} Cho hàm số $y = x + \dfrac{1}{x}$. Phương trình đường tiệm cận xiên của đồ thị hàm số là

@@TAB@@\textbf{A.} $y = x$.@@TAB@@\textbf{B.} $y = x + 1$.@@TAB@@\textbf{C.} $y = x - 1$.@@TAB@@\textbf{D.} $x = 0$.

\textbf{Lời giải.} Ta có $\lim\limits_{x \to \pm\infty} [y - x] = \lim\limits_{x \to \pm\infty} \dfrac{1}{x} = 0$, do đó đường thẳng $y = x$ là đường tiệm cận xiên của đồ thị hàm số.

\textbf{==> Chọn đáp án A.}

% Câu 6
\textbf{Câu 6.} Cho hàm số $y = x + 1 + \dfrac{2}{x + 1}$. Giao điểm hai đường tiệm cận của đồ thị hàm số là

@@TAB@@\textbf{A.} $I(1; 2)$.@@TAB@@\textbf{B.} $I(-1; 1)$.@@TAB@@\textbf{C.} $I(-1; 0)$.@@TAB@@\textbf{D.} $I(0; -1)$.

\textbf{Lời giải.} Đồ thị hàm số có tiệm cận đứng $x = -1$ và tiệm cận xiên $y = x + 1$. Thay $x = -1$ vào phương trình tiệm cận xiên ta được $y = -1 + 1 = 0$. Vậy giao điểm hai tiệm cận là $I(-1; 0)$.

\textbf{==> Chọn đáp án C.}

% Câu 7
\textbf{Câu 7.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = 3(x - 1)(x + 3)$ với mọi $x \in \mathbb{R}$. Điểm cực đại của hàm số đã cho là

@@TAB@@\textbf{A.} $x = 1$.@@TAB@@\textbf{B.} $x = -3$.@@TAB@@\textbf{C.} $x = 3$.@@TAB@@\textbf{D.} $x = -1$.

\textbf{Lời giải.} Phương trình $f'(x) = 0 \iff x = 1$ hoặc $x = -3$. Qua $x = -3$, đạo hàm $f'(x)$ đổi dấu từ dương sang âm, do đó hàm số đạt cực đại tại $x = -3$.

\textbf{==> Chọn đáp án B.}

% Câu 8
\textbf{Câu 8.} Cho hàm số $y = f(x) = x^3 + 6x^2 + 9x$. Tâm đối xứng của đồ thị là

@@TAB@@\textbf{A.} $I(-1; 0)$.@@TAB@@\textbf{B.} $I(2; -2)$.@@TAB@@\textbf{C.} $I(-2; 0)$.@@TAB@@\textbf{D.} $I(-2; -2)$.

\textbf{Lời giải.} Ta có $y' = 3x^2 + 12x + 9 \implies y'' = 6x + 12 = 0 \iff x = -2 \implies y(-2) = -2$. Tâm đối xứng của đồ thị hàm số bậc ba là điểm uốn $I(-2; -2)$.

\textbf{==> Chọn đáp án D.}

% Câu 9
\textbf{Câu 9.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x - 1)(x + 2)$ với mọi $x \in \mathbb{R}$. Số khoảng đồng biến của hàm số là

@@TAB@@\textbf{A.} $1$.@@TAB@@\textbf{B.} $3$.@@TAB@@\textbf{C.} $2$.@@TAB@@\textbf{D.} $4$.

\textbf{Lời giải.} Phương trình $f'(x) = 0 \iff x \in \{-2; 0; 1\}$. Xét dấu $f'(x)$, ta thấy $f'(x) > 0$ trên $(-2; 0)$ và $(1; +\infty)$. Vậy hàm số có đúng 2 khoảng đồng biến.

\textbf{==> Chọn đáp án C.}

% Câu 10 (BBT)
\textbf{Câu 10.} Cho hàm số $y = \dfrac{ax^2 + bx + c}{dx + e}$ ($ad \ne 0$), trong đó đa thức tử không chia hết cho đa thức mẫu. Bảng biến thiên của hàm số được cho như dưới đây:

@@CENTER_IMAGE_c10_bbt@@

Hàm số nào dưới đây có bảng biến thiên đã cho?

@@TAB@@\textbf{A.} $y = \dfrac{x^2 + 1}{x}$.@@TAB@@\textbf{B.} $y = \dfrac{x^2 - 1}{x}$.@@TAB@@\textbf{C.} $y = \dfrac{x^2 + 1}{x - 1}$.@@TAB@@\textbf{D.} $y = \dfrac{x^2 + 4}{x}$.

\textbf{Lời giải.} Từ bảng biến thiên, đồ thị có tiệm cận đứng $x = 0$, điểm cực đại $(-1; -2)$ và cực tiểu $(1; 2)$. Hàm số $y = \dfrac{x^2 + 1}{x} = x + \dfrac{1}{x}$ có tiệm cận đứng $x = 0$, đạo hàm $y' = \dfrac{x^2 - 1}{x^2} = 0 \iff x = \pm 1$, cực đại $(-1; -2)$ và cực tiểu $(1; 2)$, hoàn toàn phù hợp.

\textbf{==> Chọn đáp án A.}

% Câu 11
\textbf{Câu 11.} Cho hàm số $y = x + 2 + \dfrac{3}{x - 2}$. Phương trình đường tiệm cận xiên của đồ thị hàm số là

@@TAB@@\textbf{A.} $x = 2$.@@TAB@@\textbf{B.} $y = 2$.@@TAB@@\textbf{C.} $y = x + 2$.@@TAB@@\textbf{D.} $y = x - 2$.

\textbf{Lời giải.} Vì $\lim\limits_{x \to \pm\infty} [y - (x + 2)] = \lim\limits_{x \to \pm\infty} \dfrac{3}{x - 2} = 0$, nên đường thẳng $y = x + 2$ là đường tiệm cận xiên của đồ thị hàm số.

\textbf{==> Chọn đáp án C.}

% Câu 12
\textbf{Câu 12.} Cho hàm số $y = f(x)$ xác định trên $\mathbb{R} \setminus \{-1\}$ và có đạo hàm $f'(x) = \dfrac{x(x + 2)}{(x + 1)^2}$. Điểm cực đại của hàm số đã cho là

@@TAB@@\textbf{A.} $x = -1$.@@TAB@@\textbf{B.} $x = 0$.@@TAB@@\textbf{C.} $x = 2$.@@TAB@@\textbf{D.} $x = -2$.

\textbf{Lời giải.} Vì $(x + 1)^2 > 0$ với mọi $x \ne -1$ nên dấu của $f'(x)$ cùng dấu với $x(x + 2)$. Khi qua $x = -2$, $f'(x)$ đổi dấu từ dương sang âm, do đó hàm số đạt cực đại tại $x = -2$.

\textbf{==> Chọn đáp án D.}

@@SECTION_2_HEADER@@

% Phần 2 Câu 1 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_P2C1@@

\textbf{Câu 1.} Cho hàm số $y = \dfrac{2x + 1}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $y' = -\dfrac{3}{(x - 1)^2}$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên khoảng $(1; +\infty)$.

@@TAB@@\textbf{c)} Đồ thị có tiệm cận ngang $y = 2$.

@@TAB@@\textbf{d)} Hình bên là đồ thị của hàm số đã cho.

\textbf{Lời giải.}

- Ý a) Đúng: $y' = \dfrac{2(-1) - 1(1)}{(x - 1)^2} = -\dfrac{3}{(x - 1)^2} < 0, \; \forall x \ne 1$.

- Ý b) Sai: Vì $y' < 0$ trên $(1; +\infty)$ nên hàm số nghịch biến trên khoảng $(1; +\infty)$.

- Ý c) Đúng: $\lim\limits_{x \to \pm\infty} y = 2$ nên tiệm cận ngang là $y = 2$.

- Ý d) Sai: Với $x > 1$ thì $y = 2 + \dfrac{3}{x - 1} > 2$, nhánh đồ thị bên phải phải nằm trên đường $y = 2$, trong khi hình vẽ hiển thị nhánh bên phải nằm dưới đường $y = 2$.

\textbf{==> Đáp án: a) Đúng | b) Sai | c) Đúng | d) Sai.}

@@END_SIDE_BY_SIDE_P2C1@@

% Phần 2 Câu 2 (Side-by-side đồ thị)
@@START_SIDE_BY_SIDE_P2C2@@

\textbf{Câu 2.} Cho hàm số $y = \dfrac{ax^2 + bx + c}{dx + e}$ ($ad \ne 0$), trong đó đa thức tử không chia hết cho đa thức mẫu. Đồ thị của hàm số được cho như hình bên. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đồ thị có tiệm cận đứng $x = 1$.

@@TAB@@\textbf{b)} Đường tiệm cận xiên có phương trình $y = x + 2$.

@@TAB@@\textbf{c)} Đồ thị cắt trục tung tại điểm có tung độ bằng $2$.

@@TAB@@\textbf{d)} Hàm số nghịch biến trên toàn bộ $\mathbb{R}$.

\textbf{Lời giải.}

- Ý a) Đúng: Đồ thị có đường tiệm cận đứng là $x = 1$.

- Ý b) Đúng: Tiệm cận xiên đi qua $(0; 2)$ và $(-2; 0)$, có phương trình $y = x + 2$.

- Ý c) Sai: Đồ thị cắt trục tung tại điểm cực đại $(0; 1)$, tung độ bằng $1 \ne 2$.

- Ý d) Sai: Hàm số không xác định tại $x = 1$, không thể nghịch biến trên toàn bộ $\mathbb{R}$.

\textbf{==> Đáp án: a) Đúng | b) Đúng | c) Sai | d) Sai.}

@@END_SIDE_BY_SIDE_P2C2@@

% Phần 2 Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{(x - 2)^2}{x - 1}$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Tập xác định của hàm số là $\mathbb{R} \setminus \{1\}$.

@@TAB@@\textbf{b)} Hàm số nghịch biến trên khoảng $(-\infty; 0)$.

@@TAB@@\textbf{c)} Hàm số đạt cực tiểu tại $x = 0$.

@@TAB@@\textbf{d)} Đồ thị có tiệm cận xiên $y = x - 3$.

\textbf{Lời giải.}

Ta có $y = \dfrac{x^2 - 4x + 4}{x - 1} = x - 3 + \dfrac{1}{x - 1}$ và $y' = \dfrac{x(x - 2)}{(x - 1)^2}$.

- Ý a) Đúng: Điều kiện xác định $x \ne 1 \implies D = \mathbb{R} \setminus \{1\}$.

- Ý b) Sai: Với $x \in (-\infty; 0)$, $x(x - 2) > 0 \implies y' > 0$, hàm số đồng biến trên khoảng $(-\infty; 0)$.

- Ý c) Sai: Qua $x = 0$, $y'$ đổi dấu từ dương sang âm nên $x = 0$ là điểm cực đại.

- Ý d) Đúng: $\lim\limits_{x \to \pm\infty} [y - (x - 3)] = 0 \implies$ tiệm cận xiên là $y = x - 3$.

\textbf{==> Đáp án: a) Đúng | b) Sai | c) Đúng | d) Đúng.}

% Phần 2 Câu 4 (BBT)
\textbf{Câu 4.} Cho hàm số $y = f(x) = -x^3 + 3x + 1$. Xét tính đúng, sai của các phát biểu sau:

@@TAB@@\textbf{a)} Đạo hàm của hàm số là $f'(x) = 3(1 - x^2)$.

@@TAB@@\textbf{b)} Hàm số đồng biến trên khoảng $(-1; 1)$.

@@TAB@@\textbf{c)} Giá trị cực tiểu của hàm số bằng $1$.

@@TAB@@\textbf{d)} Bảng biến thiên dưới đây là bảng biến thiên của hàm số đã cho.

@@CENTER_IMAGE_p2_c4_bbt@@

\textbf{Lời giải.}

- Ý a) Đúng: $f'(x) = -3x^2 + 3 = 3(1 - x^2)$.

- Ý b) Đúng: Trên khoảng $(-1; 1)$, $1 - x^2 > 0 \implies f'(x) > 0$, hàm số đồng biến.

- Ý c) Sai: Tại $x = -1$, giá trị cực tiểu là $f(-1) = -1 \ne 1$.

- Ý d) Đúng: Bảng biến thiên thể hiện đúng chiều biến thiên và các giá trị cực trị $y_{\text{CT}} = -1$, $y_{\text{CĐ}} = 3$.

\textbf{==> Đáp án: a) Đúng | b) Đúng | c) Sai | d) Đúng.}

@@SECTION_3_HEADER@@

% Phần 3 Câu 1 (BBT)
\textbf{Câu 1.} Cho hàm số $y = f(x)$ có bảng biến thiên như dưới đây:

@@CENTER_IMAGE_p3_c1_bbt@@

Hàm số có bao nhiêu điểm cực trị?

\textbf{Lời giải.} Qua $x = -2$, $f'(x)$ đổi dấu từ dương sang âm nên $x = -2$ là điểm cực đại. Qua $x = 2$, $f'(x)$ đổi dấu từ âm sang dương nên $x = 2$ là điểm cực tiểu. Tại $x = 0$, hàm số không xác định nên không là điểm cực trị. Vậy hàm số có đúng $2$ điểm cực trị.

\textbf{==> Đáp án: 2.}

% Phần 3 Câu 2
\textbf{Câu 2.} Cho hàm số $y = f(x) = x^3 - 6x^2 + 9x + 1$. Tính hiệu giữa giá trị cực đại và giá trị cực tiểu của hàm số.

\textbf{Lời giải.} Ta có $f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3) = 0 \iff x = 1$ hoặc $x = 3$. Giá trị cực đại $y_{\text{CĐ}} = f(1) = 5$, giá trị cực tiểu $y_{\text{CT}} = f(3) = 1$. Hiệu giữa giá trị cực đại và giá trị cực tiểu là: $y_{\text{CĐ}} - y_{\text{CT}} = 5 - 1 = 4$.

\textbf{==> Đáp án: 4.}

% Phần 3 Câu 3
\textbf{Câu 3.} Cho hàm số $y = \dfrac{2x + 1}{x - 1}$. Gọi $I(a; b)$ là giao điểm hai đường tiệm cận. Tính $a + b$.

\textbf{Lời giải.} Đồ thị có tiệm cận đứng $x = 1$ và tiệm cận ngang $y = 2$. Giao điểm hai đường tiệm cận là $I(1; 2)$, suy ra $a = 1, b = 2$. Vậy $a + b = 1 + 2 = 3$.

\textbf{==> Đáp án: 3.}

% Phần 3 Câu 4
\textbf{Câu 4.} Cho hàm số $y = \dfrac{x^2 - 1}{x - 2}$. Tính tung độ giao điểm của đường tiệm cận xiên của đồ thị với trục tung.

\textbf{Lời giải.} Thực hiện phép chia: $y = \dfrac{x^2 - 1}{x - 2} = x + 2 + \dfrac{3}{x - 2}$. Đường tiệm cận xiên của đồ thị là $y = x + 2$. Cho $x = 0$ ta được $y = 2$. Vậy tung độ giao điểm của đường tiệm cận xiên với trục tung là $2$.

\textbf{==> Đáp án: 2.}

% Phần 3 Câu 5
\textbf{Câu 5.} Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = (x + 3)(x - 1)^2(x - 2)$ với mọi $x \in \mathbb{R}$. Tính tổng các giá trị của $x$ tại đó hàm số đạt cực trị.

\textbf{Lời giải.} Phương trình $f'(x) = 0$ có hai nghiệm đơn $x = -3$, $x = 2$ và một nghiệm bội hai $x = 1$. Đạo hàm $f'(x)$ chỉ đổi dấu qua các nghiệm đơn $x = -3$ và $x = 2$. Do đó hàm số đạt cực trị tại $x_1 = -3$ và $x_2 = 2$. Tổng các giá trị cực trị là: $(-3) + 2 = -1$.

\textbf{==> Đáp án: -1.}

% Phần 3 Câu 6
\textbf{Câu 6.} Cho hàm số $y = f(x) = x^3 - 3ax$, với $a > 0$. Biết hàm số đạt cực tiểu tại $x = 3$. Tính $a$.

\textbf{Lời giải.} Ta có $f'(x) = 3(x^2 - a) = 0 \iff x = \pm\sqrt{a}$ (do $a > 0$). Vì $f''(x) = 6x \implies f''(\sqrt{a}) = 6\sqrt{a} > 0$ nên hàm số đạt cực tiểu tại $x = \sqrt{a}$. Theo giả thiết hàm số đạt cực tiểu tại $x = 3$, suy ra $\sqrt{a} = 3 \iff a = 9$.

\textbf{==> Đáp án: 9.}

\vspace{0.4cm}
\begin{center}
\textbf{------ HẾT ------}
\end{center}

\end{document}
"""

def build_0103_doc(tex_str, output_path, is_solution=False):
    temp_tex = os.path.join(CURRENT_DIR, f"temp_0103_{'hdg' if is_solution else 'de'}.tex")
    temp_docx = os.path.join(CURRENT_DIR, f"temp_0103_{'hdg' if is_solution else 'de'}.docx")
    
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
        
        r_r = f_p.add_run("Trang Mã đề 0103")
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
    
    for p in list(doc.paragraphs):
        if "@@DOCUMENT_HEADER@@" in p.text:
            insert_header_and_code(doc, p, "0103", is_solution)
        elif "@@SECTION_1_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn.", "Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.")
        elif "@@SECTION_2_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN II. Câu trắc nghiệm đúng sai.", "Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")
        elif "@@SECTION_3_HEADER@@" in p.text:
            insert_section_header(doc, p, "PHẦN III. Câu trắc nghiệm yêu cầu trả lời ngắn.", "Thí sinh trả lời từ câu 1 đến câu 6.")
            
    # Side-by-side configurations
    sbs_configs = [
        ("C1", "c1_hinh.png", 4.8),
        ("P2C1", "p2_c1_hinh.png", 5.0),
        ("P2C2", "p2_c2_hinh.png", 4.8),
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
                
            img_path = os.path.join(HINH_ANH_0103, img_name)
            cell_1_p = cell_1.paragraphs[0]
            cell_1_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cell_1_p.paragraph_format.space_before = Pt(0)
            cell_1_p.paragraph_format.space_after = Pt(0)
            if os.path.exists(img_path):
                cell_1_p.add_run().add_picture(img_path, width=Cm(img_w))
                
            start_p._p.getparent().remove(start_p._p)
            end_p._p.getparent().remove(end_p._p)
            
    # Centered Images & Boxes
    for p in list(doc.paragraphs):
        for img_tag in ["c2_bbt", "c10_bbt", "p2_c4_bbt", "p3_c1_bbt"]:
            token = f"@@CENTER_IMAGE_{img_tag}@@"
            if token in p.text:
                img_path = os.path.join(HINH_ANH_0103, f"{img_tag}.png")
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
    print("=== TIẾN HÀNH XUẤT BẢN MÃ ĐỀ 0103 (ĐỀ BÀI + LỜI GIẢI CHI TIẾT) ===")
    build_0103_doc(tex_de_0103, OUTPUT_DE_0103, is_solution=False)
    build_0103_doc(tex_hdg_0103, OUTPUT_HDG_0103, is_solution=True)
