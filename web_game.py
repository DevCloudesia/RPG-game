#!/usr/bin/env python3
"""
Web-based version of Realm of Legends RPG
Run this to play the game in your browser!
"""

from flask import Flask, render_template, request, jsonify, session
import secrets
import copy
from character import Character
from world import World
from combat import Combat
from items import create_item, Consumable, Weapon, Armor
from quests import create_quest
from enemy import create_enemy
from random_events import RandomEvent
import random

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # 1 hour

# Store game states in memory (in production, use a database)
game_states = {}

# Add session verification
@app.before_request
def ensure_session():
    """Ensure session is properly initialized"""
    if 'game_id' not in session and request.endpoint not in ['index', 'static']:
        # Generate new game_id for API requests without one
        session['game_id'] = secrets.token_hex(16)
        session.permanent = True

class WebGame:
    """Web version of the game"""
    
    def __init__(self):
        self.player = None
        self.world = World()
        self.current_location = None
        self.combat_active = False
        self.current_enemy = None
        self.current_weather = None
        self.enemy_kill_count = 0
        self.game_over = False
        self.messages = []
        
    def to_dict(self):
        """Convert game state to dictionary"""
        return {
            'player': self.player,
            'current_location': self.current_location,
            'combat_active': self.combat_active,
            'current_enemy': self.current_enemy,
            'current_weather': self.current_weather,
            'enemy_kill_count': self.enemy_kill_count,
            'game_over': self.game_over,
            'messages': self.messages
        }
    
    def from_dict(self, data):
        """Load game state from dictionary"""
        self.player = data.get('player')
        self.current_location = data.get('current_location')
        self.combat_active = data.get('combat_active', False)
        self.current_enemy = data.get('current_enemy')
        self.current_weather = data.get('current_weather')
        self.enemy_kill_count = data.get('enemy_kill_count', 0)
        self.game_over = data.get('game_over', False)
        self.messages = data.get('messages', [])

def get_game():
    """Get or create game state for current session"""
    if 'game_id' not in session:
        session['game_id'] = secrets.token_hex(16)
        session.permanent = True
    
    game_id = session['game_id']
    
    # Try to get from memory first
    if game_id in game_states:
        game = game_states[game_id]
        print(f"[GET] Retrieved from memory - Combat: {game.combat_active if hasattr(game, 'combat_active') else False}")
        return game
    
    # If not in memory, create new
    print(f"[GET] Creating new game for session {game_id[:8]}...")
    game_states[game_id] = WebGame()
    return game_states[game_id]

def save_game(game):
    """Save game state"""
    if 'game_id' not in session:
        session['game_id'] = secrets.token_hex(16)
        session.permanent = True
    
    game_id = session['game_id']
    
    # Make absolutely sure we're storing a reference to the same object
    game_states[game_id] = game
    
    # Verify the save worked
    verify_game = game_states.get(game_id)
    if verify_game and hasattr(verify_game, 'combat_active'):
        print(f"[SAVE] ✓ Game saved - Session: {game_id[:8]}... Combat: {verify_game.combat_active}, Enemy: {verify_game.current_enemy.name if verify_game.current_enemy else None}")
    else:
        print(f"[SAVE] ✗ SAVE FAILED for session {game_id[:8]}...")
    
    # Mark session as modified
    session.modified = True

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/test_combat', methods=['POST'])
def test_combat():
    """Test endpoint to force combat"""
    game = get_game()
    
    if not game.player:
        return jsonify({'success': False, 'error': 'Start a game first'}), 400
    
    # Force create an enemy
    from enemy import create_enemy
    enemy = create_enemy('goblin', 0)
    game.current_enemy = enemy
    game.combat_active = True
    game.messages = [f"🧪 TEST: Forcing combat with {enemy.name}"]
    
    save_game(game)
    
    return jsonify({'success': True, 'message': 'Combat forced!', 'game_state': get_game_state_json(game)})

@app.route('/api/start_game', methods=['POST'])
def start_game():
    """Start a new game"""
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
            
        name = data.get('name', 'Hero')
        char_class = data.get('class', 'Warrior')
        
        # Initialize session with game_id if not present
        if 'game_id' not in session:
            session['game_id'] = secrets.token_hex(16)
        
        # Create new game instance
        game = WebGame()
        game.player = Character(name, char_class)
        game.current_location = game.world.get_starting_location()
        
        # Initialize weather
        from weather import Weather
        game.current_weather = Weather.get_random_weather()
        
        # Starting items
        game.player.add_item(create_item("health_potion"))
        game.player.add_item(create_item("health_potion"))
        game.player.add_item(create_item("mana_potion"))
        
        # Starting quest
        tutorial_quest = create_quest("tutorial")
        if tutorial_quest:
            game.player.quests.append(tutorial_quest)
        
        # Save game state
        save_game(game)
        
        return jsonify({
            'success': True,
            'message': f'Welcome, {name} the {char_class}!',
            'game_state': get_game_state_json(game)
        })
    except Exception as e:
        print(f"Error starting game: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/game_state', methods=['GET'])
def get_game_state():
    """Get current game state"""
    game = get_game()
    return jsonify(get_game_state_json(game))

def get_game_state_json(game):
    """Convert game state to JSON-serializable format"""
    if not game.player:
        return {'initialized': False}
    
    location = game.world.get_location(game.current_location)
    
    player_data = {
        'name': game.player.name,
        'class': game.player.char_class,
        'level': game.player.level,
        'hp': game.player.hp,
        'max_hp': game.player.max_hp,
        'mana': game.player.mana,
        'max_mana': game.player.max_mana,
        'attack': game.player.attack,
        'defense': game.player.defense,
        'magic': game.player.magic,
        'experience': game.player.experience,
        'exp_needed': game.player.level * 100,
        'gold': game.player.gold,
        'abilities': game.player.abilities,
        'inventory_count': len(game.player.inventory),
        'quest_count': len(game.player.quests)
    }
    
    enemy_data = None
    if game.current_enemy:
        enemy_data = {
            'name': game.current_enemy.name,
            'hp': game.current_enemy.hp,
            'max_hp': game.current_enemy.max_hp,
            'level': game.current_enemy.level
        }
    
    # Add weather data
    weather_data = None
    if game.current_weather:
        from weather import Weather
        weather_info = Weather.get_weather_info(game.current_weather)
        weather_data = {
            'name': weather_info['name'],
            'description': weather_info['description'],
            'emoji': weather_info['emoji'],
            'events': len(weather_info.get('events', []))
        }
    
    return {
        'initialized': True,
        'player': player_data,
        'location': {
            'name': location.name,
            'description': location.description,
            'has_enemies': len(location.enemy_types) > 0,
            'has_shop': location.shop,
            'connections': [game.world.get_location(c).name for c in location.connections]
        },
        'combat_active': game.combat_active,
        'enemy': enemy_data,
        'weather': weather_data,
        'messages': game.messages,
        'game_over': game.game_over
    }

@app.route('/api/explore', methods=['POST'])
def explore():
    """Explore current location"""
    try:
        game = get_game()
        
        if not game.player:
            return jsonify({'success': False, 'error': 'No active game. Please start a new game.'}), 400
        
        game.messages = []
        
        # SECRET WORLD DISCOVERY! (5% chance if not discovered yet)
        if not game.player.discovered_secret_world and game.current_location in ["dark_forest", "mountain_peak", "ancient_ruins"]:
            if random.random() < 0.05:  # 5% chance to discover!
                game.messages.append("⚠️ ✨ SOMETHING MAGICAL IS HAPPENING! ✨ ⚠️")
                game.messages.append("")
                game.messages.append("🌟 The ground shimmers with otherworldly light!")
                game.messages.append("💎 A HIDDEN PORTAL materializes before you!")
                game.messages.append("✨ Ancient runes glow with cosmic power!")
                game.messages.append("")
                game.messages.append("╔══════════════════════════════════════╗")
                game.messages.append("║  ⭐ SECRET WORLD DISCOVERED! ⭐     ║")
                game.messages.append("║                                      ║")
                game.messages.append("║    💎 CRYSTAL CAVERN 💎             ║")
                game.messages.append("║                                      ║")
                game.messages.append("║  🏆 LEGENDARY EQUIPMENT!            ║")
                game.messages.append("║  ⚠️ ELEMENTAL GUARDIANS!            ║")
                game.messages.append("║  🎲 CHANGES EVERY VISIT!            ║")
                game.messages.append("╚══════════════════════════════════════╝")
                game.messages.append("")
                game.messages.append("💫 The Crystal Cavern is now accessible from travel menu!")
                
                game.player.discovered_secret_world = True
                save_game(game)
                return jsonify({'success': True, 'secret_discovered': True, 'game_state': get_game_state_json(game)})
        
        location = game.world.get_location(game.current_location)
        
        # Crystal Cavern treasure discovery (30% chance)
        if game.current_location == "crystal_cavern":
            if random.random() < 0.3:
                legendary_items = [
                    "excalibur", "mjolnir", "shadowfang", "staff_of_cosmos", 
                    "godbow", "infinity_blade", "celestial_armor", "void_armor",
                    "phoenix_plate", "crystal_guardian", "time_weaver"
                ]
                ultra_rare = ["omni_weapon", "cosmic_armor"]
                
                game.messages.append("🎰 ✨ LEGENDARY TREASURE CHEST! ✨ 🎰")
                game.messages.append("")
                
                if random.random() < 0.05:  # Ultra rare
                    item_key = random.choice(ultra_rare)
                    game.messages.append("🌌 ⭐ ULTRA LEGENDARY! ⭐ 🌌")
                    item = create_item(item_key)
                    game.player.add_item(item)
                    game.messages.append(f"✨ {item.name}")
                    game.messages.append(f"   {item.description}")
                elif random.random() < 0.5:
                    item_key = random.choice(legendary_items)
                    item = create_item(item_key)
                    game.player.add_item(item)
                    game.messages.append(f"⭐ LEGENDARY: {item.name}")
                    game.messages.append(f"   {item.description}")
                else:
                    gold_amount = random.randint(500, 1500)
                    game.player.gold += gold_amount
                    game.messages.append(f"💰 JACKPOT: {gold_amount} gold!")
                    elixir_count = random.randint(1, 3)
                    for _ in range(elixir_count):
                        game.player.add_item(create_item("elixir"))
                    game.messages.append(f"💫 Plus {elixir_count} Elixir(s) of Life!")
                
                save_game(game)
                return jsonify({'success': True, 'treasure_found': True, 'game_state': get_game_state_json(game)})
        
        if not location.enemy_types:
            game.messages.append("✨ This area is peaceful. No enemies here!")
            game.messages.append("💡 Try traveling to the Dark Forest to find monsters!")
            save_game(game)
            return jsonify({'success': True, 'game_state': get_game_state_json(game)})
        
        # Add random event flavor (30% chance)
        if random.random() < 0.3:
            event = RandomEvent.get_exploration_event(game.current_location)
            game.messages.append(event['text'])
            
            # Handle special event types
            if event['type'] == 'gold':
                game.player.gold += event.get('amount', 0)
                game.messages.append(f"💰 +{event.get('amount', 0)} gold added to your purse!")
        
        # Higher chance of finding enemies (80%)
        if random.random() < 0.80:
            enemy = location.get_random_enemy(game.player.level)
            game.current_enemy = enemy
            game.combat_active = True
            
            # Exciting encounter with enemy taunt
            encounter_msgs = [
                f"⚡ {RandomEvent.get_combat_flavor()}",
                f"{RandomEvent.get_enemy_taunt(enemy.name)}",
                f"",
                f"╔══════════ ENEMY ENCOUNTER ══════════╗",
                f"│  👹 {enemy.name:<30} │",
                f"│  ❤️  HP: {enemy.hp}/{enemy.max_hp:<24} │",
                f"│  ⚔️  ATK: {enemy.attack:<26} │",
                f"│  🛡️  DEF: {enemy.defense:<26} │",
                f"╚══════════════════════════════════════╝",
                f"",
                f"🎯 COMBAT INITIATED! Choose your action wisely!"
            ]
            game.messages.extend(encounter_msgs)
            
            # CRITICAL: Save game state before returning
            save_game(game)
            
            # Debug logging
            print(f"[EXPLORE] Combat started! Enemy: {enemy.name}, HP: {enemy.hp}")
            print(f"[EXPLORE] Session ID: {session.get('game_id')}")
            print(f"[EXPLORE] Game combat_active: {game.combat_active}")
            
            return jsonify({'success': True, 'combat_started': True, 'game_state': get_game_state_json(game)})
        else:
            # No enemy but maybe an event
            event = RandomEvent.get_exploration_event(game.current_location)
            game.messages.append("🔍 You search the area thoroughly...")
            game.messages.append(event['text'])
            game.messages.append("💡 No enemies this time, but keep exploring!")
            save_game(game)
            return jsonify({'success': True, 'game_state': get_game_state_json(game)})
    except Exception as e:
        print(f"Error in explore: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/combat_action', methods=['POST'])
def combat_action():
    """Perform combat action"""
    # Debug: Show all game states
    print(f"\n[COMBAT ACTION] === DEBUG START ===")
    print(f"[COMBAT ACTION] Total game states in memory: {len(game_states)}")
    print(f"[COMBAT ACTION] Session ID in request: {session.get('game_id', 'NO SESSION')}")
    for gid, g in game_states.items():
        print(f"[COMBAT ACTION]   - {gid[:8]}: combat={g.combat_active if hasattr(g, 'combat_active') else '?'}, enemy={g.current_enemy.name if hasattr(g, 'current_enemy') and g.current_enemy else 'None'}")
    
    game = get_game()
    
    # Verify we have a player
    if not game.player:
        print(f"[COMBAT ACTION] ERROR: No player!")
        return jsonify({'success': False, 'error': 'No active game. Please start a new game.'}), 400
    
    game.messages = []
    
    # Debug logging
    print(f"[COMBAT ACTION] Game retrieved - Combat: {game.combat_active}, Enemy: {game.current_enemy is not None}")
    print(f"[COMBAT ACTION] === DEBUG END ===\n")
    
    if not game.combat_active or not game.current_enemy:
        return jsonify({'success': False, 'error': 'Not in combat. Try exploring to find an enemy first.'}), 400
    
    data = request.json
    action = data.get('action')
    
    # Check for weather events BEFORE combat actions (30% chance)
    from weather import Weather
    if game.current_weather:
        weather_event = Weather.trigger_weather_event(game.current_weather)
        if weather_event:
            event_message = weather_event.apply(game.player, game.current_enemy)
            game.messages.append(event_message)
            
            # Check if weather event killed anyone
            if game.player.hp <= 0:
                game.messages.append("\n💀 You were defeated by the weather!\n")
                game.game_over = True
                save_game(game)
                return jsonify({'success': True, 'defeat': True, 'game_state': get_game_state_json(game)})
            elif not game.current_enemy.is_alive():
                game.messages.append(f"\n🌩️ {game.current_enemy.name} was destroyed by the weather!\n")
                rewards_msg = Combat.combat_rewards(game.player, game.current_enemy)
                game.messages.append(rewards_msg)
                game.combat_active = False
                game.current_enemy = None
                save_game(game)
                return jsonify({'success': True, 'victory': True, 'game_state': get_game_state_json(game)})
    
    defending = False
    
    if action == 'attack':
        message, success = Combat.player_turn(game.player, game.current_enemy, "attack")
        game.messages.append(message)
        
    elif action == 'ability':
        ability = data.get('ability')
        if not ability:
            return jsonify({'success': False, 'error': 'No ability specified'})
        message, success = Combat.player_turn(game.player, game.current_enemy, "ability", ability)
        game.messages.append(message)
        
    elif action == 'defend':
        message, success = Combat.player_turn(game.player, game.current_enemy, "defend")
        game.messages.append(message)
        defending = True
        
    elif action == 'run':
        if random.random() < 0.5:
            game.messages.append("🏃 You successfully escaped!")
            game.combat_active = False
            game.current_enemy = None
            save_game(game)
            return jsonify({'success': True, 'escaped': True, 'game_state': get_game_state_json(game)})
        else:
            game.messages.append("❌ You couldn't escape!")
            
    else:
        return jsonify({'success': False, 'error': 'Invalid action'})
    
    # Check if enemy defeated
    if not game.current_enemy.is_alive():
        game.messages.append(f"\n💀 {game.current_enemy.name} has been defeated!")
        rewards_msg = Combat.combat_rewards(game.player, game.current_enemy)
        game.messages.append(rewards_msg)
        
        game.enemy_kill_count += 1
        update_quest_progress(game, "defeat_3_enemies")
        update_quest_progress(game, "defeat_5_bandits")
        update_quest_progress(game, "defeat_forest_enemy")
        update_quest_progress(game, "defeat_egg_guardian")
        
        game.combat_active = False
        game.current_enemy = None
        save_game(game)
        return jsonify({'success': True, 'victory': True, 'game_state': get_game_state_json(game)})
    
    # Enemy turn
    enemy_msg = Combat.enemy_turn(game.current_enemy, game.player, defending)
    game.messages.append(enemy_msg)
    
    # Check if player defeated
    if game.player.hp <= 0:
        game.messages.append("\n💀 You have been defeated...")
        game.game_over = True
        save_game(game)
        return jsonify({'success': True, 'defeat': True, 'game_state': get_game_state_json(game)})
    
    save_game(game)
    return jsonify({'success': True, 'game_state': get_game_state_json(game)})

@app.route('/api/use_item', methods=['POST'])
def use_item():
    """Use an item"""
    game = get_game()
    game.messages = []
    
    data = request.json
    item_index = data.get('item_index')
    
    if item_index < 0 or item_index >= len(game.player.inventory):
        return jsonify({'success': False, 'error': 'Invalid item'})
    
    item = game.player.inventory[item_index]
    
    if isinstance(item, Consumable):
        message = item.use(game.player)
        game.player.remove_item(item)
        game.messages.append(message)
    elif isinstance(item, Weapon):
        game.player.equip_weapon(item)
        game.messages.append(f"⚔️ Equipped {item.name}!")
    elif isinstance(item, Armor):
        game.player.equip_armor(item)
        game.messages.append(f"🛡️ Equipped {item.name}!")
    else:
        game.messages.append(f"{item.name}: {item.description}")
    
    save_game(game)
    return jsonify({'success': True, 'game_state': get_game_state_json(game)})

@app.route('/api/travel', methods=['POST'])
def travel():
    """Travel to new location"""
    game = get_game()
    game.messages = []
    
    data = request.json
    destination_name = data.get('destination')
    
    location = game.world.get_location(game.current_location)
    
    # Build available destinations
    destinations = list(location.connections)
    
    # Add Crystal Cavern if discovered
    if game.player.discovered_secret_world and game.current_location in ["dark_forest", "mountain_peak", "ancient_ruins"]:
        if "crystal_cavern" not in destinations:
            destinations.append("crystal_cavern")
    
    # Allow travel from Crystal Cavern
    if game.current_location == "crystal_cavern":
        destinations = ["dark_forest", "mountain_peak", "ancient_ruins"]
    
    # Find matching connection
    for conn in destinations:
        loc = game.world.get_location(conn)
        if loc.name == destination_name or conn == destination_name:
            game.current_location = conn
            if conn == "crystal_cavern":
                game.messages.append("✨ Stepping through the portal...")
                game.messages.append("💎 You enter the Crystal Cavern of Legends!")
                game.messages.append("🌈 The crystals sing their ancient song!")
            else:
                game.messages.append(f"🚶 Traveling to {loc.name}...")
            update_quest_progress(game, f"visit_{conn}")
            save_game(game)
            return jsonify({'success': True, 'game_state': get_game_state_json(game)})
    
    return jsonify({'success': False, 'error': 'Invalid destination'})

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    """Get player inventory"""
    game = get_game()
    
    inventory = []
    for i, item in enumerate(game.player.inventory):
        item_data = {
            'index': i,
            'name': item.name,
            'description': item.description,
            'type': type(item).__name__
        }
        
        if isinstance(item, Weapon):
            item_data['attack_bonus'] = item.attack_bonus
            item_data['equipped'] = (item == game.player.equipped_weapon)
        elif isinstance(item, Armor):
            item_data['defense_bonus'] = item.defense_bonus
            item_data['equipped'] = (item == game.player.equipped_armor)
        
        inventory.append(item_data)
    
    return jsonify({'success': True, 'inventory': inventory})

@app.route('/api/quests', methods=['GET'])
def get_quests():
    """Get player quests"""
    game = get_game()
    
    quests = []
    for quest in game.player.quests:
        quest_data = {
            'name': quest.name,
            'description': quest.description,
            'objectives': [],
            'complete': quest.is_complete()
        }
        
        for obj_key, completed in quest.objectives.items():
            quest_data['objectives'].append({
                'name': obj_key.replace('_', ' ').title(),
                'completed': completed
            })
        
        quests.append(quest_data)
        
        # Check if can be completed
        if quest.is_complete() and not quest.completed:
            success, message = quest.complete(game.player)
            if success:
                game.messages.append(message)
                game.player.completed_quests.append(quest)
                game.player.quests.remove(quest)
                grant_new_quests(game, quest.quest_id)
    
    completed = []
    for quest in game.player.completed_quests:
        completed.append({
            'name': quest.name,
            'description': quest.description
        })
    
    save_game(game)
    return jsonify({
        'success': True,
        'active_quests': quests,
        'completed_quests': completed,
        'messages': game.messages
    })

@app.route('/api/shop', methods=['GET'])
def get_shop():
    """Get shop items"""
    shop_items = [
        {'key': 'health_potion', 'name': 'Health Potion', 'price': 25, 'description': 'Restores 50 HP'},
        {'key': 'super_health_potion', 'name': 'Super Health Potion', 'price': 50, 'description': 'Restores 100 HP'},
        {'key': 'mana_potion', 'name': 'Mana Potion', 'price': 30, 'description': 'Restores 40 mana'},
        {'key': 'super_mana_potion', 'name': 'Super Mana Potion', 'price': 60, 'description': 'Restores 80 mana'},
        {'key': 'iron_sword', 'name': 'Iron Sword', 'price': 50, 'description': '+10 Attack'},
        {'key': 'steel_sword', 'name': 'Steel Sword', 'price': 150, 'description': '+18 Attack'},
        {'key': 'leather_armor', 'name': 'Leather Armor', 'price': 50, 'description': '+8 Defense'},
        {'key': 'chainmail', 'name': 'Chainmail', 'price': 150, 'description': '+15 Defense'},
    ]
    
    return jsonify({'success': True, 'items': shop_items})

@app.route('/api/shop/buy', methods=['POST'])
def buy_item():
    """Buy item from shop"""
    game = get_game()
    game.messages = []
    
    data = request.json
    item_key = data.get('item_key')
    
    prices = {
        'health_potion': 25,
        'super_health_potion': 50,
        'mana_potion': 30,
        'super_mana_potion': 60,
        'iron_sword': 50,
        'steel_sword': 150,
        'leather_armor': 50,
        'chainmail': 150,
    }
    
    if item_key not in prices:
        return jsonify({'success': False, 'error': 'Invalid item'})
    
    price = prices[item_key]
    
    if game.player.gold < price:
        game.messages.append("❌ Not enough gold!")
        return jsonify({'success': False, 'error': 'Not enough gold', 'game_state': get_game_state_json(game)})
    
    item = create_item(item_key)
    game.player.gold -= price
    game.player.add_item(item)
    game.messages.append(f"✨ Purchased {item.name}!")
    
    save_game(game)
    return jsonify({'success': True, 'game_state': get_game_state_json(game)})

def update_quest_progress(game, objective_key):
    """Update quest progress"""
    for quest in game.player.quests:
        if objective_key in quest.objectives and not quest.objectives[objective_key]:
            if objective_key == "defeat_3_enemies" and game.enemy_kill_count >= 3:
                quest.check_objective(objective_key)
                game.messages.append(f"\n✓ Quest objective complete: Defeat 3 enemies")
            elif objective_key == "defeat_5_bandits" and game.enemy_kill_count >= 5:
                quest.check_objective(objective_key)
                game.messages.append(f"\n✓ Quest objective complete: Defeat 5 bandits")
            else:
                quest.check_objective(objective_key)
                obj_name = objective_key.replace("_", " ").title()
                game.messages.append(f"\n✓ Quest objective complete: {obj_name}")

def grant_new_quests(game, completed_quest_id):
    """Grant new quests"""
    quest_progression = {
        "tutorial": ["gather_herbs", "bandit_camp"],
        "gather_herbs": ["ancient_ruins"],
        "bandit_camp": ["ancient_ruins"],
        "ancient_ruins": ["dragon_egg"],
        "dragon_egg": ["final_battle"]
    }
    
    if completed_quest_id in quest_progression:
        for new_quest_id in quest_progression[completed_quest_id]:
            new_quest = create_quest(new_quest_id)
            if new_quest and new_quest not in game.player.quests:
                game.player.quests.append(new_quest)
                game.messages.append(f"\n📜 New Quest: {new_quest.name}")

if __name__ == '__main__':
    import socket
    import os
    import sys
    
    # Get port from command line argument, environment variable, or use 8080
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default 8080.")
            PORT = 8080
    else:
        PORT = int(os.environ.get('PORT', 8080))
    
    # Get host - use 0.0.0.0 for external access
    HOST = os.environ.get('HOST', '0.0.0.0')
    
    # Disable debug and reloader to fix session state issues
    # (Flask reloader creates multiple processes that don't share game_states dictionary)
    DEBUG = False
    USE_RELOADER = False
    
    # Get local IP address for network access
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except:
        local_ip = "your-local-ip"
    
    print("\n" + "="*60)
    print(" "*15 + "⚔️  REALM OF LEGENDS  ⚔️")
    print("="*60)
    print("\n🌐 Starting web server...")
    print("\n📍 Access the game from:")
    print(f"   Local:    http://localhost:{PORT}")
    if DEBUG:  # Only show network IP in development
        print(f"   Network:  http://{local_ip}:{PORT}")
    print("\n✨ The game will run in your web browser!")
    if DEBUG:
        print("✨ Others on your network can play using the Network URL!")
    print("\nPress Ctrl+C to stop the server\n")
    print("="*60 + "\n")
    
    app.run(debug=DEBUG, host=HOST, port=PORT, use_reloader=USE_RELOADER)

