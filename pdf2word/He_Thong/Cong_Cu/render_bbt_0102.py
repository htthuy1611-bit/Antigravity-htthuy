import subprocess
import os
import pymupdf as fitz

bbt_dict = {
    'c1_bbt': r"""\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (8.5,-2.2);
  \draw[thick] (0,-0.6) -- (8.5,-0.6);
  \draw[thick] (0,-1.2) -- (8.5,-1.2);
  \draw[thick] (1.6,0) -- (1.6,-2.2);
  \node at (0.8,-0.3) {$x$};
  \node at (0.8,-0.9) {$f'(x)$};
  \node at (0.8,-1.7) {$f(x)$};
  \node at (2.2,-0.3) {$-\infty$};
  \node at (4.0,-0.3) {$-2$};
  \node at (6.0,-0.3) {$1$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.1,-0.9) {$+$};
  \node at (4.0,-0.9) {$0$};
  \node at (5.0,-0.9) {$-$};
  \node at (6.0,-0.9) {$0$};
  \node at (7.0,-0.9) {$+$};
  \node (p1) at (2.2,-2.0) {$-\infty$};
  \node (p2) at (4.0,-1.4) {$5$};
  \node (p3) at (6.0,-2.0) {$-4$};
  \node (p4) at (7.8,-1.4) {$+\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}""",

    'c10_hinh': r"""\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (8.5,-2.2);
  \draw[thick] (0,-0.6) -- (8.5,-0.6);
  \draw[thick] (0,-1.2) -- (8.5,-1.2);
  \draw[thick] (1.6,0) -- (1.6,-2.2);
  \draw[thick] (5.03,-0.6) -- (5.03,-2.2);
  \draw[thick] (5.09,-0.6) -- (5.09,-2.2);
  \node at (0.8,-0.3) {$x$};
  \node at (0.8,-0.9) {$f'(x)$};
  \node at (0.8,-1.7) {$f(x)$};
  \node at (2.2,-0.3) {$-\infty$};
  \node at (5.06,-0.3) {$1$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.5,-0.9) {$-$};
  \node at (6.5,-0.9) {$-$};
  \node (p1) at (2.2,-1.4) {$2$};
  \node (p2) at (4.7,-2.0) {$-\infty$};
  \node (p3) at (5.5,-1.4) {$+\infty$};
  \node (p4) at (7.8,-2.0) {$2$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}""",

    'c12_bbt': r"""\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (8.5,-2.2);
  \draw[thick] (0,-0.6) -- (8.5,-0.6);
  \draw[thick] (0,-1.2) -- (8.5,-1.2);
  \draw[thick] (1.6,0) -- (1.6,-2.2);
  \draw[thick] (5.03,-0.6) -- (5.03,-2.2);
  \draw[thick] (5.09,-0.6) -- (5.09,-2.2);
  \node at (0.8,-0.3) {$x$};
  \node at (0.8,-0.9) {$f'(x)$};
  \node at (0.8,-1.7) {$f(x)$};
  \node at (2.2,-0.3) {$-\infty$};
  \node at (5.06,-0.3) {$-1$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.5,-0.9) {$+$};
  \node at (6.5,-0.9) {$+$};
  \node (p1) at (2.2,-2.0) {$-2$};
  \node (p2) at (4.7,-1.4) {$+\infty$};
  \node (p3) at (5.5,-2.0) {$-\infty$};
  \node (p4) at (7.8,-1.4) {$-2$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}""",

    'p2_c1_bbt': r"""\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (8.5,-2.2);
  \draw[thick] (0,-0.6) -- (8.5,-0.6);
  \draw[thick] (0,-1.2) -- (8.5,-1.2);
  \draw[thick] (1.6,0) -- (1.6,-2.2);
  \node at (0.8,-0.3) {$x$};
  \node at (0.8,-0.9) {$f'(x)$};
  \node at (0.8,-1.7) {$f(x)$};
  \node at (2.2,-0.3) {$-\infty$};
  \node at (4.0,-0.3) {$0$};
  \node at (6.0,-0.3) {$2$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.1,-0.9) {$+$};
  \node at (4.0,-0.9) {$0$};
  \node at (5.0,-0.9) {$-$};
  \node at (6.0,-0.9) {$0$};
  \node at (7.0,-0.9) {$+$};
  \node (p1) at (2.2,-2.0) {$-\infty$};
  \node (p2) at (4.0,-1.4) {$2$};
  \node (p3) at (6.0,-2.0) {$-2$};
  \node (p4) at (7.8,-1.4) {$+\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}""",

    'p3_c3_bbt': r"""\begin{tikzpicture}[>=stealth,scale=1]
  \draw[thick] (0,0) rectangle (8.5,-2.2);
  \draw[thick] (0,-0.6) -- (8.5,-0.6);
  \draw[thick] (0,-1.2) -- (8.5,-1.2);
  \draw[thick] (1.6,0) -- (1.6,-2.2);
  \node at (0.8,-0.3) {$x$};
  \node at (0.8,-0.9) {$f'(x)$};
  \node at (0.8,-1.7) {$f(x)$};
  \node at (2.2,-0.3) {$-\infty$};
  \node at (4.0,-0.3) {$-2$};
  \node at (6.0,-0.3) {$1$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.1,-0.9) {$+$};
  \node at (4.0,-0.9) {$0$};
  \node at (5.0,-0.9) {$-$};
  \node at (6.0,-0.9) {$0$};
  \node at (7.0,-0.9) {$+$};
  \node (p1) at (2.2,-2.0) {$-\infty$};
  \node (p2) at (4.0,-1.4) {$5$};
  \node (p3) at (6.0,-2.0) {$-4$};
  \node (p4) at (7.8,-1.4) {$+\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}"""
}

tmp_dir = os.path.abspath('scratch_0102')
os.makedirs(tmp_dir, exist_ok=True)
out_dir = os.path.abspath('He_Thong/Hinh_Anh/Bao_Thang_3/0102')

for name, tikz_code in bbt_dict.items():
    tex_path = os.path.join(tmp_dir, f'{name}.tex')
    tex_src = r'''\documentclass[border=2pt]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\begin{document}
''' + tikz_code + r'''
\end{document}
'''
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_src)
    
    subprocess.run(['pdflatex', '-interaction=nonstopmode', f'{name}.tex'], cwd=tmp_dir, stdout=subprocess.DEVNULL)
    pdf_path = os.path.join(tmp_dir, f'{name}.pdf')
    doc = fitz.open(pdf_path)
    pix = doc[0].get_pixmap(dpi=300)
    
    out_file = os.path.join(out_dir, f'{name}.png')
    pix.save(out_file)
    print(f'Rendered 0102 BBT: {name}.png at 300 DPI: {pix.width}x{pix.height}')
