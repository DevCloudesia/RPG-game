// ============================================
// REALM OF LEGENDS - Client-Side Game Engine
// Complete RPG game running entirely in browser
// ============================================

// ============================================
// ITEMS DATABASE
// ============================================
const ITEMS = {
    // Consumables
    health_potion: { name: "Health Potion", description: "Restores 50 HP", value: 25, type: "consumable", effectType: "heal", effectAmount: 50 },
    super_health_potion: { name: "Super Health Potion", description: "Restores 100 HP", value: 50, type: "consumable", effectType: "heal", effectAmount: 100 },
    mana_potion: { name: "Mana Potion", description: "Restores 40 mana", value: 30, type: "consumable", effectType: "mana", effectAmount: 40 },
    super_mana_potion: { name: "Super Mana Potion", description: "Restores 80 mana", value: 60, type: "consumable", effectType: "mana", effectAmount: 80 },
    elixir: { name: "💫 Elixir of Life", description: "Fully restores HP and Mana!", value: 200, type: "consumable", effectType: "full_heal", effectAmount: 9999 },
    
    // Weapons
    rusty_sword: { name: "Rusty Sword", description: "An old, worn sword", value: 10, type: "weapon", attackBonus: 5 },
    iron_sword: { name: "Iron Sword", description: "A sturdy iron blade", value: 50, type: "weapon", attackBonus: 10 },
    steel_sword: { name: "Steel Sword", description: "A well-crafted steel sword", value: 150, type: "weapon", attackBonus: 18 },
    legendary_blade: { name: "Dragonbane", description: "A legendary sword forged from dragon scales", value: 1000, type: "weapon", attackBonus: 35 },
    mage_staff: { name: "Mage Staff", description: "A staff imbued with magical energy", value: 80, type: "weapon", attackBonus: 8 },
    arcane_staff: { name: "Arcane Staff", description: "Crackles with arcane power", value: 200, type: "weapon", attackBonus: 15 },
    staff_of_power: { name: "Staff of Eternity", description: "Contains the essence of ancient magic", value: 1200, type: "weapon", attackBonus: 40 },
    shadow_daggers: { name: "Shadow Daggers", description: "Twin blades that shimmer with darkness", value: 250, type: "weapon", attackBonus: 25 },
    divine_hammer: { name: "Hammer of Justice", description: "Radiates holy light", value: 300, type: "weapon", attackBonus: 28 },
    excalibur: { name: "⚔️ Excalibur", description: "The legendary sword of kings!", value: 5000, type: "weapon", attackBonus: 50 },
    mjolnir: { name: "🔨 Mjolnir", description: "The hammer of thunder gods!", value: 5500, type: "weapon", attackBonus: 55 },
    infinity_blade: { name: "✨ Infinity Blade", description: "Exists in all timelines at once!", value: 7000, type: "weapon", attackBonus: 70 },
    
    // Armor
    leather_armor: { name: "Leather Armor", description: "Light leather protection", value: 50, type: "armor", defenseBonus: 8 },
    chainmail: { name: "Chainmail Armor", description: "Interlocking metal rings", value: 150, type: "armor", defenseBonus: 15 },
    plate_armor: { name: "Plate Armor", description: "Heavy steel plating", value: 300, type: "armor", defenseBonus: 25 },
    dragon_armor: { name: "Dragon Scale Armor", description: "Armor crafted from dragon scales", value: 1500, type: "armor", defenseBonus: 45 },
    celestial_armor: { name: "🌟 Celestial Armor", description: "Blessed by the gods!", value: 6000, type: "armor", defenseBonus: 60 },
    crystal_guardian: { name: "💎 Crystal Guardian", description: "Formed from pure diamond!", value: 8000, type: "armor", defenseBonus: 80 },
};

// ============================================
// ENEMIES DATABASE
// ============================================
const ENEMIES = {
    goblin: { name: "Goblin", hp: 80, attack: 18, defense: 8, exp: 20, gold: 10, loot: { health_potion: 0.3, rusty_sword: 0.1 } },
    wolf: { name: "Dire Wolf", hp: 100, attack: 25, defense: 10, exp: 30, gold: 8, loot: { health_potion: 0.25 } },
    skeleton: { name: "Skeleton Warrior", hp: 120, attack: 30, defense: 15, exp: 40, gold: 15, loot: { health_potion: 0.3, mana_potion: 0.2, iron_sword: 0.15 } },
    orc: { name: "Orc Raider", hp: 160, attack: 35, defense: 18, exp: 50, gold: 25, loot: { health_potion: 0.4, leather_armor: 0.2, iron_sword: 0.2 } },
    dark_mage: { name: "Dark Mage", hp: 140, attack: 45, defense: 12, exp: 60, gold: 40, loot: { mana_potion: 0.5, super_health_potion: 0.3, mage_staff: 0.15 } },
    troll: { name: "Cave Troll", hp: 240, attack: 42, defense: 25, exp: 80, gold: 50, loot: { super_health_potion: 0.4, chainmail: 0.2, steel_sword: 0.15 } },
    wraith: { name: "Shadow Wraith", hp: 180, attack: 50, defense: 16, exp: 90, gold: 60, loot: { super_mana_potion: 0.4, shadow_daggers: 0.2, arcane_staff: 0.15 } },
    dragon_whelp: { name: "Dragon Whelp", hp: 300, attack: 55, defense: 30, exp: 120, gold: 100, loot: { super_health_potion: 0.6, super_mana_potion: 0.5, steel_sword: 0.3 } },
    vampire: { name: "Vampire Lord", hp: 400, attack: 65, defense: 35, exp: 150, gold: 150, loot: { super_health_potion: 0.7, super_mana_potion: 0.7, plate_armor: 0.3 } },
    demon: { name: "Demon", hp: 360, attack: 70, defense: 32, exp: 160, gold: 120, loot: { super_health_potion: 0.6, super_mana_potion: 0.6, divine_hammer: 0.2 } },
    fire_elemental: { name: "🔥 Fire Elemental", hp: 500, attack: 80, defense: 40, exp: 300, gold: 500, loot: { elixir: 0.3, excalibur: 0.15, celestial_armor: 0.15 } },
    ice_golem: { name: "❄️ Ice Golem", hp: 600, attack: 75, defense: 55, exp: 350, gold: 600, loot: { elixir: 0.3, mjolnir: 0.15, crystal_guardian: 0.15 } },
    storm_spirit: { name: "⚡ Storm Spirit", hp: 440, attack: 95, defense: 35, exp: 400, gold: 700, loot: { elixir: 0.4, infinity_blade: 0.15 } },
    crystal_titan: { name: "💎 Crystal Titan", hp: 1000, attack: 110, defense: 80, exp: 800, gold: 2000, loot: { elixir: 0.7, infinity_blade: 0.3, crystal_guardian: 0.3 } },
    ancient_dragon: { name: "Ancient Dragon", hp: 800, attack: 90, defense: 60, exp: 500, gold: 1000, loot: { legendary_blade: 0.8, dragon_armor: 0.8 } },
    dark_lord: { name: "Dark Lord Malzahar", hp: 1000, attack: 100, defense: 70, exp: 1000, gold: 2000, loot: { staff_of_power: 1.0, dragon_armor: 1.0 } }
};

// ============================================
// WORLD/LOCATIONS
// ============================================
const WORLD = {
    village: {
        name: "🏰 Willowbrook Village",
        description: `🌅 The morning sun bathes the village square in golden light.

👨‍🌾 "Hero! Thank the gods you've come!" cries Elder Marcus.
💬 "Dark forces have awakened! The Shadow Lord Malzahar has returned!"

🗺️ DESTINATIONS:
   🌲 North → Dark Forest
   🏛️ East → Ancient Ruins  
   ⛰️ South → Mountain Path
   🏪 West → Trading Post`,
        enemies: [],
        connections: ["dark_forest", "ancient_ruins", "mountain_path", "trading_post"],
        hasShop: false
    },
    trading_post: {
        name: "🏪 Trading Post",
        description: "A bustling trading post where merchants sell weapons, armor, and supplies.",
        enemies: [],
        connections: ["village"],
        hasShop: true
    },
    dark_forest: {
        name: "🌲 Darkwood Forest",
        description: `🌙 Gnarled trees whisper warnings. Corrupted creatures lurk in shadows.

⚠️ DANGER: Low-Medium | Recommended: Level 1-3
🗡️ ENEMIES: Goblins, Dire Wolves, Skeleton Warriors`,
        enemies: ["goblin", "wolf", "skeleton"],
        connections: ["village", "bandit_camp", "cursed_swamp", "crystal_cavern"]
    },
    bandit_camp: {
        name: "⚔️ Bandit Camp",
        description: "A crude camp of bandits preying on travelers. Tattered tents and stolen goods litter the area.",
        enemies: ["goblin", "orc", "skeleton"],
        connections: ["dark_forest"]
    },
    cursed_swamp: {
        name: "☠️ Cursed Swamp",
        description: "Murky waters bubble ominously. Dark magic corrupts this place. Dangerous creatures lurk in the depths.",
        enemies: ["skeleton", "wraith", "dark_mage"],
        connections: ["dark_forest", "haunted_graveyard"]
    },
    haunted_graveyard: {
        name: "💀 Haunted Graveyard",
        description: "Crumbling tombstones stretch endlessly. The restless dead walk here, unable to find peace.",
        enemies: ["skeleton", "wraith", "vampire"],
        connections: ["cursed_swamp", "dark_castle"]
    },
    ancient_ruins: {
        name: "🏛️ Ancient Ruins",
        description: "Massive stone pillars speak of a once-great civilization. Ancient magic lingers in these halls.",
        enemies: ["skeleton", "dark_mage", "wraith"],
        connections: ["village", "hidden_temple", "crystal_cavern"]
    },
    hidden_temple: {
        name: "🏛️ Hidden Temple",
        description: "A sacred temple hidden beneath the ruins, untouched for centuries. Powerful enchantments protect this place.",
        enemies: ["wraith", "demon", "dark_mage"],
        connections: ["ancient_ruins"]
    },
    mountain_path: {
        name: "⛰️ Mountain Path",
        description: "A treacherous path winds up the mountainside. The air grows thin and cold.",
        enemies: ["wolf", "orc", "troll"],
        connections: ["village", "mountain_peak"]
    },
    mountain_peak: {
        name: "🏔️ Mountain Peak",
        description: "You stand at the summit, clouds swirling around you. Dragon caves dot the mountainside. A mighty roar echoes...",
        enemies: ["dragon_whelp", "troll", "orc"],
        connections: ["mountain_path", "dragon_lair", "crystal_cavern"]
    },
    dragon_lair: {
        name: "🐉 Dragon's Lair",
        description: "Massive caverns filled with treasure hoards. An ANCIENT DRAGON slumbers on a mountain of gold...",
        enemies: ["ancient_dragon"],
        connections: ["mountain_peak"]
    },
    dark_castle: {
        name: "🏰 Dark Castle",
        description: "The fortress of the Dark Lord looms before you. This is the source of evil threatening the realm. Your final battle awaits...",
        enemies: ["demon", "vampire", "dark_mage", "dark_lord"],
        connections: ["haunted_graveyard"]
    },
    crystal_cavern: {
        name: "💎 Crystal Cavern of Legends",
        description: `✨ THE LEGENDARY CRYSTAL CAVERN ✨

💎 Massive crystals pulse with ancient power, casting rainbow light!
🏆 LEGENDARY TREASURES await the brave!

⚠️ GUARDIANS: Fire Elementals, Ice Golems, Storm Spirits, Crystal Titans!

✨ Only the bravest heroes dare enter... become a LEGEND!`,
        enemies: ["fire_elemental", "ice_golem", "storm_spirit", "crystal_titan"],
        connections: ["dark_forest", "mountain_peak", "ancient_ruins"]
    }
};

// ============================================
// SHOP ITEMS
// ============================================
const SHOP_ITEMS = [
    { key: "health_potion", price: 25 },
    { key: "super_health_potion", price: 75 },
    { key: "mana_potion", price: 30 },
    { key: "super_mana_potion", price: 80 },
    { key: "iron_sword", price: 100 },
    { key: "steel_sword", price: 250 },
    { key: "leather_armor", price: 80 },
    { key: "chainmail", price: 200 },
    { key: "plate_armor", price: 400 }
];

// ============================================
// CHARACTER CLASS
// ============================================
class Character {
    constructor(name, charClass) {
        this.name = name;
        this.charClass = charClass;
        this.level = 1;
        this.experience = 0;
        this.gold = 50;
        
        // Base stats
        this.maxHp = 100;
        this.hp = 100;
        this.maxMana = 50;
        this.mana = 50;
        this.attack = 10;
        this.defense = 5;
        this.magic = 5;
        
        // Equipment
        this.equippedWeapon = null;
        this.equippedArmor = null;
        this.inventory = [];
        
        // Abilities
        this.abilities = [];
        
        // Apply class bonuses
        this.applyClassBonuses();
    }
    
    applyClassBonuses() {
        switch(this.charClass) {
            case "Warrior":
                this.maxHp = 150;
                this.hp = 150;
                this.attack = 15;
                this.defense = 10;
                this.abilities = ["Power Strike", "Shield Bash", "Whirlwind"];
                break;
            case "Mage":
                this.maxHp = 80;
                this.hp = 80;
                this.maxMana = 100;
                this.mana = 100;
                this.magic = 20;
                this.attack = 5;
                this.abilities = ["Fireball", "Ice Blast", "Lightning Strike"];
                break;
            case "Rogue":
                this.maxHp = 100;
                this.hp = 100;
                this.attack = 12;
                this.defense = 8;
                this.abilities = ["Backstab", "Poison Strike", "Shadow Step"];
                break;
            case "Cleric":
                this.maxHp = 120;
                this.hp = 120;
                this.maxMana = 80;
                this.mana = 80;
                this.magic = 15;
                this.defense = 8;
                this.abilities = ["Heal", "Smite", "Divine Shield"];
                break;
        }
    }
    
    getTotalAttack() {
        let total = this.attack;
        if (this.equippedWeapon) {
            total += this.equippedWeapon.attackBonus;
        }
        return total;
    }
    
    getTotalDefense() {
        let total = this.defense;
        if (this.equippedArmor) {
            total += this.equippedArmor.defenseBonus;
        }
        return total;
    }
    
    takeDamage(damage) {
        const actualDamage = Math.max(1, damage - Math.floor(this.getTotalDefense() / 3));
        this.hp = Math.max(0, this.hp - actualDamage);
        return actualDamage;
    }
    
    heal(amount) {
        this.hp = Math.min(this.hp + amount, this.maxHp);
    }
    
    restoreMana(amount) {
        this.mana = Math.min(this.mana + amount, this.maxMana);
    }
    
    addExperience(amount) {
        this.experience += amount;
        const expNeeded = this.level * 100;
        if (this.experience >= expNeeded) {
            this.levelUp();
            return true;
        }
        return false;
    }
    
    levelUp() {
        this.level++;
        this.experience = 0;
        this.maxHp += 20;
        this.hp = this.maxHp;
        this.maxMana += 10;
        this.mana = this.maxMana;
        this.attack += 3;
        this.defense += 2;
        this.magic += 2;
    }
    
    getExpNeeded() {
        return this.level * 100;
    }
    
    isAlive() {
        return this.hp > 0;
    }
}

// ============================================
// ENEMY CLASS
// ============================================
class Enemy {
    constructor(type, levelModifier = 0) {
        const template = ENEMIES[type] || ENEMIES.goblin;
        this.type = type;
        this.level = 1 + levelModifier;
        this.name = `${template.name} (Lv.${this.level})`;
        
        // Scale stats with level
        this.maxHp = Math.floor(template.hp * (1 + levelModifier * 0.3));
        this.hp = this.maxHp;
        this.attack = Math.floor(template.attack * (1 + levelModifier * 0.25));
        this.defense = Math.floor(template.defense * (1 + levelModifier * 0.25));
        this.expReward = Math.floor(template.exp * (1 + levelModifier * 0.3));
        this.goldReward = Math.floor(template.gold * (1 + levelModifier * 0.25));
        this.lootTable = template.loot;
    }
    
    takeDamage(damage) {
        const actualDamage = Math.max(1, damage - Math.floor(this.defense / 3));
        this.hp = Math.max(0, this.hp - actualDamage);
        return actualDamage;
    }
    
    attackPlayer() {
        return this.attack + Math.floor(Math.random() * 5) - 2;
    }
    
    isAlive() {
        return this.hp > 0;
    }
    
    getLoot() {
        const drops = [];
        for (const [itemKey, dropChance] of Object.entries(this.lootTable)) {
            if (Math.random() < dropChance) {
                drops.push(itemKey);
            }
        }
        return drops;
    }
}

// ============================================
// GAME ENGINE
// ============================================
class GameEngine {
    constructor() {
        this.player = null;
        this.currentLocation = "village";
        this.currentEnemy = null;
        this.combatActive = false;
        this.messages = [];
        this.enemiesDefeated = 0;
        this.defending = false;
    }
    
    startGame(name, charClass) {
        this.player = new Character(name, charClass);
        this.currentLocation = "village";
        this.combatActive = false;
        this.currentEnemy = null;
        this.messages = [];
        this.enemiesDefeated = 0;
        this.addMessage(`⚔️ Welcome, ${name} the ${charClass}!`);
        this.addMessage(`📍 You begin your adventure in ${WORLD[this.currentLocation].name}`);
        return true;
    }
    
    addMessage(msg) {
        this.messages.push(msg);
        if (this.messages.length > 50) {
            this.messages.shift();
        }
    }
    
    clearMessages() {
        this.messages = [];
    }
    
    getLocation() {
        return WORLD[this.currentLocation];
    }
    
    explore() {
        this.clearMessages();
        const location = this.getLocation();
        
        if (location.enemies.length === 0) {
            this.addMessage("🔍 This area seems peaceful. No enemies here.");
            return { combatStarted: false };
        }
        
        // Random chance to find enemy
        if (Math.random() < 0.7) {
            const enemyType = location.enemies[Math.floor(Math.random() * location.enemies.length)];
            const levelMod = Math.max(0, this.player.level - 1);
            this.currentEnemy = new Enemy(enemyType, levelMod);
            this.combatActive = true;
            this.addMessage(`⚔️ A wild ${this.currentEnemy.name} appears!`);
            return { combatStarted: true, enemy: this.currentEnemy };
        } else {
            // Found something else
            const events = [
                "🔍 You searched the area but found nothing.",
                "💰 You found 5 gold coins!", 
                "🌿 You found some healing herbs and restored 20 HP!",
                "✨ You feel a mysterious energy... (+10 XP)"
            ];
            const eventIdx = Math.floor(Math.random() * events.length);
            this.addMessage(events[eventIdx]);
            
            if (eventIdx === 1) this.player.gold += 5;
            if (eventIdx === 2) this.player.heal(20);
            if (eventIdx === 3) this.player.addExperience(10);
            
            return { combatStarted: false };
        }
    }
    
    combatAction(action, abilityName = null) {
        if (!this.combatActive || !this.currentEnemy) {
            return { success: false, error: "Not in combat!" };
        }
        
        this.clearMessages();
        let playerDamage = 0;
        let enemyDamage = 0;
        this.defending = false;
        
        // Player action
        switch(action) {
            case "attack":
                const baseDamage = this.player.getTotalAttack() + Math.floor(Math.random() * 5);
                playerDamage = this.currentEnemy.takeDamage(baseDamage);
                this.addMessage(`⚔️ You attack for ${playerDamage} damage!`);
                break;
                
            case "ability":
                if (!abilityName || !this.player.abilities.includes(abilityName)) {
                    return { success: false, error: "Invalid ability!" };
                }
                if (this.player.mana < 15) {
                    return { success: false, error: "Not enough mana!" };
                }
                this.player.mana -= 15;
                const abilityDamage = Math.floor((this.player.getTotalAttack() + this.player.magic) * 1.5) + Math.floor(Math.random() * 5);
                playerDamage = this.currentEnemy.takeDamage(abilityDamage);
                this.addMessage(`✨ You use ${abilityName} for ${playerDamage} damage!`);
                break;
                
            case "defend":
                this.defending = true;
                this.addMessage("🛡️ You raise your guard!");
                break;
                
            case "run":
                if (Math.random() < 0.5) {
                    this.combatActive = false;
                    this.currentEnemy = null;
                    this.addMessage("💨 You escaped successfully!");
                    return { success: true, escaped: true };
                } else {
                    this.addMessage("❌ Failed to escape!");
                }
                break;
        }
        
        // Check if enemy is defeated
        if (!this.currentEnemy.isAlive()) {
            return this.handleVictory();
        }
        
        // Enemy turn
        let incomingDamage = this.currentEnemy.attackPlayer();
        if (this.defending) {
            incomingDamage = Math.floor(incomingDamage * 0.5);
        }
        enemyDamage = this.player.takeDamage(incomingDamage);
        this.addMessage(`👹 ${this.currentEnemy.name} attacks for ${enemyDamage} damage!`);
        
        // Check if player is defeated
        if (!this.player.isAlive()) {
            return this.handleDefeat();
        }
        
        return { 
            success: true, 
            playerDamage, 
            enemyDamage,
            victory: false,
            defeat: false
        };
    }
    
    handleVictory() {
        const enemy = this.currentEnemy;
        this.combatActive = false;
        this.enemiesDefeated++;
        
        // Rewards
        this.player.gold += enemy.goldReward;
        const leveledUp = this.player.addExperience(enemy.expReward);
        
        this.addMessage(`🎉 Victory! You defeated ${enemy.name}!`);
        this.addMessage(`💰 +${enemy.goldReward} gold | ⭐ +${enemy.expReward} XP`);
        
        if (leveledUp) {
            this.addMessage(`🎊 LEVEL UP! You are now level ${this.player.level}!`);
        }
        
        // Loot
        const loot = enemy.getLoot();
        for (const itemKey of loot) {
            if (ITEMS[itemKey]) {
                const item = { ...ITEMS[itemKey], key: itemKey };
                this.player.inventory.push(item);
                this.addMessage(`📦 You found: ${item.name}!`);
            }
        }
        
        this.currentEnemy = null;
        return { success: true, victory: true };
    }
    
    handleDefeat() {
        this.combatActive = false;
        this.currentEnemy = null;
        this.addMessage("💀 You have been defeated...");
        return { success: true, defeat: true };
    }
    
    travel(destination) {
        const location = this.getLocation();
        if (!location.connections.includes(destination)) {
            return { success: false, error: "Cannot travel there from here!" };
        }
        
        this.currentLocation = destination;
        this.clearMessages();
        this.addMessage(`🚶 You traveled to ${WORLD[destination].name}`);
        return { success: true };
    }
    
    useItem(itemIndex) {
        if (itemIndex < 0 || itemIndex >= this.player.inventory.length) {
            return { success: false, error: "Invalid item!" };
        }
        
        const item = this.player.inventory[itemIndex];
        
        if (item.type === "consumable") {
            if (item.effectType === "heal") {
                this.player.heal(item.effectAmount);
                this.addMessage(`✨ Restored ${item.effectAmount} HP!`);
            } else if (item.effectType === "mana") {
                this.player.restoreMana(item.effectAmount);
                this.addMessage(`💙 Restored ${item.effectAmount} Mana!`);
            } else if (item.effectType === "full_heal") {
                this.player.hp = this.player.maxHp;
                this.player.mana = this.player.maxMana;
                this.addMessage(`💫 Fully restored!`);
            }
            this.player.inventory.splice(itemIndex, 1);
        } else if (item.type === "weapon") {
            this.player.equippedWeapon = item;
            this.addMessage(`⚔️ Equipped ${item.name}!`);
        } else if (item.type === "armor") {
            this.player.equippedArmor = item;
            this.addMessage(`🛡️ Equipped ${item.name}!`);
        }
        
        return { success: true };
    }
    
    buyItem(itemKey) {
        const shopItem = SHOP_ITEMS.find(i => i.key === itemKey);
        if (!shopItem) return { success: false, error: "Item not in shop!" };
        
        if (this.player.gold < shopItem.price) {
            return { success: false, error: "Not enough gold!" };
        }
        
        this.player.gold -= shopItem.price;
        const item = { ...ITEMS[itemKey], key: itemKey };
        this.player.inventory.push(item);
        this.addMessage(`🛒 Purchased ${item.name}!`);
        return { success: true };
    }
    
    getShopItems() {
        return SHOP_ITEMS.map(si => ({
            key: si.key,
            price: si.price,
            ...ITEMS[si.key]
        }));
    }
    
    getGameState() {
        return {
            initialized: !!this.player,
            player: this.player ? {
                name: this.player.name,
                class: this.player.charClass,
                level: this.player.level,
                hp: this.player.hp,
                max_hp: this.player.maxHp,
                mana: this.player.mana,
                max_mana: this.player.maxMana,
                experience: this.player.experience,
                exp_needed: this.player.getExpNeeded(),
                gold: this.player.gold,
                attack: this.player.getTotalAttack(),
                defense: this.player.getTotalDefense(),
                abilities: this.player.abilities,
                inventory: this.player.inventory
            } : null,
            location: {
                name: WORLD[this.currentLocation].name,
                description: WORLD[this.currentLocation].description,
                connections: WORLD[this.currentLocation].connections,
                has_shop: WORLD[this.currentLocation].hasShop
            },
            combat_active: this.combatActive,
            enemy: this.currentEnemy ? {
                name: this.currentEnemy.name,
                hp: this.currentEnemy.hp,
                max_hp: this.currentEnemy.maxHp
            } : null,
            messages: this.messages
        };
    }
    
    // Save/Load using localStorage
    saveGame() {
        const saveData = {
            player: this.player,
            currentLocation: this.currentLocation,
            enemiesDefeated: this.enemiesDefeated
        };
        localStorage.setItem('realmOfLegendsSave', JSON.stringify(saveData));
        this.addMessage("💾 Game saved!");
        return true;
    }
    
    loadGame() {
        const saveData = localStorage.getItem('realmOfLegendsSave');
        if (!saveData) {
            return false;
        }
        
        try {
            const data = JSON.parse(saveData);
            // Recreate player with proper class methods
            this.player = new Character(data.player.name, data.player.charClass);
            Object.assign(this.player, data.player);
            this.currentLocation = data.currentLocation;
            this.enemiesDefeated = data.enemiesDefeated || 0;
            this.combatActive = false;
            this.currentEnemy = null;
            this.messages = [];
            this.addMessage("📂 Game loaded!");
            return true;
        } catch (e) {
            console.error("Failed to load save:", e);
            return false;
        }
    }
    
    hasSaveGame() {
        return localStorage.getItem('realmOfLegendsSave') !== null;
    }
    
    deleteSave() {
        localStorage.removeItem('realmOfLegendsSave');
    }
}

// Global game instance
const game = new GameEngine();
