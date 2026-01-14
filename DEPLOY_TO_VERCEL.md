# 🚀 Deploy to Vercel - Step by Step

Deploy your RPG to Vercel in 5 minutes!

---

## 📋 Prerequisites

1. Create a free account at [vercel.com](https://vercel.com)
2. Install Vercel CLI (optional but recommended)

---

## 🌐 Method 1: Deploy via Web (Easiest)

### Step 1: Push to GitHub

```bash
cd "/Users/admin/RPG game"

# Initialize git (if not already done)
git init

# Create .gitignore if needed
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

# Add all files
git add .
git commit -m "RPG Game - Ready for Vercel deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/rpg-game.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"Add New"** → **"Project"**
3. Click **"Import"** next to your GitHub repository
4. Configure:
   - **Framework Preset:** Other
   - **Build Command:** Leave empty
   - **Output Directory:** Leave empty
   - **Install Command:** `pip install -r requirements.txt`

5. Click **"Deploy"**
6. Wait 2-3 minutes for deployment
7. Get your URL: `your-project.vercel.app`

✅ **Done! Your game is now live on Vercel!**

---

## 💻 Method 2: Deploy via CLI (Advanced)

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Login

```bash
vercel login
```

### Step 3: Deploy

```bash
cd "/Users/admin/RPG game"
vercel
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? (Choose your account)
- Link to existing project? **N**
- Project name? **rpg-game**
- In which directory? **./
- Want to override settings? **N**

### Step 4: Deploy to Production

```bash
vercel --prod
```

✅ **Done! You'll get a URL like:** `rpg-game.vercel.app`

---

## ⚙️ Configuration Details

Your project includes these Vercel config files:

**vercel.json:**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "web_game.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "web_game.py"
    }
  ]
}
```

This tells Vercel:
- Use Python runtime
- Route all requests to web_game.py
- Serve static files from /static

---

## 🔧 Environment Variables (Optional)

If you want to configure settings:

1. Go to your project on Vercel
2. Click **Settings** → **Environment Variables**
3. Add:
   - `DEBUG` = `false` (for production)
   - `SECRET_KEY` = (generate a random string)

---

## 🌍 Custom Domain (Optional)

1. Go to your project on Vercel
2. Click **Settings** → **Domains**
3. Add your custom domain
4. Follow DNS configuration steps

---

## 📊 Vercel Features

✅ **Automatic HTTPS**
✅ **Global CDN**
✅ **Auto-deployments** (push to GitHub = auto-deploy)
✅ **Free tier** (generous limits)
✅ **Fast deployment** (2-3 minutes)

---

## 🔄 Update Your Game

To update the game after making changes:

**Via GitHub:**
```bash
git add .
git commit -m "Updated game"
git push
```
→ Vercel auto-deploys!

**Via CLI:**
```bash
vercel --prod
```

---

## 🆘 Troubleshooting

**Issue:** Build fails
- **Fix:** Make sure `requirements.txt` exists with Flask listed

**Issue:** 404 errors
- **Fix:** Check `vercel.json` routes configuration

**Issue:** Static files not loading
- **Fix:** Verify paths in HTML use `/static/...`

**Issue:** App doesn't start
- **Fix:** Check build logs in Vercel dashboard

---

## 📱 Share Your Game

Once deployed, share your Vercel URL:
```
https://your-project.vercel.app
```

Anyone can access it from anywhere!

---

## 💡 Pro Tips

1. **Free Tier Limits:**
   - 100GB bandwidth/month
   - 100 hours serverless function time
   - Perfect for RPG game!

2. **Performance:**
   - Vercel uses serverless functions
   - First request may be slow (cold start)
   - Subsequent requests are fast

3. **Monitoring:**
   - View analytics in Vercel dashboard
   - See deployment history
   - Check function logs

---

## 🎮 Your Vercel Deployment Checklist

- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Vercel account created
- [ ] Project imported to Vercel
- [ ] Deployment successful
- [ ] Game tested and working
- [ ] URL shared with players

---

**Your RPG is now live on Vercel! ⚔️**

Next: Deploy to a second platform (see DEPLOY_TO_RENDER.md)





