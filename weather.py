"""Weather system for the RPG game with dynamic events"""
import random

class WeatherEvent:
    """Represents a specific weather event that occurs during combat"""
    
    def __init__(self, name: str, description: str, effect_type: str, 
                 value: int, target: str = "both"):
        self.name = name
        self.description = description
        self.effect_type = effect_type  # "damage", "heal", "buff", "debuff"
        self.value = value
        self.target = target  # "player", "enemy", "both"
    
    def apply(self, player, enemy):
        """Apply the weather event effect and return a message"""
        message = f"\n🌩️ **{self.name}!** {self.description}\n"
        
        if self.effect_type == "damage":
            if self.target in ["player", "both"]:
                actual_damage = player.take_damage(self.value)
                message += f"   💥 You take {actual_damage} damage!\n"
            if self.target in ["enemy", "both"]:
                actual_damage = enemy.take_damage(self.value)
                message += f"   💥 {enemy.name} takes {actual_damage} damage!\n"
                
        elif self.effect_type == "heal":
            if self.target in ["player", "both"]:
                player.heal(self.value)
                message += f"   💚 You recover {self.value} HP!\n"
            if self.target in ["enemy", "both"]:
                enemy.heal(self.value)
                message += f"   💚 {enemy.name} recovers {self.value} HP!\n"
                
        elif self.effect_type == "buff":
            if self.target == "player":
                message += f"   ✨ Your power increases!\n"
            elif self.target == "enemy":
                message += f"   ⚠️ {enemy.name}'s power increases!\n"
                
        elif self.effect_type == "debuff":
            if self.target == "player":
                message += f"   💀 You feel weakened!\n"
            elif self.target == "enemy":
                message += f"   ✨ {enemy.name} is weakened!\n"
        
        return message


class Weather:
    """Weather effects and mechanics"""
    
    # Weather types with effects and events
    WEATHER_TYPES = {
        "sunny": {
            "name": "☀️ Sunny",
            "description": "Clear skies and bright sunshine",
            "combat_modifier": {"fire": 1.3, "ice": 0.8},
            "discovery_bonus": 0.1,
            "emoji": "☀️",
            "events": [
                WeatherEvent("Solar Flare", "A burst of sunlight energizes you!", "heal", 15, "player"),
                WeatherEvent("Blinding Light", "The enemy is blinded by the sun!", "debuff", 5, "enemy"),
            ]
        },
        "rainy": {
            "name": "🌧️ Rainy",
            "description": "Heavy rainfall soaks the ground",
            "combat_modifier": {"lightning": 1.4, "fire": 0.7},
            "visibility": -0.2,
            "emoji": "🌧️",
            "events": [
                WeatherEvent("Lightning Strike", "A bolt of lightning strikes down!", "damage", 25, "enemy"),
                WeatherEvent("Slippery Ground", "You slip on wet ground!", "damage", 10, "player"),
                WeatherEvent("Refreshing Rain", "The rain rejuvenates you!", "heal", 20, "player"),
            ]
        },
        "stormy": {
            "name": "⛈️ Stormy",
            "description": "Thunder roars and lightning strikes",
            "combat_modifier": {"lightning": 1.5, "wind": 1.3},
            "enemy_aggression": 1.2,
            "emoji": "⛈️",
            "events": [
                WeatherEvent("Thunder Crash", "Lightning strikes both fighters!", "damage", 30, "both"),
                WeatherEvent("Chain Lightning", "Lightning arcs through the air!", "damage", 35, "enemy"),
                WeatherEvent("Static Charge", "You're energized by electricity!", "buff", 10, "player"),
                WeatherEvent("Deafening Thunder", "The thunder stuns the enemy!", "debuff", 5, "enemy"),
            ]
        },
        "snowy": {
            "name": "❄️ Snowy",
            "description": "Snowflakes drift from gray clouds",
            "combat_modifier": {"ice": 1.4, "fire": 0.9},
            "movement_slow": 0.3,
            "emoji": "❄️",
            "events": [
                WeatherEvent("Blizzard Gust", "A freezing wind chills the enemy!", "damage", 20, "enemy"),
                WeatherEvent("Frostbite", "The cold saps your strength!", "damage", 15, "player"),
                WeatherEvent("Snow Healing", "The pristine snow soothes wounds!", "heal", 25, "player"),
                WeatherEvent("Ice Armor", "Snow forms a protective layer!", "buff", 10, "player"),
            ]
        },
        "foggy": {
            "name": "🌫️ Foggy",
            "description": "Thick fog obscures your vision",
            "combat_modifier": {"wind": 0.7},
            "mystery_bonus": 0.15,
            "visibility": -0.4,
            "emoji": "🌫️",
            "events": [
                WeatherEvent("Mist Confusion", "The enemy loses track of you!", "debuff", 10, "enemy"),
                WeatherEvent("Lost in Fog", "You stumble blindly!", "damage", 12, "player"),
                WeatherEvent("Shadow Cloak", "The fog conceals you!", "buff", 8, "player"),
                WeatherEvent("Ghostly Apparition", "A phantom emerges from the mist!", "damage", 18, "player"),
            ]
        },
        "windy": {
            "name": "🌬️ Windy",
            "description": "Strong winds blow across the land",
            "combat_modifier": {"wind": 1.5, "fire": 0.6},
            "discovery_bonus": 0.05,
            "emoji": "🌬️",
            "events": [
                WeatherEvent("Gale Force", "A powerful gust knocks the enemy back!", "damage", 22, "enemy"),
                WeatherEvent("Sandstorm", "Flying debris strikes you!", "damage", 16, "player"),
                WeatherEvent("Tailwind", "The wind boosts your speed!", "buff", 12, "player"),
                WeatherEvent("Dust Devil", "A whirlwind damages both fighters!", "damage", 18, "both"),
            ]
        },
        "cloudy": {
            "name": "☁️ Cloudy",
            "description": "Overcast skies dim the sunlight",
            "combat_modifier": {},
            "neutral": True,
            "emoji": "☁️",
            "events": []  # No special events for cloudy weather
        },
        "misty": {
            "name": "🌁 Misty",
            "description": "Light mist creates an ethereal atmosphere",
            "combat_modifier": {"magic": 1.2},
            "mystery_bonus": 0.2,
            "emoji": "🌁",
            "events": [
                WeatherEvent("Mystical Surge", "The mist empowers your magic!", "heal", 20, "player"),
                WeatherEvent("Phantom Touch", "A ghostly hand reaches out!", "damage", 15, "player"),
                WeatherEvent("Ethereal Veil", "The mist shields you!", "buff", 10, "player"),
            ]
        },
        "heat": {
            "name": "🔥 Scorching Heat",
            "description": "Oppressive heat radiates from above",
            "combat_modifier": {"fire": 1.4, "ice": 0.7},
            "emoji": "🔥",
            "events": [
                WeatherEvent("Heat Wave", "Intense heat drains everyone!", "damage", 20, "both"),
                WeatherEvent("Sunstroke", "The heat weakens you!", "damage", 25, "player"),
                WeatherEvent("Desert Rage", "The enemy thrives in heat!", "buff", 15, "enemy"),
                WeatherEvent("Mirage", "The heat creates illusions!", "debuff", 8, "both"),
            ]
        },
        "aurora": {
            "name": "🌌 Aurora",
            "description": "Magical lights dance across the sky (RARE!)",
            "combat_modifier": {"magic": 1.5, "all": 1.2},
            "legendary_chance": 0.5,
            "rare": True,
            "emoji": "🌌",
            "events": [
                WeatherEvent("Mystical Surge", "The aurora empowers your magic!", "heal", 30, "player"),
                WeatherEvent("Cosmic Ray", "Celestial energy strikes the enemy!", "damage", 40, "enemy"),
                WeatherEvent("Mana Overflow", "The aurora restores your energy!", "heal", 35, "player"),
                WeatherEvent("Arcane Backlash", "Magical energies go wild!", "damage", 15, "both"),
            ]
        },
        "eclipse": {
            "name": "🌑 Eclipse",
            "description": "The sun is blocked, darkness falls (RARE!)",
            "combat_modifier": {"dark": 1.6, "holy": 0.5},
            "rare_enemy_chance": 0.3,
            "rare": True,
            "emoji": "🌑",
            "events": [
                WeatherEvent("Shadow Strike", "Dark energy lashes out at the enemy!", "damage", 45, "enemy"),
                WeatherEvent("Void Touch", "Darkness drains your life force!", "damage", 30, "player"),
                WeatherEvent("Umbral Shield", "Shadows protect you!", "buff", 20, "player"),
                WeatherEvent("Eclipse Madness", "The darkness affects all!", "damage", 25, "both"),
                WeatherEvent("Vampiric Aura", "You drain life from the enemy!", "heal", 40, "player"),
            ]
        }
    }
    
    @staticmethod
    def get_random_weather(location_type="normal"):
        """Get random weather based on location"""
        if location_type == "crystal_cavern":
            # Crystal Cavern has unique weather
            rare_weathers = ["aurora", "misty", "foggy", "eclipse"]
            return random.choice(rare_weathers)
        
        # 5% chance for rare weather
        if random.random() < 0.05:
            return random.choice(["aurora", "eclipse", "heat"])
        
        # Normal weather distribution
        weights = {
            "sunny": 20,
            "cloudy": 25,
            "rainy": 15,
            "windy": 12,
            "foggy": 10,
            "stormy": 8,
            "snowy": 7,
            "misty": 3
        }
        
        weathers = list(weights.keys())
        weight_values = list(weights.values())
        
        return random.choices(weathers, weights=weight_values)[0]
    
    @staticmethod
    def get_weather_info(weather_type):
        """Get weather information"""
        return Weather.WEATHER_TYPES.get(weather_type, Weather.WEATHER_TYPES["cloudy"])
    
    @staticmethod
    def trigger_weather_event(weather_type):
        """30% chance to trigger a random weather event"""
        weather = Weather.get_weather_info(weather_type)
        events = weather.get("events", [])
        
        if events and random.random() < 0.3:  # 30% chance
            return random.choice(events)
        return None
    
    @staticmethod
    def apply_weather_to_damage(damage, attack_type, weather_type):
        """Apply weather modifier to damage"""
        weather = Weather.get_weather_info(weather_type)
        modifiers = weather.get("combat_modifier", {})
        
        # Check for specific attack type modifier
        if attack_type in modifiers:
            return int(damage * modifiers[attack_type])
        
        # Check for "all" modifier (rare weathers)
        if "all" in modifiers:
            return int(damage * modifiers["all"])
        
        return damage
    
    @staticmethod
    def get_weather_description(weather_type):
        """Get full weather description"""
        weather = Weather.get_weather_info(weather_type)
        
        desc = f"\n{'='*60}\n"
        desc += f"   {weather['emoji']} CURRENT WEATHER: {weather['name']} {weather['emoji']}\n"
        desc += f"{'='*60}\n"
        desc += f"{weather['description']}\n"
        
        # Add combat effects
        if weather.get("combat_modifier"):
            desc += f"\n⚔️ Combat Effects:\n"
            for element, mod in weather["combat_modifier"].items():
                if mod > 1:
                    desc += f"   • {element.title()} damage +{int((mod-1)*100)}%\n"
                elif mod < 1:
                    desc += f"   • {element.title()} damage {int((1-mod)*100)}%\n"
        
        # Add event warning
        if weather.get("events"):
            desc += f"\n⚠️ Weather events may occur in combat!\n"
        
        # Add special effects
        if weather.get("discovery_bonus", 0) > 0:
            desc += f"✨ Secret discovery chance increased!\n"
        
        if weather.get("mystery_bonus", 0) > 0:
            desc += f"🔮 Mysterious encounters more likely!\n"
        
        if weather.get("legendary_chance", 0) > 0:
            desc += f"🏆 LEGENDARY LOOT BOOSTED!\n"
        
        if weather.get("rare"):
            desc += f"\n⭐ RARE WEATHER EVENT! ⭐\n"
        
        desc += f"{'='*60}\n"
        
        return desc
    
    @staticmethod
    def get_weather_emoji(weather_type):
        """Get just the emoji for compact display"""
        weather = Weather.get_weather_info(weather_type)
        return weather.get("emoji", "☁️")
    
    @staticmethod
    def should_change_weather():
        """Determine if weather should change (20% chance)"""
        return random.random() < 0.2


class WeatherAbility:
    """Weather-based abilities for all classes"""
    
    WEATHER_ABILITIES = {
        # Available to all classes
        "Lightning Strike": {
            "type": "lightning",
            "damage_mult": 1.6,
            "mana_cost": 20,
            "description": "⚡ Call down lightning from the storm!",
            "weather_bonus": {"stormy": 1.3, "rainy": 1.2}
        },
        "Frost Blast": {
            "type": "ice",
            "damage_mult": 1.5,
            "mana_cost": 18,
            "description": "❄️ Freeze your enemies with icy power!",
            "weather_bonus": {"snowy": 1.3, "foggy": 1.1}
        },
        "Solar Beam": {
            "type": "fire",
            "damage_mult": 1.7,
            "mana_cost": 22,
            "description": "☀️ Harness the sun's burning energy!",
            "weather_bonus": {"sunny": 1.4}
        },
        "Wind Slash": {
            "type": "wind",
            "damage_mult": 1.4,
            "mana_cost": 15,
            "description": "🌬️ Cut through foes with razor wind!",
            "weather_bonus": {"windy": 1.3, "stormy": 1.2}
        },
        "Mist Step": {
            "type": "magic",
            "damage_mult": 1.3,
            "mana_cost": 12,
            "description": "🌁 Become one with the mist!",
            "weather_bonus": {"foggy": 1.4, "misty": 1.5}
        }
    }
    
    @staticmethod
    def get_weather_ability_damage(ability_name, base_damage, current_weather):
        """Calculate damage for weather ability"""
        ability = WeatherAbility.WEATHER_ABILITIES.get(ability_name)
        if not ability:
            return base_damage
        
        damage = int(base_damage * ability["damage_mult"])
        
        # Apply weather bonus
        weather_bonuses = ability.get("weather_bonus", {})
        if current_weather in weather_bonuses:
            damage = int(damage * weather_bonuses[current_weather])
        
        return damage


def get_weather_flavor_text(weather_type, action="explore"):
    """Get flavor text based on weather and action"""
    texts = {
        "sunny": {
            "explore": ["☀️ The bright sunshine reveals hidden paths...",
                       "☀️ Your spirits lift in the warm light!"],
            "combat": ["☀️ The sun glints off your weapon!",
                      "☀️ Solar energy empowers your attacks!"]
        },
        "rainy": {
            "explore": ["🌧️ Rain patters softly on the leaves...",
                       "🌧️ The storm may hide secrets..."],
            "combat": ["🌧️ Rain makes the ground treacherous!",
                      "🌧️ Lightning crackles in the clouds!"]
        },
        "stormy": {
            "explore": ["⛈️ Thunder rumbles ominously...",
                       "⛈️ The storm's fury is unleashed!"],
            "combat": ["⛈️ Lightning illuminates the battlefield!",
                      "⛈️ The tempest rages around you!"]
        },
        "snowy": {
            "explore": ["❄️ Snowflakes dance in the cold air...",
                       "❄️ Your breath mists in the freezing wind..."],
            "combat": ["❄️ The cold sharpens your focus!",
                      "❄️ Ice crystals form on your blade!"]
        },
        "foggy": {
            "explore": ["🌫️ Shapes move in the thick fog...",
                       "🌫️ The mist conceals mysteries..."],
            "combat": ["🌫️ The fog makes movements unpredictable!",
                      "🌫️ Vision is obscured by the mist!"]
        },
        "aurora": {
            "explore": ["🌌 Magical auroras shimmer overhead!",
                       "🌌 The lights guide you to wonders!"],
            "combat": ["🌌 Aurora energy surges through you!",
                      "🌌 Cosmic power flows freely!"]
        }
    }
    
    weather_texts = texts.get(weather_type, {}).get(action, ["The weather is calm."])
    return random.choice(weather_texts)
