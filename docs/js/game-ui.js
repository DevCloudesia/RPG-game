// ============================================
// REALM OF LEGENDS - Game UI Controller
// Handles all UI interactions and rendering
// ============================================

let gameState = null;
let selectedClass = null;

// Enemy sprite definitions
const ENEMY_SPRITES = {
    'Goblin': { bodyColor: 'linear-gradient(to bottom, #2d5a2d 0%, #1a3d1a 100%)', headColor: '#4a7c4a', size: 0.8, emoji: '👺' },
    'Dire Wolf': { bodyColor: 'linear-gradient(to bottom, #4a4a4a 0%, #2a2a2a 100%)', headColor: '#5a5a5a', size: 0.9, emoji: '🐺' },
    'Skeleton Warrior': { bodyColor: 'linear-gradient(to bottom, #d4d4d4 0%, #a0a0a0 100%)', headColor: '#e8e8e8', size: 1.0, emoji: '💀' },
    'Orc Raider': { bodyColor: 'linear-gradient(to bottom, #3d6b3d 0%, #2a4a2a 100%)', headColor: '#4a8a4a', size: 1.2, emoji: '👹' },
    'Dark Mage': { bodyColor: 'linear-gradient(to bottom, #4a2a6a 0%, #2a1a4a 100%)', headColor: '#6a4a8a', size: 1.0, emoji: '🧙' },
    'Cave Troll': { bodyColor: 'linear-gradient(to bottom, #5a6a5a 0%, #3a4a3a 100%)', headColor: '#6a7a6a', size: 1.5, emoji: '🧌' },
    'Shadow Wraith': { bodyColor: 'linear-gradient(to bottom, #2a2a4a 0%, #1a1a2a 100%)', headColor: '#3a3a5a', size: 1.1, emoji: '👻' },
    'Dragon Whelp': { bodyColor: 'linear-gradient(to bottom, #8b2500 0%, #5a1a00 100%)', headColor: '#aa4400', size: 1.3, emoji: '🐉' },
    'Vampire Lord': { bodyColor: 'linear-gradient(to bottom, #4a0a2a 0%, #2a0a1a 100%)', headColor: '#d4c4b4', size: 1.2, emoji: '🧛' },
    'Demon': { bodyColor: 'linear-gradient(to bottom, #8b0000 0%, #4a0000 100%)', headColor: '#aa2222', size: 1.3, emoji: '😈' },
    'Fire Elemental': { bodyColor: 'linear-gradient(to bottom, #ff6600 0%, #cc3300 100%)', headColor: '#ffaa00', size: 1.4, emoji: '🔥' },
    'Ice Golem': { bodyColor: 'linear-gradient(to bottom, #4a9fff 0%, #2a6fcc 100%)', headColor: '#8acfff', size: 1.5, emoji: '❄️' },
    'Storm Spirit': { bodyColor: 'linear-gradient(to bottom, #6a6aaa 0%, #4a4a8a 100%)', headColor: '#8a8acc', size: 1.2, emoji: '⚡' },
    'Crystal Titan': { bodyColor: 'linear-gradient(to bottom, #ff00ff 0%, #aa00aa 100%)', headColor: '#ff88ff', size: 1.8, emoji: '💎' },
    'Ancient Dragon': { bodyColor: 'linear-gradient(to bottom, #cc8800 0%, #886600 100%)', headColor: '#ddaa22', size: 1.7, emoji: '🐲' },
    'Dark Lord Malzahar': { bodyColor: 'linear-gradient(to bottom, #1a0a2a 0%, #0a0a1a 100%)', headColor: '#3a2a4a', size: 1.6, emoji: '👿' }
};

// Initialize game
document.addEventListener('DOMContentLoaded', () => {
    console.log('Game UI loaded!');
    
    // Check for existing save
    if (game.hasSaveGame()) {
        document.getElementById('continue-btn').style.display = 'inline-block';
    }
});

// Show character creation screen
function showCharacterCreation() {
    document.getElementById('title-screen').classList.remove('active');
    document.getElementById('character-creation').classList.add('active');
}

// Continue saved game
function continueGame() {
    if (game.loadGame()) {
        gameState = game.getGameState();
        document.getElementById('title-screen').classList.remove('active');
        document.getElementById('game-screen').classList.add('active');
        updateGameUI();
    } else {
        alert('No saved game found!');
    }
}

// Select character class
function selectClass(className) {
    selectedClass = className;
    document.querySelectorAll('.class-card').forEach(card => {
        card.classList.remove('selected');
    });
    event.currentTarget.classList.add('selected');
    document.getElementById('start-btn').disabled = false;
}

// Start the game
function startGame() {
    const name = document.getElementById('char-name').value || 'Hero';
    
    if (!selectedClass) {
        alert('Please select a class!');
        return;
    }
    
    game.startGame(name, selectedClass);
    gameState = game.getGameState();
    
    document.getElementById('character-creation').classList.remove('active');
    document.getElementById('game-screen').classList.add('active');
    
    updateGameUI();
    addMessage(`⚔️ Welcome, ${name} the ${selectedClass}!`);
    addMessage('📜 Your adventure begins in Willowbrook Village.');
    addMessage('💡 Click "Explore" to find enemies, or "Travel" to visit new locations!');
}

// Update game UI with current state
function updateGameUI() {
    gameState = game.getGameState();
    if (!gameState || !gameState.initialized) return;
    
    const player = gameState.player;
    const location = gameState.location;
    
    // Update player info
    document.getElementById('player-name').textContent = `${player.name} the ${player.class}`;
    document.getElementById('player-level').textContent = player.level;
    document.getElementById('player-gold').textContent = player.gold;
    document.getElementById('player-attack').textContent = player.attack;
    document.getElementById('player-defense').textContent = player.defense;
    
    // Update HP bar
    const hpPercent = (player.hp / player.max_hp) * 100;
    document.getElementById('hp-bar').style.width = hpPercent + '%';
    document.getElementById('hp-text').textContent = `${player.hp}/${player.max_hp}`;
    
    // Update Mana bar
    const manaPercent = (player.mana / player.max_mana) * 100;
    document.getElementById('mana-bar').style.width = manaPercent + '%';
    document.getElementById('mana-text').textContent = `${player.mana}/${player.max_mana}`;
    
    // Update EXP bar
    const expPercent = (player.experience / player.exp_needed) * 100;
    document.getElementById('exp-bar').style.width = expPercent + '%';
    document.getElementById('exp-text').textContent = `${player.experience}/${player.exp_needed} XP`;
    
    // Update location
    document.getElementById('location-name').textContent = '📍 ' + location.name;
    document.getElementById('location-description').textContent = location.description;
    
    // Show/hide shop button
    document.getElementById('shop-btn').style.display = location.has_shop ? 'inline-block' : 'none';
    
    // Update combat panel
    if (gameState.combat_active && gameState.enemy) {
        document.getElementById('combat-panel').classList.remove('hidden');
        document.getElementById('action-buttons').classList.add('hidden');
        
        const enemy = gameState.enemy;
        document.getElementById('enemy-name').textContent = enemy.name;
        document.getElementById('enemy-sprite-name').textContent = enemy.name;
        document.getElementById('player-sprite-name').textContent = player.name;
        
        const enemyHpPercent = (enemy.hp / enemy.max_hp) * 100;
        document.getElementById('enemy-hp-bar').style.width = enemyHpPercent + '%';
        document.getElementById('enemy-hp-text').textContent = `${enemy.hp}/${enemy.max_hp}`;
        document.getElementById('enemy-combat-hp').style.width = enemyHpPercent + '%';
        document.getElementById('player-combat-hp').style.width = hpPercent + '%';
        
        updateEnemySprite(enemy.name);
    } else {
        document.getElementById('combat-panel').classList.add('hidden');
        document.getElementById('action-buttons').classList.remove('hidden');
        document.getElementById('ability-panel').classList.add('hidden');
    }
    
    // Display messages
    if (gameState.messages && gameState.messages.length > 0) {
        gameState.messages.forEach(msg => addMessage(msg));
    }
}

// Update enemy sprite
function updateEnemySprite(enemyName) {
    const spriteContainer = document.getElementById('enemy-sprite');
    if (!spriteContainer) return;
    
    const baseName = enemyName.replace(/\s*\(Lv\.\d+\)/, '').replace(/^[🔥❄️⚡💎]\s*/, '');
    const spriteData = ENEMY_SPRITES[baseName] || { bodyColor: 'linear-gradient(to bottom, #8b0000 0%, #550000 100%)', headColor: '#996633', size: 1.0, emoji: '👹' };
    
    const scale = spriteData.size;
    spriteContainer.innerHTML = `
        <div style="width: 100%; height: 100%; position: relative; transform: scale(${Math.min(scale, 1.3)});">
            <div style="position: absolute; top: -70px; left: 50%; transform: translateX(-50%); font-size: ${32 * scale}px;">${spriteData.emoji}</div>
            <div style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: ${80 * scale}px; height: ${100 * scale}px; background: ${spriteData.bodyColor}; border-radius: ${40 * scale}px ${40 * scale}px 10px 10px; box-shadow: 0 5px 20px rgba(139, 0, 0, 0.5);"></div>
            <div style="position: absolute; top: ${20 - (scale - 1) * 20}px; left: 50%; transform: translateX(-50%); width: ${50 * scale}px; height: ${50 * scale}px; background: ${spriteData.headColor}; border-radius: 50%; border: 3px solid #333;"></div>
            <div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); width: 100px; height: 8px; background: #333; border-radius: 4px; border: 2px solid #fff;">
                <div id="enemy-combat-hp" style="width: 100%; height: 100%; background: linear-gradient(to right, #f00 0%, #a00 100%); border-radius: 2px;"></div>
            </div>
            <div style="position: absolute; top: -50px; left: 50%; transform: translateX(-50%); color: #fff; font-weight: bold; font-size: 14px; text-shadow: 0 0 5px #000; white-space: nowrap;"><span id="enemy-sprite-name">${enemyName}</span></div>
        </div>
    `;
}

// Add message to messages panel
function addMessage(message) {
    const messagesDiv = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.style.marginBottom = '10px';
    messagesDiv.appendChild(messageElement);
    
    const messagesPanel = document.getElementById('messages-panel');
    messagesPanel.scrollTop = messagesPanel.scrollHeight;
}

// Clear messages
function clearMessages() {
    document.getElementById('messages').innerHTML = '';
}

// Explore current location
function explore() {
    clearMessages();
    addMessage('🔍 Searching for enemies...');
    
    const result = game.explore();
    gameState = game.getGameState();
    updateGameUI();
    
    if (result.combatStarted) {
        document.getElementById('combat-panel').style.animation = 'none';
        setTimeout(() => {
            document.getElementById('combat-panel').style.animation = 'pulse 0.5s ease-in-out';
        }, 10);
    }
}

// Combat action
function combatAction(action) {
    clearMessages();
    
    const result = game.combatAction(action);
    gameState = game.getGameState();
    
    if (action === 'attack') {
        animatePlayerAttack();
    } else if (action === 'defend') {
        const player = document.getElementById('player-sprite');
        if (player) {
            player.style.filter = 'brightness(1.3) drop-shadow(0 0 20px #4af)';
            setTimeout(() => player.style.filter = '', 500);
        }
    }
    
    setTimeout(() => {
        if (gameState.combat_active && !result.victory && !result.defeat && !result.escaped) {
            animateEnemyAttack();
        }
        updateGameUI();
        
        if (result.victory) {
            showVictoryAnimation();
        }
        if (result.defeat) {
            showDefeatAnimation();
        }
    }, 600);
}

// Animate player attack
function animatePlayerAttack() {
    const player = document.getElementById('player-sprite');
    const enemy = document.getElementById('enemy-sprite');
    
    if (player) {
        player.style.transition = 'transform 0.2s ease-out';
        player.style.transform = 'translateX(100px)';
        setTimeout(() => {
            player.style.transform = 'translateX(0)';
            if (enemy) {
                enemy.style.filter = 'brightness(2)';
                setTimeout(() => enemy.style.filter = '', 200);
            }
        }, 200);
    }
}

// Animate enemy attack
function animateEnemyAttack() {
    const enemy = document.getElementById('enemy-sprite');
    const player = document.getElementById('player-sprite');
    
    if (enemy) {
        enemy.style.transition = 'transform 0.2s ease-out';
        enemy.style.transform = 'translateX(-100px)';
        setTimeout(() => {
            enemy.style.transform = 'translateX(0)';
            if (player) {
                player.style.filter = 'brightness(2) hue-rotate(90deg)';
                setTimeout(() => player.style.filter = '', 200);
            }
        }, 200);
    }
}

// Show victory animation
function showVictoryAnimation() {
    setTimeout(() => {
        const enemy = document.getElementById('enemy-sprite');
        if (enemy) {
            enemy.style.transition = 'all 1s ease-out';
            enemy.style.transform = 'translateY(100px) rotate(90deg)';
            enemy.style.opacity = '0';
        }
        
        setTimeout(() => {
            const modal = document.createElement('div');
            modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:linear-gradient(135deg,#2ecc71,#27ae60);padding:40px;border-radius:20px;border:4px solid #ffd700;z-index:9999;text-align:center;';
            modal.innerHTML = `
                <h2 style="color:#fff;font-size:2em;margin:0;">🎉 VICTORY! 🎉</h2>
                <p style="color:#fff;font-size:1.2em;margin:20px 0;">You defeated the enemy!</p>
                <button onclick="this.parentElement.remove();updateGameUI();" style="padding:15px 30px;font-size:1.1em;background:#ffd700;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">Continue</button>
            `;
            document.body.appendChild(modal);
        }, 1000);
    }, 100);
}

// Show defeat animation
function showDefeatAnimation() {
    setTimeout(() => {
        const player = document.getElementById('player-sprite');
        if (player) {
            player.style.transition = 'all 1s ease-out';
            player.style.transform = 'translateY(50px) rotate(-45deg)';
            player.style.opacity = '0.3';
        }
        
        setTimeout(() => {
            const modal = document.createElement('div');
            modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:linear-gradient(135deg,#e74c3c,#c0392b);padding:40px;border-radius:20px;border:4px solid #000;z-index:9999;text-align:center;';
            modal.innerHTML = `
                <h2 style="color:#fff;font-size:2em;margin:0;">💀 DEFEATED 💀</h2>
                <p style="color:#fff;font-size:1.2em;margin:20px 0;">You have been defeated...</p>
                <button onclick="location.reload()" style="padding:15px 30px;font-size:1.1em;background:#ffd700;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">Try Again</button>
            `;
            document.body.appendChild(modal);
        }, 1000);
    }, 100);
}

// Show abilities panel
function showAbilities() {
    const panel = document.getElementById('ability-panel');
    
    if (!panel.classList.contains('hidden')) {
        panel.classList.add('hidden');
        return;
    }
    
    panel.classList.remove('hidden');
    
    const abilities = gameState.player.abilities;
    let html = '<h4>Choose an Ability (15 mana):</h4><div class="ability-grid">';
    abilities.forEach(ability => {
        html += `<button onclick="useAbility('${ability}')" class="btn">${ability}</button>`;
    });
    html += '</div>';
    panel.innerHTML = html;
}

// Use ability
function useAbility(abilityName) {
    clearMessages();
    
    const result = game.combatAction('ability', abilityName);
    
    if (!result.success) {
        addMessage('❌ ' + result.error);
        return;
    }
    
    gameState = game.getGameState();
    animatePlayerAttack();
    
    setTimeout(() => {
        if (gameState.combat_active && !result.victory && !result.defeat) {
            animateEnemyAttack();
        }
        updateGameUI();
        document.getElementById('ability-panel').classList.add('hidden');
        
        if (result.victory) showVictoryAnimation();
        if (result.defeat) showDefeatAnimation();
    }, 600);
}

// Show inventory
function showInventory(inCombat = false) {
    const inventory = gameState.player.inventory;
    let html = '';
    
    if (inventory.length === 0) {
        html = '<p class="text-center">Your inventory is empty.</p>';
    } else {
        html = '<div class="inventory-grid">';
        inventory.forEach((item, index) => {
            html += '<div class="item-card">';
            html += `<h4>${item.name}</h4>`;
            html += `<p>${item.description}</p>`;
            
            if (item.type === 'weapon') {
                html += `<p class="item-stats">⚔️ +${item.attackBonus} Attack</p>`;
                if (gameState.player.inventory.indexOf(item) !== -1 && 
                    game.player.equippedWeapon && game.player.equippedWeapon.name === item.name) {
                    html += '<p class="equipped">✓ Equipped</p>';
                }
            } else if (item.type === 'armor') {
                html += `<p class="item-stats">🛡️ +${item.defenseBonus} Defense</p>`;
                if (game.player.equippedArmor && game.player.equippedArmor.name === item.name) {
                    html += '<p class="equipped">✓ Equipped</p>';
                }
            }
            
            html += `<button onclick="useItem(${index}, ${inCombat})" class="btn">Use</button>`;
            html += '</div>';
        });
        html += '</div>';
    }
    
    showModal('🎒 Inventory', html);
}

// Show combat inventory
function showCombatInventory() {
    showInventory(true);
}

// Use item
function useItem(itemIndex, inCombat = false) {
    const result = game.useItem(itemIndex);
    gameState = game.getGameState();
    updateGameUI();
    closeModal();
    
    if (!inCombat && result.success) {
        setTimeout(() => showInventory(), 100);
    }
}

// Show travel options
function showTravel() {
    const location = gameState.location;
    let html = '<div class="travel-grid">';
    
    location.connections.forEach(dest => {
        const destName = WORLD[dest] ? WORLD[dest].name : dest;
        html += `<div class="travel-option" onclick="travelTo('${dest}')">`;
        html += `<h4>🚶 ${destName}</h4>`;
        html += '</div>';
    });
    
    html += '</div>';
    showModal('🚶 Travel', html);
}

// Travel to location
function travelTo(destination) {
    const result = game.travel(destination);
    gameState = game.getGameState();
    clearMessages();
    updateGameUI();
    closeModal();
}

// Show shop
function showShop() {
    const items = game.getShopItems();
    let html = `<p style="color: #2ecc71; font-size: 1.2em; margin-bottom: 20px;">💰 Your Gold: ${gameState.player.gold}</p>`;
    html += '<div class="shop-grid">';
    
    items.forEach(item => {
        html += '<div class="shop-item">';
        html += `<h4>${item.name}</h4>`;
        html += `<p>${item.description}</p>`;
        html += `<p class="price">💰 ${item.price} gold</p>`;
        html += `<button onclick="buyItem('${item.key}')" class="btn">Buy</button>`;
        html += '</div>';
    });
    
    html += '</div>';
    showModal('🏪 Shop', html);
}

// Buy item
function buyItem(itemKey) {
    const result = game.buyItem(itemKey);
    
    if (!result.success) {
        alert(result.error);
        return;
    }
    
    gameState = game.getGameState();
    updateGameUI();
    closeModal();
    showShop();
}

// Save game
function saveGame() {
    game.saveGame();
    addMessage('💾 Game saved!');
}

// Show modal
function showModal(title, content) {
    document.getElementById('modal-title').textContent = title;
    document.getElementById('modal-content').innerHTML = content;
    document.getElementById('modal-overlay').classList.remove('hidden');
}

// Close modal
function closeModal() {
    document.getElementById('modal-overlay').classList.add('hidden');
}

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});
