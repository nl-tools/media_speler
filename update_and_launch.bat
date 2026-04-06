@echo off
cd /d "%~dp0"

tools\git\cmd\git.exe pull origin main
tools\python\python.exe generate_list.py

start "" index.html