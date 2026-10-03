import os, subprocess, fitz

out_latex_dir = r"c:\AnTiGraViTy-htthuy\pdf2word\He_Thong\LaTeX\TN9_Chuong5_Bai17"
out_img_dir = r"c:\AnTiGraViTy-htthuy\pdf2word\He_Thong\Hinh_Anh\TN9_Chuong5_Bai17"
scratch_dir = r"c:\AnTiGraViTy-htthuy\pdf2word\He_Thong\Cong_Cu\scratch_tn9_bai17"
os.makedirs(out_latex_dir, exist_ok=True)
os.makedirs(out_img_dir, exist_ok=True)
os.makedirs(scratch_dir, exist_ok=True)

tikz_figures = {
    "fig_c2": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=1.2, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (O1) at (0,0);
  \coordinate (O2) at (3.2,0);
  \def\rOne{2}
  \def\rTwo{1.2}
  \coordinate (A) at (2,0);
  
  \draw[blue!70!black, thick] (O1) circle (\rOne);
  \draw[red!70!black, thick] (O2) circle (\rTwo);
  
  \coordinate (B) at ($(O1)+(75.5225:\rOne)$);
  \coordinate (C) at ($(O2)+(75.5225:\rTwo)$);
  
  \draw[thick, green!50!black] ($(B)!-0.35!(C)$) -- ($(C)!-0.35!(B)$) node[right] {$d$};
  
  \coordinate (M) at ($(B)!0.5!(C)$);
  \draw[dashed, orange!80!black] (A) -- (M);
  
  \draw[gray, thin] (O1) -- (B);
  \draw[gray, thin] (O2) -- (C);
  \draw[gray, thin] (O1) -- (O2);
  
  \draw[thick, purple] (A) -- (B) -- (C) -- cycle;
  
  \draw pic[draw, angle radius=2.5mm] {right angle = O1--B--C};
  \draw pic[draw, angle radius=2.5mm] {right angle = O2--C--B};
  \draw pic[draw, angle radius=3mm, red] {right angle = B--A--C};
  
  \fill (O1) circle (1.2pt) node[below] {$O_1$};
  \fill (O2) circle (1.2pt) node[below] {$O_2$};
  \fill (A) circle (1.2pt) node[below=2pt] {$A$};
  \fill (B) circle (1.2pt) node[above left] {$B$};
  \fill (C) circle (1.2pt) node[above right] {$C$};
  \fill (M) circle (1.2pt) node[above] {$M$};
  \node[above left] at ($(O1)+(135:\rOne)$) {$(O_1)$};
  \node[above right] at ($(O2)+(45:\rTwo)$) {$(O_2)$};
\end{tikzpicture}
\end{document}
""",

    "fig_c4": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=1.1, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (O) at (0,0);
  \def\R{2.2}
  \coordinate (O') at (2.2,0);
  \def\r{1.8}
  \coordinate (C) at (-2.2,0);
  
  \draw[blue!70!black, thick] (O) circle (\R);
  \draw[red!70!black, thick] (O') circle (\r);
  
  \pgfmathsetmacro{\xint}{(2.2*2.2 - 1.8*1.8 + 2.2*2.2)/(2*2.2)}
  \pgfmathsetmacro{\yint}{sqrt(2.2*2.2 - \xint*\xint)}
  \coordinate (A) at (\xint, \yint);
  \coordinate (B) at (\xint, -\yint);
  
  \draw[thick] (C) -- (O');
  \draw[thick, green!50!black] (C) -- (A) -- (O');
  \draw[thick, green!50!black] (C) -- (B) -- (O');
  \draw[dashed, purple] (A) -- (B);
  
  \draw pic[draw, angle radius=3mm, red] {right angle = C--A--O'};
  \draw pic[draw, angle radius=3mm, red] {right angle = C--B--O'};
  
  \fill (O) circle (1.2pt) node[below] {$O$};
  \fill (O') circle (1.2pt) node[below] {$O'$};
  \fill (C) circle (1.2pt) node[left] {$C$};
  \fill (A) circle (1.2pt) node[above] {$A$};
  \fill (B) circle (1.2pt) node[below] {$B$};
  \node[above left] at ($(O)+(135:\R)$) {$(O)$};
  \node[above right] at ($(O')+(45:\r)$) {$(O')$};
\end{tikzpicture}
\end{document}
""",

    "fig_c6": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=1.1, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (O1) at (0,0);
  \def\rOne{2.4}
  \coordinate (O2) at (3.2,0);
  \def\rTwo{0.8}
  \coordinate (A) at (\rOne,0);
  
  \draw[blue!70!black, thick] (O1) circle (\rOne);
  \draw[red!70!black, thick] (O2) circle (\rTwo);
  
  \coordinate (B) at ($(O1)+(60:\rOne)$);
  \coordinate (C) at ($(O2)+(60:\rTwo)$);
  \coordinate (D) at (intersection of B--C and O1--O2);
  
  \draw[thick, green!50!black] (D) -- (B);
  \draw[gray, thin] (D) -- (O1);
  \draw[gray, thin] (O1) -- (B);
  \draw[gray, thin] (O2) -- (C);
  
  \draw[thick, purple] (B) -- (A) -- (C);
  \draw pic[draw, angle radius=3mm, red] {right angle = B--A--C};
  
  \fill (O1) circle (1.2pt) node[below] {$O_1$};
  \fill (O2) circle (1.2pt) node[below] {$O_2$};
  \fill (A) circle (1.2pt) node[below=2pt] {$A$};
  \fill (B) circle (1.2pt) node[above left] {$B$};
  \fill (C) circle (1.2pt) node[above right] {$C$};
  \fill (D) circle (1.2pt) node[below] {$D$};
  \node[above left] at ($(O1)+(120:\rOne)$) {$(O_1)$};
  \node[above right] at ($(O2)+(45:\rTwo)$) {$(O_2)$};
\end{tikzpicture}
\end{document}
""",

    "fig_c8": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=0.22, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (H) at (0,0);
  \coordinate (A) at (0,12);
  \coordinate (B) at (0,-12);
  \coordinate (O) at (16,0);
  \coordinate (O') at (9,0);
  
  \draw[blue!70!black, thick] (O) circle (20);
  \draw[red!70!black, thick] (O') circle (15);
  
  \draw[thick, purple] (A) -- (B);
  \draw[thick, orange!80!black] (H) -- (O) -- ++(5,0);
  
  \draw[dashed, gray] (O) -- (A) node[midway, above right] {$20$};
  \draw[dashed, gray] (O') -- (A) node[midway, left] {$15$};
  
  \draw[fill=gray!30] (0,0) rectangle (1.2,1.2);
  
  \fill (A) circle (3pt) node[above] {$A$};
  \fill (B) circle (3pt) node[below] {$B$};
  \fill (H) circle (3pt) node[below left] {$H$};
  \fill (O') circle (3pt) node[below] {$O'$};
  \fill (O) circle (3pt) node[below] {$O$};
  
  \node[right] at ($(O)+(15,10)$) {$(O; 20)$};
  \node[above right] at ($(O')+(5,12)$) {$(O'; 15)$};
  \node[below] at (4.5, 0) {$9$};
  \node[above] at (12.5, 0) {$OO'=7$};
  \node[left] at (0, 6) {$12$};
\end{tikzpicture}
\end{document}
""",

    "fig_c9": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=1.1, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (O) at (0,0);
  \def\R{2.2}
  \coordinate (O') at (3.6,0);
  \def\r{1.4}
  \coordinate (A) at (\R,0);
  
  \draw[blue!70!black, thick] (O) circle (\R);
  \draw[red!70!black, thick] (O') circle (\r);
  
  \coordinate (M) at ($(O)+(77.16:\R)$);
  \coordinate (N) at ($(O')+(77.16:\r)$);
  \coordinate (P) at ($(O)+(-77.16:\R)$);
  \coordinate (Q) at ($(O')+(-77.16:\r)$);
  
  \draw[dashed, orange!80!black] (-2.5,0) -- (5.5,0) node[right] {$OO'$};
  
  \draw[thick, purple] (M) -- (N) -- (Q) -- (P) -- cycle;
  \draw[dashed, gray] (M) -- (P);
  \draw[dashed, gray] (N) -- (Q);
  
  \fill (O) circle (1.2pt) node[below] {$O$};
  \fill (O') circle (1.2pt) node[below] {$O'$};
  \fill (A) circle (1.2pt) node[below=2pt] {$A$};
  \fill (M) circle (1.2pt) node[above left] {$M$};
  \fill (N) circle (1.2pt) node[above right] {$N$};
  \fill (P) circle (1.2pt) node[below left] {$P$};
  \fill (Q) circle (1.2pt) node[below right] {$Q$};
  \node[above left] at ($(O)+(135:\R)$) {$(O)$};
  \node[above right] at ($(O')+(45:\r)$) {$(O')$};
\end{tikzpicture}
\end{document}
""",

    "fig_c10": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=0.9, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \pgfmathsetmacro{\dOO}{sqrt(40)}
  \pgfmathsetmacro{\hA}{12 / \dOO}
  \pgfmathsetmacro{\xH}{36 / \dOO}
  \coordinate (O) at (0,0);
  \coordinate (O') at (\dOO, 0);
  \coordinate (H) at (\xH, 0);
  \coordinate (A) at (\xH, \hA);
  \coordinate (B) at (\xH, -\hA);
  
  \draw[blue!70!black, thick] (O) circle (6);
  \draw[red!70!black, thick] (O') circle (2);
  
  \draw[thick] (O) -- (O');
  \draw[thick, green!50!black] (O) -- (A) node[midway, above left] {$6$};
  \draw[thick, green!50!black] (O') -- (A) node[midway, above right] {$2$};
  \draw[thick, purple] (A) -- (B);
  
  \draw pic[draw, angle radius=3mm, red] {right angle = O--A--O'};
  \draw pic[draw, angle radius=2.5mm] {right angle = A--H--O'};
  
  \fill (O) circle (1.2pt) node[below left] {$O$};
  \fill (O') circle (1.2pt) node[below right] {$O'$};
  \fill (A) circle (1.2pt) node[above] {$A$};
  \fill (B) circle (1.2pt) node[below] {$B$};
  \fill (H) circle (1.2pt) node[below=2pt] {$H$};
  \node[left] at ($(O)+(150:6)$) {$(O)$};
  \node[right] at ($(O')+(30:2)$) {$(O')$};
\end{tikzpicture}
\end{document}
""",

    "fig_c11": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=0.18, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (O2) at (-15,0);
  \coordinate (O3) at (15,0);
  \coordinate (O1) at (0,20);
  
  \coordinate (A) at (0,0);
  \coordinate (C) at (-6,12);
  \coordinate (B) at (6,12);
  
  \draw[blue!70!black, thick] (O1) circle (10);
  \draw[red!70!black, thick] (O2) circle (15);
  \draw[orange!70!black, thick] (O3) circle (15);
  
  \draw[dashed, gray] (O1) -- (O2) -- (O3) -- cycle;
  \draw[thick, green!50!black] (O1) -- (A);
  
  \draw[thick, purple, fill=purple!10] (A) -- (B) -- (C) -- cycle;
  
  \draw[fill=gray!25] (-1,0) rectangle (0,1);
  
  \fill (O1) circle (3pt) node[above] {$O_1$};
  \fill (O2) circle (3pt) node[below left] {$O_2$};
  \fill (O3) circle (3pt) node[below right] {$O_3$};
  \fill (A) circle (3pt) node[below=2pt] {$A$};
  \fill (B) circle (3pt) node[above right] {$B$};
  \fill (C) circle (3pt) node[above left] {$C$};
  
  \node[above] at (0,30.5) {$(O_1)$};
  \node[below left] at (-15,-15.5) {$(O_2)$};
  \node[below right] at (15,-15.5) {$(O_3)$};
\end{tikzpicture}
\end{document}
""",

    "fig_c12": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=0.55, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (O) at (0,0);
  \coordinate (A) at (6,0);
  \coordinate (B) at (-6,0);
  \coordinate (D) at (60:6);
  
  \def\r{3}
  \coordinate (O') at (9,0);
  \coordinate (C) at (12,0);
  \coordinate (E) at ($(O')+(60:\r)$);
  
  \draw[blue!70!black, thick] (O) circle (6);
  \draw[red!70!black, thick] (O') circle (\r);
  
  \draw[thick, green!50!black] ($(D)!-0.3!(E)$) -- ($(E)!-0.3!(D)$);
  \draw[thick] (B) -- (C);
  
  \coordinate (M) at (intersection of B--D and C--E);
  \draw[thick, purple] (B) -- (M);
  \draw[thick, purple] (C) -- (M);
  \draw[thick, purple] (A) -- (D);
  \draw[thick, purple] (A) -- (E);
  
  \draw[dashed, gray] (O) -- (D);
  \draw[dashed, gray] (O') -- (E);
  
  \draw pic[draw, angle radius=3mm, red] {right angle = D--A--E};
  \draw pic[draw, angle radius=3mm, red] {right angle = A--D--M};
  \draw pic[draw, angle radius=3mm, red] {right angle = A--E--M};
  
  \fill (O) circle (2pt) node[below] {$O$};
  \fill (O') circle (2pt) node[below] {$O'$};
  \fill (A) circle (2pt) node[below=2pt] {$A$};
  \fill (B) circle (2pt) node[left] {$B$};
  \fill (C) circle (2pt) node[right] {$C$};
  \fill (D) circle (2pt) node[above left] {$D$};
  \fill (E) circle (2pt) node[above right] {$E$};
  \fill (M) circle (2pt) node[above] {$M$};
  \node[above left] at ($(O)+(135:6)$) {$(O)$};
  \node[above right] at ($(O')+(45:\r)$) {$(O')$};
\end{tikzpicture}
\end{document}
""",

    "fig_c15": r"""\documentclass[tikz,border=3mm]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes}
\begin{document}
\begin{tikzpicture}[scale=0.9, font=\footnotesize, >=stealth, line join=round, line cap=round]
  \coordinate (O) at (0,0);
  \def\R{3}
  \coordinate (O') at (4.5,0);
  \def\r{1.5}
  \coordinate (A) at (3,0);
  
  \coordinate (B) at ($(O)+(60:\R)$);
  \coordinate (D) at ($(O')+(60:\r)$);
  \coordinate (I) at (9,0);
  
  \draw[blue!70!black, thick] (O) circle (\R);
  \draw[red!70!black, thick] (O') circle (\r);
  
  \draw[thick] (-3.5,0) -- (10.5,0);
  \draw[thick, green!50!black] (O) -- (B) node[midway, left] {$R$};
  \draw[thick, green!50!black] (O') -- (D) node[midway, left] {$r$};
  \draw[thick, purple] (B) -- (I);
  
  \coordinate (G) at ($(O)+(-70.5:\R)$);
  \coordinate (H) at ($(O')+(-70.5:\r)$);
  \draw[thick, orange!80!black] ($(G)!-0.3!(H)$) -- ($(H)!-0.5!(G)$) node[right] {$GH$};
  \draw[dashed, gray] (O) -- (G);
  \draw[dashed, gray] (O') -- (H);
  
  \fill (O) circle (1.5pt) node[below] {$O$};
  \fill (O') circle (1.5pt) node[below] {$O'$};
  \fill (A) circle (1.5pt) node[below=2pt] {$A$};
  \fill (B) circle (1.5pt) node[above left] {$B$};
  \fill (D) circle (1.5pt) node[above right] {$D$};
  \fill (I) circle (1.5pt) node[below] {$I$};
  \fill (G) circle (1.5pt) node[below left] {$G$};
  \fill (H) circle (1.5pt) node[below right] {$H$};
  \node[above left] at ($(O)+(120:\R)$) {$(O)$};
  \node[above right] at ($(O')+(45:\r)$) {$(O')$};
\end{tikzpicture}
\end{document}
"""
}

for name, code in tikz_figures.items():
    tex_path = os.path.join(scratch_dir, f"{name}.tex")
    pdf_path = os.path.join(scratch_dir, f"{name}.pdf")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(code)
    
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{name}.tex"]
    res = subprocess.run(cmd, cwd=scratch_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0:
        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=300)
        pix.save(os.path.join(out_img_dir, f"{name}.png"))
        pix.save(os.path.join(out_latex_dir, f"{name}.png"))
        print(f"Compiled and rendered {name} successfully!")
    else:
        print(f"Error compiling {name}")

print("All TikZ figures updated successfully!")
