# -*- coding: utf-8 -*-
import os, sys, re

base_dir = os.path.dirname(os.path.abspath(__file__))
tex_path = os.path.join(base_dir, 'chapters', 'bai_01_he_quy_chieu_trang_31_53.tex')
fig_dir = os.path.join(base_dir, 'figures')

with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.splitlines()

errors = []

# 1. Check all graphic files exist
figs = re.findall(r'\\includegraphics(?:\[.*?\])?\{(.*?)\}', text)
for fig in set(figs):
    fig_file = os.path.join(fig_dir, fig)
    if not os.path.exists(fig_file):
        errors.append(f'Missing figure: {fig}')

# 2. Check blank line before \shortans
for idx, line in enumerate(lines):
    if r'\shortans' in line:
        if idx == 0 or lines[idx-1].strip() != '':
            errors.append(f'Line {idx+1}: \\shortans does not have a blank line before it! Previous line: {lines[idx-1]}')

# 3. Check no period before closing brace in \choice and \choiceTF
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
        if len(args) == 4:
            results.append(args)
            pos = cur
        else:
            pos = m.end()
    return results

choices = parse_cmd_args('choice', text)
for idx, c in enumerate(choices):
    for o_idx, opt in enumerate(c):
        if opt.strip().endswith('.'):
            errors.append(f'\\choice #{idx+1} option #{o_idx+1} ends with a dot: "{opt.strip()}"')

choiceTFs = parse_cmd_args('choiceTF', text)
for idx, c in enumerate(choiceTFs):
    for o_idx, opt in enumerate(c):
        if opt.strip().endswith('.'):
            errors.append(f'\\choiceTF #{idx+1} option #{o_idx+1} ends with a dot: "{opt.strip()}"')

# 4. Check no hardcoded 'Chọn đáp án' in \loigiai
loigiai_blocks = re.findall(r'\\loigiai\{(.*?)\}\s*(?=\\end\{ex\}|\\end\{vd\}|\Z)', text, flags=re.DOTALL)
for lg in loigiai_blocks:
    if 'Chọn đáp án' in lg:
        errors.append('Found hardcoded "Chọn đáp án" in \\loigiai')

# 5. Check itemchoice in all choiceTF \loigiai
ex_blocks = re.findall(r'\\begin\{ex\}(.*?)\\end\{ex\}', text, flags=re.DOTALL)
for ex in ex_blocks:
    if r'\choiceTF' in ex:
        if r'\begin{itemchoice}' not in ex or r'\end{itemchoice}' not in ex:
            errors.append('Found \\choiceTF without \\begin{itemchoice} in \\loigiai')
        itemch_count = len(re.findall(r'\\itemch\b', ex))
        if itemch_count != 4:
            errors.append(f'Found \\choiceTF with {itemch_count} \\itemch (expected 4)')

# 6. Check no 'Đáp án:' in shortans \loigiai
for ex in ex_blocks:
    if r'\shortans' in ex:
        lg = re.search(r'\\loigiai\{(.*?)\}', ex, flags=re.DOTALL)
        if lg and 'Đáp án:' in lg.group(1):
            errors.append('Found "Đáp án:" in shortans \\loigiai')

if errors:
    print('ERRORS FOUND:')
    for e in errors:
        print('  -', e)
    sys.exit(1)
else:
    print(f'ALL SYSTEM RULES VERIFIED PERFECTLY! (0 errors)')
    print(f'  - Figures checked: {len(set(figs))} OK')
    print(f'  - \\choice parsed: {len(choices)} (0 ending dots)')
    print(f'  - \\choiceTF parsed: {len(choiceTFs)} (0 ending dots)')
    print(f'  - \\shortans checked: {len(re.findall(r"\\shortans", text))} (all have blank line before)')
    print(f'  - itemchoice environments: {len(re.findall(r"\\begin\{itemchoice\}", text))} (all 4 items)')
