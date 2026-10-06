# -*- coding: utf-8 -*-
"""
BIÊN DỊCH LẠI TOÀN BỘ CÁC FILE ĐỀ VÀ HƯỚNG DẪN GIẢI CHO TẤT CẢ 21 TRƯỜNG (LỚP 10, 11, 12)
ĐẢM BẢO TẤT CẢ FILE PDF CẬP NHẬT 100% TỪ NOI_DUNG.TEX ĐÃ SẠCH DẤU CHẤM.
"""

import os
import sys
import subprocess
import time
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

GRADES = [
    ("VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1", [
        "01_THPT_Bui_Thi_Xuan_De_207",
        "02_THPT_Hai_Ba_Trung_De_209",
        "03_THPT_Nguyen_Hue_De_494",
        "04_THPT_Nguyen_Hue_De_101",
        "05_THPT_Nguyen_Tat_Thanh_De_102",
        "06_THPT_Phan_Dang_Luu_De_1008",
        "07_THPT_Quoc_Hoc_De_104",
    ]),
    ("VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1", [
        "01_Chuyen_DHKH_Hue_De_132",
        "02_THPT_Hai_Ba_Trung_2425_De_132",
        "03_THPT_Hai_Ba_Trung_2526_De_001",
        "04_THPT_Nguyen_Hue_De_101",
        "05_THPT_Phan_Dang_Luu_De_2106",
        "06_THPT_Phu_Bai_De_111",
        "07_THPT_Quoc_Hoc_De_562",
    ]),
    ("VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1", [
        "01_THPT_Bui_Thi_Xuan_De_429",
        "02_THPT_Bui_Thi_Xuan_De_101",
        "03_THPT_Cao_Thang_De_246",
        "04_THPT_Nguyen_Hue_De_029",
        "05_THPT_Phan_Dang_Luu_De_1204",
        "06_THPT_Quoc_Hoc_De_122",
        "07_THPT_Hai_Ba_Trung_2425_De_101",
        "08_THPT_Hai_Ba_Trung_2526_De_101",
        "09_THPT_Quoc_Hoc_2526_De_101",
    ])
]

def compile_tex(exam_dir, tex_file):
    base_name = os.path.splitext(tex_file)[0]
    pdf_file = f"{base_name}.pdf"
    full_pdf = os.path.join(exam_dir, pdf_file)
    
    # Ensure ans dir exists
    os.makedirs(os.path.join(exam_dir, "ans"), exist_ok=True)
    
    print(f"  Biên dịch {tex_file}...")
    time.sleep(0.2)
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], cwd=exam_dir, capture_output=True, text=True, encoding='latin-1', errors='replace')
    if res.returncode != 0:
        print(f"    [Lỗi pass 1]: {res.stdout[-250:]}")
        time.sleep(1.0)
        res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], cwd=exam_dir, capture_output=True, text=True, encoding='latin-1', errors='replace')
    
    if res.returncode == 0:
        time.sleep(0.3)
        res2 = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], cwd=exam_dir, capture_output=True, text=True, encoding='latin-1', errors='replace')
        if os.path.exists(full_pdf):
            time.sleep(0.2)
            doc = fitz.open(full_pdf)
            p = len(doc)
            doc.close()
            print(f"    -> OK: {p} trang")
            return True
    print(f"    [THẤT BẠI] {tex_file}")
    return False

def main():
    print("=" * 80)
    print("BIÊN DỊCH LẠI TOÀN BỘ 21 ĐỀ VÀ HƯỚNG DẪN GIẢI")
    print("=" * 80)
    
    total_compiled = 0
    total_success = 0
    
    for grade_folder, exams in GRADES:
        print(f"\n>>> KHỐI: {grade_folder}")
        grade_path = os.path.join(SAN_PHAM_BASE, grade_folder)
        mirror_grade_path = os.path.join(MIRROR_BASE, grade_folder)
        
        for subfolder in exams:
            exam_dir = os.path.join(grade_path, subfolder)
            mirror_exam_dir = os.path.join(mirror_grade_path, subfolder)
            print(f"\n[Trường] {subfolder}")
            
            # Find _De_ and _HDG_ tex files
            tex_files = [f for f in os.listdir(exam_dir) if f.endswith('.tex') and ('_De_' in f or f.endswith('_De.tex') or '_HDG_' in f or f.endswith('_HDG.tex'))]
            for tf in sorted(tex_files):
                total_compiled += 1
                if compile_tex(exam_dir, tf):
                    total_success += 1
                    # Mirror pdf to mirror folder
                    pdf_name = os.path.splitext(tf)[0] + '.pdf'
                    src_pdf = os.path.join(exam_dir, pdf_name)
                    dst_pdf = os.path.join(mirror_exam_dir, pdf_name)
                    if os.path.exists(src_pdf):
                        try:
                            os.makedirs(mirror_exam_dir, exist_ok=True)
                            shutil.copy2(src_pdf, dst_pdf)
                        except Exception as e:
                            print(f"    [Mirror warning] {e}")

    print("\n" + "=" * 80)
    print(f"TỔNG KẾT: Đã biên dịch {total_success}/{total_compiled} file thành công!")
    print("=" * 80)

if __name__ == "__main__":
    main()
