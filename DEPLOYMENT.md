# 🌐 Deployment Guide - Host Your RPG Online

Host your RPG game so anyone can play it from anywhere!

---

## 🏠 Option 1: Local Network Access (Easiest)

**Perfect for:** Playing with friends/family on same WiFi

### Steps:
1. Start the server:
```bash
./start_web.sh
```

2. Look for the **Network URL** in the output:
```
Local:    http://localhost:8080
Network:  http://192.168.x.x:8080  ← Share this!
```

3. Share the Network URL with anyone on your WiFi

**Note:** They must be on the same WiFi network as you!

---

## ☁️ Option 2: PythonAnywhere (Free, Recommended)

**Perfect for:** Free hosting, easy setup, stays online 24/7

### Steps:

1. **Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)** (Free account)

2. **Upload your files:**
   - Click "Files" tab
   - Upload all `.py` files
   - Upload `templates/` and `static/` folders

3. **Open a Bash console:**
```bash
# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 rpg-env

# Install Flask
pip install Flask
```

4. **Create WSGI file:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - Click on WSGI configuration file
   - Replace contents with:

```python
import sys
path = '/home/YOUR_USERNAME/rpg-game'
if path not in sys.path:
    sys.path.append(path)

from web_game import app as application
```

5. **Configure:**
   - Set Source code: `/home/YOUR_USERNAME/rpg-game`
   - Set Working directory: same
   - Set Virtualenv: `/home/YOUR_USERNAME/.virtualenvs/rpg-env`

6. **Reload** and visit: `YOUR_USERNAME.pythonanywhere.com`

---

## 🚀 Option 3: Replit (Fastest Setup)

**Perfect for:** Quick online hosting, no setup needed

### Steps:

1. **Go to [replit.com](https://replit.com)** and sign up

2. **Create new Repl:**
   - Click "Create Repl"
   - Choose "Python"
   - Name it "RPG-Game"

3. **Upload files:**
   - Upload all your `.py` files
   - Create `templates/` folder and upload `index.html`
   - Create `static/css/` and `static/js/` folders
   - Upload `style.css` and `game.js`

4. **Create `.replit` file:**
```toml
run = "python web_game.py"
```

5. **Click "Run"** and Replit will give you a URL!

---

## 🐳 Option 4: Railway.app (Modern, Auto-deploys)

**Perfect for:** GitHub integration, professional deployment

### Steps:

1. **Push code to GitHub:**
```bash
cd "/Users/admin/RPG game"
git init
git add .
git commit -m "RPG Game"
git branch -M main
git remote add origin YOUR_GITHUB_URL
git push -u origin main
```

2. **Create `Procfile`:**
```
web: python web_game.py
```

3. **Create `railway.json`:**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python web_game.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

4. **Deploy:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-deploy!

5. **Set environment variables:**
   - Add `PORT` variable (Railway will provide this)
   - Update `web_game.py` to use `os.environ.get('PORT', 8080)`

---

## 🔧 Option 5: Render.com (Free Tier Available)

**Perfect for:** Free hosting with auto-sleep after inactivity

### Steps:

1. **Push to GitHub** (see Railway steps above)

2. **Create `render.yaml`:**
```yaml
services:
  - type: web
    name: rpg-game
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python web_game.py
```

3. **Go to [render.com](https://render.com):**
   - Sign up with GitHub
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Render will auto-deploy!

---

## 📱 Option 6: Ngrok (Temporary Public URL)

**Perfect for:** Quick testing, temporary sharing

### Steps:

1. **Download ngrok:** [ngrok.com/download](https://ngrok.com/download)

2. **Start your game locally:**
```bash
./start_web.sh
```

3. **In another terminal:**
```bash
ngrok http 8080
```

4. **Share the ngrok URL** (e.g., `https://abc123.ngrok.io`)

**Note:** Free tier URLs expire when you close ngrok!

---

## 🌍 Option 7: Glitch (Browser-Based IDE)

**Perfect for:** No installation, code in browser

### Steps:

1. **Go to [glitch.com](https://glitch.com)** and sign up

2. **Create New Project:**
   - Click "New Project" → "glitch-hello-python"

3. **Upload your files:**
   - Delete default files
   - Upload all `.py` files
   - Create folders and upload templates/static files

4. **Edit `requirements.txt`:**
```
Flask==3.0.0
```

5. **Glitch auto-starts!** Click "Show" to see your game

---

## 📝 Required File Changes for Production

### Update `web_game.py` for production:

```python
import os

if __name__ == '__main__':
    import socket
    
    # Get port from environment or use 8080
    PORT = int(os.environ.get('PORT', 8080))
    
    # Get host - use 0.0.0.0 for external access
    HOST = os.environ.get('HOST', '0.0.0.0')
    
    # Disable debug in production
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print("\n" + "="*60)
    print(" "*15 + "⚔️  REALM OF LEGENDS  ⚔️")
    print("="*60)
    print(f"\n🌐 Starting web server on port {PORT}...")
    print("="*60 + "\n")
    
    app.run(debug=DEBUG, host=HOST, port=PORT)
```

### Create `requirements.txt`:
```
Flask==3.0.0
```

### Create `.gitignore`:
```
venv/
__pycache__/
*.pyc
savegame.pkl
.DS_Store
```

---

## 🔐 Security Notes for Production

⚠️ **Important for public hosting:**

1. **Disable Debug Mode:**
```python
app.run(debug=False, host='0.0.0.0', port=PORT)
```

2. **Use Environment Variables:**
```python
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))
```

3. **Add Rate Limiting:**
```bash
pip install Flask-Limiter
```

4. **Use Production WSGI Server:**
```bash
pip install gunicorn
gunicorn web_game:app
```

---

## 💰 Cost Comparison

| Platform | Free Tier | Always On | Custom Domain |
|----------|-----------|-----------|---------------|
| **PythonAnywhere** | ✅ Yes | ✅ Yes | ❌ Paid only |
| **Replit** | ✅ Yes | ⚠️ Sleeps | ✅ Yes |
| **Railway** | ⚠️ Trial | ✅ Yes | ✅ Yes |
| **Render** | ✅ Yes | ⚠️ Sleeps | ✅ Yes |
| **Ngrok** | ✅ Yes | ❌ Temporary | ❌ No |
| **Glitch** | ✅ Yes | ⚠️ Sleeps | ✅ Yes |

---

## 🎯 Quick Recommendations

**Just want to share with friends?**
→ Use **Local Network** (Option 1)

**Want free 24/7 hosting?**
→ Use **PythonAnywhere** (Option 2)

**Need it online NOW?**
→ Use **Replit** (Option 3)

**Want professional deployment?**
→ Use **Railway** (Option 4)

**Just testing temporarily?**
→ Use **Ngrok** (Option 6)

---

## 🆘 Troubleshooting

**Problem:** Port already in use
- **Solution:** Change PORT in web_game.py

**Problem:** Can't access from other devices
- **Solution:** Check firewall settings, ensure host='0.0.0.0'

**Problem:** Game doesn't load
- **Solution:** Check browser console for errors, verify all files uploaded

**Problem:** Sessions not persisting
- **Solution:** Use persistent storage or database for production

---

## 📚 Next Steps

After deploying:
1. Test all game features
2. Share the URL with friends
3. Monitor usage and performance
4. Consider adding user accounts
5. Add persistent database storage

---

**Your game is ready to be shared with the world! ⚔️🌍**






