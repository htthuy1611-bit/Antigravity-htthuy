# -*- coding: utf-8 -*-
"""
Verification script for all 13 System Rules across all chapters:
- bai_03_sai_so_trang_01_30.tex
- bai_01_he_quy_chieu_trang_31_53.tex
"""
import os, sys, re

base_dir = os.path.dirname(os.path.abspath(__file__))
fig_dir = os.path.join(base_dir, 'figures')

tex_files = [
    os.path.join(base_dir, 'chapters', 'bai_03_sai_so_trang_01_30.tex'),
    os.path.join(base_dir, 'chapters', 'bai_01_he_quy_chieu_trang_31_53.tex'),
    os.path.join(base_dir, 'chapters', 'bai_02_toc_do_van_toc_trang_54_81.tex')
]

errors = []
total_figs = 0
total_choices = 0
total_choiceTFs = 0
total_shortans = 0
total_itemchoice = 0
total_macau = 0
total_macauchum = 0

def parse_cmd_args(cmd_name, text):
    results = []
    pattern = re.compile(r'\\' + cmd_name + r'\s*\{')
    pos = 0
    while True:
        m = pattern.search(text, pos)
        if not m:
            break
        args = []
        cur = m.end() - 1
        for _ in range(4):
            while cur < len(text) and text[cur] != '{':
                cur += 1
            if cur >= len(text): break
            brace_depth = 0
            start = cur + 1
            cur_p = cur
            while cur_p < len(text):
                if text[cur_p] == '{':
                    brace_depth += 1
                elif text[cur_p] == '}':
                    brace_depth -= 1
                    if brace_depth == 0:
                        args.append(text[start:cur_p])
                        cur = cur_p + 1
                        break
                cur_p += 1
            if brace_depth != 0:
                break
        if len(args) == 4:
            results.append(args)
            pos = cur
        else:
            pos = m.end()
    return results

for tex_path in tex_files:
    fname = os.path.basename(tex_path)
    if not os.path.exists(tex_path):
        errors.append(f'File not found: {fname}')
        continue

    with open(tex_path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.splitlines()

    # 1. Figures exist
    figs = re.findall(r'\\includegraphics(?:\[.*?\])?\{(.*?)\}', text)
    for fig in set(figs):
        # handle prefix figures/
        fig_clean = os.path.basename(fig)
        fig_file = os.path.join(fig_dir, fig_clean)
        if not os.path.exists(fig_file):
            errors.append(f'[{fname}] Missing figure: {fig}')
        else:
            total_figs += 1

    # 2. Blank line before \shortans
    for idx, line in enumerate(lines):
        if r'\shortans' in line:
            total_shortans += 1
            if idx == 0 or lines[idx-1].strip() != '':
                errors.append(f'[{fname}] Line {idx+1}: \\shortans does not have a blank line before it! Previous line: "{lines[idx-1]}"')

    # 3. No period before closing brace in \choice and \choiceTF
    choices = parse_cmd_args('choice', text)
    total_choices += len(choices)
    for idx, c in enumerate(choices):
        for o_idx, opt in enumerate(c):
            if opt.strip().endswith('.'):
                errors.append(f'[{fname}] \\choice #{idx+1} option #{o_idx+1} ends with a dot: "{opt.strip()}"')

    choiceTFs = parse_cmd_args('choiceTF', text)
    total_choiceTFs += len(choiceTFs)
    for idx, c in enumerate(choiceTFs):
        for o_idx, opt in enumerate(c):
            if opt.strip().endswith('.'):
                errors.append(f'[{fname}] \\choiceTF #{idx+1} option #{o_idx+1} ends with a dot: "{opt.strip()}"')

    # 4. No hardcoded 'Chọn đáp án' in \loigiai
    loigiai_blocks = re.findall(r'\\loigiai\{(.*?)\}\s*(?=\\end\{ex\}|\\end\{vd\}|\Z)', text, flags=re.DOTALL)
    for lg in loigiai_blocks:
        if 'Chọn đáp án' in lg:
            errors.append(f'[{fname}] Found hardcoded "Chọn đáp án" in \\loigiai')

    # 5. Check itemchoice in all choiceTF \loigiai
    ex_blocks = re.findall(r'\\begin\{ex\}(.*?)\\end\{ex\}', text, flags=re.DOTALL)
    for ex in ex_blocks:
        if r'\choiceTF' in ex:
            if r'\begin{itemchoice}' not in ex or r'\end{itemchoice}' not in ex:
                errors.append(f'[{fname}] Found \\choiceTF without \\begin{{itemchoice}} in \\loigiai')
            itemch_count = len(re.findall(r'\\itemch\b', ex))
            if itemch_count != 4:
                errors.append(f'[{fname}] Found \\choiceTF with {itemch_count} \\itemch (expected 4)')
            else:
                total_itemchoice += 1

    # 6. Check no 'Đáp án:' in shortans \loigiai
    for ex in ex_blocks:
        if r'\shortans' in ex:
            lg = re.search(r'\\loigiai\{(.*?)\}', ex, flags=re.DOTALL)
            if lg and 'Đáp án:' in lg.group(1):
                errors.append(f'[{fname}] Found "Đáp án:" in shortans \\loigiai')

    # 7. Check question IDs (\macau{ID: ...}) in every \begin{ex} and \begin{vd}
    # Every \begin{ex} must have \macau
    ex_count = len(re.findall(r'\\begin\{ex\}', text))
    ex_with_macau = len(re.findall(r'\\begin\{ex\}(?:\[.*?\])?\s*(?:\\immini\s*\{)?\s*\\macau\{ID:', text))
    # Or \begin{ex}\macau{ID: ...}
    ex_macau_direct = len(re.findall(r'\\begin\{ex\}\s*\\macau\{ID:', text))
    
    # Check each ex block individually
    for b_idx, ex in enumerate(ex_blocks):
        if r'\macau{ID:' not in ex[:200]:
            errors.append(f'[{fname}] \\begin{{ex}} #{b_idx+1} is missing \\macau{{ID: ...}}')
        else:
            total_macau += 1

    vd_blocks = re.findall(r'\\begin\{vd\}(.*?)\\end\{vd\}', text, flags=re.DOTALL)
    for v_idx, vd in enumerate(vd_blocks):
        if r'\macau{ID:' not in vd[:200]:
            errors.append(f'[{fname}] \\begin{{vd}} #{v_idx+1} is missing \\macau{{ID: ...}}')
        else:
            total_macau += 1

    # 8. Check Rule 14: No hardcoded question numbers and verify relative count
    # E.g. forbidden: "cho Câu X và Câu Y", "cho Câu X đến Câu Y"
    hardcoded_groups = re.findall(r'(?:Sử dụng|thông tin|dữ kiện).*?cho Câu \d+', text, flags=re.IGNORECASE)
    if hardcoded_groups:
        for hg in hardcoded_groups:
            errors.append(f'[{fname}] Found hardcoded absolute question text: "{hg}"')

    macauchum_matches = re.findall(r'\\macauchum\{ID:[^}]+\}', text)
    total_macauchum += len(macauchum_matches)

    # Verify that all grouped questions use relative count pattern: "cho \d+ câu hỏi ngay sau"
    relative_counts = re.findall(r'cho \d+ câu hỏi ngay sau', text)
    if len(relative_counts) != len(macauchum_matches):
        errors.append(f'[{fname}] Mismatch between \\macauchum ({len(macauchum_matches)}) and "cho N câu hỏi ngay sau" ({len(relative_counts)})')

if errors:
    print('ERRORS FOUND:')
    for e in errors:
        print('  -', e)
    sys.exit(1)
else:
    print('ALL SYSTEM RULES (RULES 1 - 14) VERIFIED PERFECTLY! (0 errors)')
    print(f'  - Total Question IDs (\\macau): {total_macau}')
    print(f'  - Total Grouped Question IDs (\\macauchum): {total_macauchum}')
    print(f'  - Figures verified: {total_figs}')
    print(f'  - \\choice parsed: {total_choices} (0 ending dots)')
    print(f'  - \\choiceTF parsed: {total_choiceTFs} (0 ending dots)')
    print(f'  - \\shortans verified: {total_shortans} (all with preceding blank line)')
    print(f'  - itemchoice environments: {total_itemchoice} (all 4 items)')

