@echo off
pip install pyinstaller
pyinstaller -D --icon=someotherthing/fex.ico --clean --distpath dist\windows main.py 
rmdir /s /q build
del main.spec