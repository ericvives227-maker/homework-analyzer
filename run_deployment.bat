@echo off
cls
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║     AI HOMEWORK ANALYZER - AUTOMATED DEPLOYMENT               ║
echo ║              Follow the prompts below                          ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed!
    echo.
    echo Please install Git first:
    echo 1. Go to https://git-scm.com/download/win
    echo 2. Download and run the installer
    echo 3. Click Next through setup
    echo 4. Come back and run this script again
    echo.
    pause
    exit /b 1
)

echo ✅ Git is installed!
echo.

REM Get user info
set /p email="Enter your email: "
set /p username="Enter your GitHub username: "
set /p repo="Enter repository name (default: homework-analyzer): "

if "%repo%"=="" set repo=homework-analyzer

echo.
echo ═══════════════════════════════════════════════════════════════
echo STEP 1: Initializing Git Repository...
echo ═══════════════════════════════════════════════════════════════
echo.

git init
git config --global user.email "%email%"
git config --global user.name "%username%"

echo ✅ Git initialized

echo.
echo ═══════════════════════════════════════════════════════════════
echo STEP 2: Adding Files...
echo ═══════════════════════════════════════════════════════════════
echo.

git add .

echo ✅ Files staged

echo.
echo ═══════════════════════════════════════════════════════════════
echo STEP 3: Committing...
echo ═══════════════════════════════════════════════════════════════
echo.

git commit -m "Initial commit - AI Homework Analyzer with step-by-step solutions"

echo ✅ Files committed

echo.
echo ═══════════════════════════════════════════════════════════════
echo IMPORTANT: Complete These Steps in Browser Manually
echo ═══════════════════════════════════════════════════════════════
echo.
echo 1. Go to https://github.com/new
echo 2. Create repository named: %repo%
echo 3. GitHub will show you commands like:
echo    git remote add origin https://github.com/%username%/%repo%.git
echo    git branch -M main
echo    git push -u origin main
echo 4. Copy those commands and paste them in PowerShell
echo.
echo THEN:
echo 5. Go to https://railway.app
echo 6. Create account/login
echo 7. Click "Start New Project" -> "Deploy from GitHub"
echo 8. Select %username%/%repo% -> Deploy Now
echo.
echo ═══════════════════════════════════════════════════════════════
echo.
echo ✅ Local Git setup complete!
echo.
echo Next steps:
echo 1. Open https://github.com/new in your browser
echo 2. Create repository: %repo%
echo 3. Copy the git remote/push commands from GitHub
echo 4. Paste in PowerShell
echo 5. Your site will be live in 2-5 minutes!
echo.
pause
