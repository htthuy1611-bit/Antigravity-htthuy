import os
import subprocess
import fitz

BASE_DIR = r"c:\AnTiGraViTy-htthuy\pdf2word"
OUT_DIR = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", "Bao_Thang_3", "0103")
LATEX_DIR = os.path.join(BASE_DIR, "He_Thong", "LaTeX", "Bao_Thang_3", "0103")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(LATEX_DIR, exist_ok=True)

BBT_TIKZ = {
    "c2_bbt": r"""
\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (8.5,-2.2);
  \draw[thick] (0,-0.6) -- (8.5,-0.6);
  \draw[thick] (0,-1.2) -- (8.5,-1.2);
  \draw[thick] (1.6,0) -- (1.6,-2.2);
  \node at (0.8,-0.3) {$x$};
  \node at (0.8,-0.9) {$f'(x)$};
  \node at (0.8,-1.7) {$f(x)$};
  \node at (2.2,-0.3) {$-\infty$};
  \node at (4.0,-0.3) {$-1$};
  \node at (6.0,-0.3) {$2$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.1,-0.9) {$-$};
  \node at (4.0,-0.9) {$0$};
  \node at (5.0,-0.9) {$+$};
  \node at (6.0,-0.9) {$0$};
  \node at (7.0,-0.9) {$-$};
  \node (p1) at (2.2,-1.4) {$+\infty$};
  \node (p2) at (4.0,-2.0) {$-3$};
  \node (p3) at (6.0,-1.4) {$4$};
  \node (p4) at (7.8,-2.0) {$-\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}
""",
    "c10_bbt": r"""
\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (9.3,-2.2);
  \draw[thick] (0,-0.6) -- (9.3,-0.6);
  \draw[thick] (0,-1.2) -- (9.3,-1.2);
  \draw[thick] (1.5,0) -- (1.5,-2.2);
  \draw[thick] (5.32,-0.6) -- (5.32,-2.2);
  \draw[thick] (5.38,-0.6) -- (5.38,-2.2);
  \node at (0.75,-0.3) {$x$};
  \node at (0.75,-0.9) {$f'(x)$};
  \node at (0.75,-1.7) {$f(x)$};
  \node at (2.1,-0.3) {$-\infty$};
  \node at (3.8,-0.3) {$-1$};
  \node at (5.35,-0.3) {$0$};
  \node at (6.9,-0.3) {$1$};
  \node at (8.6,-0.3) {$+\infty$};
  \node at (3.0,-0.9) {$+$};
  \node at (3.8,-0.9) {$0$};
  \node at (4.6,-0.9) {$-$};
  \node at (6.1,-0.9) {$-$};
  \node at (6.9,-0.9) {$0$};
  \node at (7.8,-0.9) {$+$};
  \node (p1) at (2.1,-2.0) {$-\infty$};
  \node (p2) at (3.8,-1.4) {$-2$};
  \node (p3) at (4.9,-2.0) {$-\infty$};
  \node (p4) at (5.8,-1.4) {$+\infty$};
  \node (p5) at (6.9,-2.0) {$2$};
  \node (p6) at (8.6,-1.4) {$+\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p4) -- (p5);
  \draw[->] (p5) -- (p6);
\end{tikzpicture}
""",
    "p2_c4_bbt": r"""
\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (8.5,-2.2);
  \draw[thick] (0,-0.6) -- (8.5,-0.6);
  \draw[thick] (0,-1.2) -- (8.5,-1.2);
  \draw[thick] (1.6,0) -- (1.6,-2.2);
  \node at (0.8,-0.3) {$x$};
  \node at (0.8,-0.9) {$f'(x)$};
  \node at (0.8,-1.7) {$f(x)$};
  \node at (2.2,-0.3) {$-\infty$};
  \node at (4.0,-0.3) {$-1$};
  \node at (6.0,-0.3) {$1$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.1,-0.9) {$-$};
  \node at (4.0,-0.9) {$0$};
  \node at (5.0,-0.9) {$+$};
  \node at (6.0,-0.9) {$0$};
  \node at (7.0,-0.9) {$-$};
  \node (p1) at (2.2,-1.4) {$+\infty$};
  \node (p2) at (4.0,-2.0) {$-1$};
  \node (p3) at (6.0,-1.4) {$3$};
  \node (p4) at (7.8,-2.0) {$-\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}
""",
    "p3_c1_bbt": r"""
\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (9.3,-2.2);
  \draw[thick] (0,-0.6) -- (9.3,-0.6);
  \draw[thick] (0,-1.2) -- (9.3,-1.2);
  \draw[thick] (1.5,0) -- (1.5,-2.2);
  \draw[thick] (5.32,-0.6) -- (5.32,-2.2);
  \draw[thick] (5.38,-0.6) -- (5.38,-2.2);
  \node at (0.75,-0.3) {$x$};
  \node at (0.75,-0.9) {$f'(x)$};
  \node at (0.75,-1.7) {$f(x)$};
  \node at (2.1,-0.3) {$-\infty$};
  \node at (3.8,-0.3) {$-2$};
  \node at (5.35,-0.3) {$0$};
  \node at (6.9,-0.3) {$2$};
  \node at (8.6,-0.3) {$+\infty$};
  \node at (3.0,-0.9) {$+$};
  \node at (3.8,-0.9) {$0$};
  \node at (4.6,-0.9) {$-$};
  \node at (6.1,-0.9) {$-$};
  \node at (6.9,-0.9) {$0$};
  \node at (7.8,-0.9) {$+$};
  \node (p1) at (2.1,-2.0) {$-\infty$};
  \node (p2) at (3.8,-1.4) {$-3$};
  \node (p3) at (4.9,-2.0) {$-\infty$};
  \node (p4) at (5.8,-1.4) {$+\infty$};
  \node (p5) at (6.9,-2.0) {$5$};
  \node (p6) at (8.6,-1.4) {$+\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p4) -- (p5);
  \draw[->] (p5) -- (p6);
\end{tikzpicture}
"""
}

tex_template = r"""\documentclass[border=2pt]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\begin{document}
%s
\end{document}
"""

scratch_dir = os.path.join(BASE_DIR, "He_Thong", "Cong_Cu", "scratch_0103")
os.makedirs(scratch_dir, exist_ok=True)

for name, tikz_code in BBT_TIKZ.items():
    tex_path = os.path.join(scratch_dir, f"{name}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_template % tikz_code)
    
    print(f"[*] Compiling {name} via pdflatex...")
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{name}.tex"]
    res = subprocess.run(cmd, cwd=scratch_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="ignore")
    
    pdf_path = os.path.join(scratch_dir, f"{name}.pdf")
    if os.path.exists(pdf_path):
        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=300)
        
        # Save to both Hinh_Anh and LaTeX folder
        out_png = os.path.join(OUT_DIR, f"{name}.png")
        latex_png = os.path.join(LATEX_DIR, f"{name}.png")
        pix.save(out_png)
        pix.save(latex_png)
        print(f"[THÀNH CÔNG] Rendered: {name}.png ({pix.width}x{pix.height})")
    else:
        print(f"[LỖI] Cannot compile {name}. Output:\n", res.stdout[-800:])

print("\nHoàn tất kết xuất 4 bảng biến thiên cho Mã đề 0103!")
