# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG TẠO FILE WRAPPER VÀ BIÊN DỊCH BẢN CHỮA BÀI TRỰC TUYẾN (CÓ 4 DÒNG CHẤM DƯỚI MỖI CÂU)
CHO TOÀN BỘ 20 TRƯỜNG CỦA 3 BỘ ĐỀ VẬT LÝ 10, 11, 12 GIỮA KỲ 1.
"""

import os
import sys
import subprocess
import shutil
import fitz

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"c:\AnTiGraViTy-htthuy"
SAN_PHAM_BASE = os.path.join(BASE_DIR, "SAN PHAM")
MIRROR_BASE = os.path.join(BASE_DIR, "pdf2word", "San_Pham")
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch", "merge_covers")
os.makedirs(SCRATCH_DIR, exist_ok=True)

EXAM_CONFIGS = [
    # ----------------------------------------------------
    # VẬT LÝ 10
    # ----------------------------------------------------
    {
        "grade": 10,
        "folder_name": "VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1",
        "subject": "VẬT LÍ 10",
        "total_exams": 7,
        "exams": [
            ("01_THPT_Bui_Thi_Xuan_De_207", "VL10_BTX_ChuaBai_207", "Đề 1: THPT Bùi Thị Xuân (Mã đề 207)"),
            ("02_THPT_Hai_Ba_Trung_De_209", "VL10_HBT_ChuaBai_209", "Đề 2: THPT Hai Bà Trưng (Mã đề 209)"),
            ("03_THPT_Nguyen_Hue_De_494", "VL10_NH_ChuaBai_494", "Đề 3: THPT Nguyễn Huệ - Đề 1 (Mã đề 494)"),
            ("04_THPT_Nguyen_Hue_De_101", "PHY10_Nguyen_Hue_ChuaBai_101", "Đề 4: THPT Nguyễn Huệ - Đề 2 (Mã đề 101)"),
            ("05_THPT_Nguyen_Tat_Thanh_De_102", "VL10_NTT_ChuaBai_102", "Đề 5: THPT Nguyễn Tất Thành (Mã đề 102)"),
            ("06_THPT_Phan_Dang_Luu_De_1008", "VL10_PDL_ChuaBai_1008", "Đề 6: THPT Phan Đăng Lưu (Mã đề 1008)"),
            ("07_THPT_Quoc_Hoc_De_104", "VL10_QH_ChuaBai_104", "Đề 7: THPT Chuyên Quốc Học - Huế (Mã đề 104)"),
        ],
        "out_main": "VL10_TongHop_ChuaBai.pdf",
        "out_alias": "VL10_GHKI_TongHop_ChuaBai.pdf"
    },
    # ----------------------------------------------------
    # VẬT LÝ 11
    # ----------------------------------------------------
    {
        "grade": 11,
        "folder_name": "VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1",
        "subject": "VẬT LÍ 11",
        "total_exams": 7,
        "exams": [
            ("01_Chuyen_DHKH_Hue_De_132", "VL11_DHKH_ChuaBai_132", "Đề 1: THPT Đại học Khoa học (Mã đề 132)"),
            ("02_THPT_Hai_Ba_Trung_2425_De_132", "VL11_HBT_2425_ChuaBai_132", "Đề 2: THPT Hai Bà Trưng 2024-2025 (Mã đề 132)"),
            ("03_THPT_Hai_Ba_Trung_2526_De_001", "VL11_HBT_ChuaBai_001", "Đề 3: THPT Hai Bà Trưng 2025-2026 (Mã đề 001)"),
            ("04_THPT_Nguyen_Hue_De_101", "VL11_NH_ChuaBai_101", "Đề 4: THPT Nguyễn Huệ (Mã đề 101)"),
            ("05_THPT_Phan_Dang_Luu_De_2106", "VL11_PDL_ChuaBai_2106", "Đề 5: THPT Phan Đăng Lưu (Mã đề 2106)"),
            ("06_THPT_Phu_Bai_De_111", "VL11_PHUBAI_ChuaBai_111", "Đề 6: THPT Phú Bài (Mã đề 111)"),
            ("07_THPT_Quoc_Hoc_De_562", "VL11_QH_ChuaBai_562", "Đề 7: THPT Chuyên Quốc Học - Huế (Mã đề 562)"),
        ],
        "out_main": "VL11_TongHop_ChuaBai.pdf",
        "out_alias": "VL11_GHKI_TongHop_ChuaBai.pdf"
    },
    # ----------------------------------------------------
    # VẬT LÝ 12
    # ----------------------------------------------------
    {
        "grade": 12,
        "folder_name": "VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1",
        "subject": "VẬT LÍ 12",
        "total_exams": 9,
        "exams": [
            ("01_THPT_Bui_Thi_Xuan_De_429", "VL12_BTX_ChuaBai_429", "Đề 1: THPT Bùi Thị Xuân - Đề 1 (Mã đề 429)"),
            ("02_THPT_Bui_Thi_Xuan_De_101", "VL12_BTX_ChuaBai_101", "Đề 2: THPT Bùi Thị Xuân - Đề 2 (Mã đề 101)"),
            ("03_THPT_Cao_Thang_De_246", "VL12_CAOTHANG_ChuaBai_246", "Đề 3: THPT Cao Thắng (Mã đề 246)"),
            ("04_THPT_Nguyen_Hue_De_029", "VL12_NH_ChuaBai_029", "Đề 4: THPT Nguyễn Huệ (Mã đề 029)"),
            ("05_THPT_Phan_Dang_Luu_De_1204", "VL12_PDL_ChuaBai_1204", "Đề 5: THPT Phan Đăng Lưu (Mã đề 1204)"),
            ("06_THPT_Quoc_Hoc_De_122", "VL12_QH_ChuaBai_122", "Đề 6: THPT Chuyên Quốc Học - Huế 2024-2025 (Mã đề 122)"),
            ("07_THPT_Hai_Ba_Trung_2425_De_101", "VL12_HBT_2425_ChuaBai_101", "Đề 7: THPT Hai Bà Trưng 2024-2025 (Mã đề 101)"),
            ("08_THPT_Hai_Ba_Trung_2526_De_101", "VL12_HBT_2526_ChuaBai_101", "Đề 8: THPT Hai Bà Trưng 2025-2026 (Mã đề 101)"),
            ("09_THPT_Quoc_Hoc_2526_De_101", "VL12_QH_2526_ChuaBai_101", "Đề 9: THPT Chuyên Quốc Học - Huế 2025-2026 (Mã đề 101)"),
        ],
        "out_main": "VL12_TongHop_ChuaBai.pdf",
        "out_alias": "VL12_GHKI_TongHop_ChuaBai.pdf"
    }
]

def generate_chua_bai_wrappers_and_compile():
    print("=" * 80)
    print("BƯỚC 1: TẠO WRAPPER VÀ BIÊN DỊCH CÁC ĐỀ CHỮA BÀI (4 DÒNG CHẤM)")
    print("=" * 80)

    for col in EXAM_CONFIGS:
        grade_dir = os.path.join(SAN_PHAM_BASE, col["folder_name"])
        mirror_grade_dir = os.path.join(MIRROR_BASE, col["folder_name"])

        for subfolder, wrapper_base, title in col["exams"]:
            exam_dir = os.path.join(grade_dir, subfolder)
            mirror_exam_dir = os.path.join(mirror_grade_dir, subfolder)
            
            # Find the existing student wrapper file to extract macros
            de_files = [f for f in os.listdir(exam_dir) if f.endswith('.tex') and ('_De_' in f or f.endswith('_De.tex'))]
            if not de_files:
                raise FileNotFoundError(f"Không tìm thấy file đề trong {exam_dir}")
            ref_de = os.path.join(exam_dir, de_files[0])
            with open(ref_de, 'r', encoding='utf-8') as fp:
                de_text = fp.read()

            # Create ChuaBai wrapper by changing \input to Master_ChuaBai.tex
            chua_bai_text = de_text.replace(r"\input{../Master/Master_De.tex}", r"\input{../Master/Master_ChuaBai.tex}")
            if r"\input{../Master/Master_ChuaBai.tex}" not in chua_bai_text:
                # Fallback if different format
                chua_bai_text = de_text.replace("Master_De.tex", "Master_ChuaBai.tex")

            cb_tex_path = os.path.join(exam_dir, f"{wrapper_base}.tex")
            with open(cb_tex_path, 'w', encoding='utf-8') as fp:
                fp.write(chua_bai_text)

            # Compile with pdflatex
            print(f"[{col['subject']} -> {subfolder}] Biên dịch {wrapper_base}.tex...")
            res = subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{wrapper_base}.tex"], cwd=exam_dir, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"  [LỖI] {res.stdout[-400:]}")
            else:
                cb_pdf = os.path.join(exam_dir, f"{wrapper_base}.pdf")
                pcount = len(fitz.open(cb_pdf))
                print(f"  -> Thành công: {pcount} trang")

            # Mirror to mirror folder
            os.makedirs(mirror_exam_dir, exist_ok=True)
            shutil.copy2(cb_tex_path, os.path.join(mirror_exam_dir, f"{wrapper_base}.tex"))
            cb_pdf = os.path.join(exam_dir, f"{wrapper_base}.pdf")
            if os.path.exists(cb_pdf):
                shutil.copy2(cb_pdf, os.path.join(mirror_exam_dir, f"{wrapper_base}.pdf"))

def generate_cover_chua_bai(col):
    tag = f"cover_{col['grade']}_chuabai"
    grade_dir = os.path.join(SAN_PHAM_BASE, col["folder_name"])

    # Calculate page ranges
    cur_page = 2
    items_tex = ""
    for subfolder, wrapper_base, title in col["exams"]:
        cb_pdf = os.path.join(grade_dir, subfolder, f"{wrapper_base}.pdf")
        doc = fitz.open(cb_pdf)
        pcount = len(doc)
        end_page = cur_page + pcount - 1
        items_tex += f"\\item \\textbf{{{title}}} \\hfill \\textsl{{Trang {cur_page} -- {end_page}}} ({pcount} trang)\\\\[6pt]\n"
        cur_page += pcount

    tex = r"""\documentclass[11pt,a5paper]{article}
\usepackage[utf8]{vietnam}
\usepackage[top=0.8cm,bottom=1.0cm,left=0.9cm,right=0.9cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{tcolorbox}
\tcbuselibrary{skins}

\begin{document}
\thispagestyle{empty}

\begin{tcolorbox}[colback=blue!5!white,colframe=blue!80!black,arc=3mm,boxrule=1.2pt,center,width=\textwidth]
\centering
\vspace{0.1cm}
{\large\bfseries\color{blue!85!black} LỚP LÝ THẦY NGỌC}\\[3pt]
{\footnotesize\bfseries SĐT: 0935216256 \quad $\bullet$ \quad GV: TRẦN VĂN THIỆN NGỌC}\\[2pt]
{\scriptsize\textbf{CS1:} 50/2C Phạm Thị Liên \quad $\bullet$ \quad \textbf{CS2:} P A15 THPT Nguyễn Huệ \quad $\bullet$ \quad \textbf{CS3:} 24 Đặng Thái Thân}
\vspace{0.1cm}
\end{tcolorbox}

\vspace{0.25cm}

\begin{center}
{\Large\bfseries\color{red!85!black} TUYỂN TẬP """ + str(col["total_exams"]) + r""" BỘ ĐỀ THI GIỮA KỲ I}\\[5pt]
{\large\bfseries\color{blue!80!black} MÔN: """ + col["subject"] + r"""}\\[4pt]
{\normalsize\bfseries\color{magenta!85!black} (BẢN CHỮA BÀI TRỰC TUYẾN A5 -- CHIẾU MÀN HÌNH TO RÕ)}\\[5pt]
{\textit{\scriptsize Tài liệu dành cho Thầy chữa bài trực tiếp / Livestream ôn luyện học sinh}}
\end{center}

\vspace{0.2cm}

\begin{tcolorbox}[colback=white,colframe=red!75!black,arc=2.5mm,boxrule=1pt,title={\bfseries\normalsize MỤC LỤC BỘ ĐỀ THI CHỮA BÀI TRỰC TUYẾN (KHỔ A5)},center,width=\textwidth]
\vspace{0.1cm}
\begin{enumerate}
""" + items_tex + r"""\end{enumerate}
\vspace{0.05cm}
\end{tcolorbox}

\vfill
\begin{center}
{\scriptsize\color{gray!80!black}\textit{Tài liệu lưu hành nội bộ Lớp Lý Thầy Ngọc -- Chúc các em học tập và ôn luyện đạt kết quả xuất sắc!}}
\end{center}

\end{document}
"""
    tex_path = os.path.join(SCRATCH_DIR, f"{tag}.tex")
    with open(tex_path, 'w', encoding='utf-8') as fp:
        fp.write(tex)

    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{tag}.tex"], cwd=SCRATCH_DIR, capture_output=True, text=True)
    return os.path.join(SCRATCH_DIR, f"{tag}.pdf")

def merge_chua_bai_collections():
    print("\n" + "=" * 80)
    print("BƯỚC 2: GOM TỔNG HỢP CÁC FILE PDF CHỮA BÀI THÀNH FILE TỔNG HỢP TỪNG KHỐI")
    print("=" * 80)

    for col in EXAM_CONFIGS:
        cover_pdf = generate_cover_chua_bai(col)
        grade_dir = os.path.join(SAN_PHAM_BASE, col["folder_name"])
        out_dir = os.path.join(grade_dir, "00_Tong_Hop_Cac_De")
        mirror_out_dir = os.path.join(MIRROR_BASE, col["folder_name"], "00_Tong_Hop_Cac_De")
        os.makedirs(out_dir, exist_ok=True)
        os.makedirs(mirror_out_dir, exist_ok=True)

        main_path = os.path.join(out_dir, col["out_main"])
        alias_path = os.path.join(out_dir, col["out_alias"])

        master = fitz.open()

        # 1. Add Cover Page
        toc = [[1, "Trang bìa & Mục lục tuyển tập chữa bài", 1]]
        c_doc = fitz.open(cover_pdf)
        master.insert_pdf(c_doc)

        # 2. Add each exam and record bookmark
        cur_page = 2
        for subfolder, wrapper_base, title in col["exams"]:
            sub_pdf = os.path.join(grade_dir, subfolder, f"{wrapper_base}.pdf")
            s_doc = fitz.open(sub_pdf)
            toc.append([1, title, cur_page])
            cur_page += len(s_doc)
            master.insert_pdf(s_doc)

        # Set Bookmarks
        master.set_toc(toc)

        # Set Metadata
        master.set_metadata({
            "title": f"Tuyển tập Bộ đề thi Giữa kỳ I - {col['subject']} (Bản chữa bài trực tuyến)",
            "author": "TRẦN VĂN THIỆN NGỌC - LỚP LÝ THẦY NGỌC",
            "subject": f"{col['subject']} - Thừa Thiên Huế",
            "keywords": f"Lớp Lý Thầy Ngọc, Trần Văn Thiện Ngọc, {col['subject']}, Chữa bài trực tuyến, 4 dòng chấm, Giữa kỳ 1"
        })

        # Save
        master.save(main_path, garbage=4, deflate=True)
        shutil.copy2(main_path, alias_path)

        # Mirror
        shutil.copy2(main_path, os.path.join(mirror_out_dir, col["out_main"]))
        shutil.copy2(alias_path, os.path.join(mirror_out_dir, col["out_alias"]))

        print(f"  [XUẤT BẢN THÀNH CÔNG] {col['subject']} Bản Chữa Bài: {len(master)} trang")
        print(f"    -> {main_path}")
        print(f"    -> {alias_path}")

def main():
    generate_chua_bai_wrappers_and_compile()
    merge_chua_bai_collections()
    print("\n" + "=" * 80)
    print("HOÀN TẤT 100% CẢ 3 BỘ ĐỀ VẬT LÝ 10, 11, 12 BẢN CHỮA BÀI ONLINE!")
    print("=" * 80)

if __name__ == "__main__":
    main()
