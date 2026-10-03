@echo off
setlocal
cd /d "%~dp0"

echo Magnet temperature regression
echo.
echo Database.db is missing. This batch does not run a model and does not start Streamlit.
echo It opens the write-up only.
echo.
echo README:
echo   %~dp0README.md
echo.
echo The page loads only if Launch-Portfolio.bat at the repo root is already running.
echo http://127.0.0.1:43123/projects/pmsm-temperature-regression
echo.
start "" "http://127.0.0.1:43123/projects/pmsm-temperature-regression"
pause
