@echo off
pyinstaller --onefile --icon=fex.ico --clean --distpath dist\ main.py 
rmdir /s /q build