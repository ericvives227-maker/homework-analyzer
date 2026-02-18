# Railway.app Deployment Guide

## 🚀 Deploy in 5 Minutes

### Step 1: Prepare GitHub

1. **Initialize Git Repository** (if not already done):
```bash
cd homework.ai.py
git init
git add .
git commit -m "Initial commit - AI Homework Analyzer"
```

2. **Create GitHub Repository**:
   - Go to https://github.com/new
   - Create repository: `homework-analyzer`
   - Copy the commands shown and run:
```bash
git remote add origin https://github.com/YOUR_USERNAME/homework-analyzer.git
git branch -M main
git push -u origin main
```

---

### Step 2: Deploy on Railway.app

1. **Go to https://railway.app**

2. **Click "Start New Project"**

3. **Select "Deploy from GitHub"**
   - Authenticate with GitHub
   - Select: `homework-analyzer` repository
   - Click "Deploy"

4. **Railway automatically:**
   - ✅ Detects Python
   - ✅ Reads requirements.txt
   - ✅ Installs dependencies
   - ✅ Reads Procfile
   - ✅ Starts web server
   - ✅ Assigns public URL

---

### Step 3: Get Your Live URL

1. **On Railway Dashboard:**
   - Go to "Deployments"
   - Wait for deployment to complete (2-5 minutes)
   - Click on the deployment
   - Find "Domains" section
   - Your URL: `https://your-app-name.up.railway.app`

2. **Your site is LIVE!** 🎉

---

## 📱 Using Your Website

### Share with Others:
- Send them: `https://your-app-name.up.railway.app`
- They can upload PDFs and get solutions
- No installation needed!

### Features Available:
- 📚 Step-by-step solutions
- 📊 Cliff notes summary
- 🖨️ Print-friendly format
- 📤 Upload unlimited PDFs
- 👥 Share with friends

---

## 🔧 Auto-Deploy Updates

**Every time you push to GitHub, Railway automatically redeploys!**

```bash
# Make changes locally
git add .
git commit -m "Your changes"
git push origin main

# Railway detects and deploys automatically ✅
```

---

## 📊 Monitor Your App

**On Railway Dashboard:**
- ✅ View logs in real-time
- ✅ Check CPU/Memory usage
- ✅ See deployment status
- ✅ Restart services if needed

---

## 💰 Pricing

### Free Tier Includes:
- **$5/month credit**
- Enough for 1-2 apps
- Automatic reload if usage exceeds credit
- No credit card required to start

### If You Need More:
- Upgrade to paid plan
- Remove old unused apps
- Share resources between apps

---

## 🐛 Troubleshooting

### App won't deploy?
```bash
# Check if files are committed
git status

# If files show as "Changes not staged", commit them:
git add .
git commit -m "Fix"
git push origin main
```

### Build fails?
- Check Railway logs for errors
- Ensure requirements.txt has all dependencies
- Verify Procfile is correct

### Site is slow?
- Free tier has limited resources
- Upgrade plan if needed
- Close unused apps

---

## 🎯 What's Deployed

✅ Your homework analyzer  
✅ All solution generators  
✅ PDF upload & analysis  
✅ Step-by-step solutions  
✅ Cliff notes summary  
✅ Beautiful web interface  

---

## 📞 Next Steps

1. **Create GitHub account** (if you don't have one)
2. **Push your code to GitHub** (follow Step 1 above)
3. **Deploy on Railway.app** (follow Step 2 above)
4. **Share your URL with friends!** 🚀

---

## 🎓 Setup Checklist

- [ ] GitHub account created
- [ ] Repository created
- [ ] Code pushed to GitHub
- [ ] Railway.app account created
- [ ] GitHub connected to Railway
- [ ] Deploy started
- [ ] Waiting for deployment... (2-5 min)
- [ ] Got public URL
- [ ] Testing app works
- [ ] Sharing with friends! ✅

---

**Your professional homework analyzer is going live!** 🚀
