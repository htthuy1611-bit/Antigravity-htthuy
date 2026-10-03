import os
import sys
import json
import hashlib
from datetime import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
DE_GOC_DIR = os.path.join(BASE_DIR, "De_Goc")
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
HE_THONG_DIR = os.path.join(BASE_DIR, "He_Thong")
HISTORY_JSON = os.path.join(HE_THONG_DIR, "Lich_Su_Xu_Ly.json")
HISTORY_MD = os.path.join(HE_THONG_DIR, "Lich_Su_Xu_Ly.md")

os.makedirs(DE_GOC_DIR, exist_ok=True)
os.makedirs(SAN_PHAM_DIR, exist_ok=True)
os.makedirs(HE_THONG_DIR, exist_ok=True)

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest().upper()

def load_history():
    if os.path.exists(HISTORY_JSON):
        try:
            with open(HISTORY_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_files": 0,
        "completed_files": 0,
        "pending_files": 0,
        "records": {}
    }

def save_history(history):
    history["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history["total_files"] = len(history["records"])
    history["completed_files"] = sum(1 for r in history["records"].values() if r.get("status") == "HOAN_THANH")
    history["pending_files"] = history["total_files"] - history["completed_files"]
    
    with open(HISTORY_JSON, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
        
    generate_markdown(history)

def generate_markdown(history):
    lines = [
        "# 📋 LỊCH SỬ VÀ TRẠNG THÁI XỬ LÝ ĐỀ THI (LỚP TOÁN CÔ THÚY)",
        "",
        f"> **Lần cập nhật gần nhất:** `{history['updated_at']}`  ",
        f"> **Tổng số đề gốc:** `{history['total_files']}` | **Đã hoàn thành:** `{history['completed_files']}` | **Đang chờ xử lý:** `{history['pending_files']}`",
        "",
        "| STT | File Đề Gốc (PDF) | Sản Phẩm Word (.docx) | Sản Phẩm PDF (.pdf) | Trạng Thái | Ngày Xử Lý | Ghi Chú |",
        "| :---: | :--- | :--- | :--- | :---: | :---: | :--- |"
    ]
    
    idx = 1
    for fname, rec in sorted(history["records"].items()):
        status_icon = "✅ Đã xong" if rec.get("status") == "HOAN_THANH" else "⏳ Chờ xử lý"
        pdf_goc_path = f"file:///{os.path.join(DE_GOC_DIR, fname).replace(chr(92), '/')}"
        
        docx_rel = rec.get("output_docx", "")
        if docx_rel and os.path.exists(os.path.join(BASE_DIR, docx_rel)):
            docx_abs = f"file:///{os.path.join(BASE_DIR, docx_rel).replace(chr(92), '/')}"
            docx_link = f"[{os.path.basename(docx_rel)}]({docx_abs})"
        else:
            docx_link = "*(chưa có)*"
            
        pdf_prod_rel = rec.get("output_pdf", "")
        if pdf_prod_rel and os.path.exists(os.path.join(BASE_DIR, pdf_prod_rel)):
            pdf_prod_abs = f"file:///{os.path.join(BASE_DIR, pdf_prod_rel).replace(chr(92), '/')}"
            pdf_prod_link = f"[{os.path.basename(pdf_prod_rel)}]({pdf_prod_abs})"
        else:
            pdf_prod_link = "*(chưa có)*"
            
        date_proc = rec.get("date_processed", rec.get("date_added", "-"))
        note = rec.get("note", "")
        
        lines.append(f"| {idx} | [{fname}]({pdf_goc_path}) | {docx_link} | {pdf_prod_link} | {status_icon} | `{date_proc}` | {note} |")
        idx += 1
        
    lines.append("")
    lines.append("---")
    lines.append("### 💡 Hướng dẫn vận hành:")
    lines.append("1. **Thêm đề mới**: Chép file `.pdf` cần chuyển đổi vào thư mục [`De_Goc/`](file:///c:/AnTiGraViTy-htthuy/pdf2word/De_Goc).")
    lines.append("2. **Kiểm tra danh sách chờ**: Chạy `python He_Thong/Cong_Cu/quan_ly_de_goc.py --pending` hoặc yêu cầu trợ lý xử lý.")
    lines.append("3. **Sản phẩm xuất ra**: Tự động đặt tên trùng khớp theo file gốc và lưu tại thư mục [`San_Pham/`](file:///c:/AnTiGraViTy-htthuy/pdf2word/San_Pham).")

    with open(HISTORY_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def scan_de_goc():
    history = load_history()
    pdf_files = [f for f in os.listdir(DE_GOC_DIR) if f.lower().endswith(".pdf")]
    
    print(f"[*] Quét thư mục Đề Gốc: {DE_GOC_DIR}")
    print(f"[*] Tìm thấy {len(pdf_files)} file PDF trong De_Goc/.")
    
    new_count = 0
    for pdf in pdf_files:
        pdf_path = os.path.join(DE_GOC_DIR, pdf)
        file_size = os.path.getsize(pdf_path)
        file_sha256 = compute_sha256(pdf_path)
        
        base_name = os.path.splitext(pdf)[0]
        expected_docx = f"San_Pham/{base_name}.docx"
        expected_pdf = f"San_Pham/{base_name}.pdf"
        
        if pdf not in history["records"]:
            # File mới thêm vào
            docx_exists = os.path.exists(os.path.join(BASE_DIR, expected_docx))
            pdf_exists = os.path.exists(os.path.join(BASE_DIR, expected_pdf))
            
            status = "HOAN_THANH" if (docx_exists and pdf_exists) else "CHUA_XU_LY"
            history["records"][pdf] = {
                "file_name": pdf,
                "file_relpath": f"De_Goc/{pdf}",
                "sha256": file_sha256,
                "size_bytes": file_size,
                "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "date_processed": datetime.now().strftime("%Y-%m-%d %H:%M:%S") if status == "HOAN_THANH" else None,
                "status": status,
                "output_docx": expected_docx if docx_exists else None,
                "output_pdf": expected_pdf if pdf_exists else None,
                "note": "File mới nạp vào hệ thống" if status == "CHUA_XU_LY" else "Đã phát hiện file sản phẩm tương ứng"
            }
            new_count += 1
            print(f"  + [MỚI] Phát hiện file: {pdf} (Trạng thái: {status})")
        else:
            # File đã có trong lịch sử, kiểm tra xem có bị chỉnh sửa không
            rec = history["records"][pdf]
            if rec.get("sha256") != file_sha256:
                print(f"  ! [CẢNH BÁO] File {pdf} đã bị sửa đổi nội dung! Chuyển trạng thái sang CHUA_XU_LY.")
                rec["sha256"] = file_sha256
                rec["size_bytes"] = file_size
                rec["status"] = "CHUA_XU_LY"
                rec["note"] = "File gốc đã thay đổi nội dung (cần chạy lại)"
            else:
                # Kiểm tra xem sản phẩm có còn tồn tại không
                docx_path = os.path.join(BASE_DIR, rec.get("output_docx", ""))
                if not os.path.exists(docx_path) and rec.get("status") == "HOAN_THANH":
                    print(f"  ! File sản phẩm {rec.get('output_docx')} bị thiếu! Chuyển trạng thái sang CHUA_XU_LY.")
                    rec["status"] = "CHUA_XU_LY"

    save_history(history)
    print(f"\n[KẾT QUẢ QUÉT]")
    print(f"  - Tổng số file trong De_Goc/: {history['total_files']}")
    print(f"  - Đã hoàn thành sản phẩm: {history['completed_files']}")
    print(f"  - Đang chờ xử lý (mới nạp): {history['pending_files']}")
    print(f"  - Bảng lịch sử Markdown đã lưu tại: {HISTORY_MD}")
    return history

def get_pending_files():
    history = load_history()
    pending = []
    for fname, rec in history["records"].items():
        if rec.get("status") != "HOAN_THANH":
            pending.append(fname)
    return pending

if __name__ == "__main__":
    if "--pending" in sys.argv:
        p = get_pending_files()
        if p:
            print(f"[DANH SÁCH FILE CHƯA XỬ LÝ] ({len(p)} file):")
            for f in p:
                print(f"  -> {f}")
        else:
            print("[THÔNG BÁO] Tất cả file trong De_Goc/ đều đã được xử lý hoàn tất!")
    else:
        scan_de_goc()
