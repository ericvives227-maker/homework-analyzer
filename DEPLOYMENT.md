# AI Homework Analyzer - Website Deployment Guide

## Quick Start (Local)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python web_professional.py
```

Then visit: **http://localhost:5000**

---

## Deploy to Production (Cloud)

### Option 1: **Render.com** (Recommended - Free)

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/homework-analyzer.git
   git push -u origin main
   ```

3. **Deploy on Render**
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub repo
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `gunicorn web_professional:app`
   - Environment variable: `PYTHON_VERSION=3.11`
   - Click "Create Web Service"

4. **Your site will be live at:** `https://your-app-name.onrender.com`

---

### Option 2: **Heroku** (Free tier ended, but setup below)

```bash
# Install Heroku CLI
# Then:
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

---

### Option 3: **Railway.app** (Easy - Free tier)

1. Go to https://railway.app
2. Click "Start a New Project"
3. Select "Deploy from GitHub"
4. Connect your repo
5. Auto-detects Python and deploys

---

### Option 4: **PythonAnywhere** (Simple)

1. Go to https://www.pythonanywhere.com
2. Create account (free tier available)
3. Upload files via web interface
4. Configure web app with Flask
5. Reload and access your site

---

## Features

✅ **Step-by-Step Solutions** - Complete detailed explanations  
✅ **Multiple Problem Types** - Calculus, Algebra, Physics, Chemistry, Geometry  
✅ **Cliff Notes Summary** - Compiled theories and formulas  
✅ **Professional Design** - Beautiful, responsive UI  
✅ **PDF Upload** - Drag & drop or click to select  
✅ **Print-Friendly** - Generate reports  
✅ **Network Sharing** - Share with friends  

---

## File Structure

```
homework.ai.py/
├── web_professional.py       # Main web app
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment configuration
├── src/
│   ├── homework_solver.py   # Core solver engine
│   ├── detailed_solver.py   # Detailed solutions
│   └── visualizer.py        # Graph generation
├── templates/
│   └── detailed_solution.html # Web interface
├── reports/
│   └── uploads/             # PDF storage
└── static/                  # CSS, JS, images (if needed)
```

---

## Environment Variables (Production)

If deploying, set these:
- `FLASK_ENV=production`
- `DEBUG=false`
- `MAX_CONTENT_LENGTH=104857600` (100MB for PDFs)

---

## Troubleshooting

**"Module not found" error?**
```bash
pip install -r requirements.txt
```

**PDF upload fails?**
- Check file size (max 100MB)
- Ensure it's a valid PDF

**Slow performance?**
- Render free tier has limited resources
- Consider upgrading or using Railway.app

---

## Support

For issues:
1. Check terminal/logs in deployment platform
2. Ensure all dependencies installed
3. Verify Flask version compatibility

**Your homework solver is now ready to share with the world!** 🚀
