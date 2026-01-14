"""Status ailments and effects system"""
import random

class StatusEffect:
    """Base class for status effects"""
    
    def __init__(self, name, duration, effect_type):
        self.name = name
        self.duration = duration  # Number of turns remaining
        self.effect_type = effect_type  # 'buff' or 'debuff'
        self.icon = "✨"
        
    def apply_turn_effect(self, target):
        """Apply the effect at the start of each turn"""
        self.duration -= 1
        return None
    
    def is_expired(self):
        """Check if effect has expired"""
        return self.duration <= 0


class BurnEffect(StatusEffect):
    """Burning status - deals damage each turn"""
    
    def __init__(self, damage_per_turn=5, duration=3):
        super().__init__("Burning", duration, "debuff")
        self.damage_per_turn = damage_per_turn
        self.icon = "🔥"
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        target.hp = max(0, target.hp - self.damage_per_turn)
        return f"🔥 {target.name} burns for {self.damage_per_turn} damage! ({self.duration} turns left)"


class PoisonEffect(StatusEffect):
    """Poison status - deals increasing damage each turn"""
    
    def __init__(self, base_damage=3, duration=4):
        super().__init__("Poisoned", duration, "debuff")
        self.base_damage = base_damage
        self.turn_count = 0
        self.icon = "☠️"
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        self.turn_count += 1
        damage = self.base_damage * self.turn_count  # Increases each turn!
        target.hp = max(0, target.hp - damage)
        return f"☠️ {target.name} takes {damage} poison damage! ({self.duration} turns left)"


class FrozenEffect(StatusEffect):
    """Frozen status - cannot act, takes extra damage"""
    
    def __init__(self, duration=2):
        super().__init__("Frozen", duration, "debuff")
        self.icon = "❄️"
        self.damage_multiplier = 1.5
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        # 30% chance to break free each turn
        if random.random() < 0.3:
            self.duration = 0
            return f"❄️ {target.name} broke free from the ice!"
        return f"❄️ {target.name} is frozen solid! Cannot act! ({self.duration} turns left)"


class StunnedEffect(StatusEffect):
    """Stunned status - cannot act for 1 turn"""
    
    def __init__(self):
        super().__init__("Stunned", 1, "debuff")
        self.icon = "💫"
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"💫 {target.name} is stunned and cannot move!"


class BleedingEffect(StatusEffect):
    """Bleeding status - deals damage and reduces healing"""
    
    def __init__(self, damage_per_turn=4, duration=3):
        super().__init__("Bleeding", duration, "debuff")
        self.damage_per_turn = damage_per_turn
        self.icon = "🩸"
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        target.hp = max(0, target.hp - self.damage_per_turn)
        return f"🩸 {target.name} bleeds for {self.damage_per_turn} damage! ({self.duration} turns left)"


class ParalyzedEffect(StatusEffect):
    """Paralyzed status - 50% chance to miss attacks"""
    
    def __init__(self, duration=3):
        super().__init__("Paralyzed", duration, "debuff")
        self.icon = "⚡"
        self.miss_chance = 0.5
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"⚡ {target.name} is paralyzed! May miss attacks! ({self.duration} turns left)"


class ConfusedEffect(StatusEffect):
    """Confused status - may attack self"""
    
    def __init__(self, duration=2):
        super().__init__("Confused", duration, "debuff")
        self.icon = "😵"
        self.self_damage_chance = 0.4
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"😵 {target.name} is confused! ({self.duration} turns left)"


# === BENEFICIAL STATUS EFFECTS (BUFFS) ===

class RegenEffect(StatusEffect):
    """Regeneration - restores HP each turn"""
    
    def __init__(self, heal_per_turn=8, duration=4):
        super().__init__("Regenerating", duration, "buff")
        self.heal_per_turn = heal_per_turn
        self.icon = "💚"
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        old_hp = target.hp
        target.hp = min(target.max_hp, target.hp + self.heal_per_turn)
        healed = target.hp - old_hp
        return f"💚 {target.name} regenerates {healed} HP! ({self.duration} turns left)"


class StrengthBuffEffect(StatusEffect):
    """Strength buff - increased attack damage"""
    
    def __init__(self, attack_bonus=10, duration=3):
        super().__init__("Empowered", duration, "buff")
        self.attack_bonus = attack_bonus
        self.icon = "💪"
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"💪 {target.name} feels empowered! +{self.attack_bonus} attack! ({self.duration} turns left)"


class DefenseBuffEffect(StatusEffect):
    """Defense buff - increased defense"""
    
    def __init__(self, defense_bonus=8, duration=3):
        super().__init__("Shielded", duration, "buff")
        self.defense_bonus = defense_bonus
        self.icon = "🛡️"
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"🛡️ {target.name} is shielded! +{self.defense_bonus} defense! ({self.duration} turns left)"


class HasteEffect(StatusEffect):
    """Haste - chance for double attacks"""
    
    def __init__(self, duration=3):
        super().__init__("Hasted", duration, "buff")
        self.icon = "⚡"
        self.double_attack_chance = 0.5
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"⚡ {target.name} moves with incredible speed! ({self.duration} turns left)"


class BerserkEffect(StatusEffect):
    """Berserk - high attack but lower defense"""
    
    def __init__(self, duration=3):
        super().__init__("Berserk", duration, "buff")
        self.icon = "😡"
        self.attack_multiplier = 1.5
        self.defense_multiplier = 0.7
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"😡 {target.name} enters a berserker rage! ({self.duration} turns left)"


class InvulnerableEffect(StatusEffect):
    """Invulnerable - greatly reduced damage (rare buff)"""
    
    def __init__(self, duration=2):
        super().__init__("Invulnerable", duration, "buff")
        self.icon = "✨"
        self.damage_reduction = 0.8  # 80% damage reduction!
        
    def apply_turn_effect(self, target):
        self.duration -= 1
        return f"✨ {target.name} is nearly invulnerable! ({self.duration} turns left)"


class StatusAilmentManager:
    """Manages status effects for characters/enemies"""
    
    def __init__(self):
        self.active_effects = []
    
    def add_effect(self, effect):
        """Add a new status effect"""
        # Remove existing effect of same type
        self.active_effects = [e for e in self.active_effects if e.name != effect.name]
        self.active_effects.append(effect)
        return f"{effect.icon} {effect.name} applied!"
    
    def process_turn_effects(self, target):
        """Process all active effects at start of turn"""
        messages = []
        
        # Apply each effect
        for effect in self.active_effects[:]:  # Copy list to safely modify
            msg = effect.apply_turn_effect(target)
            if msg:
                messages.append(msg)
            
            # Remove expired effects
            if effect.is_expired():
                messages.append(f"   {effect.icon} {effect.name} wore off!")
                self.active_effects.remove(effect)
        
        return messages
    
    def get_active_effects_display(self):
        """Get string showing active effects"""
        if not self.active_effects:
            return ""
        
        effects_str = " | ".join([f"{e.icon} {e.name} ({e.duration})" for e in self.active_effects])
        return f"Status: {effects_str}"
    
    def has_effect(self, effect_name):
        """Check if target has specific effect"""
        return any(e.name == effect_name for e in self.active_effects)
    
    def get_effect(self, effect_name):
        """Get specific effect by name"""
        for effect in self.active_effects:
            if effect.name == effect_name:
                return effect
        return None
    
    def is_stunned(self):
        """Check if target is stunned/frozen and cannot act"""
        return self.has_effect("Stunned") or self.has_effect("Frozen")
    
    def get_attack_modifier(self):
        """Get combined attack modifier from all effects"""
        modifier = 1.0
        bonus = 0
        
        for effect in self.active_effects:
            if isinstance(effect, StrengthBuffEffect):
                bonus += effect.attack_bonus
            elif isinstance(effect, BerserkEffect):
                modifier *= effect.attack_multiplier
        
        return modifier, bonus
    
    def get_defense_modifier(self):
        """Get combined defense modifier from all effects"""
        modifier = 1.0
        bonus = 0
        
        for effect in self.active_effects:
            if isinstance(effect, DefenseBuffEffect):
                bonus += effect.defense_bonus
            elif isinstance(effect, BerserkEffect):
                modifier *= effect.defense_multiplier
            elif isinstance(effect, InvulnerableEffect):
                modifier *= (1 - effect.damage_reduction)
        
        return modifier, bonus
    
    def get_damage_taken_multiplier(self):
        """Get damage multiplier for incoming damage"""
        multiplier = 1.0
        
        for effect in self.active_effects:
            if isinstance(effect, FrozenEffect):
                multiplier *= effect.damage_multiplier
            elif isinstance(effect, InvulnerableEffect):
                multiplier *= (1 - effect.damage_reduction)
        
        return multiplier
    
    def check_paralysis_miss(self):
        """Check if paralyzed and should miss attack"""
        if self.has_effect("Paralyzed"):
            paralysis = self.get_effect("Paralyzed")
            if random.random() < paralysis.miss_chance:
                return True
        return False
    
    def check_confusion_self_damage(self, attacker):
        """Check if confused and attacks self"""
        if self.has_effect("Confused"):
            confusion = self.get_effect("Confused")
            if random.random() < confusion.self_damage_chance:
                return True
        return False
    
    def check_haste_double_attack(self):
        """Check if hasted and gets double attack"""
        if self.has_effect("Hasted"):
            haste = self.get_effect("Hasted")
            if random.random() < haste.double_attack_chance:
                return True
        return False
    
    def clear_all(self):
        """Remove all status effects"""
        self.active_effects.clear()


# Factory functions for easy status effect creation
def create_status_effect(effect_type, **kwargs):
    """Create a status effect by type"""
    effects = {
        "burn": BurnEffect,
        "poison": PoisonEffect,
        "frozen": FrozenEffect,
        "stunned": StunnedEffect,
        "bleeding": BleedingEffect,
        "paralyzed": ParalyzedEffect,
        "confused": ConfusedEffect,
        "regen": RegenEffect,
        "strength": StrengthBuffEffect,
        "defense": DefenseBuffEffect,
        "haste": HasteEffect,
        "berserk": BerserkEffect,
        "invulnerable": InvulnerableEffect
    }
    
    effect_class = effects.get(effect_type)
    if effect_class:
        return effect_class(**kwargs)
    return None


# Ability-based status effect infliction chances
STATUS_INFLICT_ABILITIES = {
    "Fireball": {"effect": "burn", "chance": 0.3},
    "Ice Blast": {"effect": "frozen", "chance": 0.25},
    "Lightning Strike": {"effect": "paralyzed", "chance": 0.35},
    "Poison Strike": {"effect": "poison", "chance": 0.5},
    "Backstab": {"effect": "bleeding", "chance": 0.4},
    "Shield Bash": {"effect": "stunned", "chance": 0.4},
    "Heal": {"effect": "regen", "chance": 1.0, "self": True},
    "Divine Shield": {"effect": "defense", "chance": 1.0, "self": True},
    "Berserker Rage": {"effect": "berserk", "chance": 1.0, "self": True},
}

