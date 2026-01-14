# ⚔️ Realm of Legends - Text-Based RPG

An immersive text-based RPG adventure where you embark on an epic quest to defeat the Dark Lord and save the realm!

## ✨ NEW: SECRET WORLD! 💎

**Discover the Crystal Cavern of Legends!**
- 🎲 **Randomly appears** while exploring (5% chance)
- 🏆 **16 Legendary Items** - The most powerful equipment in the game!
- ⚔️ **4 Elemental Guardians** - Fire, Ice, Storm, and Crystal enemies
- 💰 **Random Treasures** - Different every visit!
- 🌈 **Beautiful Visuals** - Special animations and glowing effects

👉 **See [SECRET_WORLD_GUIDE.md](SECRET_WORLD_GUIDE.md) for complete details!**

## 🎮 Features

### 🧙 Character Classes
- **Warrior** - High HP and devastating physical attacks
  - Abilities: Power Strike, Shield Bash, Berserker Rage
- **Mage** - Master of destructive magic
  - Abilities: Fireball, Ice Shard, Lightning Bolt
- **Rogue** - Swift and deadly assassin
  - Abilities: Backstab, Poison Dagger, Shadow Step
- **Cleric** - Holy warrior with healing powers
  - Abilities: Heal, Holy Smite, Divine Shield

### ⚔️ Combat System
- Strategic turn-based combat
- Special abilities with mana costs
- Attack, defend, or use items
- Option to flee from battles
- Experience and leveling system

### 🗺️ Vast World to Explore
Over 13 unique locations including:
- Peaceful Village (starting area)
- Dark Forest (mysterious and dangerous)
- Ancient Ruins (secrets of the past)
- Mountain Peak (domain of dragons)
- Haunted Graveyard (realm of the undead)
- Dark Castle (final confrontation)
- **💎 Crystal Cavern** (SECRET WORLD - Discover it by exploring!)

### 📜 Epic Quest System
- Main storyline with multiple chapters
- Side quests with unique rewards
- Quest tracking and objectives
- Progressive difficulty

### 🎒 Inventory & Equipment
- Weapons, armor, and consumables
- Equipment system that affects stats
- Shop to buy supplies
- Loot drops from enemies
- **NEW: Legendary Equipment** from the Crystal Cavern!
  - 🌈 Omniblade (+100 ATK) - God-tier weapon!
  - 🌌 Cosmic Armor (+120 DEF) - Ultimate defense!
  - Plus 14 more legendary items!

### 💾 Save System
- Save your progress anytime
- Load and continue your adventure

## 🚀 How to Play

### Installation

1. Make sure you have Python 3.6+ installed
2. No additional dependencies for terminal version!
3. For web version: Flask will be installed automatically

### Starting the Game

**🌐 Web Version (Recommended - Play in Browser!):**
```bash
./start_web.sh
```
Then open your browser to `http://localhost:8080`

**Want to host online?** See `QUICK_DEPLOY.md` for free cloud hosting!

**💻 Terminal Version (Classic Text-Based):**
```bash
python main.py
```

Or make it executable:
```bash
chmod +x main.py
./main.py
```

### Controls

The game uses a simple text-based menu system. Just enter the number or letter of your choice and press Enter.

### Tips for Success

1. **Keep potions handy** - Stock up at the Trading Post
2. **Use abilities wisely** - Manage your mana carefully
3. **Explore thoroughly** - Each location has unique enemies and rewards
4. **Complete quests** - They provide valuable experience and items
5. **Save often** - Don't lose your progress!
6. **Level up** - Fight enemies to gain experience and become stronger
7. **Equip the best gear** - Always check your inventory after battles
8. **🆕 Keep exploring!** - The secret Crystal Cavern appears randomly (5% chance)
9. **🆕 Return to the Crystal Cavern** - Treasures change each visit!
10. **🆕 Challenge the Elementals** - They drop the best loot in the game!

## 🎯 Game Progression

1. **Early Game** - Start in Peaceful Village, complete tutorial quest
2. **Mid Game** - Explore Dark Forest, Ancient Ruins, and Mountain Path
3. **Late Game** - Face powerful enemies in Cursed Swamp and Haunted Graveyard
4. **End Game** - Challenge the Ancient Dragon and Dark Lord

## 🐉 Enemy Types

From weakest to strongest:
- Goblins and Wolves
- Skeleton Warriors
- Orc Raiders
- Dark Mages
- Cave Trolls
- Shadow Wraiths
- Dragon Whelps
- Vampire Lords
- Demons
- **Ancient Dragon** (Boss)
- **Dark Lord Malzahar** (Final Boss)

### 💎 NEW: Elemental Guardians (Crystal Cavern)
- 🔥 **Fire Elemental** (HP: 250+, ATK: 45)
- ❄️ **Ice Golem** (HP: 300+, DEF: 28) 
- ⚡ **Storm Spirit** (HP: 220, ATK: 55)
- 💎 **Crystal Titan** (HP: 500+, Ultimate Boss!)

## 🏆 Victory Conditions

Defeat the Dark Lord in his castle to win the game and save the realm!

## 📝 Game Files

- `main.py` - Game entry point
- `game.py` - Main game engine and loop
- `character.py` - Character classes and stats
- `enemy.py` - Enemy definitions
- `items.py` - Items, weapons, and armor
- `combat.py` - Combat system
- `world.py` - World map and locations
- `quests.py` - Quest system
- `savegame.pkl` - Save file (created when you save)

## 🎨 About

This RPG features:
- Rich narrative and world-building
- Strategic combat with class-specific abilities
- Character progression and customization
- Multiple paths to explore
- Challenging boss battles
- Engaging quest system

Perfect for fans of classic text-based RPGs and roguelikes!

## 🛠️ Technical Details

- Written in Python 3
- No external dependencies
- Uses pickle for save/load functionality
- Object-oriented design with modular architecture

---

**Enjoy your adventure, brave hero! The fate of the realm rests in your hands! ⚔️**

