# -*- coding: utf-8 -*-
"""
TỰ ĐỘNG CHÈN MÃ CÂU HỎI DUY NHẤT (\macau{ID: ...}) CHO TOÀN BỘ CÁC CÂU HỎI LATEX TRONG DỰ ÁN
Bảo đảm:
1. Mỗi câu có đúng 1 mã câu hỏi duy nhất, không trùng lặp.
2. Mã câu hỏi được định nghĩa hiển thị ở file Giáo viên, ẩn hoàn toàn ở file Học sinh.
"""

import os
import sys
import re
import shutil

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

FILES_CONFIG = [
    # --- VẬT LÝ 10 ---
    ("SAN PHAM/VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1/01_THPT_Bui_Thi_Xuan_De_207/noi_dung.tex", "VL10-BTX207-C"),
    ("SAN PHAM/VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1/02_THPT_Hai_Ba_Trung_De_209/noi_dung.tex", "VL10-HBT209-C"),
    ("SAN PHAM/VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1/03_THPT_Nguyen_Hue_De_494/noi_dung.tex", "VL10-NH494-C"),
    ("SAN PHAM/VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1/04_THPT_Nguyen_Hue_De_101/noi_dung.tex", "VL10-NH101-C"),
    ("SAN PHAM/VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1/05_THPT_Nguyen_Tat_Thanh_De_102/noi_dung.tex", "VL10-NTT102-C"),
    ("SAN PHAM/VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1/06_THPT_Phan_Dang_Luu_De_1008/noi_dung.tex", "VL10-PDL1008-C"),
    ("SAN PHAM/VAT LY 10 - BỘ ĐỀ GIỮA KỲ 1/07_THPT_Quoc_Hoc_De_104/noi_dung.tex", "VL10-QH104-C"),

    # --- VẬT LÝ 11 ---
    ("SAN PHAM/VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1/01_Chuyen_DHKH_Hue_De_132/noi_dung.tex", "VL11-DHKH132-C"),
    ("SAN PHAM/VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1/02_THPT_Hai_Ba_Trung_2425_De_132/noi_dung.tex", "VL11-HBT2425-C"),
    ("SAN PHAM/VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1/03_THPT_Hai_Ba_Trung_2526_De_001/noi_dung.tex", "VL11-HBT2526-C"),
    ("SAN PHAM/VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1/04_THPT_Nguyen_Hue_De_101/noi_dung.tex", "VL11-NH101-C"),
    ("SAN PHAM/VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1/05_THPT_Phan_Dang_Luu_De_2106/noi_dung.tex", "VL11-PDL2106-C"),
    ("SAN PHAM/VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1/06_THPT_Phu_Bai_De_111/noi_dung.tex", "VL11-PB111-C"),
    ("SAN PHAM/VAT LY 11 - BỘ ĐỀ GIỮA KỲ 1/07_THPT_Quoc_Hoc_De_562/noi_dung.tex", "VL11-QH562-C"),

    # --- VẬT LÝ 12 ---
    ("SAN PHAM/VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1/01_THPT_Bui_Thi_Xuan_De_429/noi_dung.tex", "VL12-BTX429-C"),
    ("SAN PHAM/VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1/02_THPT_Bui_Thi_Xuan_De_101/noi_dung.tex", "VL12-BTX101-C"),
    ("SAN PHAM/VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1/03_THPT_Cao_Thang_De_246/noi_dung.tex", "VL12-CT246-C"),
    ("SAN PHAM/VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1/04_THPT_Nguyen_Hue_De_029/noi_dung.tex", "VL12-NH029-C"),
    ("SAN PHAM/VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1/05_THPT_Phan_Dang_Luu_De_1204/noi_dung.tex", "VL12-PDL1204-C"),
    ("SAN PHAM/VAT LY 12 - BỘ ĐỀ GIỮA KỲ 1/06_THPT_Quoc_Hoc_De_122/noi_dung.tex", "VL12-QH122-C"),

    # --- TOÁN 10 ---
    ("SAN PHAM/TOAN 10 - KNTT/Chuong_5_Bai_1/noi_dung.tex", "TOAN10-C5B1-C"),
    ("SAN PHAM/TOAN 10 - KNTT/Chuong_5_Bai_2/noi_dung.tex", "TOAN10-C5B2-C"),
    ("SAN PHAM/TOAN 10 - KNTT/Chuong_5_Bai_3/noi_dung.tex", "TOAN10-C5B3-C"),

    # --- TOÁN 9 ---
    ("SAN PHAM/TOAN 9 - KNTT/noi_dung.tex", "TOAN9-C5B17-C"),

    # --- ĐỀ THI 2009 ---
    ("SAN PHAM/DE THI 2009/De_Thi_2009.tex", "DETHI2009-C"),

    # --- BẢO THẮNG 3 (LÀO CAI) ---
    ("pdf2word/He_Thong/LaTeX/Bao_Thang_3/0101/noi_dung.tex", "TOAN12-BT3-0101-C"),
    ("pdf2word/He_Thong/LaTeX/Bao_Thang_3/0102/noi_dung.tex", "TOAN12-BT3-0102-C"),
    ("pdf2word/He_Thong/LaTeX/Bao_Thang_3/0103/noi_dung.tex", "TOAN12-BT3-0103-C"),
    ("pdf2word/He_Thong/LaTeX/Bao_Thang_3/0104/noi_dung.tex", "TOAN12-BT3-0104-C"),
]

def inject_macau_by_split(text, prefix):
    parts = text.split(r'\begin{ex}')
    new_parts = []
    count = 0
    for part in parts[1:]:
        if r'\macau{' in part[:120]:
            new_parts.append(part)
            continue
        count += 1
        cid = f'{prefix}{count:02d}'
        macau_tag = f'\\macau{{ID: {cid}}}'
        
        # Strip leading comment like %[11V1-...]
        m_comment = re.match(r'^%[^\n]*\n', part)
        if m_comment:
            part = part[m_comment.end():]
            
        m_immini = re.match(r'^(\s*\\immini\s*\{)', part)
        if m_immini:
            new_part = part[:m_immini.end()] + macau_tag + part[m_immini.end():]
        else:
            m_nw = re.search(r'\S', part)
            if m_nw:
                new_part = part[:m_nw.start()] + macau_tag + part[m_nw.start():]
            else:
                new_part = ' ' + macau_tag + part
        new_parts.append(new_part)
        
    return parts[0] + ''.join(r'\begin{ex}' + p for p in new_parts), count

def main():
    total_injected = 0
    for rel_path, prefix in FILES_CONFIG:
        abs_path = os.path.abspath(rel_path)
        if not os.path.exists(abs_path):
            print(f"[BỎ QUA] Không tìm thấy {rel_path}")
            continue
        with open(abs_path, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        
        new_content, count = inject_macau_by_split(content, prefix)
        with open(abs_path, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        
        print(f"[THÀNH CÔNG] {rel_path} -> Đã chèn {count} mã câu hỏi với prefix [{prefix}]")
        total_injected += count

        # Đồng bộ sang pdf2word/San_Pham tương ứng nếu file nằm trong SAN PHAM
        if rel_path.startswith("SAN PHAM/"):
            mirror_path = rel_path.replace("SAN PHAM/", "pdf2word/San_Pham/")
            os.makedirs(os.path.dirname(mirror_path), exist_ok=True)
            shutil.copy2(abs_path, mirror_path)

    print("=" * 70)
    print(f"TỔNG CỘNG ĐÃ CHÈN {total_injected} MÃ CÂU HỎI MỚI VÀO CÁC FILE ĐỀ THI!")

if __name__ == "__main__":
    main()
