# -*- coding: utf-8 -*-
"""
HỆ THỐNG GOM BỘ ĐỀ VẬT LÝ 10, 11 VÀ 12 THÀNH CÁC FILE PDF TỔNG HỢP
BẢN QUYỀN ĐỘC QUYỀN: LỚP LÝ THẦY NGỌC - GV: TRẦN VĂN THIỆN NGỌC - SĐT: 0935216256
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

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
BASE_DIR = r"c:\AnTiGraViTy-htthuy"
SAN_PHAM_BASE = os.path.join(BASE_DIR, "SAN PHAM")
MIRROR_BASE = os.path.join(BASE_DIR, "pdf2word", "San_Pham")
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch", "merge_covers")
os.makedirs(SCRATCH_DIR, exist_ok=True)

COLLECTIONS = [
    # ----------------------------------------------------
    # VẬT LÝ 10
    # ----------------------------------------------------
    {
        "grade": 10,
        "folder_name": "VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1",
        "subject": "VẬT LÍ 10",
        "total_exams": 7,
        "de_files": [
            ("Đề 1: THPT Bùi Thị Xuân (Mã đề 207)", "VL10_BTX_De_207.pdf"),
            ("Đề 2: THPT Hai Bà Trưng (Mã đề 209)", "VL10_HBT_De_209.pdf"),
            ("Đề 3: THPT Nguyễn Huệ - Đề 1 (Mã đề 494)", "VL10_NH_De_494.pdf"),
            ("Đề 4: THPT Nguyễn Huệ - Đề 2 (Mã đề 101)", "PHY10_Nguyen_Hue_De_101.pdf"),
            ("Đề 5: THPT Nguyễn Tất Thành (Mã đề 102)", "VL10_NTT_De_102.pdf"),
            ("Đề 6: THPT Phan Đăng Lưu (Mã đề 1008)", "VL10_PDL_De_1008.pdf"),
            ("Đề 7: THPT Chuyên Quốc Học - Huế (Mã đề 104)", "VL10_QH_De_104.pdf"),
        ],
        "hdg_files": [
            ("HDG 1: THPT Bùi Thị Xuân (Mã đề 207)", "VL10_BTX_HDG_207.pdf"),
            ("HDG 2: THPT Hai Bà Trưng (Mã đề 209)", "VL10_HBT_HDG_209.pdf"),
            ("HDG 3: THPT Nguyễn Huệ - Đề 1 (Mã đề 494)", "VL10_NH_HDG_494.pdf"),
            ("HDG 4: THPT Nguyễn Huệ - Đề 2 (Mã đề 101)", "PHY10_Nguyen_Hue_HDG_101.pdf"),
            ("HDG 5: THPT Nguyễn Tất Thành (Mã đề 102)", "VL10_NTT_HDG_102.pdf"),
            ("HDG 6: THPT Phan Đăng Lưu (Mã đề 1008)", "VL10_PDL_HDG_1008.pdf"),
            ("HDG 7: THPT Chuyên Quốc Học - Huế (Mã đề 104)", "VL10_QH_HDG_104.pdf"),
        ],
        "out_names": {
            "de_main": "VL10_TongHop_De.pdf",
            "de_alias": "VL10_GHKI_TongHop_HocSinh.pdf",
            "hdg_main": "VL10_TongHop_HDG.pdf",
            "hdg_alias": "VL10_GHKI_TongHop_GiaoVien.pdf",
        }
    },
    # ----------------------------------------------------
    # VẬT LÝ 11
    # ----------------------------------------------------
    {
        "grade": 11,
        "folder_name": "VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1",
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
        "folder_name": "VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1",
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

def find_file_in_grade(grade_folder, fname):
    """Tìm đường dẫn chính xác của file pdf trong folder grade"""
    for root, dirs, files in os.walk(grade_folder):
        if fname in files:
            return os.path.join(root, fname)
    return None

def generate_cover_pdf(col, is_sol):
    role = "GIÁO VIÊN" if is_sol else "HỌC SINH"
    sub_title = "HƯỚNG DẪN GIẢI CHI TIẾT" if is_sol else "ĐỀ BÀI KIỂM TRA TỰ LUYỆN"
    file_list = col["hdg_files"] if is_sol else col["de_files"]
    tag = f"cover_{col['grade']}_{'hdg' if is_sol else 'de'}"
    grade_dir = os.path.join(SAN_PHAM_BASE, col["folder_name"])

    # Calculate page ranges
    cur_page = 2
    items_tex = ""
    for title, fname in file_list:
        pdf_path = find_file_in_grade(grade_dir, fname)
        if not pdf_path:
            raise FileNotFoundError(f"Không tìm thấy file: {fname} trong {grade_dir}")
        doc = fitz.open(pdf_path)
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
{\Large\bfseries\color{blue!85!black} LỚP LÝ THẦY NGỌC}\\[4pt]
{\small\bfseries SĐT: 0935216256 \quad $\bullet$ \quad Giáo viên: TRẦN VĂN THIỆN NGỌC}\\[3pt]
{\footnotesize\textbf{CS1:} 50/2C Phạm Thị Liên \quad $\bullet$ \quad \textbf{CS2:} P A15 THPT Nguyễn Huệ \quad $\bullet$ \quad \textbf{CS3:} 24 Đặng Thái Thân}
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
{\footnotesize\color{gray!80!black}\textit{Tài liệu lưu hành nội bộ Lớp Lý Thầy Ngọc -- Chúc các em học tập và ôn luyện đạt kết quả xuất sắc!}}
\end{center}

\end{document}
"""
    tex_path = os.path.join(SCRATCH_DIR, f"{tag}.tex")
    with open(tex_path, 'w', encoding='utf-8') as fp:
        fp.write(tex)

    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{tag}.tex"], cwd=SCRATCH_DIR, capture_output=True, text=True)
    pdf_path = os.path.join(SCRATCH_DIR, f"{tag}.pdf")
    return pdf_path

def merge_grade_collection(col, is_sol):
    cover_pdf = generate_cover_pdf(col, is_sol)
    file_list = col["hdg_files"] if is_sol else col["de_files"]
    out_dict = col["out_names"]
    main_name = out_dict["hdg_main"] if is_sol else out_dict["de_main"]
    alias_name = out_dict["hdg_alias"] if is_sol else out_dict["de_alias"]

    grade_dir = os.path.join(SAN_PHAM_BASE, col["folder_name"])
    out_dir = os.path.join(grade_dir, "00_Tong_Hop_Cac_De")
    os.makedirs(out_dir, exist_ok=True)

    mirror_grade_dir = os.path.join(MIRROR_BASE, col["folder_name"])
    mirror_out_dir = os.path.join(mirror_grade_dir, "00_Tong_Hop_Cac_De")
    os.makedirs(mirror_out_dir, exist_ok=True)

    main_path = os.path.join(out_dir, main_name)
    alias_path = os.path.join(out_dir, alias_name)

    # Master Doc
    master = fitz.open()

    # 1. Add Cover Page
    toc = [[1, "Trang bìa & Mục lục tuyển tập", 1]]
    c_doc = fitz.open(cover_pdf)
    master.insert_pdf(c_doc)

    # 2. Add each exam and record bookmark
    cur_page = 2
    for title, fname in file_list:
        sub_path = find_file_in_grade(grade_dir, fname)
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
        "author": "TRẦN VĂN THIỆN NGỌC - LỚP LÝ THẦY NGỌC",
        "subject": f"{col['subject']} - Thừa Thiên Huế",
        "keywords": f"Lớp Lý Thầy Ngọc, Trần Văn Thiện Ngọc, {col['subject']}, Đề thi giữa kỳ 1, Thừa Thiên Huế"
    })

    # Save to out_dir
    master.save(main_path, garbage=4, deflate=True)
    shutil.copy2(main_path, alias_path)

    # Mirror to mirror_out_dir
    shutil.copy2(main_path, os.path.join(mirror_out_dir, main_name))
    shutil.copy2(alias_path, os.path.join(mirror_out_dir, alias_name))

    print(f"  [XUẤT BẢN THÀNH CÔNG] {col['subject']} - {role_str}: {len(master)} trang")
    print(f"    -> {main_path}")
    print(f"    -> {alias_path}")

def main():
    print("=" * 80)
    print(" BẮT ĐẦU XUẤT BẢN TOÀN BỘ CÁC FILE PDF TỔNG HỢP VẬT LÝ 10, 11, 12 - LỚP LÝ THẦY NGỌC")
    print("=" * 80)

    for col in COLLECTIONS:
        print(f"\n--- TIẾN HÀNH {col['subject']} ---")
        # 1. Đề thi (Học sinh)
        merge_grade_collection(col, False)
        # 2. Hướng dẫn giải (Giáo viên)
        merge_grade_collection(col, True)

    print("\n" + "=" * 80)
    print(" HOÀN TẤT 100% XUẤT BẢN CÁC FILE TỔNG HỢP VẬT LÝ!")
    print("=" * 80)

if __name__ == "__main__":
    main()
