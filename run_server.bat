@echo off
REM Sanal ortamı aktif et
call .venv\Scripts\activate

REM FastAPI uygulamasını başlat
uvicorn main:app --reload

pause
