"""Render mọi fig_*.tex trong He_Thong/Hinh_Anh/<FOLDER> -> PDF (vector) + PNG 300 DPI.
Cách dùng: python render_figs.py BTX_10"""
import os
import sys
import glob
import subprocess
import pymupdf as fitz

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def render(fig_dir, name):
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                         cwd=fig_dir, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    pdf = os.path.join(fig_dir, name + ".pdf")
    if res.returncode != 0 or not os.path.exists(pdf):
        print(f"[LỖI] {name}:\n" + res.stdout[-1500:])
        return False
    doc = fitz.open(pdf)
    pix = doc[0].get_pixmap(dpi=300, alpha=False)
    pix.save(os.path.join(fig_dir, name + ".png"))
    doc.close()
    for ext in (".aux", ".log"):
        p = os.path.join(fig_dir, name + ext)
        if os.path.exists(p):
            os.remove(p)
    print(f"[OK] {name}.png ({pix.width}x{pix.height})")
    return True


if __name__ == "__main__":
    fig_dir = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", sys.argv[1])
    names = [os.path.splitext(os.path.basename(f))[0] for f in sorted(glob.glob(os.path.join(fig_dir, "fig_*.tex")))]
    ok = all([render(fig_dir, n) for n in names])
    sys.exit(0 if ok else 1)
