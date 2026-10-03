@echo off
setlocal
cd /d "%~dp0"

echo Magnet temperature regression
echo.
echo Pipeline page. There is no model and no Database.db, so this does not predict a temperature.
echo.
echo http://127.0.0.1:8509
echo.

python -c "import streamlit" 1>nul 2>nul
if errorlevel 1 (
  echo Installing the pinned Streamlit from requirements.txt
  python -m pip install -r requirements.txt
  if errorlevel 1 (
    echo pip install failed. Python 3 must be on PATH as python.
    pause
    exit /b 1
  )
)

python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8509 --browser.serverAddress 127.0.0.1 --browser.gatherUsageStats false
pause
