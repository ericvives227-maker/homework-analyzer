@echo off
REM Deployment Helper for Railway.app
REM This script automates git initialization and commits

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║     RAILWAY.APP DEPLOYMENT - STEP 1 (Prepare Code)           ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Initialize git if not already done
if not exist .git (
    echo 📦 Initializing Git repository...
    git init
    echo ✅ Git initialized
) else (
    echo ✅ Git already initialized
)

echo.
echo 📝 Adding all files...
git add .

echo.
echo 💾 Creating initial commit...
git commit -m "Initial commit - AI Homework Analyzer with step-by-step solutions and cliff notes"

echo.
echo ✅ STEP 1 COMPLETE!
echo.
echo NEXT STEPS:
echo.
echo 1. Go to: https://github.com/new
echo 2. Create repository: "homework-analyzer"
echo 3. Copy the commands shown and paste them here (or run deploy_to_github.bat)
echo.
echo The commands will look like:
echo   git remote add origin https://github.com/YOUR_USERNAME/homework-analyzer.git
echo   git branch -M main
echo   git push -u origin main
echo.
echo After pushing to GitHub:
echo   Go to https://railway.app
echo   Click "Start New Project"
echo   Select "Deploy from GitHub"
echo   Choose your repository
echo   Click "Deploy"
echo.
pause
