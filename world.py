"""World map and locations"""
import random
from weather import Weather

class Location:
    """Represents a location in the game world"""
    def __init__(self, name: str, description: str, enemy_types: list, 
                 connections: list, shop: bool = False, quest_location: bool = False):
        self.name = name
        self.description = description
        self.enemy_types = enemy_types  # List of possible enemy types
        self.connections = connections  # List of connected location names
        self.shop = shop
        self.quest_location = quest_location
        self.current_weather = Weather.get_random_weather()  # Add weather to location
        
    def get_random_enemy(self, player_level: int):
        """Get a random enemy appropriate for this location"""
        if not self.enemy_types:
            return None
        
        from enemy import create_enemy
        enemy_type = random.choice(self.enemy_types)
        level_modifier = max(0, player_level - 1)
        return create_enemy(enemy_type, level_modifier)
    
    def update_weather(self):
        """Update location weather (20% chance to change)"""
        if Weather.should_change_weather():
            old_weather = self.current_weather
            self.current_weather = Weather.get_random_weather()
            return old_weather != self.current_weather
        return False
    
    def get_weather_description(self):
        """Get current weather description"""
        return Weather.get_weather_description(self.current_weather)

# Define the game world
WORLD = {
    "village": Location(
        name="🏰 Willowbrook Village",
        description="""
🌅 The morning sun bathes the village square in golden light.

👨‍🌾 "Hero! Thank the gods you've come!" cries Elder Marcus, rushing toward you.
💬 "Dark forces have awakened! The Shadow Lord Malzahar has returned from 
   the ancient void, corrupting everything he touches!"

👴 Elder Marcus: "We need brave souls like you. The prophecy speaks of a 
   champion who will gather the Four Sacred Relics and stop him!"

🗺️ DESTINATIONS:
   🌲 North → Dark Forest (Strange lights seen at night...)
   🏛️ East → Ancient Ruins (Scholars report dark magic)
   ⛰️ South → Mountain Path (Dragons stir in their lairs)
   🏪 West → Trading Post (Stock up on supplies!)
   
⚠️ "Be careful out there. Trust in your strength, and may fortune guide you!"
""",
        enemy_types=[],
        connections=["dark_forest", "ancient_ruins", "mountain_path", "trading_post"],
        shop=False,
        quest_location=True
    ),
    
    "trading_post": Location(
        name="Trading Post",
        description="""
A bustling trading post where merchants from across the realm
gather to sell their wares. You can see weapons, armor, and
supplies of all kinds.
""",
        enemy_types=[],
        connections=["village"],
        shop=True,
        quest_location=False
    ),
    
    "dark_forest": Location(
        name="🌲 Darkwood Forest",
        description="""
🌙 Moonlight struggles to pierce through the twisted canopy above.
   Gnarled trees seem to whisper warnings in an ancient tongue.

👻 "Tressspassersss..." hisses a voice from the shadows.
💀 The corrupted creatures here were once normal forest animals,
   twisted by Malzahar's dark magic into aggressive monsters!

🔍 ATMOSPHERE: Mist swirls at your feet. Glowing eyes watch from the darkness.
⚠️ DANGER LEVEL: Low-Medium | Recommended: Level 1-3

🗡️ ENEMIES SIGHTED:
   • Corrupted Goblins (servants of darkness)
   • Shadow Wolves (possessed by evil spirits)  
   • Skeleton Warriors (the restless dead)

💡 "Stay alert! These woods hold secrets... and treasure!"
""",
        enemy_types=["goblin", "wolf", "skeleton"],
        connections=["village", "bandit_camp", "cursed_swamp"],
        quest_location=True
    ),
    
    "bandit_camp": Location(
        name="Bandit Camp",
        description="""
A crude camp set up by bandits preying on travelers.
Tattered tents and stolen goods litter the area.
The bandits eye you with hostile intent.
""",
        enemy_types=["goblin", "orc", "skeleton"],
        connections=["dark_forest"],
        quest_location=True
    ),
    
    "cursed_swamp": Location(
        name="Cursed Swamp",
        description="""
Murky waters bubble ominously, and a foul mist hangs in the air.
This place feels wrong, corrupted by dark magic.
Dangerous creatures lurk in the depths.
""",
        enemy_types=["skeleton", "wraith", "dark_mage"],
        connections=["dark_forest", "haunted_graveyard"],
        quest_location=False
    ),
    
    "haunted_graveyard": Location(
        name="Haunted Graveyard",
        description="""
Crumbling tombstones stretch as far as the eye can see.
The restless dead walk here, unable to find peace.
A dark power emanates from deep within...
""",
        enemy_types=["skeleton", "wraith", "vampire"],
        connections=["cursed_swamp", "dark_castle"],
        quest_location=False
    ),
    
    "ancient_ruins": Location(
        name="Ancient Ruins",
        description="""
Massive stone pillars and crumbling walls speak of a once-great
civilization. Ancient magic still lingers in these halls.
What secrets do these ruins hold?
""",
        enemy_types=["skeleton", "dark_mage", "wraith"],
        connections=["village", "hidden_temple"],
        quest_location=True
    ),
    
    "hidden_temple": Location(
        name="Hidden Temple",
        description="""
A sacred temple hidden beneath the ruins, untouched for centuries.
Powerful enchantments protect this place.
You feel both awe and danger in equal measure.
""",
        enemy_types=["wraith", "demon", "dark_mage"],
        connections=["ancient_ruins"],
        quest_location=False
    ),
    
    "mountain_path": Location(
        name="Mountain Path",
        description="""
A treacherous path winds up the mountainside.
The air grows thin and cold as you climb higher.
Few dare to venture into these peaks.
""",
        enemy_types=["wolf", "orc", "troll"],
        connections=["village", "mountain_peak"],
        quest_location=False
    ),
    
    "mountain_peak": Location(
        name="Mountain Peak",
        description="""
You stand at the summit, clouds swirling around you.
Ancient caves dot the mountainside - the domain of dragons.
A mighty roar echoes across the peaks...
""",
        enemy_types=["dragon_whelp", "troll", "orc"],
        connections=["mountain_path", "dragon_lair"],
        quest_location=True
    ),
    
    "dragon_lair": Location(
        name="Dragon's Lair",
        description="""
Massive caverns filled with treasure hoards and dragon bones.
The heat is intense, and the smell of sulfur fills the air.
An ANCIENT DRAGON slumbers on a mountain of gold...
""",
        enemy_types=["ancient_dragon"],
        connections=["mountain_peak"],
        quest_location=False
    ),
    
    "dark_castle": Location(
        name="Dark Castle",
        description="""
The fortress of the Dark Lord looms before you, wreathed in
shadow and malevolent energy. This is the source of the evil
that threatens the realm.

Your final battle awaits...
""",
        enemy_types=["demon", "vampire", "dark_mage", "dark_lord"],
        connections=["haunted_graveyard"],
        quest_location=True
    ),
    
    "crystal_cavern": Location(
        name="💎 Crystal Cavern of Legends",
        description="""
╔══════════════════════════════════════════════════════════════╗
║          ✨ THE LEGENDARY CRYSTAL CAVERN ✨                  ║
╚══════════════════════════════════════════════════════════════╝

🌟 You step into a breathtaking realm of wonder!

💎 Massive crystals pulse with ancient power, casting rainbow light
   across walls of pure diamond. The air itself shimmers with magic.
   
🏆 LEGENDARY TREASURES are scattered throughout the cavern:
   ⚔️  Godforged weapons that heroes only dream of
   🛡️  Armor blessed by the ancient dragon gods
   💰 Gold beyond your wildest imagination
   
⚠️  WARNING: This sacred place is guarded by ELEMENTAL GUARDIANS!
   🔥 Fire Elementals (Burning with ancient rage)
   ❄️  Ice Golems (Frozen protectors of eternity)
   ⚡ Storm Spirits (Crackling with unlimited power)
   💎 Crystal Titans (Nearly indestructible!)
   
🎲 The cavern shifts and changes - no two visits are the same!
   Every treasure chest holds different legendary items!
   
✨ "Only the bravest heroes dare enter..." whisper the crystals.
   "But those who survive... become LEGENDS!"
   
🌈 The crystals sing an ancient song of power and glory...
""",
        enemy_types=["fire_elemental", "ice_golem", "storm_spirit", "crystal_titan"],
        connections=["dark_forest", "mountain_peak", "ancient_ruins"],
        shop=False,
        quest_location=False
    ),
}

class World:
    """Manages the game world"""
    def __init__(self):
        self.locations = WORLD
        
    def get_location(self, location_name: str):
        """Get a location by name"""
        return self.locations.get(location_name)
    
    def get_starting_location(self) -> str:
        """Get the starting location"""
        return "village"



