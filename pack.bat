@echo off
pyinstaller -D --icon=fex.ico --clean --distpath dist\ main.py 
rmdir /s /q build
del main.spec