@echo off
cd /d "%~dp0"

echo Updating video list...
python generate_list.py

netstat -ano | findstr :8000 >nul
if %errorlevel%==0 (
    echo Server already running
) else (
    python -m RangeHTTPServer 8000
)

echo Starting browser...
start chrome http://localhost:8000