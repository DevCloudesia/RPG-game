"""Enemy classes and definitions"""
import random
from status_effects import StatusAilmentManager

class Enemy:
    """Base enemy class"""
    def __init__(self, name: str, level: int, hp: int, attack: int, defense: int, 
                 exp_reward: int, gold_reward: int, loot_table: dict = None):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        self.loot_table = loot_table or {}
        self.status_manager = StatusAilmentManager()  # Add status effects to enemies
        
    def take_damage(self, damage: int) -> int:
        """Take damage reduced by defense"""
        actual_damage = max(1, damage - self.defense // 3)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage
    
    def attack_player(self) -> int:
        """Calculate attack damage with some randomness"""
        return self.attack + random.randint(-2, 2)
    
    def is_alive(self) -> bool:
        """Check if enemy is still alive"""
        return self.hp > 0
    
    def get_loot(self):
        """Randomly determine loot drops"""
        drops = []
        for item_key, drop_chance in self.loot_table.items():
            if random.random() < drop_chance:
                drops.append(item_key)
        return drops

    # Enemy templates
def create_enemy(enemy_type: str, level_modifier: int = 0):
    """Factory function to create enemies with level scaling"""
    
    enemies = {
        "goblin": {
            "name": "Goblin",
            "hp": 80,  # Increased from 40
            "attack": 18,  # Increased from 8
            "defense": 8,  # Increased from 3
            "exp": 20,
            "gold": 10,
            "loot": {"health_potion": 0.3, "rusty_sword": 0.1}
        },
        "wolf": {
            "name": "Dire Wolf",
            "hp": 100,  # Increased from 50
            "attack": 25,  # Increased from 12
            "defense": 10,  # Increased from 4
            "exp": 30,
            "gold": 8,
            "loot": {"health_potion": 0.25}
        },
        "skeleton": {
            "name": "Skeleton Warrior",
            "hp": 120,  # Increased from 60
            "attack": 30,  # Increased from 15
            "defense": 15,  # Increased from 6
            "exp": 40,
            "gold": 15,
            "loot": {"health_potion": 0.3, "mana_potion": 0.2, "iron_sword": 0.15}
        },
        "orc": {
            "name": "Orc Raider",
            "hp": 160,  # Increased from 80
            "attack": 35,  # Increased from 18
            "defense": 18,  # Increased from 8
            "exp": 50,
            "gold": 25,
            "loot": {"health_potion": 0.4, "leather_armor": 0.2, "iron_sword": 0.2}
        },
        "dark_mage": {
            "name": "Dark Mage",
            "hp": 140,  # Increased from 70
            "attack": 45,  # Increased from 25
            "defense": 12,  # Increased from 5
            "exp": 60,
            "gold": 40,
            "loot": {"mana_potion": 0.5, "super_health_potion": 0.3, "mage_staff": 0.15}
        },
        "troll": {
            "name": "Cave Troll",
            "hp": 240,  # Increased from 120
            "attack": 42,  # Increased from 22
            "defense": 25,  # Increased from 12
            "exp": 80,
            "gold": 50,
            "loot": {"super_health_potion": 0.4, "chainmail": 0.2, "steel_sword": 0.15}
        },
        "wraith": {
            "name": "Shadow Wraith",
            "hp": 180,  # Increased from 90
            "attack": 50,  # Increased from 28
            "defense": 16,  # Increased from 7
            "exp": 90,
            "gold": 60,
            "loot": {"super_mana_potion": 0.4, "shadow_daggers": 0.2, "arcane_staff": 0.15}
        },
        "dragon_whelp": {
            "name": "Dragon Whelp",
            "hp": 300,  # Increased from 150
            "attack": 55,  # Increased from 30
            "defense": 30,  # Increased from 15
            "exp": 120,
            "gold": 100,
            "loot": {"super_health_potion": 0.6, "super_mana_potion": 0.5, "steel_sword": 0.3}
        },
        "vampire": {
            "name": "Vampire Lord",
            "hp": 400,  # Increased from 200
            "attack": 65,  # Increased from 35
            "defense": 35,  # Increased from 18
            "exp": 150,
            "gold": 150,
            "loot": {"super_health_potion": 0.7, "super_mana_potion": 0.7, "plate_armor": 0.3}
        },
        "demon": {
            "name": "Demon",
            "hp": 360,  # Increased from 180
            "attack": 70,  # Increased from 40
            "defense": 32,  # Increased from 16
            "exp": 160,
            "gold": 120,
            "loot": {"super_health_potion": 0.6, "super_mana_potion": 0.6, "divine_hammer": 0.2}
        },
        
        # CRYSTAL CAVERN LEGENDARY ENEMIES - EXTREMELY POWERFUL
        "fire_elemental": {
            "name": "🔥 Fire Elemental",
            "hp": 500,  # Increased from 250
            "attack": 80,  # Increased from 45
            "defense": 40,  # Increased from 20
            "exp": 300,
            "gold": 500,
            "loot": {
                "elixir": 0.3,
                "excalibur": 0.15, 
                "mjolnir": 0.15,
                "celestial_armor": 0.15,
                "giant_potion": 0.4,
                "super_health_potion": 0.8,
                "super_mana_potion": 0.8
            }
        },
        "ice_golem": {
            "name": "❄️ Ice Golem",
            "hp": 600,  # Increased from 300
            "attack": 75,  # Increased from 42
            "defense": 55,  # Increased from 28
            "exp": 350,
            "gold": 600,
            "loot": {
                "elixir": 0.3,
                "shadowfang": 0.15,
                "godbow": 0.15,
                "void_armor": 0.15,
                "phoenix_plate": 0.15,
                "super_health_potion": 0.9,
                "super_mana_potion": 0.9
            }
        },
        "storm_spirit": {
            "name": "⚡ Storm Spirit",
            "hp": 440,  # Increased from 220
            "attack": 95,  # Increased from 55
            "defense": 35,  # Increased from 18
            "exp": 400,
            "gold": 700,
            "loot": {
                "elixir": 0.4,
                "staff_of_cosmos": 0.2,
                "infinity_blade": 0.15,
                "crystal_guardian": 0.15,
                "time_weaver": 0.15,
                "super_health_potion": 1.0,
                "super_mana_potion": 1.0
            }
        },
        "crystal_titan": {
            "name": "💎 Crystal Titan",
            "hp": 1000,  # Increased from 500
            "attack": 110,  # Increased from 60
            "defense": 80,  # Increased from 40
            "exp": 800,
            "gold": 2000,
            "loot": {
                "elixir": 0.7,
                "omni_weapon": 0.25,
                "cosmic_armor": 0.25,
                "infinity_blade": 0.3,
                "crystal_guardian": 0.3,
                "super_health_potion": 1.0,
                "super_mana_potion": 1.0,
                "giant_potion": 1.0
            }
        },
    }
    
    # Boss enemies - SIGNIFICANTLY STRONGER
    bosses = {
        "ancient_dragon": {
            "name": "Ancient Dragon",
            "hp": 800,  # Increased from 400
            "attack": 90,  # Increased from 50
            "defense": 60,  # Increased from 30
            "exp": 500,
            "gold": 1000,
            "loot": {"legendary_blade": 0.8, "dragon_armor": 0.8, "super_health_potion": 1.0, "super_mana_potion": 1.0}
        },
        "dark_lord": {
            "name": "Dark Lord Malzahar",
            "hp": 1000,  # Increased from 500
            "attack": 100,  # Increased from 60
            "defense": 70,  # Increased from 35
            "exp": 1000,
            "gold": 2000,
            "loot": {"staff_of_power": 1.0, "dragon_armor": 1.0, "super_health_potion": 1.0, "super_mana_potion": 1.0}
        }
    }
    
    all_enemies = {**enemies, **bosses}
    
    if enemy_type not in all_enemies:
        enemy_type = "goblin"
    
    template = all_enemies[enemy_type]
    level = 1 + level_modifier
    
    # Scale stats with level - MORE AGGRESSIVE SCALING
    scaled_hp = int(template["hp"] * (1 + level_modifier * 0.3))  # Increased from 0.2
    scaled_attack = int(template["attack"] * (1 + level_modifier * 0.25))  # Increased from 0.15
    scaled_defense = int(template["defense"] * (1 + level_modifier * 0.25))  # Increased from 0.15
    scaled_exp = int(template["exp"] * (1 + level_modifier * 0.3))
    scaled_gold = int(template["gold"] * (1 + level_modifier * 0.25))
    
    return Enemy(
        name=f"{template['name']} (Lv.{level})",
        level=level,
        hp=scaled_hp,
        attack=scaled_attack,
        defense=scaled_defense,
        exp_reward=scaled_exp,
        gold_reward=scaled_gold,
        loot_table=template["loot"]
    )





