@echo off
cd /d "%~dp0"

git pull origin main
python generate_list.py
start "" index.html