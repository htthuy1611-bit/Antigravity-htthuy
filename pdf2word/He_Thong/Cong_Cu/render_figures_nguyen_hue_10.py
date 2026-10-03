import os
import sys
import subprocess
import pymupdf as fitz

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"c:\AnTiGraViTy-htthuy\pdf2word"
OUT_DIR = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", "Nguyen_Hue_10")
LATEX_DIR = os.path.join(BASE_DIR, "He_Thong", "LaTeX", "Nguyen_Hue_10")
SCRATCH_DIR = os.path.join(BASE_DIR, "He_Thong", "Cong_Cu", "scratch_nguyen_hue_10")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(LATEX_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

TIKZ_FIGURES = {
    "c7_rac": r"""
\begin{tikzpicture}[scale=0.8]
  % Bin body
  \draw[very thick] (-0.7,0.8) -- (-0.5,-0.9) -- (0.5,-0.9) -- (0.7,0.8) -- cycle;
  % Vertical ribs on bin
  \draw[thick] (-0.3,0.7) -- (-0.22,-0.8);
  \draw[thick] (0,0.7) -- (0,-0.8);
  \draw[thick] (0.3,0.7) -- (0.22,-0.8);
  % Bin lid
  \draw[very thick,rounded corners=1pt] (-0.85,0.8) -- (-0.85,1.05) -- (0.85,1.05) -- (0.85,0.8) -- cycle;
  \draw[very thick] (-0.3,1.05) arc (180:0:0.3 and 0.18);
  % Wheels
  \draw[very thick,fill=white] (-0.45,-1.05) circle (0.18);
  \draw[very thick,fill=white] (0.45,-1.05) circle (0.18);
  \draw[fill=black] (-0.45,-1.05) circle (0.06);
  \draw[fill=black] (0.45,-1.05) circle (0.06);
  % Horizontal bar below wheels (standard WEEE requirement)
  \fill[black] (-0.9,-1.4) rectangle (0.9,-1.25);
  % Thick Cross (X) over bin
  \draw[line width=2.5pt] (-1.1,1.15) -- (1.1,-1.05);
  \draw[line width=2.5pt] (1.1,1.15) -- (-1.1,-1.05);
\end{tikzpicture}
""",
    "c8_dothidt": r"""
\begin{tikzpicture}[>=stealth,scale=1.1]
  \draw[->,thick] (-0.2,0) -- (4.5,0) node[above] {$t$};
  \draw[->,thick] (0,-0.2) -- (0,2.8) node[right] {$d$};
  \node[below left] at (0,0) {$0$};
  \coordinate (A) at (1.8,2.0);
  \coordinate (B) at (3.8,2.0);
  \draw[very thick] (0,0) -- (A) -- (B);
  \draw[dashed] (1.8,0) node[below] {$t_1$} -- (A);
  \draw[dashed] (3.8,0) node[below] {$t_2$} -- (B);
\end{tikzpicture}
""",
    "c15_dothi4": r"""
\begin{tikzpicture}[>=stealth,scale=0.9]
  % Graph I: d - t linear through origin
  \begin{scope}[shift={(0,0)}]
    \draw[->,thick] (-0.2,0) -- (2.3,0) node[right] {$t$};
    \draw[->,thick] (0,-0.2) -- (0,2.2) node[above] {$d$};
    \node[below left] at (0,0) {$O$};
    \draw[very thick] (0,0) -- (1.8,1.8);
    \node[below] at (1.0,-0.4) {(I)};
  \end{scope}
  
  % Graph II: d - t horizontal
  \begin{scope}[shift={(3.2,0)}]
    \draw[->,thick] (-0.2,0) -- (2.3,0) node[right] {$t$};
    \draw[->,thick] (0,-0.2) -- (0,2.2) node[above] {$d$};
    \node[below left] at (0,0) {$O$};
    \draw[very thick] (0,1.2) -- (1.8,1.2);
    \node[below] at (1.0,-0.4) {(II)};
  \end{scope}

  % Graph III: v - t linear through origin
  \begin{scope}[shift={(6.4,0)}]
    \draw[->,thick] (-0.2,0) -- (2.3,0) node[right] {$t$};
    \draw[->,thick] (0,-0.2) -- (0,2.2) node[above] {$v$};
    \node[below left] at (0,0) {$O$};
    \draw[very thick] (0,0) -- (1.8,1.8);
    \node[below] at (1.0,-0.4) {(III)};
  \end{scope}

  % Graph IV: v - t horizontal
  \begin{scope}[shift={(9.6,0)}]
    \draw[->,thick] (-0.2,0) -- (2.3,0) node[right] {$t$};
    \draw[->,thick] (0,-0.2) -- (0,2.2) node[above] {$v$};
    \node[below left] at (0,0) {$O$};
    \draw[very thick] (0,1.2) -- (1.8,1.2);
    \node[below] at (1.0,-0.4) {(IV)};
  \end{scope}
\end{tikzpicture}
""",
    "p2_c3_dothi3": r"""
\begin{tikzpicture}[>=stealth,scale=1.0]
  % Hinh a
  \begin{scope}[shift={(0,0)}]
    \draw[->,thick] (-0.2,0) -- (2.8,0) node[right] {$t$};
    \draw[->,thick] (0,-0.2) -- (0,2.5) node[above] {$v$};
    \node[below left] at (0,0) {$0$};
    \draw[very thick] (0,0) -- (2.0,2.0);
    \node[below] at (1.2,-0.5) {\textbf{Hình a}};
  \end{scope}
  
  % Hinh b
  \begin{scope}[shift={(3.8,0)}]
    \draw[->,thick] (-0.2,0) -- (2.8,0) node[right] {$t$};
    \draw[->,thick] (0,-0.2) -- (0,2.5) node[above] {$v$};
    \node[below left] at (0,0) {$0$};
    \node[left] at (0,0.8) {$v_0$};
    \draw[very thick] (0,0.8) -- (2.0,2.0);
    \node[below] at (1.2,-0.5) {\textbf{Hình b}};
  \end{scope}

  % Hinh c
  \begin{scope}[shift={(7.6,0)}]
    \draw[->,thick] (-0.2,0) -- (2.8,0) node[right] {$t$};
    \draw[->,thick] (0,-0.2) -- (0,2.5) node[above] {$v$};
    \node[below left] at (0,0) {$0$};
    \node[left] at (0,1.8) {$v_0$};
    \draw[very thick] (0,1.8) -- (2.0,0);
    \node[below] at (1.2,-0.5) {\textbf{Hình c}};
  \end{scope}
\end{tikzpicture}
""",
    "p3_c1_dothi": r"""
\begin{tikzpicture}[>=stealth,x=1.1cm,y=0.9cm]
  % Grid
  \draw[dashed,gray!60] (0,0) grid[xstep=1,ystep=1] (5,3);
  % Axes
  \draw[->,thick] (-0.3,0) -- (5.6,0) node[right] {$t(\text{s})$};
  \draw[->,thick] (0,-0.3) -- (0,3.5) node[above] {$d(\text{m})$};
  \node[below left] at (0,0) {$0$};
  \foreach \x in {1,2,3,4,5} \node[below] at (\x,0) {$\x$};
  \node[left] at (0,1) {$10$};
  \node[left] at (0,2) {$20$};
  \node[left] at (0,3) {$30$};
  % Graph line
  \draw[line width=1.5pt] (0,0) -- (2,3) -- (4,2);
  % Dashed lines
  \draw[thick,dashed] (2,0) -- (2,3) -- (0,3);
  \draw[thick,dashed] (4,0) -- (4,2) -- (0,2);
\end{tikzpicture}
""",
    "p3_c3_dothi": r"""
\begin{tikzpicture}[>=stealth,x=0.25cm,y=0.08cm]
  \draw[->,thick] (-1.5,0) -- (33,0) node[above] {$t(\text{s})$};
  \draw[->,thick] (0,-3) -- (0,36) node[above] {$v(\text{m/s})$};
  \node[below left] at (0,0) {$0$};
  \foreach \x in {5,10,15,20,25,30} \node[below] at (\x,0) {\scriptsize $\x$};
  \node[left] at (0,30) {$30$};
  \draw[dashed,thick] (0,30) -- (15,30);
  \draw[dashed,thick] (10,0) -- (10,30);
  \draw[dashed,thick] (15,0) -- (15,30);
  \draw[line width=1.5pt] (0,0) -- (10,30) -- (15,30) -- (30,0);
\end{tikzpicture}
""",
    "p3_c5_dothi": r"""
\begin{tikzpicture}[>=stealth,x=0.045cm,y=0.035cm]
  % Grid
  \draw[dashed,gray!70] (0,0) grid[xstep=40,ystep=40] (160,120);
  % Axes
  \draw[->,thick] (-8,0) -- (180,0) node[right] {$t(\text{s})$};
  \draw[->,thick] (0,-8) -- (0,140) node[above] {$v(\text{cm/s})$};
  \node[below left] at (0,0) {$0$};
  \foreach \x in {40,80,120,160} \node[below] at (\x,0) {\scriptsize $\x$};
  \foreach \y in {40,80,120} \node[left] at (0,\y) {\scriptsize $\y$};
  % Points and Labels
  \node[below right] at (0,40) {$A$};
  \node[above] at (40,120) {$B$};
  \node[above left] at (40,0) {$C$};
  \node[above] at (80,120) {$D$};
  \node[above left] at (80,0) {$E$};
  \node[above right] at (160,0) {$F$};
  % Graph line
  \draw[line width=1.5pt] (0,40) -- (40,120) -- (80,120) -- (160,0);
\end{tikzpicture}
"""
}

tex_template = r"""\documentclass[border=3pt]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\begin{document}
%s
\end{document}
"""

print("[*] Bắt đầu biên dịch 7 hình TikZ cho đề Nguyễn Huệ...")
for name, tikz_code in TIKZ_FIGURES.items():
    tex_path = os.path.join(SCRATCH_DIR, f"{name}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_template % tikz_code)
    
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{name}.tex"]
    res = subprocess.run(cmd, cwd=SCRATCH_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="ignore")
    
    pdf_path = os.path.join(SCRATCH_DIR, f"{name}.pdf")
    if os.path.exists(pdf_path):
        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=300)
        
        out_png = os.path.join(OUT_DIR, f"{name}.png")
        latex_png = os.path.join(LATEX_DIR, f"{name}.png")
        pix.save(out_png)
        pix.save(latex_png)
        print(f"[THÀNH CÔNG] Rendered: {name}.png ({pix.width}x{pix.height} px)")
    else:
        print(f"[LỖI] Không thể compile {name}:")
        print(res.stdout[-600:])

print("\nHoàn tất kết xuất 100% hình ảnh vector TikZ sắc nét!")
