import os
import sys
import glob

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path=None):
    if not os.path.exists(pdf_path):
        print(f"[LỖI] Không tìm thấy file: {pdf_path}")
        return False
    
    if not docx_path:
        base_name, _ = os.path.splitext(pdf_path)
        docx_path = f"{base_name}.docx"

    print(f"[*] Đang chuyển đổi: {os.path.basename(pdf_path)} -> {os.path.basename(docx_path)}...")
    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()
        print(f"[THÀNH CÔNG] Đã tạo file Word: {docx_path}")
        return True
    except Exception as e:
        print(f"[LỖI] Xảy ra sự cố khi chuyển đổi: {e}")
        return False

def convert_all_in_current_dir():
    pdf_files = glob.glob("*.pdf")
    if not pdf_files:
        print("[THÔNG BÁO] Không có file PDF nào trong thư mục hiện tại.")
        print("Hãy sao chép file PDF vào thư mục này rồi chạy lại kịch bản.")
        return

    print(f"[*] Tìm thấy {len(pdf_files)} file PDF cần chuyển đổi.")
    for pdf_file in pdf_files:
        convert_pdf_to_docx(pdf_file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Nếu truyền đường dẫn file qua tham số dòng lệnh hoặc kéo thả
        for arg in sys.argv[1:]:
            if os.path.isfile(arg) and arg.lower().endswith(".pdf"):
                convert_pdf_to_docx(arg)
            elif os.path.isdir(arg):
                for f in glob.glob(os.path.join(arg, "*.pdf")):
                    convert_pdf_to_docx(f)
    else:
        # Nếu chạy trực tiếp không có tham số: quét toàn bộ file PDF trong thư mục
        convert_all_in_current_dir()
