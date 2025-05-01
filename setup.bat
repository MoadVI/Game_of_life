@echo off

pip install pygame
pip install pyinstaller
pyinstaller --onefile game_of_life.py
cd dist
game_of_life.exe
