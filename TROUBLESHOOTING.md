# 🔧 Troubleshooting Guide

## ❌ "Error performing action" in Browser

### Quick Fixes:

1. **Refresh the browser page**
   - Press `F5` or `Ctrl+R` (Windows/Linux)
   - Press `Cmd+R` (Mac)
   - This clears any stuck game state

2. **Clear browser cache**
   - Press `Ctrl+Shift+Delete` (Windows/Linux)
   - Press `Cmd+Shift+Delete` (Mac)
   - Or try incognito/private mode

3. **Check browser console**
   - Press `F12` to open Developer Tools
   - Click "Console" tab
   - Look for red error messages
   - Screenshot and report any errors you see

4. **Restart the server**
   ```bash
   # Stop the server
   pkill -f "python web_game.py"
   
   # Start it again
   python web_game.py 8000
   ```

5. **Use a different browser**
   - Try Chrome, Firefox, or Safari
   - Some browsers have better compatibility

---

## Common Issues & Solutions:

### Issue: "Error performing action" when exploring

**Cause:** Session state might be corrupted

**Solution:**
1. Open browser console (F12)
2. Type: `sessionStorage.clear()`
3. Press Enter
4. Refresh the page
5. Start a new game

---

### Issue: Buttons not responding

**Cause:** JavaScript not loaded properly

**Solution:**
1. Check that these files exist:
   - `static/js/game.js`
   - `static/css/style.css`
   - `templates/index.html`

2. Restart server:
   ```bash
   pkill -f "python web_game.py"
   python web_game.py 8000
   ```

3. Clear browser cache and refresh

---

### Issue: Game state not saving

**Cause:** Flask sessions issue

**Solution:**
- The web version uses session-based saves
- Don't clear cookies while playing
- Each browser tab has its own game
- Use "Save Game" in terminal version for persistent saves

---

### Issue: Can't start new game

**Solution:**
1. Check server is running:
   ```bash
   curl http://localhost:8000/
   ```

2. Test the API:
   ```bash
   curl -X POST http://localhost:8000/api/start_game \
     -H "Content-Type: application/json" \
     -d '{"name":"Test","class":"Warrior"}'
   ```

3. If both work, the issue is in the browser - clear cache

---

### Issue: Secret world not appearing

**Cause:** It's intentionally rare!

**Solution:**
- 5% chance = 1 in 20 tries on average
- Keep exploring in:
  - Dark Forest
  - Mountain Peak  
  - Ancient Ruins
- Be patient - it's meant to be special!
- Could take 30-50 exploration attempts

---

### Issue: Port 8000 already in use

**Solution:**
```bash
# Check what's using port 8000
lsof -ti:8000

# Kill the process
kill $(lsof -ti:8000)

# Or use a different port
python web_game.py 8001
```

---

### Issue: Flask not found

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate

# Install Flask
pip install Flask

# Run game
python web_game.py 8000
```

---

## Still Having Issues?

### Get detailed error information:

1. **Check server logs:**
   - Look at the terminal where you ran `python web_game.py`
   - Any Python errors will show there

2. **Check browser console:**
   - Press F12
   - Look in Console tab
   - Look in Network tab (for failed requests)

3. **Test API endpoints:**
   ```bash
   # Test server is running
   curl http://localhost:8000/
   
   # Test game state
   curl http://localhost:8000/api/game_state
   
   # Test start game
   curl -X POST http://localhost:8000/api/start_game \
     -H "Content-Type: application/json" \
     -d '{"name":"Hero","class":"Warrior"}'
   ```

4. **Verify files:**
   ```bash
   # Check all required files exist
   ls -la static/js/game.js
   ls -la static/css/style.css
   ls -la templates/index.html
   ls -la web_game.py
   ls -la character.py
   ls -la game.py
   ```

---

## Emergency Reset:

If everything is broken:

```bash
# Stop all servers
pkill -f "python web_game.py"

# Delete any corrupted save files
rm -f savegame.pkl

# Restart fresh
python web_game.py 8000
```

Then open: http://localhost:8000

---

## Quick Diagnostic:

Run this to check everything:

```bash
cd "/Users/admin/RPG game"

# Test Python imports
python -c "from web_game import app; print('✅ Imports work')"

# Test server
curl -s http://localhost:8000/ > /dev/null && echo "✅ Server running" || echo "❌ Server not running"

# Test files exist
test -f static/js/game.js && echo "✅ JS file exists" || echo "❌ JS missing"
test -f static/css/style.css && echo "✅ CSS file exists" || echo "❌ CSS missing"
test -f templates/index.html && echo "✅ HTML file exists" || echo "❌ HTML missing"
```

---

## Alternative: Use Terminal Version

If web version continues to have issues, the terminal version is more stable:

```bash
python main.py
```

All the same features work, just without the fancy graphics!

---

## Report a Bug:

If you found a real bug, please note:
1. What action you were trying to perform
2. What error message you saw
3. Browser console errors (F12 → Console)
4. Server terminal output
5. Steps to reproduce

---

**Most errors are fixed by:**
1. ✅ Refreshing the browser
2. ✅ Clearing browser cache
3. ✅ Restarting the server

Good luck, adventurer! ⚔️


