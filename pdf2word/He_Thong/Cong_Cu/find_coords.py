import fitz
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

doc = fitz.open(r'c:\AnTiGraViTy-htthuy\pdf2word\De_Thi_Goc_2009.pdf')

def search_text(page, q):
    res = page.search_for(q)
    print(f'Search "{q}":', res)

print('--- Page 1 ---')
p1 = doc[0]
search_text(p1, 'Câu 4')
search_text(p1, 'Câu 5')
search_text(p1, 'Câu 8')
search_text(p1, 'Trang 1/4')

print('--- Page 2 ---')
p2 = doc[1]
search_text(p2, 'PHẦN II')
search_text(p2, 'Câu 1')
search_text(p2, 'a) Đồ thị')
search_text(p2, 'Câu 2')
search_text(p2, 'Câu 3')

print('--- Page 3 ---')
p3 = doc[2]
search_text(p3, 'a) Máy bay')
search_text(p3, 'PHẦN III')
search_text(p3, 'Câu 2')
search_text(p3, 'Câu 3')
