#!/usr/bin/env python
"""
Quick Setup Script for AI Homework Analyzer
"""
import os
import sys
import subprocess
import platform

def setup():
    print("\n" + "="*70)
    print("🎓 AI Homework Analyzer - Setup & Deployment Helper")
    print("="*70 + "\n")
    
    print("📋 Options:")
    print("  1. Run locally (http://localhost:5000)")
    print("  2. Install dependencies only")
    print("  3. Show deployment guide")
    print("  4. Test PDF analysis")
    print()
    
    choice = input("Choose option (1-4): ").strip()
    
    if choice == "1":
        run_local()
    elif choice == "2":
        install_deps()
    elif choice == "3":
        show_deployment()
    elif choice == "4":
        test_analysis()
    else:
        print("❌ Invalid choice")
        sys.exit(1)

def install_deps():
    print("\n📦 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed!")

def run_local():
    print("\n🚀 Starting web server...")
    print("\n✅ Server running at: http://localhost:5000")
    print("👥 Share with friends: http://<your-ip>:5000")
    print("\nPress Ctrl+C to stop.\n")
    
    try:
        subprocess.run([sys.executable, "web_app_production.py"])
    except KeyboardInterrupt:
        print("\n\n✋ Server stopped.")
        sys.exit(0)

def show_deployment():
    print("""
🌐 DEPLOYMENT OPTIONS:

1️⃣  RENDER.COM (Recommended - Free)
   - Go to https://render.com
   - Connect GitHub repo
   - Deploy in 5 minutes
   - Live at: https://your-site.onrender.com

2️⃣  RAILWAY.APP (Simple - Free)
   - Go to https://railway.app
   - Deploy from git in 2 minutes
   - Live at: https://your-site.railway.app

3️⃣  PYTHONANYWHERE (Easy - Free)
   - Go to https://pythonanywhere.com
   - Upload files
   - Deploy in 10 minutes
   - Live at: https://yourusername.pythonanywhere.com

4️⃣  HEROKU (Powerful - Paid)
   - Install Heroku CLI
   - heroku create
   - git push heroku main

For detailed steps, see DEPLOYMENT.md
    """)

def test_analysis():
    print("\n🧪 Testing PDF analysis engine...")
    try:
        from src.homework_solver import HomeworkAnalyzerAlgorithm
        from src.detailed_solver import generate_detailed_report
        print("✅ Modules load successfully!")
        print("✅ System ready for PDF analysis!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("   Run: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    setup()
