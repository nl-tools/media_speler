@echo off
cd /d "%~dp0"

echo Installing/updating Python dependencies...
python -m pip install --upgrade pip
python -m pip install RangeHTTPServer

echo Updating video list...
python generate_list.py

echo Starting browser...
start "" http://localhost:8000

echo Starting video server...
python -m RangeHTTPServer 8000

