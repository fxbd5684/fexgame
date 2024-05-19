sudo apt-get install python3 python3-pip
pip3 install pyinstaller 
pyinstaller -D --icon=someotherthing/fex.ico --clean --distpath dist/linux main.py 
rm -rf build 
