"""Combat system"""
import random
from typing import Tuple

class Combat:
    """Handles combat encounters"""
    
    @staticmethod
    def player_turn(player, enemy, action: str, ability_name: str = None) -> Tuple[str, bool]:
        """Execute player's turn in combat"""
        messages = []
        
        if action == "attack":
            # Check for critical hit (15% chance)
            is_critical = random.random() < 0.15
            
            # Normal attack with dramatic messages
            base_damage = player.attack + random.randint(-3, 3)
            
            if is_critical:
                base_damage = int(base_damage * 2.5)  # Critical does 2.5x damage!
                messages.append("╔═══════════════════════════════════╗")
                messages.append("│ 💥💥 CRITICAL HIT!!! 💥💥      │")
                messages.append("╚═══════════════════════════════════╝")
            
            actual_damage = enemy.take_damage(base_damage)
            
            # Dramatic hit messages based on damage
            if actual_damage > player.attack * 2:
                hit_msgs = [
                    f"⚡⚡ DEVASTATING BLOW! {actual_damage} damage!",
                    f"💥💥 CRUSHING STRIKE! {actual_damage} damage!",
                    f"🌟 LEGENDARY HIT! {actual_damage} damage!"
                ]
            elif actual_damage > player.attack:
                hit_msgs = [
                    f"⚔️ POWERFUL SLASH! {actual_damage} damage!",
                    f"💥 SOLID HIT! {actual_damage} damage!",
                    f"🗡️ STRONG STRIKE! {actual_damage} damage!"
                ]
            else:
                hit_msgs = [
                    f"⚔️ Quick attack! {actual_damage} damage!",
                    f"🗡️ Swift strike! {actual_damage} damage!",
                    f"💨 Grazing hit! {actual_damage} damage!"
                ]
            
            messages.append(random.choice(hit_msgs))
            
            # Visual HP bar
            hp_percent = (enemy.hp / enemy.max_hp) * 100
            hp_blocks = int(hp_percent / 10)
            hp_bar = "█" * hp_blocks + "░" * (10 - hp_blocks)
            messages.append(f"   🎯 {enemy.name}: [{hp_bar}] {enemy.hp}/{enemy.max_hp}")
            
        elif action == "ability" and ability_name:
            # Use special ability
            success, message, *damage_list = player.use_ability(ability_name, enemy)
            
            if not success:
                messages.append(f"❌ {message}")
                return "\n".join(messages), False
                
            messages.append(f"✨ {message}")
            
            if damage_list and damage_list[0] > 0:
                actual_damage = enemy.take_damage(damage_list[0])
                messages.append(f"   💥 CRITICAL! Dealt {actual_damage} damage!")
                messages.append(f"   🎯 {enemy.name} HP: {enemy.hp}/{enemy.max_hp}")
                
        elif action == "defend":
            # Defend (temporary defense boost)
            messages.append(f"🛡️  {player.name} raises their shield!")
            messages.append(f"   💪 Defense increased! Next attack will deal less damage!")
            return "\n".join(messages), True
            
        else:
            messages.append("❌ Invalid action!")
            return "\n".join(messages), False
        
        # Check if enemy is defeated
        if not enemy.is_alive():
            from random_events import RandomEvent
            messages.append("")
            messages.append("╔═══════════════════════════════════╗")
            messages.append("│    🎊 VICTORY! 🎊               │")
            messages.append(f"│  {enemy.name} defeated!        │")
            messages.append("╚═══════════════════════════════════╝")
            messages.append(RandomEvent.get_victory_quote())
            
        return "\n".join(messages), True
    
    @staticmethod
    def enemy_turn(enemy, player, defending: bool = False) -> str:
        """Execute enemy's turn in combat"""
        messages = []
        
        if not enemy.is_alive():
            return ""
        
        damage = enemy.attack_player()
        
        if defending:
            damage = max(1, damage // 2)
            messages.append(f"🛡️  BLOCKED! {player.name} reduces damage!")
        
        actual_damage = player.take_damage(damage)
        
        # Dramatic enemy attack messages with intensity based on damage
        if actual_damage > player.defense * 2:
            attack_msgs = [
                f"💀 DEVASTATING! {enemy.name} deals {actual_damage} damage!",
                f"⚡ BRUTAL STRIKE! {actual_damage} damage taken!",
                f"💥 MASSIVE HIT! {enemy.name} deals {actual_damage} damage!"
            ]
        else:
            attack_msgs = [
                f"👹 {enemy.name} strikes! {actual_damage} damage!",
                f"💀 {enemy.name} attacks for {actual_damage} damage!",
                f"⚔️ {enemy.name} hits for {actual_damage} damage!"
            ]
        messages.append(random.choice(attack_msgs))
        
        # Visual HP bar for player
        hp_percent = (player.hp / player.max_hp) * 100
        hp_blocks = int(hp_percent / 10)
        hp_bar = "█" * hp_blocks + "░" * (10 - hp_blocks)
        
        if hp_percent < 30:
            messages.append(f"   💔 [{hp_bar}] {player.hp}/{player.max_hp} ⚠️ CRITICAL!")
        elif hp_percent < 50:
            messages.append(f"   ❤️  [{hp_bar}] {player.hp}/{player.max_hp} ⚠️ LOW HP!")
        else:
            messages.append(f"   ❤️  [{hp_bar}] {player.hp}/{player.max_hp}")
        
        if player.hp <= 0:
            messages.append("")
            messages.append("╔═══════════════════════════════════╗")
            messages.append("│      💀 DEFEATED 💀              │")
            messages.append("│  You have fallen in battle...    │")
            messages.append("╚═══════════════════════════════════╝")
        elif player.hp < player.max_hp * 0.3:
            messages.append(f"   🚨 DANGER! Use a health potion NOW!")
            
        return "\n".join(messages)
    
    @staticmethod
    def combat_rewards(player, enemy) -> str:
        """Grant rewards after defeating an enemy"""
        messages = []
        from random_events import RandomEvent
        
        messages.append("")
        messages.append("╔══════════ REWARDS ══════════╗")
        
        # Experience with bonus chance
        exp_bonus = 1.0
        if random.random() < 0.2:  # 20% chance for bonus XP
            exp_bonus = 1.5
            messages.append("│ 🌟 BONUS XP! +50%!        │")
        
        total_exp = int(enemy.exp_reward * exp_bonus)
        player.add_experience(total_exp)
        messages.append(f"│ ✨ +{total_exp} Experience        │")
        
        # Gold with possible bonus
        gold_bonus = enemy.gold_reward
        if random.random() < 0.15:  # 15% chance for bonus gold
            gold_bonus = int(gold_bonus * 1.8)
            messages.append("│ 💎 EXTRA GOLD FOUND!      │")
        
        player.gold += gold_bonus
        messages.append(f"│ 💰 +{gold_bonus} Gold              │")
        messages.append("╚═══════════════════════════════╝")
        
        # Check for level up
        exp_needed = player.level * 100
        if player.experience >= exp_needed:
            player.level_up()
            messages.append("")
            messages.append("╔═══════════════════════════════════╗")
            messages.append(f"│    ⭐ LEVEL UP! ⭐               │")
            messages.append(f"│    Now Level {player.level}!               │")
            messages.append("╚═══════════════════════════════════╝")
            messages.append(RandomEvent.get_level_up_message(player.level))
            messages.append(f"📈 Stats: HP {player.max_hp} | ATK {player.attack} | DEF {player.defense}")
        
        # Loot drops
        loot = enemy.get_loot()
        if loot:
            from items import create_item
            messages.append("")
            messages.append("🎁 TREASURE FOUND!")
            for item_key in loot:
                item = create_item(item_key)
                if item:
                    player.add_item(item)
                    messages.append(f"   ✨ {item.name}")
        
        return "\n".join(messages)



