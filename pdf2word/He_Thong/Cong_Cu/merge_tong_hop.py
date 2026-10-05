# -*- coding: utf-8 -*-
"""
HỆ THỐNG GOM BỘ ĐỀ VẬT LÝ 11 VÀ 12 THÀNH CÁC FILE PDF TỔNG HỢP
  1. Vật lý 11:
     - Bản Học sinh (Đề thi): VL11_TongHop_De.pdf (kèm alias VL11_GHKI_TongHop_HocSinh.pdf)
     - Bản Giáo viên (HDG):   VL11_TongHop_HDG.pdf (kèm alias VL11_GHKI_TongHop_GiaoVien.pdf)
  2. Vật lý 12:
     - Bản Học sinh (Đề thi): VL12_TongHop_De.pdf (kèm alias VL12_GHKI_TongHop_HocSinh.pdf)
     - Bản Giáo viên (HDG):   VL12_TongHop_HDG.pdf (kèm alias VL12_GHKI_TongHop_GiaoVien.pdf)

Trang bìa & Mục lục thiết kế chuẩn LaTeX, kèm PDF Bookmarks điều hướng từng trường.
Bản quyền độc quyền: LỚP TOÁN CÔ THÚY - GV: HỒ THỊ THÚY - SĐT: 0935.322.328 - 50/2C Phạm Thị Liên
"""

import os
import sys
import shutil
import subprocess
import fitz

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch", "merge_covers")
os.makedirs(SCRATCH_DIR, exist_ok=True)

COLLECTIONS = [
    # ----------------------------------------------------
    # VẬT LÝ 11
    # ----------------------------------------------------
    {
        "grade": 11,
        "subject": "VẬT LÍ 11",
        "total_exams": 7,
        "de_files": [
            ("Đề 1: THPT Đại học Khoa học (Mã đề 132)", "VL11_DHKH_De_132.pdf"),
            ("Đề 2: THPT Hai Bà Trưng 2024-2025 (Mã đề 132)", "VL11_HBT_2425_De_132.pdf"),
            ("Đề 3: THPT Hai Bà Trưng 2025-2026 (Mã đề 001)", "VL11_HBT_De_001.pdf"),
            ("Đề 4: THPT Nguyễn Huệ (Mã đề 101)", "VL11_NH_De_101.pdf"),
            ("Đề 5: THPT Phan Đăng Lưu (Mã đề 2106)", "VL11_PDL_De_2106.pdf"),
            ("Đề 6: THPT Phú Bài (Mã đề 111)", "VL11_PHUBAI_De_111.pdf"),
            ("Đề 7: THPT Chuyên Quốc Học - Huế (Mã đề 562)", "VL11_QH_De_562.pdf"),
        ],
        "hdg_files": [
            ("HDG 1: THPT Đại học Khoa học (Mã đề 132)", "VL11_DHKH_HDG_132.pdf"),
            ("HDG 2: THPT Hai Bà Trưng 2024-2025 (Mã đề 132)", "VL11_HBT_2425_HDG_132.pdf"),
            ("HDG 3: THPT Hai Bà Trưng 2025-2026 (Mã đề 001)", "VL11_HBT_HDG_001.pdf"),
            ("HDG 4: THPT Nguyễn Huệ (Mã đề 101)", "VL11_NH_HDG_101.pdf"),
            ("HDG 5: THPT Phan Đăng Lưu (Mã đề 2106)", "VL11_PDL_HDG_2106.pdf"),
            ("HDG 6: THPT Phú Bài (Mã đề 111)", "VL11_PHUBAI_HDG_111.pdf"),
            ("HDG 7: THPT Chuyên Quốc Học - Huế (Mã đề 562)", "VL11_QH_HDG_562.pdf"),
        ],
        "out_names": {
            "de_main": "VL11_TongHop_De.pdf",
            "de_alias": "VL11_GHKI_TongHop_HocSinh.pdf",
            "hdg_main": "VL11_TongHop_HDG.pdf",
            "hdg_alias": "VL11_GHKI_TongHop_GiaoVien.pdf",
        }
    },
    # ----------------------------------------------------
    # VẬT LÝ 12
    # ----------------------------------------------------
    {
        "grade": 12,
        "subject": "VẬT LÍ 12",
        "total_exams": 6,
        "de_files": [
            ("Đề 1: THPT Bùi Thị Xuân - Đề 1 (Mã đề 429)", "VL12_BTX_De_429.pdf"),
            ("Đề 2: THPT Bùi Thị Xuân - Đề 2 (Mã đề 101)", "VL12_BTX_De_101.pdf"),
            ("Đề 3: THPT Cao Thắng (Mã đề 246)", "VL12_CAOTHANG_De_246.pdf"),
            ("Đề 4: THPT Nguyễn Huệ (Mã đề 029)", "VL12_NH_De_029.pdf"),
            ("Đề 5: THPT Phan Đăng Lưu (Mã đề 1204)", "VL12_PDL_De_1204.pdf"),
            ("Đề 6: THPT Chuyên Quốc Học - Huế (Mã đề 122)", "VL12_QH_De_122.pdf"),
        ],
        "hdg_files": [
            ("HDG 1: THPT Bùi Thị Xuân - Đề 1 (Mã đề 429)", "VL12_BTX_HDG_429.pdf"),
            ("HDG 2: THPT Bùi Thị Xuân - Đề 2 (Mã đề 101)", "VL12_BTX_HDG_101.pdf"),
            ("HDG 3: THPT Cao Thắng (Mã đề 246)", "VL12_CAOTHANG_HDG_246.pdf"),
            ("HDG 4: THPT Nguyễn Huệ (Mã đề 029)", "VL12_NH_HDG_029.pdf"),
            ("HDG 5: THPT Phan Đăng Lưu (Mã đề 1204)", "VL12_PDL_HDG_1204.pdf"),
            ("HDG 6: THPT Chuyên Quốc Học - Huế (Mã đề 122)", "VL12_QH_HDG_122.pdf"),
        ],
        "out_names": {
            "de_main": "VL12_TongHop_De.pdf",
            "de_alias": "VL12_GHKI_TongHop_HocSinh.pdf",
            "hdg_main": "VL12_TongHop_HDG.pdf",
            "hdg_alias": "VL12_GHKI_TongHop_GiaoVien.pdf",
        }
    }
]

def generate_cover_pdf(col, is_sol):
    role = "GIÁO VIÊN" if is_sol else "HỌC SINH"
    sub_title = "HƯỚNG DẪN GIẢI CHI TIẾT" if is_sol else "ĐỀ BÀI KIỂM TRA TỰ LUYỆN"
    file_list = col["hdg_files"] if is_sol else col["de_files"]
    tag = f"cover_{col['grade']}_{'hdg' if is_sol else 'de'}"

    # Calculate page ranges
    cur_page = 2
    items_tex = ""
    for title, fname in file_list:
        doc = fitz.open(os.path.join(SAN_PHAM_DIR, fname))
        pcount = len(doc)
        end_page = cur_page + pcount - 1
        items_tex += f"\\item \\textbf{{{title}}} \\hfill \\textsl{{Trang {cur_page} -- {end_page}}} ({pcount} trang)\\\\[6pt]\n"
        cur_page += pcount

    tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage[top=1.4cm,bottom=1.6cm,left=1.6cm,right=1.6cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{tcolorbox}
\tcbuselibrary{skins}

\begin{document}
\thispagestyle{empty}

\begin{tcolorbox}[colback=blue!5!white,colframe=blue!80!black,arc=4mm,boxrule=1.5pt,center,width=\textwidth]
\centering
\vspace{0.15cm}
{\Large\bfseries\color{blue!85!black} LỚP TOÁN CÔ THÚY}\\[4pt]
{\small\bfseries SĐT: 0935.322.328 \quad $\bullet$ \quad Địa chỉ: 50/2C Phạm Thị Liên}\\[2pt]
{\footnotesize\color{gray!90!black} Giáo viên: HỒ THỊ THÚY}
\vspace{0.15cm}
\end{tcolorbox}

\vspace{0.4cm}

\begin{center}
{\huge\bfseries\color{red!85!black} TUYỂN TẬP """ + str(col["total_exams"]) + r""" BỘ ĐỀ THI GIỮA KỲ I}\\[8pt]
{\LARGE\bfseries\color{blue!80!black} MÔN: """ + col["subject"] + r"""}\\[6pt]
{\large\bfseries\color{magenta!85!black} (BẢN DÀNH CHO """ + role + r""" -- """ + sub_title + r""")}\\[8pt]
{\textit{\small Tuyển tập các trường THPT trọng điểm Thừa Thiên Huế -- Năm học 2024--2025 \& 2025--2026}}
\end{center}

\vspace{0.3cm}

\begin{tcolorbox}[colback=white,colframe=red!75!black,arc=3mm,boxrule=1.2pt,title={\bfseries\large MỤC LỤC BỘ ĐỀ THI},center,width=\textwidth]
\vspace{0.15cm}
\begin{enumerate}
""" + items_tex + r"""\end{enumerate}
\vspace{0.1cm}
\end{tcolorbox}

\vfill
\begin{center}
{\footnotesize\color{gray!80!black}\textit{Tài liệu lưu hành nội bộ Lớp Toán Cô Thúy -- Chúc các em học tập và ôn luyện đạt kết quả xuất sắc!}}
\end{center}

\end{document}
"""
    tex_path = os.path.join(SCRATCH_DIR, f"{tag}.tex")
    with open(tex_path, 'w', encoding='utf-8') as fp:
        fp.write(tex)

    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{tag}.tex"], cwd=SCRATCH_DIR, capture_output=True, text=True)
    pdf_path = os.path.join(SCRATCH_DIR, f"{tag}.pdf")
    return pdf_path

def merge_pdf_collection(col, is_sol):
    cover_pdf = generate_cover_pdf(col, is_sol)
    file_list = col["hdg_files"] if is_sol else col["de_files"]
    out_dict = col["out_names"]
    main_name = out_dict["hdg_main"] if is_sol else out_dict["de_main"]
    alias_name = out_dict["hdg_alias"] if is_sol else out_dict["de_alias"]
    main_path = os.path.join(SAN_PHAM_DIR, main_name)
    alias_path = os.path.join(SAN_PHAM_DIR, alias_name)

    # Master Doc
    master = fitz.open()

    # 1. Add Cover Page
    toc = [[1, "Trang bìa & Mục lục tuyển tập", 1]]
    c_doc = fitz.open(cover_pdf)
    master.insert_pdf(c_doc)

    # 2. Add each exam and record bookmark
    cur_page = 2
    for title, fname in file_list:
        sub_path = os.path.join(SAN_PHAM_DIR, fname)
        s_doc = fitz.open(sub_path)
        toc.append([1, title, cur_page])
        cur_page += len(s_doc)
        master.insert_pdf(s_doc)

    # Set Bookmarks
    master.set_toc(toc)

    # Set Metadata
    role_str = "Giáo viên (Hướng dẫn giải chi tiết)" if is_sol else "Học sinh (Đề bài kiểm tra)"
    master.set_metadata({
        "title": f"Tuyển tập Bộ đề thi Giữa kỳ I - {col['subject']} ({role_str})",
        "author": "HỒ THỊ THÚY - LỚP TOÁN CÔ THÚY",
        "subject": f"{col['subject']} - Thừa Thiên Huế",
        "keywords": "Lớp Toán Cô Thúy, Vật lý 11, Vật lý 12, Đề thi giữa kỳ 1, Thừa Thiên Huế"
    })

    # Save
    master.save(main_path, garbage=4, deflate=True)
    shutil.copy2(main_path, alias_path)
    print(f"  [XUẤT BẢN] {main_name} ({len(master)} trang) & alias {alias_name}")

def main():
    print("=" * 80)
    print(" BẮT ĐẦU GOM TỔNG HỢP TOÀN BỘ ĐỀ VẬT LÝ 11 VÀ 12 THÀNH CÁC FILE PDF TỔNG")
    print("=" * 80)

    for col in COLLECTIONS:
        print(f"\n--- TIẾN HÀNH {col['subject']} ---")
        # 1. Đề thi (Học sinh)
        merge_pdf_collection(col, False)
        # 2. HDG (Giáo viên)
        merge_pdf_collection(col, True)

    print("\n" + "=" * 80)
    print("HOÀN THÀNH 100% CẢ 4 FILE PDF TỔNG HỢP CHO HỌC SINH VÀ GIÁO VIÊN!")
    print("=" * 80)

if __name__ == "__main__":
    main()
