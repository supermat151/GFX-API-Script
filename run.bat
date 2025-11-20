@echo off
setlocal

REM Change to the Scripts directory
cd Scripts

REM Run the Python script and capture the output
powershell -Command "python GFX_Long_Duration_Testing.py | Tee-Object -FilePath ..\output.txt"

REM Read the expected folder name from the file
set /p expected_folder_name=<..\folder_name.txt

REM Define the expected folder path
set "expected_folder_path=C:\Users\gta\Desktop\GFX API Script\%expected_folder_name%"

REM Check if the folder exists, if not create it
if not exist "%expected_folder_path%" (
    mkdir "%expected_folder_path%"
)

REM Move the output.txt file to the expected folder
move "..\output.txt" "%expected_folder_path%\output.txt"

REM Clean up the temporary file
del "..\folder_name.txt"

:end
endlocal