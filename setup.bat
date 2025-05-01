@echo off

pip install pygame
pip install pyinstaller
pyinstaller --onefile game_of_life.py

move dist\game_of_life.exe
rmdir /s /q build
rmdir /s /q dist
del game_of_life.spec
del README.md
del game_of_life.py
del setup.bat
