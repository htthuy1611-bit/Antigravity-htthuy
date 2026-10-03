import zipfile
import re
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with zipfile.ZipFile(r'C:\Users\user\AppData\Roaming\Microsoft\Word\STARTUP\BTPRO2020.dotm') as z:
    xml = z.read('customUI/customUI14.xml').decode('utf-8', errors='ignore')
    m = re.search(r'label="[^"]*Chu&#7849;n h&#243;a[^"]*"', xml)
    if m:
        pos = m.start()
        print(xml[pos-50:pos+2500])
