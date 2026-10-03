import subprocess
import os

figures = {
    "fig_cau4": r"""\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{calc,arrows.meta}
\begin{document}
\begin{tikzpicture}[scale=0.55, font=\footnotesize, >=stealth]
	\draw[->] (-1.8,0) -- (6.8,0) node[below] {$x$};
	\draw[->] (0,-3.2) -- (0,4.8) node[left] {$y$};
	\fill (0,0) circle (1.5pt) node[below right] {$O$};
	\draw[dashed] (-1,0) node[below] {$-1$} -- (-1,1);
	\draw[dashed] (2,0) node[above] {$2$} -- (2,-2);
	\draw[dashed] (6,0) node[below] {$6$} -- (6,4);
	\draw[dashed] (0,-2) -- (2,-2);
	\draw[dashed] (0,2) node[left] {$2$} -- (0,2);
	\draw[thick, smooth, domain=-1:2] plot (\x, {-\x*\x + 2});
	\draw[thick, smooth, domain=2:6] plot (\x, {1.5*\x - 5});
	\fill (-1,1) circle (1.5pt) (2,-2) circle (1.5pt) (6,4) circle (1.5pt) (0,2) circle (1.5pt);
\end{tikzpicture}
\end{document}
""",
    "fig_cau8": r"""\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{calc,arrows.meta}
\begin{document}
\begin{tikzpicture}[scale=0.55, font=\footnotesize, >=stealth]
	\draw[->] (-1.8,0) -- (5.8,0) node[below] {$x$};
	\draw[->] (0,-1.8) -- (0,3.8) node[left] {$y$};
	\fill (0,0) circle (1.5pt) node[below right] {$O$};
	\draw[dashed] (-1,0) node[below] {$-1$} -- (-1,-1) -- (0,-1) node[left] {$-1$};
	\draw[dashed] (1,0) node[below] {$1$} -- (1,3) -- (0,3) node[left] {$3$};
	\draw[dashed] (5,0) node[above] {$5$} -- (5,-1) -- (0,-1);
	\draw[thick, smooth, domain=-1:1] plot (\x, {-(\x-1)*(\x-1) + 3});
	\draw[thick, smooth, domain=1:5] plot (\x, {-(\x-1) + 3});
	\fill (-1,-1) circle (1.5pt) (1,3) circle (1.5pt) (5,-1) circle (1.5pt) (0,1) circle (1.5pt);
	\node[right] at (0,1) {$1$};
\end{tikzpicture}
\end{document}
""",
    "fig_bbt": r"""\documentclass[border=2pt]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz,tkz-tab}
\begin{document}
\begin{tikzpicture}
	\tkzTabInit[lgt=1.2,espcl=2.2]{$x$/0.7,$y'$/0.7,$y$/1.8}{$-\infty$,$-1$,$1$,$+\infty$}
	\tkzTabLine{,-,$0$,+,$0$,-,}
	\tkzTabVar{+/$142$,-/$8$,+/$38$,-/$14$}
\end{tikzpicture}
\end{document}
""",
    "fig_tamgiac": r"""\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{calc}
\begin{document}
\begin{tikzpicture}[scale=0.7, font=\footnotesize]
	\coordinate (A) at (1,4.2);
	\coordinate (B) at (-0.8,1.2);
	\coordinate (C) at (3.2,0);
	\coordinate (D) at ($(A)!0.25!(C)$);
	\coordinate (E) at ($(A)!0.25!(B)$);
	\coordinate (F) at ($(A)!0.25!(D)$);
	\draw[thick] (A)--(B)--(C)--cycle;
	\draw[thick] (B)--(D)--(E)--(F);
	\node[above] at (A) {$A$};
	\node[left] at (B) {$B$};
	\node[right] at (C) {$C$};
	\node[right] at (D) {$D$};
	\node[left] at (E) {$E$};
	\node[right] at (F) {$F$};
\end{tikzpicture}
\end{document}
""",
    "fig_maybay": r"""\documentclass[tikz,border=2pt]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usetikzlibrary{calc,arrows.meta}
\begin{document}
\begin{tikzpicture}[scale=0.7, font=\footnotesize, >=stealth]
	\draw[->] (0,0) -- (-2.2,-1.8) node[below] {$x$ (Nam)};
	\draw[->] (0,0) -- (5.5,0) node[right] {$y$ (Đông)};
	\draw[->] (0,0) -- (0,3.8) node[above] {$z$};
	\fill (0,0) circle (1.5pt) node[above left] {$O$};
	\coordinate (P0) at (-1.3,-1.0);
	\coordinate (Pxy) at (2.4,-1.0);
	\coordinate (M) at (2.4,2.5);
	\draw[dashed] (0,0) -- (P0) node[left] {$150$} -- (Pxy) -- (3.7,0) node[above] {$300$};
	\draw[dashed] (Pxy) -- (M) -- (0,3.5) node[left] {$9$};
	\fill (M) circle (2.5pt);
	\draw[thick] (M) ++(-0.25,-0.12) -- ++(0.5,0.25) ++(-0.15,0.15) -- ++(-0.2,-0.5);
	\node[above right] at (M) {Máy bay};
\end{tikzpicture}
\end{document}
""",
    "fig_shipper": r"""\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\begin{document}
\begin{tikzpicture}[scale=0.7, font=\scriptsize]
	\coordinate (A) at (-2.6,0);
	\coordinate (B) at (-1,1.8);
	\coordinate (C) at (1.4,1.8);
	\coordinate (D) at (2.8,0.4);
	\coordinate (E) at (1.4,-1.6);
	\coordinate (F) at (-1,-1.6);
	\coordinate (G) at (0.2,-0.2);
	
	\draw[thick] (A)--(B) node[midway,above left] {$4$};
	\draw[thick] (B)--(C) node[midway,above] {$8$};
	\draw[thick] (C)--(D) node[midway,above right] {$10$};
	\draw[thick] (D)--(E) node[midway,below right] {$12$};
	\draw[thick] (E)--(F) node[midway,below] {$10$};
	\draw[thick] (F)--(A) node[midway,below left] {$5$};
	
	\draw[thick] (A)--(G) node[pos=0.35,above] {$17$};
	\draw[thick] (B)--(G) node[pos=0.4,right] {$8$};
	\draw[thick] (C)--(G) node[pos=0.4,left] {$9$};
	\draw[thick] (D)--(G) node[pos=0.4,above] {$18$};
	\draw[thick] (E)--(G) node[pos=0.4,right] {$6$};
	\draw[thick] (F)--(G) node[pos=0.4,below] {$7$};
	\draw[thick] (B)--(F) node[pos=0.7,right] {$3$};
	\draw[thick] (C)--(E) node[pos=0.3,right] {$6$};
	
	\foreach \p/\l/\pos in {A/A/left, B/B/above, C/C/above, D/D/right, E/E/below, F/F/below, G/G/below right} {
		\fill (\p) circle (2pt);
		\node[\pos] at (\p) {$\l$};
	}
\end{tikzpicture}
\end{document}
"""
}

for name, code in figures.items():
    tex_path = f"{name}.tex"
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(code)
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_path], stdout=subprocess.DEVNULL)
    subprocess.run(["magick", "-density", "300", f"{name}.pdf", f"{name}.png"], stdout=subprocess.DEVNULL)
    print(f"Rendered: {name}.png")
