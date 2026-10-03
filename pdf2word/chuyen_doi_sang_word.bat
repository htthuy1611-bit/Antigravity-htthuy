@echo off
chcp 65001 > nul
echo ============================================================
echo       CONG CU CHUYEN DOI PDF SANG WORD (DOCX)
echo ============================================================
echo.

cd /d "%~dp0"

if "%~1"=="" (
    echo Dang quet va chuyen doi tat ca file PDF trong thu muc...
    python pdf_to_word.py
) else (
    echo Dang chuyen doi file duoc keo tha vao...
    python pdf_to_word.py "%~1"
)

echo.
echo ============================================================
echo Hoan tat! Nhan phim bat ky de thoat...
pause > nul
