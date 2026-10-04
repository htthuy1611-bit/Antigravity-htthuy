"""Render TikZ standalone figures of VL10 - THPT Hai Bà Trưng (Mã đề 209) to PDF + PNG 300 DPI."""
import os
import sys
import subprocess
import pymupdf as fitz

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FIG_DIR = os.path.join(BASE_DIR, "He_Thong", "Hinh_Anh", "HBT_10")
FIGS = ["fig_cau2", "fig_cau12", "fig_cau13", "fig_cau17", "fig_cau21"]


def render(name):
    tex = os.path.join(FIG_DIR, name + ".tex")
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                         cwd=FIG_DIR, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    pdf = os.path.join(FIG_DIR, name + ".pdf")
    if res.returncode != 0 or not os.path.exists(pdf):
        print(f"[LỖI] {name}:\n" + res.stdout[-1500:])
        return False
    doc = fitz.open(pdf)
    pix = doc[0].get_pixmap(dpi=300, alpha=False)
    pix.save(os.path.join(FIG_DIR, name + ".png"))
    doc.close()
    for ext in (".aux", ".log"):
        p = os.path.join(FIG_DIR, name + ext)
        if os.path.exists(p):
            os.remove(p)
    print(f"[OK] {name}.png ({pix.width}x{pix.height})")
    return True


if __name__ == "__main__":
    ok = all(render(f) for f in FIGS)
    sys.exit(0 if ok else 1)
