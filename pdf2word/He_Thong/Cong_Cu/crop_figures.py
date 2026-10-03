import fitz

doc = fitz.open(r'c:\AnTiGraViTy-htthuy\pdf2word\De_Thi_Goc_2009.pdf')

# Thiết lập tỷ lệ zoom để ảnh cực kỳ sắc nét (zoom = 4.0 tương đương ~300-400 DPI)
mat = fitz.Matrix(4.0, 4.0)

crops = {
    # Page 1: Đồ thị Câu 4 (x0, y0, x1, y1)
    "fig_cau4.png": (0, fitz.Rect(380, 362, 560, 482)),
    # Page 1: Đồ thị Câu 8
    "fig_cau8.png": (0, fitz.Rect(390, 665, 555, 795)),
    # Page 2: Bảng biến thiên Câu 1 Phần 2
    "fig_bbt.png": (1, fitz.Rect(180, 385, 420, 515)),
    # Page 2: Tam giác Câu 2 Phần 2
    "fig_tamgiac.png": (1, fitz.Rect(440, 575, 560, 735)),
    # Page 3: Máy bay Oxyz Câu 3 Phần 2
    "fig_maybay.png": (2, fitz.Rect(180, 35, 430, 235)),
    # Page 3: Sơ đồ Shipper Câu 2 Phần 3
    "fig_shipper.png": (2, fitz.Rect(340, 640, 560, 775)),
}

import os
out_dir = r"c:\AnTiGraViTy-htthuy\pdf2word\He_Thong\Hinh_Anh"
latex_dir = r"c:\AnTiGraViTy-htthuy\pdf2word\He_Thong\LaTeX"

for name, (page_idx, rect) in crops.items():
    page = doc[page_idx]
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    
    out_path = os.path.join(out_dir, name)
    pix.save(out_path)
    
    latex_path = os.path.join(latex_dir, name)
    pix.save(latex_path)
    print(f"Cropped {name}: size={pix.width}x{pix.height} to {out_path}")

print("Hoàn tất crop 6 hình ảnh từ PDF gốc!")
