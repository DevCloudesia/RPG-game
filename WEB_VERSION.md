# 🌐 Web Version - Realm of Legends

Play the RPG directly in your web browser with a modern, beautiful UI!

## Features

✨ **Modern Web Interface**
- Beautiful gradient backgrounds and animations
- Responsive design (works on desktop and mobile)
- Real-time stat updates
- Smooth combat animations

🎮 **All Game Features**
- Character creation with visual class selection
- Real-time HP/Mana/EXP bars
- Interactive combat system
- Inventory management with visual grid
- Quest tracking with objectives
- Shop interface
- Travel between locations
- Save/Load functionality (session-based)

## Quick Start

### Method 1: Easy Start (Recommended)
```bash
./start_web.sh
```

The script will:
1. Create a virtual environment (if needed)
2. Install Flask automatically
3. Start the web server
4. Show you the URL to open

### Method 2: Manual Start
```bash
# Create virtual environment (first time only)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask (first time only)
pip install Flask

# Start the server
python web_game.py
```

### Method 3: Using existing venv
If you already have a virtual environment with Flask:
```bash
source venv/bin/activate
python web_game.py
```

## Opening the Game

Once the server is running, open your browser and go to:
```
http://localhost:5000
```

Or if accessing from another device on the same network:
```
http://YOUR_LOCAL_IP:5000
```

## Controls

The web version uses mouse/touch controls:
- **Click buttons** to perform actions
- **Click on class cards** during character creation
- **Click items** in inventory to use/equip
- **Click destinations** to travel
- **Click abilities** during combat

## Game Flow

1. **Title Screen** - Click "Begin Your Quest"
2. **Character Creation**
   - Enter your name
   - Click a class card to select
   - Click "Start Adventure"
3. **Main Game**
   - Explore locations
   - Fight enemies in turn-based combat
   - Complete quests
   - Manage inventory
   - Buy from shops
   - Travel to new areas

## Combat Interface

When in combat, you'll see:
- Enemy HP bar at the top
- Your character stats on the left
- Combat action buttons
- Ability panel (when clicking "Abilities")
- Item panel (when clicking "Items")

## Features Unique to Web Version

- **Visual Feedback**: Color-coded HP/Mana bars
- **Animations**: Smooth transitions and effects
- **Modal Windows**: Clean interfaces for inventory, quests, shop
- **Live Updates**: Real-time stat changes
- **Better Organization**: Visual grids for items and locations
- **Responsive Design**: Play on any device

## Technical Details

- **Backend**: Python Flask (RESTful API)
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: Session-based (in-memory)
- **Port**: 5000 (default)
- **Host**: 0.0.0.0 (accessible from network)

## Troubleshooting

**Problem**: Port 5000 already in use
- **Solution**: Edit `web_game.py` and change the port number

**Problem**: Can't access from another device
- **Solution**: Check your firewall settings and use your local IP address

**Problem**: Flask not installed
- **Solution**: Run `./start_web.sh` or manually install with `pip install Flask`

**Problem**: Browser shows "Connection Refused"
- **Solution**: Make sure the server is running (check terminal for errors)

## Browser Compatibility

Works best on:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

Minimum requirements:
- JavaScript enabled
- CSS3 support
- Modern browser (released in last 3 years)

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

---

**Enjoy your web-based adventure! ⚔️🌐**






