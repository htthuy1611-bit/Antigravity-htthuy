# -*- coding: utf-8 -*-
"""
HỆ THỐNG XUẤT BẢN TOÀN DIỆN BỘ ĐỀ VẬT LÝ LỚP 11 VÀ 12 (GIỮA KỲ I)
Gồm 13 đề:
  - 7 đề Vật lý 11: DHKH, HBT (24-25), HBT (25-26), NH, PDL, PHUBAI, QH
  - 6 đề Vật lý 12: BTX (Đề 1), BTX (Đề 2), CAOTHANG, NH, PDL, QH
Bản quyền độc quyền: LỚP TOÁN CÔ THÚY - GV: HỒ THỊ THÚY - SĐT: 0935.322.328 - 50/2C Phạm Thị Liên
Kiến trúc: Master Main (Master_De.tex & Master_HDG.tex)
Không chuyển sang Word theo yêu cầu của Giáo viên.
"""

import os
import sys
import re
import shutil
import subprocess

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
SAN_PHAM_DIR = os.path.join(BASE_DIR, "San_Pham")
MASTER_DIR = os.path.join(BASE_DIR, "He_Thong", "LaTeX", "Master")
STY_SRC = os.path.join(BASE_DIR, "He_Thong", "Quy_Chuan", "ex_test.sty")

os.makedirs(SAN_PHAM_DIR, exist_ok=True)

BRAND = r"Lớp Toán Cô Thúy -- SĐT: 0935.322.328 -- 50/2C Phạm Thị Liên"
LETTERS = "ABCD"

# TikZ thay thế cho VL11-DHKH
TIKZ_DHKH_1 = r"""\begin{tikzpicture}[>=stealth, scale=0.9, font=\footnotesize]
    \draw[->] (-0.2, 0) -- (6.5, 0) node[right] {$t\text{ (s)}$};
    \draw[->] (0, -2.2) -- (0, 2.4) node[above] {$x\text{ (cm)}$};
    \node[below left] at (0, 0) {$O$};
    \node[left] at (0, 1.8) {$A$};
    \node[left] at (0, -1.8) {$-A$};
    \draw[thick, blue, domain=0:6.28, samples=100] plot (\x, {1.8*cos(deg(\x))});
    \node[blue, above right] at (1.57, 0) {$(1)$};
    \draw[thick, red, dashed, domain=0:6.28, samples=100] plot (\x, {-1.8*cos(deg(\x))});
    \node[red, below right] at (1.57, 0) {$(2)$};
\end{tikzpicture}"""

TIKZ_DHKH_2 = r"""\begin{tikzpicture}[>=stealth, scale=0.9, font=\footnotesize]
    \draw[->] (-0.2, 0) -- (6.5, 0) node[right] {$t\text{ (s)}$};
    \draw[->] (0, -2.5) -- (0, 2.7) node[above] {$v\text{ (cm/s)}$};
    \node[below left] at (0, 0) {$O$};
    \draw[thick, blue!80!black, domain=0:6.28, samples=100] plot (\x, {2.0*sin(deg(\x))});
    \draw[dashed, red] (1.57, 2.0) -- (0, 2.0) node[left] {$5$};
    \draw[dashed, gray] (1.57, 0) -- (1.57, 2.0);
    \draw[dashed, red] (4.71, -2.0) -- (0, -2.0) node[left] {$-5$};
    \draw[dashed, gray] (4.71, 0) -- (4.71, -2.0);
    \filldraw[red] (1.57, 2.0) circle (1.5pt);
\end{tikzpicture}"""

EXAMS = [
    # ------------------ VẬT LÝ 11 ------------------
    {
        "id": "VL11_DHKH",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-11", "VL11-GHKI-DHKH-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL11_DHKH"),
        "school": "THPT ĐẠI HỌC KHOA HỌC",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 11",
        "year": "2025 -- 2026",
        "made": "132",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL11_DHKH_De_132",
        "out_hdg": "VL11_DHKH_HDG_132",
        "special": "dhkh_11"
    },
    {
        "id": "VL11_HBT_2425",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-11", "VL11-GHKI-HBT-2425.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL11_HBT_2425"),
        "school": "THPT HAI BÀ TRƯNG",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 11",
        "year": "2024 -- 2025",
        "made": "132",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL11_HBT_2425_De_132",
        "out_hdg": "VL11_HBT_2425_HDG_132",
    },
    {
        "id": "VL11_HBT_2526",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-11", "VL11-GHKI-HBT-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL11_HBT_2526"),
        "school": "THPT HAI BÀ TRƯNG",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 11",
        "year": "2025 -- 2026",
        "made": "001",
        "time": "40 phút (Không kể thời gian phát đề)",
        "out_de": "VL11_HBT_De_001",
        "out_hdg": "VL11_HBT_HDG_001",
    },
    {
        "id": "VL11_NH",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-11", "VL11-GHKI-NH-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL11_NH"),
        "school": "THPT NGUYỄN HUỆ",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 11",
        "year": "2025 -- 2026",
        "made": "101",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL11_NH_De_101",
        "out_hdg": "VL11_NH_HDG_101",
        "special": "nh_11"
    },
    {
        "id": "VL11_PDL",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-11", "VL11-GHKI-PDL-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL11_PDL"),
        "school": "THPT PHAN ĐĂNG LƯU",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 11",
        "year": "2025 -- 2026",
        "made": "2106",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL11_PDL_De_2106",
        "out_hdg": "VL11_PDL_HDG_2106",
    },
    {
        "id": "VL11_PHUBAI",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-11", "VL11-GHKI-PHUBAI-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL11_PHUBAI"),
        "school": "THPT PHÚ BÀI",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 11",
        "year": "2025 -- 2026",
        "made": "111",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL11_PHUBAI_De_111",
        "out_hdg": "VL11_PHUBAI_HDG_111",
    },
    {
        "id": "VL11_QH",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-11", "VL11-GHKI-QH-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL11_QH"),
        "school": "THPT CHUYÊN QUỐC HỌC - HUẾ",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 11",
        "year": "2025 -- 2026",
        "made": "562",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL11_QH_De_562",
        "out_hdg": "VL11_QH_HDG_562",
    },
    # ------------------ VẬT LÝ 12 ------------------
    {
        "id": "VL12_BTX_01",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-12", "VL12-GHKI-BTX-2526-01.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL12_BTX_01"),
        "school": "THPT BÙI THỊ XUÂN",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 12",
        "year": "2025 -- 2026",
        "made": "429",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL12_BTX_De_429",
        "out_hdg": "VL12_BTX_HDG_429",
    },
    {
        "id": "VL12_BTX_02",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-12", "VL12-GHKI-BTX-2526-02.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL12_BTX_02"),
        "school": "THPT BÙI THỊ XUÂN",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 12",
        "year": "2025 -- 2026",
        "made": "101",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL12_BTX_De_101",
        "out_hdg": "VL12_BTX_HDG_101",
        "special": "btx_12_02"
    },
    {
        "id": "VL12_CAOTHANG",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-12", "VL12-GHKI-CAOTHANG-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL12_CAOTHANG"),
        "school": "THPT CAO THẮNG",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 12",
        "year": "2025 -- 2026",
        "made": "246",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL12_CAOTHANG_De_246",
        "out_hdg": "VL12_CAOTHANG_HDG_246",
    },
    {
        "id": "VL12_NH",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-12", "VL12-GHKI-NH-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL12_NH"),
        "school": "THPT NGUYỄN HUỆ",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 12",
        "year": "2025 -- 2026",
        "made": "029",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL12_NH_De_029",
        "out_hdg": "VL12_NH_HDG_029",
    },
    {
        "id": "VL12_PDL",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-12", "VL12-GHKI-PDL-2526.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL12_PDL"),
        "school": "THPT PHAN ĐĂNG LƯU",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 12",
        "year": "2025 -- 2026",
        "made": "1204",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL12_PDL_De_1204",
        "out_hdg": "VL12_PDL_HDG_1204",
    },
    {
        "id": "VL12_QH",
        "src": os.path.join(BASE_DIR, "De_Goc", "2026-Dethi-GHK1-12", "VL12-GHKI-QH-2425.tex"),
        "target_dir": os.path.join(BASE_DIR, "He_Thong", "LaTeX", "VL12_QH"),
        "school": "THPT CHUYÊN QUỐC HỌC - HUẾ",
        "exam_de": "KIỂM TRA GIỮA KỲ I",
        "exam_hdg": "GIỮA KỲ I",
        "subject": "VẬT LÍ 12",
        "year": "2024 -- 2025",
        "made": "122",
        "time": "45 phút (Không kể thời gian phát đề)",
        "out_de": "VL12_QH_De_122",
        "out_hdg": "VL12_QH_HDG_122",
    }
]

def parse_balanced_braces(text, start_pos=0):
    groups = []
    i = start_pos
    n = len(text)
    while i < n:
        if text[i] == '{':
            depth = 1
            j = i + 1
            while j < n and depth > 0:
                if text[j] == '\\':
                    j += 2
                    continue
                elif text[j] == '{': depth += 1
                elif text[j] == '}': depth -= 1
                j += 1
            groups.append(text[i+1:j-1])
            i = j
        else: i += 1
    return groups

def clean_source_tex(raw, spec):
    # Loại bỏ hình đặc biệt
    if spec.get("special") == "dhkh_11":
        raw = raw.replace(r"\includegraphics[scale=1]{HINHVE-phai-Tikz/VL11-GHKI-DHKH-2526-hinh1}", TIKZ_DHKH_1)
        raw = raw.replace(r"\includegraphics[scale=1]{HINHVE-phai-Tikz/VL11-GHKI-DHKH-2526-hinh2}", TIKZ_DHKH_2)
    elif spec.get("special") == "btx_12_02":
        raw = raw.replace(r"\includegraphics[scale=0.4]{HINHVE-phai-Tikz/VL12-GHKI-BTX-2526-DE2-hinh1}", "")
    
    # Bỏ các comment hình cũ
    raw = re.sub(r'%\s*\\includegraphics.*?\n', '', raw)

    # Cắt bỏ phần dethi header cũ
    idx_dethi_end = raw.find(r'\end{dethi}')
    if idx_dethi_end != -1:
        body = raw[idx_dethi_end + len(r'\end{dethi}'):]
    else:
        body = raw

    # Cắt bỏ phần đáp án cũ ở cuối
    # Các mốc kết thúc: \newpage trước bảng đáp án, \indapan, hoặc nhãn kết thúc
    cut_pos = len(body)
    for marker in [r'\newpage' + '\n' + r'\begin{center} \textbf{BẢNG ĐÁP ÁN',
                   r'\newpage' + '\n' + r'\begin{center}' + '\n' + r'\textbf{\Large BẢNG ĐÁP ÁN',
                   r'\indapan{', r'\indapan[TF]{', r'\indapan[SA]{']:
        p = body.find(marker)
        if p != -1 and p < cut_pos:
            # Tìm dòng \newpage trước đó nếu có
            np_pos = body.rfind(r'\newpage', 0, p)
            if np_pos != -1 and (p - np_pos) < 300:
                cut_pos = min(cut_pos, np_pos)
            else:
                cut_pos = min(cut_pos, p)
    
    content = body[:cut_pos].strip()

    # Xóa các dòng thương hiệu cũ nếu có
    old_brands = ["LỚP LÝ THẦY KHÁNH", "LỚP VẬT LÝ THẦY NGỌC", "0935.216.256"]
    for ob in old_brands:
        content = content.replace(ob, "")

    return content

def extract_answer_table_tex(content, made):
    # Lấy các dòng không bắt đầu bằng %
    active_lines = [l for l in content.splitlines() if not l.strip().startswith('%')]
    text = '\n'.join(active_lines)

    # 1. P1
    p1 = []
    for m in re.finditer(r'\\choice(?![T])', text):
        rest = text[m.end():]
        end_m = re.search(r'\\loigiai|\\end\{ex\}', rest)
        block = rest[:end_m.start()] if end_m else rest[:500]
        choices = parse_balanced_braces(block)
        ans = "?"
        for idx, c in enumerate(choices[:4]):
            if r'\True' in c:
                ans = LETTERS[idx]
                break
        p1.append(ans)

    # 2. P2 (TF)
    p2 = []
    for m in re.finditer(r'\\choiceTF', text):
        rest = text[m.end():]
        end_m = re.search(r'\\loigiai|\\end\{ex\}', rest)
        block = rest[:end_m.start()] if end_m else rest[:500]
        choices = parse_balanced_braces(block)
        row = []
        for c in choices[:4]:
            row.append("Đ" if r'\True' in c else "S")
        p2.append(row)

    # 3. P3 (SA)
    p3 = []
    for m in re.finditer(r'\\shortans(?:\[.*?\])?\{([^}]+)\}', text):
        p3.append(m.group(1).strip())

    tex = "\\vspace{0.4cm}\n"
    tex += "\\noindent\\begin{minipage}{\\linewidth}\n"
    tex += f"\\begin{{center}}{{\\large\\bfseries\\color{{red!80!black}} BẢNG ĐÁP ÁN -- MÃ ĐỀ {made}}}\\end{{center}}\n\\vspace{{0.15cm}}\n"

    # In bảng P1
    if p1:
        tex += "\\noindent\\textbf{Phần I (Câu trắc nghiệm nhiều phương án lựa chọn).}\\par\\smallskip\n"
        # Chia theo nhóm 12 hoặc 16 câu mỗi bảng
        chunk_size = 12 if len(p1) <= 12 else (16 if len(p1) <= 16 else 12)
        for start_idx in range(0, len(p1), chunk_size):
            chunk = p1[start_idx:start_idx + chunk_size]
            cols = len(chunk)
            col_spec = "|c" * (cols + 1) + "|"
            tex += "\\begin{center}\n\\begin{tabular}{" + col_spec + "}\\hline\n"
            tex += "\\textbf{Câu} & " + " & ".join(str(start_idx + i + 1) for i in range(cols)) + " \\\\ \\hline\n"
            tex += "\\textbf{Đáp án} & " + " & ".join(f"\\textbf{{{ans}}}" for ans in chunk) + " \\\\ \\hline\n"
            tex += "\\end{tabular}\n\\end{center}\n"

    # In bảng P2
    if p2:
        tex += "\\noindent\\textbf{Phần II (Câu trắc nghiệm Đúng/Sai).}\\par\\smallskip\n"
        tex += "\\begin{center}\n\\begin{tabular}{|c|c|c|c|c|}\\hline\n"
        tex += "\\textbf{Câu} & \\textbf{a)} & \\textbf{b)} & \\textbf{c)} & \\textbf{d)} \\\\ \\hline\n"
        for i, row in enumerate(p2):
            while len(row) < 4: row.append("-")
            tex += f"{i+1} & " + " & ".join(row[:4]) + " \\\\ \\hline\n"
        tex += "\\end{tabular}\n\\end{center}\n"

    # In bảng P3
    if p3:
        tex += "\\noindent\\textbf{Phần III (Câu trắc nghiệm trả lời ngắn).}\\par\\smallskip\n"
        cols = len(p3)
        col_spec = "|c" * (cols + 1) + "|"
        tex += "\\begin{center}\n\\begin{tabular}{" + col_spec + "}\\hline\n"
        tex += "\\textbf{Câu} & " + " & ".join(str(i + 1) for i in range(cols)) + " \\\\ \\hline\n"
        tex += "\\textbf{Đáp án} & " + " & ".join(ans for ans in p3) + " \\\\ \\hline\n"
        tex += "\\end{tabular}\n\\end{center}\n"

    tex += "\\end{minipage}\n"
    return tex

def compile_pdf(target_dir, name):
    for run in range(2):
        res = subprocess.run(["pdflatex", "-interaction=nonstopmode", name + ".tex"], cwd=target_dir,
                             capture_output=True, text=True, encoding='utf-8', errors='ignore')
    log_file = os.path.join(target_dir, name + ".log")
    errors = []
    pages = "?"
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as fp:
            log_text = fp.read()
        errors = [l for l in log_text.splitlines() if l.startswith('!')]
        m = re.search(r"Output written on .*?\((\d+) pages?", log_text)
        if m: pages = m.group(1)
    return len(errors) == 0, len(errors), pages, errors

def process_single_exam(exam):
    print("=" * 80)
    print(f"XỬ LÝ ĐỀ: {exam['id']} ({exam['subject']} - {exam['school']})")
    print("=" * 80)

    tdir = exam["target_dir"]
    os.makedirs(tdir, exist_ok=True)
    os.makedirs(os.path.join(tdir, "ans"), exist_ok=True)

    # 1. Copy ex_test.sty
    shutil.copy2(STY_SRC, os.path.join(tdir, "ex_test.sty"))

    # 2. Đọc file nguồn & chuẩn hóa
    with open(exam["src"], 'r', encoding='utf-8', errors='ignore') as fp:
        raw = fp.read()

    noi_dung = clean_source_tex(raw, exam)
    noi_dung_path = os.path.join(tdir, "noi_dung.tex")
    with open(noi_dung_path, 'w', encoding='utf-8') as fp:
        fp.write(noi_dung)
    print(f"  [1/4] Đã tạo noi_dung.tex ({len(noi_dung)} bytes)")

    # 3. Tạo bảng đáp án
    bang_dap_an = extract_answer_table_tex(noi_dung, exam["made"])
    bang_dap_an_path = os.path.join(tdir, "bang_dap_an.tex")
    with open(bang_dap_an_path, 'w', encoding='utf-8') as fp:
        fp.write(bang_dap_an)
    print("  [2/4] Đã tạo bang_dap_an.tex")

    # 4. Tạo wrapper Đề và HDG
    wrapper_de = f"""\\def\\tentruong{{{exam['school']}}}
\\def\\tenkythi{{{exam['exam_de']}}}
\\def\\monhoc{{{exam['subject']}}}
\\def\\namhoc{{{exam['year']}}}
\\def\\made{{{exam['made']}}}
\\def\\thoigian{{{exam['time']}}}
\\def\\headertype{{dethi}}
\\def\\brand{{{BRAND}}}
\\def\\giaovien{{HỒ THỊ THÚY}}
\\def\\noidungfile{{noi_dung.tex}}

\\input{{../Master/Master_De.tex}}
"""

    wrapper_hdg = f"""\\def\\tentruong{{{exam['school']}}}
\\def\\tenkythi{{{exam['exam_hdg']}}}
\\def\\monhoc{{{exam['subject']}}}
\\def\\namhoc{{{exam['year']}}}
\\def\\made{{{exam['made']}}}
\\def\\thoigian{{{exam['time']}}}
\\def\\headertype{{dethi}}
\\def\\brand{{{BRAND}}}
\\def\\giaovien{{HỒ THỊ THÚY}}
\\def\\noidungfile{{noi_dung.tex}}
\\def\\inbangdapan{{\\input{{bang_dap_an.tex}}}}

\\input{{../Master/Master_HDG.tex}}
"""

    with open(os.path.join(tdir, exam["out_de"] + ".tex"), 'w', encoding='utf-8') as fp:
        fp.write(wrapper_de)
    with open(os.path.join(tdir, exam["out_hdg"] + ".tex"), 'w', encoding='utf-8') as fp:
        fp.write(wrapper_hdg)
    print("  [3/4] Đã tạo file wrapper Master Main Đề & HDG")

    # 5. Biên dịch pdflatex (2 passes)
    ok_de, err_de, p_de, errs_de = compile_pdf(tdir, exam["out_de"])
    print(f"  [PDF Đề]  {exam['out_de']}.pdf: {'THÀNH CÔNG' if ok_de else 'LỖI'} ({err_de} lỗi, {p_de} trang)")
    if not ok_de:
        for e in errs_de[:5]: print("     !", e)

    ok_hdg, err_hdg, p_hdg, errs_hdg = compile_pdf(tdir, exam["out_hdg"])
    print(f"  [PDF HDG] {exam['out_hdg']}.pdf: {'THÀNH CÔNG' if ok_hdg else 'LỖI'} ({err_hdg} lỗi, {p_hdg} trang)")
    if not ok_hdg:
        for e in errs_hdg[:5]: print("     !", e)

    # 6. Copy vào San_Pham
    for out_name, ok in [(exam["out_de"], ok_de), (exam["out_hdg"], ok_hdg)]:
        src_pdf = os.path.join(tdir, out_name + ".pdf")
        if os.path.exists(src_pdf):
            dst_pdf = os.path.join(SAN_PHAM_DIR, out_name + ".pdf")
            try:
                shutil.copy2(src_pdf, dst_pdf)
                print(f"  [COPY] Đã copy sang San_Pham/{out_name}.pdf")
            except PermissionError:
                alt = os.path.join(SAN_PHAM_DIR, out_name + "_moi.pdf")
                shutil.copy2(src_pdf, alt)
                print(f"  [CẢNH BÁO] {out_name}.pdf đang mở -> Lưu {os.path.basename(alt)}")

    return ok_de and ok_hdg

def main():
    print("================================================================================")
    print(" BẮT ĐẦU XUẤT BẢN TOÀN BỘ 13 ĐỀ VẬT LÝ LỚP 11 VÀ 12 (GIỮA HỌC KỲ I)")
    print("================================================================================")
    
    success = 0
    total = len(EXAMS)

    for i, exam in enumerate(EXAMS, 1):
        print(f"\n[{i}/{total}] TIẾN HÀNH...")
        ok = process_single_exam(exam)
        if ok: success += 1

    print("\n" + "=" * 80)
    print(f"TỔNG KẾT: {success}/{total} ĐỀ BIÊN DỊCH THÀNH CÔNG HOÀN TOÀN (0 LỖI)!")
    print("================================================================================")

if __name__ == "__main__":
    main()
