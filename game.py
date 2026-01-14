"""Main game engine and game loop"""
import random
import pickle
import os
from character import Character
from world import World
from combat import Combat
from items import create_item, Consumable, Weapon, Armor
from quests import create_quest
from enemy import create_enemy
from weather import Weather, get_weather_flavor_text

class Game:
    """Main game class that manages the game state"""
    
    def __init__(self):
        self.player = None
        self.world = World()
        self.current_location = None
        self.combat_active = False
        self.current_enemy = None
        self.game_over = False
        self.enemy_kill_count = 0
        
    def start_new_game(self):
        """Start a new game"""
        print("\n" + "="*60)
        print(" "*15 + "⚔️  REALM OF LEGENDS  ⚔️")
        print("="*60)
        print("\nWelcome, brave adventurer!")
        print("\nLong ago, the realm was peaceful. But the Dark Lord has")
        print("risen, spreading darkness across the land. Only a hero")
        print("can stop him and restore peace to the kingdom...")
        print("\n" + "="*60)
        
        # Character creation
        name = input("\nWhat is your name, hero? ").strip()
        if not name:
            name = "Hero"
            
        print("\nChoose your class:")
        print("1. Warrior - High HP and physical damage")
        print("2. Mage - Powerful magical attacks")
        print("3. Rogue - Quick strikes and stealth")
        print("4. Cleric - Healing and holy magic")
        
        class_choice = input("\nEnter your choice (1-4): ").strip()
        class_map = {
            "1": "Warrior",
            "2": "Mage",
            "3": "Rogue",
            "4": "Cleric"
        }
        
        char_class = class_map.get(class_choice, "Warrior")
        
        # Create player character
        self.player = Character(name, char_class)
        self.current_location = self.world.get_starting_location()
        
        # Give starting items
        self.player.add_item(create_item("health_potion"))
        self.player.add_item(create_item("health_potion"))
        self.player.add_item(create_item("mana_potion"))
        
        # Give starting quest
        tutorial_quest = create_quest("tutorial")
        self.player.quests.append(tutorial_quest)
        
        print(f"\n✨ Welcome, {name} the {char_class}!")
        print(self.player.display_stats())
        print("\n📜 Quest Received: First Steps")
        print("   Defeat 3 enemies to prove your worth.\n")
        
        input("Press Enter to begin your adventure...")
        
    def show_location(self):
        """Display current location"""
        location = self.world.get_location(self.current_location)
        
        # Update weather sometimes
        if location.update_weather():
            print("\n🌤️ The weather is changing...")
        
        print("\n" + "="*60)
        print(f"📍 {location.name}")
        print("="*60)
        print(location.description)
        
        # Show current weather
        print(location.get_weather_description())
        
    def main_menu(self):
        """Display main menu and handle player input"""
        location = self.world.get_location(self.current_location)
        
        print("\n" + "-"*60)
        print("What would you like to do?")
        print("-"*60)
        print("1. Explore (Look for enemies)")
        print("2. Travel to another location")
        print("3. View Character Stats")
        print("4. Inventory")
        print("5. Quests")
        
        if location.shop:
            print("6. Visit Shop")
            
        print("S. Save Game")
        print("Q. Quit")
        print("-"*60)
        
        choice = input("\nYour choice: ").strip().lower()
        return choice
    
    def explore(self):
        """Explore current location and potentially encounter enemies"""
        location = self.world.get_location(self.current_location)
        
        # Show weather flavor text
        print(f"\n{get_weather_flavor_text(location.current_weather, 'explore')}")
        
        # Weather bonus for discovery
        weather_info = Weather.get_weather_info(location.current_weather)
        discovery_bonus = weather_info.get("discovery_bonus", 0)
        
        # SECRET WORLD DISCOVERY! (5% base chance + weather bonus)
        if not self.player.discovered_secret_world and self.current_location in ["dark_forest", "mountain_peak", "ancient_ruins"]:
            discovery_chance = 0.05 + discovery_bonus
            if random.random() < discovery_chance:
                self.discover_secret_world()
                return
        
        if not location.enemy_types:
            print("\n✨ This area is peaceful. No enemies to fight here.")
            input("\nPress Enter to continue...")
            return
            
        print("\n🔍 You search the area...")
        
        # Random chance of finding legendary loot in Crystal Cavern
        if self.current_location == "crystal_cavern":
            if random.random() < 0.3:  # 30% chance of treasure!
                self.find_crystal_treasure()
                return
        
        # Random chance of encounter
        if random.random() < 0.7:  # 70% chance
            enemy = location.get_random_enemy(self.player.level)
            print(f"\n⚠️  A wild {enemy.name} appears!")
            self.start_combat(enemy)
        else:
            print("\n✨ You don't find any enemies this time.")
            input("\nPress Enter to continue...")
    
    def start_combat(self, enemy):
        """Start a combat encounter"""
        self.combat_active = True
        self.current_enemy = enemy
        
        print("\n" + "="*60)
        print(f"⚔️  COMBAT: {self.player.name} vs {enemy.name}")
        print("="*60)
        
        while self.combat_active:
            self.combat_turn()
            
    def combat_turn(self):
        """Handle a single combat turn"""
        enemy = self.current_enemy
        
        # Display status
        print(f"\n{self.player.name}: HP {self.player.hp}/{self.player.max_hp} | Mana {self.player.mana}/{self.player.max_mana}")
        print(f"{enemy.name}: HP {enemy.hp}/{enemy.max_hp}")
        
        print("\n1. Attack")
        print("2. Use Ability")
        print("3. Use Item")
        print("4. Defend")
        print("5. Run Away")
        
        choice = input("\nYour action: ").strip()
        
        defending = False
        
        if choice == "1":
            # Attack
            message, success = Combat.player_turn(self.player, enemy, "attack")
            print(f"\n{message}")
            
        elif choice == "2":
            # Use ability
            print("\nYour Abilities:")
            for i, ability in enumerate(self.player.abilities, 1):
                print(f"{i}. {ability}")
            print("0. Back")
            
            ability_choice = input("\nChoose ability: ").strip()
            
            if ability_choice == "0":
                return
                
            try:
                ability_index = int(ability_choice) - 1
                if 0 <= ability_index < len(self.player.abilities):
                    ability = self.player.abilities[ability_index]
                    message, success = Combat.player_turn(self.player, enemy, "ability", ability)
                    print(f"\n{message}")
                else:
                    print("\n❌ Invalid ability!")
                    return
            except ValueError:
                print("\n❌ Invalid input!")
                return
                
        elif choice == "3":
            # Use item
            self.use_item_in_combat()
            return
            
        elif choice == "4":
            # Defend
            message, success = Combat.player_turn(self.player, enemy, "defend")
            print(f"\n{message}")
            defending = True
            
        elif choice == "5":
            # Run away
            if random.random() < 0.5:  # 50% chance
                print("\n🏃 You successfully escaped!")
                self.combat_active = False
                self.current_enemy = None
                input("\nPress Enter to continue...")
                return
            else:
                print("\n❌ You couldn't escape!")
                
        else:
            print("\n❌ Invalid action!")
            return
        
        # Check if enemy is defeated
        if not enemy.is_alive():
            self.end_combat(victory=True)
            return
            
        # Enemy turn
        enemy_message = Combat.enemy_turn(enemy, self.player, defending)
        print(f"\n{enemy_message}")
        
        # Check if player is defeated
        if self.player.hp <= 0:
            self.end_combat(victory=False)
            return
            
        input("\nPress Enter to continue...")
    
    def use_item_in_combat(self):
        """Use an item during combat"""
        consumables = [item for item in self.player.inventory if isinstance(item, Consumable)]
        
        if not consumables:
            print("\n❌ No usable items!")
            input("\nPress Enter to continue...")
            return
            
        print("\nYour Items:")
        for i, item in enumerate(consumables, 1):
            print(f"{i}. {item.name} - {item.description}")
        print("0. Back")
        
        choice = input("\nChoose item: ").strip()
        
        if choice == "0":
            return
            
        try:
            item_index = int(choice) - 1
            if 0 <= item_index < len(consumables):
                item = consumables[item_index]
                message = item.use(self.player)
                self.player.remove_item(item)
                print(f"\n{message}")
            else:
                print("\n❌ Invalid item!")
        except ValueError:
            print("\n❌ Invalid input!")
            
        input("\nPress Enter to continue...")
    
    def end_combat(self, victory: bool):
        """End combat encounter"""
        self.combat_active = False
        
        if victory:
            print("\n" + "="*60)
            print("🎉 VICTORY!")
            print("="*60)
            
            # Grant rewards
            rewards_message = Combat.combat_rewards(self.player, self.current_enemy)
            print(rewards_message)
            
            # Update quest progress
            self.enemy_kill_count += 1
            self.update_quest_progress("defeat_3_enemies")
            self.update_quest_progress("defeat_5_bandits")
            self.update_quest_progress("defeat_forest_enemy")
            self.update_quest_progress("defeat_egg_guardian")
            
        else:
            print("\n" + "="*60)
            print("💀 DEFEAT")
            print("="*60)
            print("\nYou have been defeated...")
            
            # 25% chance for divine resurrection!
            if random.random() < 0.25:
                restore_amount = int(self.player.max_hp * 0.75)  # Restore 75% HP
                self.player.hp = restore_amount
                print("\n" + "="*60)
                print("✨ DIVINE RESURRECTION! ✨")
                print("="*60)
                print(f"The gods have blessed you with a second chance!")
                print(f"💚 Restored {restore_amount} HP!")
                print(f"You rise again to fight another day!")
                print("="*60)
            else:
                print("Your adventure ends here.")
                self.game_over = True
            
        self.current_enemy = None
        input("\nPress Enter to continue...")
    
    def travel(self):
        """Travel to a new location"""
        location = self.world.get_location(self.current_location)
        
        print("\n" + "-"*60)
        print("Where would you like to travel?")
        print("-"*60)
        
        # Build list of available destinations
        destinations = list(location.connections)
        
        # Add Crystal Cavern if discovered and in certain locations
        if self.player.discovered_secret_world and self.current_location in ["dark_forest", "mountain_peak", "ancient_ruins"]:
            if "crystal_cavern" not in destinations:
                destinations.append("crystal_cavern")
        
        # Also allow travel from Crystal Cavern back to connected areas
        if self.current_location == "crystal_cavern":
            destinations = ["dark_forest", "mountain_peak", "ancient_ruins"]
        
        for i, conn in enumerate(destinations, 1):
            dest = self.world.get_location(conn)
            if conn == "crystal_cavern":
                print(f"{i}. {dest.name} ✨ (SECRET WORLD)")
            else:
                print(f"{i}. {dest.name}")
        print("0. Stay here")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "0":
            return
            
        try:
            conn_index = int(choice) - 1
            if 0 <= conn_index < len(destinations):
                self.current_location = destinations[conn_index]
                new_location = self.world.get_location(self.current_location)
                
                if self.current_location == "crystal_cavern":
                    print("\n✨ Stepping through the portal...")
                    print("💎 You enter the Crystal Cavern of Legends!")
                    print("🌈 The crystals sing their ancient song!")
                else:
                    print(f"\n🚶 Traveling to {new_location.name}...")
                
                # Update quest progress
                self.update_quest_progress(f"visit_{self.current_location}")
                
                input("\nPress Enter to continue...")
            else:
                print("\n❌ Invalid choice!")
                input("\nPress Enter to continue...")
        except ValueError:
            print("\n❌ Invalid input!")
            input("\nPress Enter to continue...")
    
    def show_inventory(self):
        """Display and manage inventory"""
        while True:
            print("\n" + "="*60)
            print("🎒 INVENTORY")
            print("="*60)
            print(f"Gold: {self.player.gold}")
            print()
            
            if not self.player.inventory:
                print("Your inventory is empty.")
            else:
                for i, item in enumerate(self.player.inventory, 1):
                    if isinstance(item, Weapon):
                        equipped = " (Equipped)" if item == self.player.equipped_weapon else ""
                        print(f"{i}. {item.name} - +{item.attack_bonus} Attack{equipped}")
                    elif isinstance(item, Armor):
                        equipped = " (Equipped)" if item == self.player.equipped_armor else ""
                        print(f"{i}. {item.name} - +{item.defense_bonus} Defense{equipped}")
                    elif isinstance(item, Consumable):
                        print(f"{i}. {item.name} - {item.description}")
                    else:
                        print(f"{i}. {item.name} - {item.description}")
            
            print("\nOptions:")
            print("1. Use/Equip Item")
            print("2. Drop Item")
            print("0. Back")
            
            choice = input("\nYour choice: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self.use_equip_item()
            elif choice == "2":
                self.drop_item()
    
    def use_equip_item(self):
        """Use or equip an item"""
        if not self.player.inventory:
            return
            
        item_num = input("\nEnter item number: ").strip()
        
        try:
            item_index = int(item_num) - 1
            if 0 <= item_index < len(self.player.inventory):
                item = self.player.inventory[item_index]
                
                if isinstance(item, Consumable):
                    message = item.use(self.player)
                    self.player.remove_item(item)
                    print(f"\n{message}")
                elif isinstance(item, Weapon):
                    self.player.equip_weapon(item)
                    print(f"\n⚔️  Equipped {item.name}!")
                elif isinstance(item, Armor):
                    self.player.equip_armor(item)
                    print(f"\n🛡️  Equipped {item.name}!")
                else:
                    print(f"\n{item.name}: {item.description}")
                    
                input("\nPress Enter to continue...")
            else:
                print("\n❌ Invalid item number!")
        except ValueError:
            print("\n❌ Invalid input!")
    
    def drop_item(self):
        """Drop an item from inventory"""
        if not self.player.inventory:
            return
            
        item_num = input("\nEnter item number to drop: ").strip()
        
        try:
            item_index = int(item_num) - 1
            if 0 <= item_index < len(self.player.inventory):
                item = self.player.inventory[item_index]
                confirm = input(f"\nDrop {item.name}? (y/n): ").strip().lower()
                if confirm == 'y':
                    self.player.remove_item(item)
                    print(f"\n🗑️  Dropped {item.name}")
                    input("\nPress Enter to continue...")
            else:
                print("\n❌ Invalid item number!")
        except ValueError:
            print("\n❌ Invalid input!")
    
    def show_quests(self):
        """Display active and completed quests"""
        print("\n" + "="*60)
        print("📜 QUESTS")
        print("="*60)
        
        if self.player.quests:
            print("\nActive Quests:")
            for quest in self.player.quests:
                print(f"\n• {quest.name}")
                print(f"  {quest.description}")
                print("  Objectives:")
                for obj_key, completed in quest.objectives.items():
                    status = "✓" if completed else "○"
                    obj_name = obj_key.replace("_", " ").title()
                    print(f"    {status} {obj_name}")
                    
                # Check if quest can be completed
                if quest.is_complete() and not quest.completed:
                    success, message = quest.complete(self.player)
                    if success:
                        print(f"\n{message}")
                        self.player.completed_quests.append(quest)
                        self.player.quests.remove(quest)
                        
                        # Grant new quests
                        self.grant_new_quests(quest.quest_id)
        else:
            print("\nNo active quests.")
            
        if self.player.completed_quests:
            print("\n\nCompleted Quests:")
            for quest in self.player.completed_quests:
                print(f"✓ {quest.name}")
        
        input("\nPress Enter to continue...")
    
    def grant_new_quests(self, completed_quest_id: str):
        """Grant new quests based on completed quest"""
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
                if new_quest and new_quest not in self.player.quests:
                    self.player.quests.append(new_quest)
                    print(f"\n📜 New Quest: {new_quest.name}")
                    print(f"   {new_quest.description}")
    
    def update_quest_progress(self, objective_key: str):
        """Update progress on active quests"""
        for quest in self.player.quests:
            if objective_key in quest.objectives and not quest.objectives[objective_key]:
                # Special handling for count-based objectives
                if objective_key == "defeat_3_enemies" and self.enemy_kill_count >= 3:
                    quest.check_objective(objective_key)
                    print(f"\n✓ Quest objective complete: Defeat 3 enemies")
                elif objective_key == "defeat_5_bandits" and self.enemy_kill_count >= 5:
                    quest.check_objective(objective_key)
                    print(f"\n✓ Quest objective complete: Defeat 5 bandits")
                else:
                    quest.check_objective(objective_key)
                    obj_name = objective_key.replace("_", " ").title()
                    print(f"\n✓ Quest objective complete: {obj_name}")
    
    def discover_secret_world(self):
        """Player discovers the secret Crystal Cavern!"""
        print("\n" + "="*60)
        print("⚠️  SOMETHING STRANGE IS HAPPENING...")
        print("="*60)
        input("\nPress Enter to continue...")
        
        print("\n🌟 The ground beneath you begins to shimmer!")
        input()
        print("💎 A hidden portal materializes out of thin air!")
        input()
        print("✨ Ancient runes glow with otherworldly power!")
        input()
        
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          ⭐ SECRET WORLD DISCOVERED! ⭐                  ║
║                                                          ║
║              💎 CRYSTAL CAVERN OF LEGENDS 💎             ║
║                                                          ║
║  A legendary realm hidden from mortal eyes for eons!     ║
║  Only the chosen few ever find this sacred place!        ║
║                                                          ║
║  🏆 LEGENDARY EQUIPMENT awaits inside!                   ║
║  ⚠️  But beware - ELEMENTAL GUARDIANS protect it!       ║
║                                                          ║
║  🎲 This place is DIFFERENT every time you visit!        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")
        
        self.player.discovered_secret_world = True
        
        enter = input("\n💎 Enter the Crystal Cavern? (y/n): ").strip().lower()
        if enter == 'y':
            self.current_location = "crystal_cavern"
            print("\n✨ You step through the portal into a realm of legends...")
            print("💎 The crystals sing with ancient power!")
            print("🌈 This is the most beautiful place you've ever seen!")
        else:
            print("\n💫 The portal remains open. You can travel here anytime now!")
        
        input("\nPress Enter to continue...")
    
    def find_crystal_treasure(self):
        """Find random legendary treasure in Crystal Cavern"""
        print("\n" + "="*60)
        print("🎰 ✨ LEGENDARY TREASURE CHEST DISCOVERED! ✨ 🎰")
        print("="*60)
        
        # Random legendary items
        legendary_items = [
            "excalibur", "mjolnir", "shadowfang", "staff_of_cosmos", 
            "godbow", "infinity_blade", "celestial_armor", "void_armor",
            "phoenix_plate", "crystal_guardian", "time_weaver"
        ]
        
        # Ultra rare items (lower chance)
        ultra_rare = ["omni_weapon", "cosmic_armor"]
        
        # Determine what to find
        if random.random() < 0.05:  # 5% chance for ULTRA RARE
            item_key = random.choice(ultra_rare)
            print("\n🌌 ✨ 💫 ULTRA LEGENDARY ITEM! 💫 ✨ 🌌")
            print("🎉 THE GODS SMILE UPON YOU!")
        elif random.random() < 0.4:  # 40% chance for legendary
            item_key = random.choice(legendary_items)
            print("\n⭐ LEGENDARY ITEM FOUND! ⭐")
        else:
            # Gold and potions
            gold_amount = random.randint(500, 1500)
            self.player.gold += gold_amount
            print(f"\n💰 JACKPOT! You found {gold_amount} gold!")
            
            # Add some elixirs
            elixir_count = random.randint(1, 3)
            for _ in range(elixir_count):
                self.player.add_item(create_item("elixir"))
            print(f"💫 Plus {elixir_count} Elixir(s) of Life!")
            
            input("\nPress Enter to continue...")
            return
        
        # Give the legendary item
        item = create_item(item_key)
        self.player.add_item(item)
        
        print(f"\n✨ Obtained: {item.name}!")
        print(f"   {item.description}")
        
        if isinstance(item, Weapon):
            print(f"   ⚔️  Attack: +{item.attack_bonus}")
        elif isinstance(item, Armor):
            print(f"   🛡️  Defense: +{item.defense_bonus}")
        
        # Bonus gold
        bonus_gold = random.randint(300, 800)
        self.player.gold += bonus_gold
        print(f"\n💰 Bonus: +{bonus_gold} gold!")
        
        input("\nPress Enter to continue...")
    
    def visit_shop(self):
        """Visit the shop to buy items"""
        print("\n" + "="*60)
        print("🏪 TRADING POST")
        print("="*60)
        print(f"Your Gold: {self.player.gold}")
        print("\nAvailable Items:")
        print("\n1. Health Potion - 25 gold")
        print("2. Super Health Potion - 50 gold")
        print("3. Mana Potion - 30 gold")
        print("4. Super Mana Potion - 60 gold")
        print("5. Iron Sword - 50 gold")
        print("6. Steel Sword - 150 gold")
        print("7. Leather Armor - 50 gold")
        print("8. Chainmail - 150 gold")
        print("0. Leave")
        
        choice = input("\nWhat would you like to buy? ").strip()
        
        shop_items = {
            "1": ("health_potion", 25),
            "2": ("super_health_potion", 50),
            "3": ("mana_potion", 30),
            "4": ("super_mana_potion", 60),
            "5": ("iron_sword", 50),
            "6": ("steel_sword", 150),
            "7": ("leather_armor", 50),
            "8": ("chainmail", 150),
        }
        
        if choice in shop_items:
            item_key, price = shop_items[choice]
            if self.player.gold >= price:
                item = create_item(item_key)
                self.player.gold -= price
                self.player.add_item(item)
                print(f"\n✨ Purchased {item.name}!")
            else:
                print("\n❌ Not enough gold!")
        elif choice != "0":
            print("\n❌ Invalid choice!")
            
        input("\nPress Enter to continue...")
    
    def save_game(self):
        """Save the current game state"""
        save_data = {
            "player": self.player,
            "current_location": self.current_location,
            "enemy_kill_count": self.enemy_kill_count
        }
        
        try:
            with open("savegame.pkl", "wb") as f:
                pickle.dump(save_data, f)
            print("\n💾 Game saved successfully!")
        except Exception as e:
            print(f"\n❌ Error saving game: {e}")
            
        input("\nPress Enter to continue...")
    
    def load_game(self):
        """Load a saved game"""
        if not os.path.exists("savegame.pkl"):
            return False
            
        try:
            with open("savegame.pkl", "rb") as f:
                save_data = pickle.load(f)
                
            self.player = save_data["player"]
            self.current_location = save_data["current_location"]
            self.enemy_kill_count = save_data["enemy_kill_count"]
            
            print("\n💾 Game loaded successfully!")
            return True
        except Exception as e:
            print(f"\n❌ Error loading game: {e}")
            return False
    
    def run(self):
        """Main game loop"""
        while not self.game_over:
            self.show_location()
            choice = self.main_menu()
            
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.travel()
            elif choice == "3":
                print(self.player.display_stats())
                input("\nPress Enter to continue...")
            elif choice == "4":
                self.show_inventory()
            elif choice == "5":
                self.show_quests()
            elif choice == "6" and self.world.get_location(self.current_location).shop:
                self.visit_shop()
            elif choice == "s":
                self.save_game()
            elif choice == "q":
                confirm = input("\nAre you sure you want to quit? (y/n): ").strip().lower()
                if confirm == 'y':
                    print("\nThanks for playing! Goodbye!")
                    self.game_over = True
        
        print("\n" + "="*60)
        print(" "*20 + "GAME OVER")
        print("="*60)





