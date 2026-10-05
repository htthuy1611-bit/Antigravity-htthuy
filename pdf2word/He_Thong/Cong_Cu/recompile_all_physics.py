# -*- coding: utf-8 -*-
import os, sys, subprocess

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r"c:\AnTiGraViTy-htthuy\SAN PHAM"
grades = [
    "VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1",
    "VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1",
    "VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1"
]

compiled = 0
failed = []

for g in grades:
    g_path = os.path.join(base_dir, g)
    subdirs = [d for d in os.listdir(g_path) if os.path.isdir(os.path.join(g_path, d)) and d not in ["Master", "00_Tong_Hop_Cac_De"]]
    for sub in sorted(subdirs):
        folder = os.path.join(g_path, sub)
        tex_files = [f for f in os.listdir(folder) if f.endswith('.tex') and f not in ['bang_dap_an.tex', 'noi_dung.tex', 'ex_test.sty'] and not f.startswith('fig_')]
        for tf in tex_files:
            print(f"[{g} -> {sub}] Compiling {tf}...")
            res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tf], cwd=folder, capture_output=True, text=True, errors='ignore')
            if res.returncode == 0:
                compiled += 1
            else:
                failed.append((f"{sub}/{tf}", res.stdout[-400:]))

print("=" * 70)
print(f"Hoàn tất: {compiled}/{compiled + len(failed)} file biên dịch thành công!")
if failed:
    for name, err in failed:
        print(f"Lỗi ở {name}:\n{err}\n")
