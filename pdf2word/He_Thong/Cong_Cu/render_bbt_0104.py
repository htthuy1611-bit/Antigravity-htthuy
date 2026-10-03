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
OUT_DIR = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", "Bao_Thang_3", "0104")
LATEX_DIR = os.path.join(BASE_DIR, "He_Thong", "LaTeX", "Bao_Thang_3", "0104")
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
  \node at (4.0,-0.3) {$0$};
  \node at (6.0,-0.3) {$4$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.1,-0.9) {$+$};
  \node at (4.0,-0.9) {$0$};
  \node at (5.0,-0.9) {$-$};
  \node at (6.0,-0.9) {$0$};
  \node at (7.0,-0.9) {$+$};
  \node (p1) at (2.2,-2.0) {$-\infty$};
  \node (p2) at (4.0,-1.4) {$7$};
  \node (p3) at (6.0,-2.0) {$-1$};
  \node (p4) at (7.8,-1.4) {$+\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p3) -- (p4);
\end{tikzpicture}
""",
    "c12_bbt": r"""
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
\end{tikzpicture}
""",
    "p2_c1_bbt": r"""
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
  \node at (3.8,-0.3) {$-3$};
  \node at (5.35,-0.3) {$-2$};
  \node at (6.9,-0.3) {$-1$};
  \node at (8.6,-0.3) {$+\infty$};
  \node at (3.0,-0.9) {$+$};
  \node at (3.8,-0.9) {$0$};
  \node at (4.6,-0.9) {$-$};
  \node at (6.1,-0.9) {$-$};
  \node at (6.9,-0.9) {$0$};
  \node at (7.8,-0.9) {$+$};
  \node (p1) at (2.1,-2.0) {$-\infty$};
  \node (p2) at (3.8,-1.4) {$-4$};
  \node (p3) at (4.9,-2.0) {$-\infty$};
  \node (p4) at (5.8,-1.4) {$+\infty$};
  \node (p5) at (6.9,-2.0) {$0$};
  \node (p6) at (8.6,-1.4) {$+\infty$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p2) -- (p3);
  \draw[->] (p4) -- (p5);
  \draw[->] (p5) -- (p6);
\end{tikzpicture}
""",
    "p3_c6_bbt": r"""
\begin{tikzpicture}[>=stealth,scale=1]
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
  \node at (5.06,-0.3) {$-2$};
  \node at (7.8,-0.3) {$+\infty$};
  \node at (3.5,-0.9) {$-$};
  \node at (6.5,-0.9) {$-$};
  \node (p1) at (2.2,-1.4) {$-1$};
  \node (p2) at (4.7,-2.0) {$-\infty$};
  \node (p3) at (5.5,-1.4) {$+\infty$};
  \node (p4) at (7.8,-2.0) {$-1$};
  \draw[->] (p1) -- (p2);
  \draw[->] (p3) -- (p4);
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

scratch_dir = os.path.join(BASE_DIR, "He_Thong", "Cong_Cu", "scratch_0104")
os.makedirs(scratch_dir, exist_ok=True)

# 1. Render TikZ BBTs
for name, tikz_code in BBT_TIKZ.items():
    tex_path = os.path.join(scratch_dir, f"{name}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_template % tikz_code)
    
    print(f"[*] Đang biên dịch BBT {name} qua pdflatex...")
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{name}.tex"]
    res = subprocess.run(cmd, cwd=scratch_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="ignore")
    
    pdf_path = os.path.join(scratch_dir, f"{name}.pdf")
    if os.path.exists(pdf_path):
        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=300)
        
        out_png = os.path.join(OUT_DIR, f"{name}.png")
        latex_png = os.path.join(LATEX_DIR, f"{name}.png")
        pix.save(out_png)
        pix.save(latex_png)
        print(f"[THÀNH CÔNG] Rendered BBT: {name}.png ({pix.width}x{pix.height})")
    else:
        print(f"[LỖI] Không thể compile {name}:", res.stdout[-800:])

# 2. Crop graphs from original PDF
print("\n[*] Đang crop 3 đồ thị hàm số từ PDF gốc...")
orig_pdf = os.path.join(BASE_DIR, "De_Goc", "de-khao-sat-toan-12-nam-2026-2027-truong-thpt-bao-thang-3-lao-cai.pdf")
doc_orig = fitz.open(orig_pdf)

crops = {
    # Page 11 (index 10): Câu 9
    "c9_hinh.png": (10, fitz.Rect(240, 568, 355, 666)),
    # Page 12 (index 11): Câu 3 Phần II
    "p2_c3_hinh.png": (11, fitz.Rect(240, 528, 365, 626)),
    # Page 13 (index 12): Câu 4 Phần II
    "p2_c4_hinh.png": (12, fitz.Rect(240, 138, 355, 245)),
}

for name, (page_idx, rect) in crops.items():
    page = doc_orig[page_idx]
    mat = fitz.Matrix(4.0, 4.0)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    
    out_png = os.path.join(OUT_DIR, name)
    latex_png = os.path.join(LATEX_DIR, name)
    pix.save(out_png)
    pix.save(latex_png)
    print(f"[THÀNH CÔNG] Cropped graph: {name} ({pix.width}x{pix.height})")

print("\nHoàn tất toàn bộ 7 hình ảnh (4 BBT + 3 đồ thị) cho Mã đề 0104!")
