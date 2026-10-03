import re
import os
import sys
import subprocess

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def extract_braced(s, start):
    pos = s.find('{', start)
    if pos == -1:
        return None, -1
    depth = 1
    i = pos + 1
    while i < len(s) and depth > 0:
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
        i += 1
    if depth == 0:
        return s[pos+1:i-1], i
    return None, -1

def replace_choice_with_balanced(text, cmd_name, replace_fn):
    idx = 0
    res = []
    pattern = '\\' + cmd_name
    while True:
        pos = text.find(pattern, idx)
        if pos == -1:
            res.append(text[idx:])
            break
        res.append(text[idx:pos])
        cur = pos + len(pattern)
        args = []
        for _ in range(4):
            arg, cur = extract_braced(text, cur)
            if arg is None:
                break
            args.append(arg)
        if len(args) == 4:
            res.append(replace_fn(args))
            idx = cur
        else:
            res.append(pattern)
            idx = pos + len(pattern)
    return ''.join(res)

def prepare_latex_for_pandoc(tex_path, output_path):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if m:
        body = m.group(1)
    else:
        body = content

    # 1. Câu 4
    body = re.sub(
        r'\\immini\{\s*(.*?)\s*\}\{\s*\\begin\{tikzpicture\}.*?domain=2:6.*?\\end\{tikzpicture\}\s*\}',
        r'\\begin{tabular}{@{}p{0.68\\textwidth}p{0.3\\textwidth}@{}}\n\1 & \\includegraphics[width=0.28\\textwidth]{fig_cau4.png}\n\\end{tabular}',
        body, flags=re.DOTALL
    )

    # 2. Câu 8
    body = re.sub(
        r'\\immini\{\s*(.*?)\s*\}\{\s*\\begin\{tikzpicture\}.*?domain=1:5.*?\\end\{tikzpicture\}\s*\}',
        r'\\begin{tabular}{@{}p{0.68\\textwidth}p{0.3\\textwidth}@{}}\n\1 & \\includegraphics[width=0.28\\textwidth]{fig_cau8.png}\n\\end{tabular}',
        body, flags=re.DOTALL
    )

    # 3. Câu 1 Phần 2: Bảng biến thiên
    body = re.sub(
        r'\\begin\{center\}\s*\\begin\{tikzpicture\}\s*\\tkzTabInit.*?\\end\{tikzpicture\}\s*\\end\{center\}',
        r'\\begin{center}\\includegraphics[width=0.75\\textwidth]{fig_bbt.png}\\end{center}',
        body, flags=re.DOTALL
    )

    # 4. Câu 2 Phần 2: Tam giác
    body = re.sub(
        r'\\immini\{\s*(.*?)\s*\}\{\s*\\begin\{tikzpicture\}.*?coordinate \(A\).*?coordinate \(D\).*?\\end\{tikzpicture\}\s*\}',
        r'\\begin{tabular}{@{}p{0.7\\textwidth}p{0.28\\textwidth}@{}}\n\1 & \\includegraphics[width=0.26\\textwidth]{fig_tamgiac.png}\n\\end{tabular}',
        body, flags=re.DOTALL
    )

    # 5. Câu 3 Phần 2: Máy bay
    body = re.sub(
        r'\\immini\{\s*(.*?)\s*\}\{\s*\\begin\{tikzpicture\}.*?Máy bay.*?\\end\{tikzpicture\}\s*\}',
        r'\\begin{tabular}{@{}p{0.68\\textwidth}p{0.3\\textwidth}@{}}\n\1 & \\includegraphics[width=0.28\\textwidth]{fig_maybay.png}\n\\end{tabular}',
        body, flags=re.DOTALL
    )

    # 6. Câu 2 Phần 3: Shipper
    body = re.sub(
        r'\\immini\{\s*(.*?)\s*\}\{\s*\\begin\{tikzpicture\}.*?pos=0.35,above.*?\\end\{tikzpicture\}\s*\}',
        r'\\begin{tabular}{@{}p{0.65\\textwidth}p{0.32\\textwidth}@{}}\n\1 & \\includegraphics[width=0.3\\textwidth]{fig_shipper.png}\n\\end{tabular}',
        body, flags=re.DOTALL
    )

    # Thay đổi môi trường ex thành số câu tự động
    parts = body.split(r'\setcounter{ex}{0}')
    new_parts = []
    for part in parts:
        ex_count = 0
        def replace_ex(match):
            nonlocal ex_count
            ex_count += 1
            inner = match.group(1).strip()
            return f"\n\n\\textbf{{Câu {ex_count}.}} {inner}\n\n"
        p = re.sub(r'\\begin\{ex\}(.*?)\\end\{ex\}', replace_ex, part, flags=re.DOTALL)
        new_parts.append(p)
    body = '\n'.join(new_parts)

    # Xử lý \choice bằng balanced braces
    def format_choice(args):
        c1, c2, c3, c4 = [a.replace(r'\True', '').strip() for a in args]
        return f"\n\n\\begin{{tabular}}{{@{{}}p{{0.24\\textwidth}}p{{0.24\\textwidth}}p{{0.24\\textwidth}}p{{0.24\\textwidth}}@{{}}}}\n\\textbf{{A.}} {c1} & \\textbf{{B.}} {c2} & \\textbf{{C.}} {c3} & \\textbf{{D.}} {c4}\n\\end{{tabular}}\n\n"

    body = replace_choice_with_balanced(body, 'choice', format_choice)

    # Xử lý \choiceTF bằng balanced braces
    def format_choicetf(args):
        c1, c2, c3, c4 = [a.replace(r'\True', '').strip() for a in args]
        return f"\n\n\\begin{{enumerate}}[label=\\alph*)]\n\\item {c1}\n\\item {c2}\n\\item {c3}\n\\item {c4}\n\\end{{enumerate}}\n\n"

    body = replace_choice_with_balanced(body, 'choiceTF', format_choicetf)

    # Xử lý \par\shortans[oly]{ans} -> Khung KQ
    body = re.sub(r'\\par\\shortans\[oly\]\{[^}]*\}', r'\n\n\\textbf{KQ:} \\fbox{\\phantom{\\rule{2.5cm}{0.5cm}}}\n\n', body)

    # Dọn dẹp
    body = re.sub(r'\\loigiai\{.*?\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\setcounter\{.*?\}\{.*?\}', '', body)

    template = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage[top=2cm,bottom=2cm,left=2cm,right=2cm]{geometry}
\begin{document}
""" + body + r"""
\end{document}
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    print(f"Đã tạo file tiền xử lý cho Pandoc: {output_path}")

if __name__ == '__main__':
    prepare_latex_for_pandoc('De_Thi_2009.tex', 'De_Thi_2009_pandoc.tex')
    pandoc_exe = os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")
    cmd = [pandoc_exe, 'De_Thi_2009_pandoc.tex', '-o', 'De_Thi_2009.docx']
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        print("[THÀNH CÔNG] Đã tạo file Word chuẩn: De_Thi_2009.docx")
    else:
        print("[LỖI PANDOC]:", res.stderr)
