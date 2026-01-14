# 🎨 Deploy to Render - Step by Step

Deploy your RPG to Render for a second hosting instance!

---

## 📋 Prerequisites

1. Create a free account at [render.com](https://render.com)
2. Code in GitHub repository (see DEPLOY_TO_VERCEL.md for GitHub setup)

---

## 🚀 Deployment Steps

### Step 1: Sign Up on Render

1. Go to [render.com](https://render.com)
2. Click **"Get Started"**
3. Sign up with GitHub (easiest option)
4. Authorize Render to access your repositories

### Step 2: Create New Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository:
   - If not connected, click "Configure account" 
   - Grant access to your rpg-game repository
3. Select **rpg-game** repository

### Step 3: Configure Service

Fill in the settings:

**Basic Settings:**
- **Name:** `rpg-game` (or any name you want)
- **Region:** Choose closest to you (e.g., Oregon)
- **Branch:** `main`
- **Root Directory:** Leave blank
- **Runtime:** `Python 3`

**Build Settings:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python web_game.py`

**Instance Type:**
- Select **"Free"** (perfect for your RPG!)

### Step 4: Environment Variables (Optional)

Click **"Advanced"** and add:
- `PYTHON_VERSION` = `3.11.0`
- `DEBUG` = `false`

### Step 5: Deploy!

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for initial deployment
3. Watch the build logs (you'll see Flask installing, etc.)
4. When done, you'll see: **"Your service is live at..."**

✅ **Done! Your game is now live on Render!**

Your URL: `https://rpg-game-xxxx.onrender.com`

---

## 📝 Configuration File

Your project includes `render.yaml` for easy deployment:

```yaml
services:
  - type: web
    name: rpg-game
    env: python
    region: oregon
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: python web_game.py
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: DEBUG
        value: false
```

This automatically configures everything!

---

## 🔄 Automatic Deployments

Render automatically deploys when you push to GitHub:

```bash
# Make changes to your game
git add .
git commit -m "Updated game mechanics"
git push
```

→ Render detects the push and redeploys automatically! 🎉

---

## 📊 Render Features

✅ **Free Tier Available**
- 750 hours/month free
- Spins down after 15 min of inactivity
- Spins up automatically when accessed

✅ **Automatic HTTPS**
✅ **Auto-deploy from GitHub**
✅ **Environment variables**
✅ **Easy scaling**

---

## ⚡ Important: Free Tier Behavior

**Spin Down After Inactivity:**
- Free services sleep after 15 minutes of no requests
- First request after sleep takes ~30 seconds to wake up
- Subsequent requests are instant

**To Keep It Always Awake (Optional):**
- Upgrade to paid tier ($7/month)
- Or use a service like UptimeRobot to ping your URL every 5 minutes

---

## 🌍 Custom Domain (Optional)

1. Go to your service in Render
2. Click **"Settings"** → **"Custom Domains"**
3. Click **"Add Custom Domain"**
4. Enter your domain
5. Update your DNS records as instructed

---

## 📈 Monitor Your Service

**View Logs:**
1. Go to your service dashboard
2. Click **"Logs"** tab
3. See real-time application logs

**View Metrics:**
1. Click **"Metrics"** tab
2. See CPU, memory usage
3. View request rates

**View Events:**
1. Click **"Events"** tab
2. See deployment history
3. Track all service updates

---

## 🔄 Update Your Game

**Method 1: Push to GitHub (Recommended)**
```bash
git add .
git commit -m "Game update"
git push
```
→ Auto-deploys in 2-3 minutes

**Method 2: Manual Deploy**
1. Go to service dashboard
2. Click **"Manual Deploy"** → **"Deploy latest commit"**

---

## 🆘 Troubleshooting

**Issue:** Service fails to start
- **Fix:** Check logs in Render dashboard
- Verify `requirements.txt` has Flask

**Issue:** "Application failed to respond"
- **Fix:** Check start command is `python web_game.py`
- Verify PORT environment variable is used

**Issue:** Service is slow to respond
- **Fix:** This is normal for free tier (spin-up time)
- First request after sleep takes ~30 seconds

**Issue:** Build fails
- **Fix:** Check build logs
- Ensure all dependencies in requirements.txt

---

## 🎮 Share Your Game

Once deployed, share your Render URL:
```
https://your-game.onrender.com
```

Anyone can play from anywhere!

---

## 💡 Pro Tips

1. **Keep Service Awake:**
   - Use UptimeRobot (free) to ping your URL every 5 minutes
   - Prevents spin-down for better player experience

2. **Monitor Health:**
   - Set up health check endpoint
   - Render auto-restarts if health check fails

3. **View Analytics:**
   - Check "Metrics" for usage stats
   - Monitor memory and CPU usage

4. **Upgrade Later:**
   - Start with free tier
   - Upgrade to paid ($7/mo) if you get lots of players
   - Paid tier = no spin-down, more resources

---

## 🎯 Your Render Deployment Checklist

- [ ] Render account created
- [ ] GitHub repository connected
- [ ] Web service created
- [ ] Configuration completed
- [ ] Deployment successful
- [ ] Game tested and working
- [ ] URL shared with players
- [ ] (Optional) UptimeRobot set up

---

## 🌟 Why Two Deployments?

Having your game on both **Vercel** and **Render** means:

✅ **Redundancy** - If one is down, players can use the other
✅ **Load Distribution** - Split players between two servers
✅ **Testing** - Test updates on one before pushing to both
✅ **Comparison** - See which platform works better for you

---

**Your RPG is now live on Render! ⚔️**

You now have TWO live URLs:
1. Vercel: `https://your-project.vercel.app`
2. Render: `https://rpg-game-xxxx.onrender.com`

Share both URLs and let two people play simultaneously!





