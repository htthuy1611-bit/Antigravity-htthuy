import os
import sys
import subprocess
import glob

def compile_tex_to_pdf(tex_path):
    if not os.path.exists(tex_path):
        print(f"[LỖI] Không tìm thấy file: {tex_path}")
        return False
    
    tex_dir = os.path.dirname(os.path.abspath(tex_path))
    tex_file = os.path.basename(tex_path)
    
    print(f"[*] Đang biên dịch: {tex_file} -> PDF...")
    try:
        # Chạy pdflatex (chạy 2 lần để cập nhật số trang/nhãn tham chiếu)
        cmd = ["pdflatex", "-synctex=1", "-interaction=nonstopmode", tex_file]
        res = subprocess.run(cmd, cwd=tex_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
        
        pdf_name = os.path.splitext(tex_file)[0] + ".pdf"
        pdf_path = os.path.join(tex_dir, pdf_name)
        if os.path.exists(pdf_path):
            print(f"[THÀNH CÔNG] Đã tạo file PDF: {pdf_name}")
            return True
        else:
            print("[LỖI] Không thể tạo file PDF. Chi tiết lỗi:")
            print(res.stdout[-1500:] if len(res.stdout) > 1500 else res.stdout)
            return False
    except Exception as e:
        print(f"[LỖI] Không thể chạy pdflatex: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if os.path.isfile(arg) and arg.lower().endswith(".tex"):
                compile_tex_to_pdf(arg)
    else:
        tex_files = glob.glob("*.tex")
        if not tex_files:
            print("[THÔNG BÁO] Không có file .tex nào trong thư mục.")
        for tex in tex_files:
            compile_tex_to_pdf(tex)
