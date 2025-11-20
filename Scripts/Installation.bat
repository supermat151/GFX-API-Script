rem @echo off
set http_proxy=http://proxy-chain.intel.com:912
set https_proxy=http://proxy-chain.intel.com:912
C:\python38\python.exe -m pip install --upgrade pip 
pip install pyautogui 
pip install psutil 
start cmd /k python "C:\Users\gta\Desktop\GFX API Script\Scripts\GFX_Long_Duration_Testing.py"

