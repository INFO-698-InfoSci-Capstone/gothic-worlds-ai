@echo off
setlocal enabledelayedexpansion

REM === Load environment variables from .env file ===
for /f "usebackq tokens=1,* delims==" %%i in (".env") do (
    set "%%i=%%j"
)

REM === Kill processes on BACKEND_PORT ===
echo Checking for processes on port %BACKEND_PORT%...
set "pids="
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :%BACKEND_PORT%') do (
    if not "%%a"=="0" set "pids=!pids! %%a"
)
for %%a in (!pids!) do (
    echo Found process %%a on port %BACKEND_PORT%. Killing...
    taskkill /PID %%a /F >nul 2>&1
)

REM === Kill processes on FRONTEND_PORT ===
echo Checking for processes on port %FRONTEND_PORT%...
set "pids="
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :%FRONTEND_PORT%') do (
    if not "%%a"=="0" set "pids=!pids! %%a"
)
for %%a in (!pids!) do (
    echo Found process %%a on port %FRONTEND_PORT%. Killing...
    taskkill /PID %%a /F >nul 2>&1
)

REM === Delete frontend/.next unless skipped ===
if "%1"=="--skip-next" (
    echo Skipping .next deletion...
) else (
    echo Checking for .next folder to delete...
    if exist "frontend\.next" (
        rmdir /s /q "frontend\.next"
        echo .next folder deleted.
    ) else (
        echo .next folder does not exist.
    )
)

REM === Start backend ===
echo Starting Narrator AI backend...
start "Backend" cmd /c "cd backend && npx ts-node index.ts"

REM === Delay to allow backend to initialize ===
ping 127.0.0.1 -n 3 >nul

REM === Start frontend ===
echo Starting Narrator AI frontend...
start "Frontend" cmd /c "cd frontend && npm run dev"

REM === Wait for user input ===
echo ====================================
echo Narrator AI is running!
echo Backend:  %BACKEND_HOST%:%BACKEND_PORT%
echo Frontend: %FRONTEND_HOST%:%FRONTEND_PORT%
echo ====================================
echo Press any key to stop all servers...
pause >nul

REM === Kill all node processes started ===
echo Stopping all Node processes (frontend + backend)...
taskkill /IM node.exe /F >nul 2>&1 && echo Servers stopped. || echo No Node processes found.

endlocal