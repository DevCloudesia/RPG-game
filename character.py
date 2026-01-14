"""Character class and player management"""
import random
from status_effects import StatusAilmentManager

class Character:
    """Player character class"""
    
    def __init__(self, name: str, char_class: str):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.experience = 0
        self.gold = 50
        
        # Stats based on class
        self.max_hp = 100
        self.hp = 100
        self.max_mana = 50
        self.mana = 50
        self.attack = 10
        self.defense = 5
        self.magic = 5
        
        # Equipment
        self.equipped_weapon = None
        self.equipped_armor = None
        self.inventory = []
        
        # Quests
        self.quests = []
        self.completed_quests = []
        
        # Abilities based on class
        self.abilities = []
        
        # Secret world discovered flag
        self.discovered_secret_world = False
        
        # Status ailments manager
        self.status_manager = StatusAilmentManager()
        
        # Apply class bonuses
        self._apply_class_bonuses()
        
    def _apply_class_bonuses(self):
        """Apply bonuses based on character class"""
        if self.char_class == "Warrior":
            self.max_hp = 150
            self.hp = 150
            self.attack = 15
            self.defense = 10
            self.abilities = ["Power Strike", "Shield Bash", "Whirlwind"]
            
        elif self.char_class == "Mage":
            self.max_hp = 80
            self.hp = 80
            self.max_mana = 100
            self.mana = 100
            self.magic = 20
            self.attack = 5
            self.abilities = ["Fireball", "Ice Blast", "Lightning Strike"]
            
        elif self.char_class == "Rogue":
            self.max_hp = 100
            self.hp = 100
            self.attack = 12
            self.defense = 8
            self.abilities = ["Backstab", "Poison Strike", "Shadow Step"]
            
        elif self.char_class == "Cleric":
            self.max_hp = 120
            self.hp = 120
            self.max_mana = 80
            self.mana = 80
            self.magic = 15
            self.defense = 8
            self.abilities = ["Heal", "Smite", "Divine Shield"]
    
    def add_experience(self, amount: int):
        """Add experience and handle leveling"""
        self.experience += amount
        exp_needed = self.level * 100
        
        if self.experience >= exp_needed:
            self.level_up()
            
    def level_up(self):
        """Level up the character"""
        self.level += 1
        self.experience = 0
        
        # Increase stats
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mana += 10
        self.mana = self.max_mana
        self.attack += 3
        self.defense += 2
        self.magic += 2
        
    def heal(self, amount: int):
        """Heal the character"""
        self.hp = min(self.hp + amount, self.max_hp)
        
    def restore_mana(self, amount: int):
        """Restore mana"""
        self.mana = min(self.mana + amount, self.max_mana)
    
    def take_damage(self, damage: int) -> int:
        """Take damage reduced by defense and status effects"""
        # Apply status effect damage modifiers
        damage = int(damage * self.status_manager.get_damage_taken_multiplier())
        
        actual_damage = max(1, damage - self.get_total_defense() // 3)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage
    
    def use_ability(self, ability_name: str, target):
        """Use a special ability"""
        import random
        
        if ability_name not in self.abilities:
            return False, f"{ability_name} is not available!", 0
        
        # Mana costs for abilities
        mana_cost = 15
        
        if self.mana < mana_cost:
            return False, f"⚠️ Not enough mana! Need {mana_cost}, have {self.mana}", 0
        
        # Use mana
        self.mana -= mana_cost
        
        # Calculate ability damage (stronger than normal attack)
        base_damage = self.get_total_attack() + self.magic
        damage_multiplier = 1.5  # Abilities do 1.5x damage
        
        # Add randomness
        damage = int(base_damage * damage_multiplier) + random.randint(-3, 5)
        
        # Apply damage to target
        if hasattr(target, 'take_damage'):
            actual_damage = target.take_damage(damage)
        else:
            actual_damage = damage
            target.hp = max(0, target.hp - actual_damage)
        
        message = f"⚡ {self.name} used {ability_name}! Dealt {actual_damage} damage!"
        
        return True, message, actual_damage
        
    def add_item(self, item):
        """Add item to inventory"""
        self.inventory.append(item)
        
    def remove_item(self, item):
        """Remove item from inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            
    def equip_weapon(self, weapon):
        """Equip a weapon"""
        self.equipped_weapon = weapon
        
    def equip_armor(self, armor):
        """Equip armor"""
        self.equipped_armor = armor
        
    def get_total_attack(self) -> int:
        """Get total attack including equipment and status effects"""
        total = self.attack
        if self.equipped_weapon:
            total += self.equipped_weapon.attack_bonus
        
        # Apply status effect modifiers
        modifier, bonus = self.status_manager.get_attack_modifier()
        total = int((total + bonus) * modifier)
        
        return total
        
    def get_total_defense(self) -> int:
        """Get total defense including equipment and status effects"""
        total = self.defense
        if self.equipped_armor:
            total += self.equipped_armor.defense_bonus
        
        # Apply status effect modifiers
        modifier, bonus = self.status_manager.get_defense_modifier()
        total = int((total + bonus) * modifier)
        
        return total
        
    def is_alive(self) -> bool:
        """Check if character is alive"""
        return self.hp > 0
        
    def display_stats(self) -> str:
        """Display character stats"""
        weapon_name = self.equipped_weapon.name if self.equipped_weapon else "None"
        armor_name = self.equipped_armor.name if self.equipped_armor else "None"
        
        stats = f"""
╔══════════════════════════════════════════════════════════╗
║  👤 {self.name:<48} ║
║  🎭 Class: {self.char_class:<43} ║
║  ⭐ Level: {self.level:<43} ║
╠══════════════════════════════════════════════════════════╣
║  ❤️  HP: {self.hp}/{self.max_hp:<44} ║
║  💙 Mana: {self.mana}/{self.max_mana:<41} ║
║  ⚔️  Attack: {self.get_total_attack():<42} ║
║  🛡️  Defense: {self.get_total_defense():<41} ║
║  ✨ Magic: {self.magic:<43} ║
╠══════════════════════════════════════════════════════════╣
║  🗡️  Weapon: {weapon_name:<42} ║
║  🛡️  Armor: {armor_name:<43} ║
║  💰 Gold: {self.gold:<45} ║
║  📊 EXP: {self.experience}/{self.level * 100:<42} ║
╚══════════════════════════════════════════════════════════╝
"""
        
        # Add status effects display
        status_display = self.status_manager.get_active_effects_display()
        if status_display:
            stats += f"\n{status_display}\n"
        
        return stats

