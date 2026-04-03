@echo off
echo Starting Vanguard-EMS Setup...
cd /d "%~dp0"

echo Installing dependencies...
pip install -r requirements.txt

echo Starting Backend Engine...
start cmd /k "python -m backend.main"

echo Waiting for backend to spin up...
timeout /t 3 /nobreak > nul

echo Starting Ambulance Simulator...
start cmd /k "python simulator\ambulance_driver.py"

echo Opening Dashboard...
start frontend\index.html

echo System is running!
