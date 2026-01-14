"""Quest system and storyline"""

class Quest:
    """Base quest class"""
    def __init__(self, quest_id: str, name: str, description: str, 
                 objectives: dict, rewards: dict):
        self.quest_id = quest_id
        self.name = name
        self.description = description
        self.objectives = objectives  # {objective: completed}
        self.rewards = rewards  # {exp, gold, items}
        self.completed = False
        
    def check_objective(self, objective_key: str) -> bool:
        """Mark an objective as complete"""
        if objective_key in self.objectives:
            self.objectives[objective_key] = True
            return True
        return False
    
    def is_complete(self) -> bool:
        """Check if all objectives are complete"""
        return all(self.objectives.values())
    
    def complete(self, player):
        """Complete the quest and grant rewards"""
        if not self.is_complete():
            return False, "Quest objectives not complete!"
            
        self.completed = True
        messages = []
        
        messages.append(f"\n🎊 Quest Complete: {self.name}")
        
        # Grant rewards
        if "exp" in self.rewards:
            player.gain_experience(self.rewards["exp"])
            messages.append(f"✨ Gained {self.rewards['exp']} experience!")
            
        if "gold" in self.rewards:
            player.gold += self.rewards["gold"]
            messages.append(f"💰 Received {self.rewards['gold']} gold!")
            
        if "items" in self.rewards:
            from items import create_item
            messages.append("🎁 Received items:")
            for item_key in self.rewards["items"]:
                item = create_item(item_key)
                if item:
                    player.add_item(item)
                    messages.append(f"   - {item.name}")
                    
        return True, "\n".join(messages)

# Define available quests
QUESTS = {
    "tutorial": Quest(
        quest_id="tutorial",
        name="First Steps",
        description="Defeat 3 enemies to prove your worth.",
        objectives={"defeat_3_enemies": False},
        rewards={"exp": 50, "gold": 30, "items": ["health_potion", "mana_potion"]}
    ),
    
    "gather_herbs": Quest(
        quest_id="gather_herbs",
        name="The Healer's Request",
        description="The village healer needs rare herbs from the Dark Forest.",
        objectives={"visit_dark_forest": False, "defeat_forest_enemy": False},
        rewards={"exp": 100, "gold": 75, "items": ["super_health_potion", "super_health_potion"]}
    ),
    
    "bandit_camp": Quest(
        quest_id="bandit_camp",
        name="Clear the Bandit Camp",
        description="Bandits have been terrorizing travelers. Clear their camp.",
        objectives={"visit_bandit_camp": False, "defeat_5_bandits": False},
        rewards={"exp": 150, "gold": 100, "items": ["steel_sword", "leather_armor"]}
    ),
    
    "ancient_ruins": Quest(
        quest_id="ancient_ruins",
        name="Secrets of the Ancients",
        description="Explore the Ancient Ruins and recover the Ancient Key.",
        objectives={"visit_ancient_ruins": False, "find_ancient_key": False},
        rewards={"exp": 200, "gold": 150, "items": ["arcane_staff", "chainmail"]}
    ),
    
    "dragon_egg": Quest(
        quest_id="dragon_egg",
        name="The Dragon's Egg",
        description="A dragon egg has been stolen. Recover it from the Mountain Peak.",
        objectives={"visit_mountain_peak": False, "defeat_egg_guardian": False, "get_dragon_egg": False},
        rewards={"exp": 300, "gold": 250, "items": ["legendary_blade", "plate_armor"]}
    ),
    
    "final_battle": Quest(
        quest_id="final_battle",
        name="The Dark Lord's Downfall",
        description="Face the Dark Lord in his castle and save the realm!",
        objectives={"visit_dark_castle": False, "defeat_dark_lord": False},
        rewards={"exp": 1000, "gold": 5000, "items": ["staff_of_power", "dragon_armor"]}
    )
}

def create_quest(quest_id: str):
    """Create a new quest instance"""
    if quest_id in QUESTS:
        template = QUESTS[quest_id]
        return Quest(
            quest_id=template.quest_id,
            name=template.name,
            description=template.description,
            objectives=template.objectives.copy(),
            rewards=template.rewards.copy()
        )
    return None






