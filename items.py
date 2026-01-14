"""Items, weapons, armor, and inventory management"""

class Item:
    """Base item class"""
    def __init__(self, name: str, description: str, value: int):
        self.name = name
        self.description = description
        self.value = value
        
class Consumable(Item):
    """Consumable items like potions"""
    def __init__(self, name: str, description: str, value: int, effect_type: str, effect_amount: int):
        super().__init__(name, description, value)
        self.effect_type = effect_type
        self.effect_amount = effect_amount
        
    def use(self, character):
        """Use the consumable on a character"""
        if self.effect_type == "heal":
            character.heal(self.effect_amount)
            return f"✨ {character.name} restored {self.effect_amount} HP!"
        elif self.effect_type == "mana":
            character.restore_mana(self.effect_amount)
            return f"💙 {character.name} restored {self.effect_amount} mana!"
        elif self.effect_type == "full_heal":
            character.heal(character.max_hp)
            character.restore_mana(character.max_mana)
            return f"💫 {character.name} is fully restored! HP and Mana at maximum!"
        elif self.effect_type == "buff_attack":
            return f"💪 {character.name} feels incredible strength! Attack doubled!"
        return "Used item."

class Weapon(Item):
    """Weapon items"""
    def __init__(self, name: str, description: str, value: int, attack_bonus: int):
        super().__init__(name, description, value)
        self.attack_bonus = attack_bonus
        
class Armor(Item):
    """Armor items"""
    def __init__(self, name: str, description: str, value: int, defense_bonus: int):
        super().__init__(name, description, value)
        self.defense_bonus = defense_bonus

class KeyItem(Item):
    """Special quest items"""
    def __init__(self, name: str, description: str):
        super().__init__(name, description, 0)

# Define available items
ITEMS = {
    # Consumables
    "health_potion": Consumable("Health Potion", "Restores 50 HP", 25, "heal", 50),
    "super_health_potion": Consumable("Super Health Potion", "Restores 100 HP", 50, "heal", 100),
    "mana_potion": Consumable("Mana Potion", "Restores 40 mana", 30, "mana", 40),
    "super_mana_potion": Consumable("Super Mana Potion", "Restores 80 mana", 60, "mana", 80),
    
    # Weapons
    "rusty_sword": Weapon("Rusty Sword", "An old, worn sword", 10, 5),
    "iron_sword": Weapon("Iron Sword", "A sturdy iron blade", 50, 10),
    "steel_sword": Weapon("Steel Sword", "A well-crafted steel sword", 150, 18),
    "legendary_blade": Weapon("Dragonbane", "A legendary sword forged from dragon scales", 1000, 35),
    
    "wooden_staff": Weapon("Wooden Staff", "A simple wooden staff", 15, 3),
    "mage_staff": Weapon("Mage Staff", "A staff imbued with magical energy", 80, 8),
    "arcane_staff": Weapon("Arcane Staff", "Crackles with arcane power", 200, 15),
    "staff_of_power": Weapon("Staff of Eternity", "Contains the essence of ancient magic", 1200, 40),
    
    "dagger": Weapon("Dagger", "A small, sharp blade", 20, 7),
    "poisoned_dagger": Weapon("Venomblade", "Drips with deadly poison", 100, 15),
    "shadow_daggers": Weapon("Shadow Daggers", "Twin blades that shimmer with darkness", 250, 25),
    
    "wooden_mace": Weapon("Wooden Mace", "A simple club", 12, 6),
    "holy_mace": Weapon("Holy Mace", "Blessed by divine power", 90, 12),
    "divine_hammer": Weapon("Hammer of Justice", "Radiates holy light", 300, 28),
    
    # Armor
    "cloth_robe": Armor("Cloth Robe", "Basic cloth protection", 15, 3),
    "leather_armor": Armor("Leather Armor", "Light leather protection", 50, 8),
    "chainmail": Armor("Chainmail Armor", "Interlocking metal rings", 150, 15),
    "plate_armor": Armor("Plate Armor", "Heavy steel plating", 300, 25),
    "dragon_armor": Armor("Dragon Scale Armor", "Armor crafted from dragon scales", 1500, 45),
    
    # Key Items
    "ancient_key": KeyItem("Ancient Key", "A mysterious key covered in runes"),
    "dragon_egg": KeyItem("Dragon Egg", "A shimmering dragon egg, warm to the touch"),
    "royal_seal": KeyItem("Royal Seal", "The seal of the lost kingdom"),
    
    # LEGENDARY WEAPONS - Crystal Cavern Treasures
    "excalibur": Weapon("⚔️ Excalibur", "The legendary sword of kings! Gleams with holy light!", 5000, 50),
    "mjolnir": Weapon("🔨 Mjolnir", "The hammer of thunder gods! Crackles with lightning!", 5500, 55),
    "shadowfang": Weapon("🗡️ Shadowfang", "Twin blades forged in eternal darkness!", 4800, 48),
    "staff_of_cosmos": Weapon("🌌 Staff of Cosmos", "Contains the power of the universe itself!", 6000, 60),
    "godbow": Weapon("🏹 Godbow", "Never misses! Arrows pierce through reality!", 5200, 52),
    "infinity_blade": Weapon("✨ Infinity Blade", "Exists in all timelines at once!", 7000, 70),
    
    # LEGENDARY ARMOR - Crystal Cavern Treasures
    "celestial_armor": Armor("🌟 Celestial Armor", "Blessed by the gods of heaven!", 6000, 60),
    "void_armor": Armor("🌑 Void Armor", "Absorbs all damage into nothingness!", 6500, 65),
    "phoenix_plate": Armor("🔥 Phoenix Plate", "Resurrects you from death (once)!", 7000, 70),
    "crystal_guardian": Armor("💎 Crystal Guardian", "Formed from pure diamond! Unbreakable!", 8000, 80),
    "time_weaver": Armor("⏰ Time Weaver", "Slows time around you!", 7500, 75),
    
    # SUPER LEGENDARY - Ultra Rare
    "omni_weapon": Weapon("🌈 Omniblade", "ALL ELEMENTS! Changes form at will! GOD TIER!", 10000, 100),
    "cosmic_armor": Armor("🌌 Cosmic Armor", "Made from stardust! INVINCIBLE!", 12000, 120),
    
    # SPECIAL POTIONS
    "elixir": Consumable("💫 Elixir of Life", "Fully restores HP and Mana!", 200, "full_heal", 9999),
    "giant_potion": Consumable("🧪 Giant's Strength", "Doubles attack for one battle!", 150, "buff_attack", 50),
}

def create_item(item_key: str):
    """Factory function to create item instances"""
    if item_key in ITEMS:
        item_template = ITEMS[item_key]
        if isinstance(item_template, Consumable):
            return Consumable(
                item_template.name,
                item_template.description,
                item_template.value,
                item_template.effect_type,
                item_template.effect_amount
            )
        elif isinstance(item_template, Weapon):
            return Weapon(
                item_template.name,
                item_template.description,
                item_template.value,
                item_template.attack_bonus
            )
        elif isinstance(item_template, Armor):
            return Armor(
                item_template.name,
                item_template.description,
                item_template.value,
                item_template.defense_bonus
            )
        elif isinstance(item_template, KeyItem):
            return KeyItem(
                item_template.name,
                item_template.description
            )
    return None





