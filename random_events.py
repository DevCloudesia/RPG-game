"""Random events and encounters for more interesting gameplay"""
import random

class RandomEvent:
    """Random events that can occur during exploration"""
    
    @staticmethod
    def get_exploration_event(location_name):
        """Get a random event based on location"""
        
        events = {
            "village": [
                {"type": "npc", "text": "👨‍🌾 Farmer John: 'I saw strange lights in the Dark Forest last night. Be careful!'"},
                {"type": "npc", "text": "🧙‍♀️ Mystic Sarah: 'The stars speak of great danger... but also great reward!'"},
                {"type": "gold", "amount": 10, "text": "💰 You found 10 gold coins on the ground!"},
                {"type": "lore", "text": "📜 You overhear villagers: 'The Shadow Lord was defeated 1000 years ago...'"},
            ],
            
            "dark_forest": [
                {"type": "lore", "text": "🌙 An eerie howl echoes through the trees. Your blood runs cold..."},
                {"type": "treasure", "text": "✨ You spot something glowing in the bushes!"},
                {"type": "ambush", "text": "⚠️ You feel eyes watching you from the shadows..."},
                {"type": "lore", "text": "🍃 The wind whispers: 'Turn back... turn back...'"},
                {"type": "mystery", "text": "👣 Fresh tracks lead deeper into the forest. Human? Or something else?"},
            ],
            
            "mountain_path": [
                {"type": "lore", "text": "🏔️ The mountain trembles. The ancient dragons are awakening!"},
                {"type": "npc", "text": "🧗 Mountaineer: 'I've seen dragon fire in the peaks! Don't go up there alone!'"},
                {"type": "danger", "text": "💨 A fierce wind nearly knocks you off the cliff!"},
                {"type": "treasure", "text": "⛏️ An old mining cart contains forgotten treasures!"},
            ],
            
            "ancient_ruins": [
                {"type": "lore", "text": "📖 Ancient text: 'Four relics unite, darkness takes flight...'"},
                {"type": "mystery", "text": "🔮 A magical barrier shimmers ahead. You'll need more power to pass."},
                {"type": "ghost", "text": "👻 'Help us...' whisper the spirits of ancient scholars."},
                {"type": "treasure", "text": "💎 Ancient artifacts lie scattered among the rubble!"},
            ],
            
            "crystal_cavern": [
                {"type": "magic", "text": "🌈 The crystals sing an ancient song that fills you with power!"},
                {"type": "vision", "text": "💫 You see visions of legendary heroes who came before you!"},
                {"type": "power", "text": "⚡ Energy from the crystals flows through your body!"},
                {"type": "mystery", "text": "✨ 'Only the worthy may claim our treasures...' whisper the crystals."},
                {"type": "wonder", "text": "💎 The cavern shifts and changes before your eyes! Each visit is unique!"},
                {"type": "treasure", "text": "🎲 Treasure chests materialize randomly from the crystal walls!"},
                {"type": "warning", "text": "⚠️ The Elemental Guardians sense your presence..."},
                {"type": "blessing", "text": "🌟 The ancient magic here makes you feel invincible!"},
            ],
        }
        
        location_events = events.get(location_name, [
            {"type": "neutral", "text": "🔍 You search the area carefully..."}
        ])
        
        return random.choice(location_events)
    
    @staticmethod
    def get_combat_flavor():
        """Get random combat flavor text"""
        flavors = [
            "💥 The clash of steel rings out!",
            "⚡ Magic crackles in the air!",
            "🔥 Battle fury overtakes you!",
            "❄️ Time seems to slow as you focus...",
            "🌟 Your determination blazes bright!",
            "⚔️ This is what you were born for!",
            "💪 You feel your ancestors watching!",
            "🎯 Every move counts!",
        ]
        return random.choice(flavors)
    
    @staticmethod
    def get_victory_quote():
        """Get random victory quote"""
        quotes = [
            "💪 'Strength and honor!' you shout triumphantly!",
            "🎉 'For the kingdom!' Your victory cry echoes!",
            "⚔️ 'Another one bites the dust!'",
            "🌟 You feel the thrill of victory coursing through you!",
            "👑 'I am inevitable!'",
            "✨ The spirits of heroes past smile upon you!",
            "🔥 'Bring me another!' you challenge the darkness!",
            "💎 Glory and treasure await the brave!",
        ]
        return random.choice(quotes)
    
    @staticmethod
    def get_level_up_message(level):
        """Get exciting level up message"""
        messages = [
            f"🎊 LEVEL {level}! You feel power surging through your veins!",
            f"⭐ LEVEL {level}! The gods recognize your strength!",
            f"💪 LEVEL {level}! You've become a true warrior!",
            f"🔥 LEVEL {level}! Your legend grows!",
            f"✨ LEVEL {level}! Even your enemies fear you now!",
        ]
        return random.choice(messages)
    
    @staticmethod
    def get_critical_hit_message():
        """Get critical hit message"""
        messages = [
            "💥 CRITICAL HIT! Devastating blow!",
            "⚡ MEGA DAMAGE! That's gotta hurt!",
            "🎯 PERFECT STRIKE! Maximum damage!",
            "💢 CRUSHING BLOW! Critical success!",
            "🌟 LEGENDARY HIT! The stuff of tales!",
        ]
        return random.choice(messages)
    
    @staticmethod
    def get_enemy_taunt(enemy_name):
        """Get random enemy taunt"""
        taunts = [
            f"👹 {enemy_name}: 'You dare challenge ME?!'",
            f"💀 {enemy_name}: 'Your bones will join my collection!'",
            f"🗡️ {enemy_name}: 'Prepare to meet your doom!'",
            f"⚔️ {enemy_name}: 'I'll make this quick!'",
            f"🔥 {enemy_name}: 'Face the wrath of darkness!'",
        ]
        return random.choice(taunts)



