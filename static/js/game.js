// Game state
let gameState = null;
let selectedClass = null;

// Enemy sprite definitions - unique visuals for each enemy type
const ENEMY_SPRITES = {
    'Goblin': {
        bodyColor: 'linear-gradient(to bottom, #2d5a2d 0%, #1a3d1a 100%)',
        headColor: '#4a7c4a',
        size: 0.8,
        emoji: '👺'
    },
    'Dire Wolf': {
        bodyColor: 'linear-gradient(to bottom, #4a4a4a 0%, #2a2a2a 100%)',
        headColor: '#5a5a5a',
        size: 0.9,
        emoji: '🐺'
    },
    'Skeleton Warrior': {
        bodyColor: 'linear-gradient(to bottom, #d4d4d4 0%, #a0a0a0 100%)',
        headColor: '#e8e8e8',
        size: 1.0,
        emoji: '💀'
    },
    'Orc Raider': {
        bodyColor: 'linear-gradient(to bottom, #3d6b3d 0%, #2a4a2a 100%)',
        headColor: '#4a8a4a',
        size: 1.2,
        emoji: '👹'
    },
    'Dark Mage': {
        bodyColor: 'linear-gradient(to bottom, #4a2a6a 0%, #2a1a4a 100%)',
        headColor: '#6a4a8a',
        size: 1.0,
        emoji: '🧙'
    },
    'Cave Troll': {
        bodyColor: 'linear-gradient(to bottom, #5a6a5a 0%, #3a4a3a 100%)',
        headColor: '#6a7a6a',
        size: 1.5,
        emoji: '🧌'
    },
    'Shadow Wraith': {
        bodyColor: 'linear-gradient(to bottom, #2a2a4a 0%, #1a1a2a 100%)',
        headColor: '#3a3a5a',
        size: 1.1,
        emoji: '👻'
    },
    'Dragon Whelp': {
        bodyColor: 'linear-gradient(to bottom, #8b2500 0%, #5a1a00 100%)',
        headColor: '#aa4400',
        size: 1.3,
        emoji: '🐉'
    },
    'Vampire Lord': {
        bodyColor: 'linear-gradient(to bottom, #4a0a2a 0%, #2a0a1a 100%)',
        headColor: '#d4c4b4',
        size: 1.2,
        emoji: '🧛'
    },
    'Demon': {
        bodyColor: 'linear-gradient(to bottom, #8b0000 0%, #4a0000 100%)',
        headColor: '#aa2222',
        size: 1.3,
        emoji: '😈'
    },
    'Fire Elemental': {
        bodyColor: 'linear-gradient(to bottom, #ff6600 0%, #cc3300 100%)',
        headColor: '#ffaa00',
        size: 1.4,
        emoji: '🔥'
    },
    'Ice Golem': {
        bodyColor: 'linear-gradient(to bottom, #4a9fff 0%, #2a6fcc 100%)',
        headColor: '#8acfff',
        size: 1.5,
        emoji: '❄️'
    },
    'Storm Spirit': {
        bodyColor: 'linear-gradient(to bottom, #6a6aaa 0%, #4a4a8a 100%)',
        headColor: '#8a8acc',
        size: 1.2,
        emoji: '⚡'
    },
    'Crystal Titan': {
        bodyColor: 'linear-gradient(to bottom, #ff00ff 0%, #aa00aa 100%)',
        headColor: '#ff88ff',
        size: 1.8,
        emoji: '💎'
    },
    'Ancient Dragon': {
        bodyColor: 'linear-gradient(to bottom, #cc8800 0%, #886600 100%)',
        headColor: '#ddaa22',
        size: 1.7,
        emoji: '🐲'
    },
    'Dark Lord Malzahar': {
        bodyColor: 'linear-gradient(to bottom, #1a0a2a 0%, #0a0a1a 100%)',
        headColor: '#3a2a4a',
        size: 1.6,
        emoji: '👿'
    }
};

// Initialize game
document.addEventListener('DOMContentLoaded', () => {
    console.log('Game loaded!');
});

// Show character creation screen
function showCharacterCreation() {
    document.getElementById('title-screen').classList.remove('active');
    document.getElementById('character-creation').classList.add('active');
}

// Select character class
function selectClass(className) {
    selectedClass = className;
    
    // Update UI
    document.querySelectorAll('.class-card').forEach(card => {
        card.classList.remove('selected');
    });
    event.currentTarget.classList.add('selected');
    
    // Enable start button
    document.getElementById('start-btn').disabled = false;
}

// Start the game
async function startGame() {
    const name = document.getElementById('char-name').value || 'Hero';
    
    if (!selectedClass) {
        alert('Please select a class!');
        return;
    }
    
    try {
        const response = await fetch('/api/start_game', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, class: selectedClass })
        });
        
        const data = await response.json();
        
        if (data.success) {
            gameState = data.game_state;
            
            // Hide character creation, show game screen
            document.getElementById('character-creation').classList.remove('active');
            document.getElementById('game-screen').classList.add('active');
            
            updateGameUI();
            addMessage(data.message);
            addMessage('📜 Quest Received: First Steps - Defeat 3 enemies to prove your worth.');
        } else {
            // Show specific error if available
            const errorMsg = data.error || 'Unknown error occurred';
            console.error('Game start failed:', errorMsg);
            alert('Failed to start game: ' + errorMsg);
        }
    } catch (error) {
        console.error('Error starting game:', error);
        alert('Failed to start game. Please check the console for details.');
    }
}

// Update game UI with current state
function updateGameUI() {
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
    
    // Update weather display
    if (gameState.weather) {
        const weather = gameState.weather;
        const weatherDiv = document.getElementById('weather-display');
        if (weatherDiv) {
            const hasEvents = weather.events && weather.events > 0;
            weatherDiv.innerHTML = `
                <div class="weather-info">
                    <div class="weather-header">
                        <strong style="font-size: 1.1em; color: #ffd700;">${weather.emoji} ${weather.name}</strong>
                    </div>
                    <p style="margin: 5px 0; font-size: 0.9em;">${weather.description}</p>
                    ${hasEvents ? 
                        '<p style="color: #ff6b6b; font-size: 0.85em; margin-top: 5px; font-weight: 600;">⚠️ Weather events may occur in combat!</p>' 
                        : ''}
                </div>
            `;
        }
    }
    
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
        
        // Reset and update enemy sprite visibility and appearance
        const enemySprite = document.getElementById('enemy-sprite');
        const playerSprite = document.getElementById('player-sprite');
        if (enemySprite) {
            enemySprite.style.opacity = '1';
            enemySprite.style.transform = 'translateX(0) rotate(0)';
            enemySprite.style.transition = 'all 0.3s ease';
        }
        if (playerSprite) {
            playerSprite.style.opacity = '1';
            playerSprite.style.transform = 'translateX(0) rotate(0)';
            playerSprite.style.transition = 'all 0.3s ease';
        }
        
        // Update enemy sprite appearance based on enemy type
        updateEnemySprite(enemy.name);
        
        // Update sprite HP bars
        if (window.visualEffects) {
            window.visualEffects.animateHPDrain('player-combat-hp', player.hp, player.max_hp);
            window.visualEffects.animateHPDrain('enemy-combat-hp', enemy.hp, enemy.max_hp);
        }
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

// Update enemy sprite based on enemy type
function updateEnemySprite(enemyName) {
    const spriteContainer = document.getElementById('enemy-sprite');
    if (!spriteContainer) return;
    
    // Extract base enemy name (remove level indicator like "(Lv.1)")
    const baseName = enemyName.replace(/\s*\(Lv\.\d+\)/, '').replace(/^[🔥❄️⚡💎]\s*/, '');
    
    // Get sprite data or use default
    const spriteData = ENEMY_SPRITES[baseName] || {
        bodyColor: 'linear-gradient(to bottom, #8b0000 0%, #550000 100%)',
        headColor: '#996633',
        size: 1.0,
        emoji: '👹'
    };
    
    const scale = spriteData.size;
    const bodyWidth = 80 * scale;
    const bodyHeight = 100 * scale;
    const headSize = 50 * scale;
    
    // Build the sprite HTML with unique appearance
    spriteContainer.innerHTML = `
        <div style="width: 100%; height: 100%; position: relative; transform: scale(${Math.min(scale, 1.3)});">
            <!-- Enemy Emoji Icon (floating above) -->
            <div style="position: absolute; top: -70px; left: 50%; transform: translateX(-50%); font-size: ${32 * scale}px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.5));">${spriteData.emoji}</div>
            
            <!-- Enemy Character Visual -->
            <div style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: ${bodyWidth}px; height: ${bodyHeight}px; background: ${spriteData.bodyColor}; border-radius: ${bodyWidth/2}px ${bodyWidth/2}px 10px 10px; box-shadow: 0 5px 20px rgba(139, 0, 0, 0.5);"></div>
            
            <!-- Head -->
            <div style="position: absolute; top: ${20 - (scale - 1) * 20}px; left: 50%; transform: translateX(-50%); width: ${headSize}px; height: ${headSize}px; background: ${spriteData.headColor}; border-radius: 50%; border: 3px solid #333; box-shadow: 0 0 15px rgba(255, 0, 0, 0.3);"></div>
            
            <!-- Weapon/Claw -->
            <div style="position: absolute; bottom: ${30 * scale}px; left: -10px; width: ${60 * scale}px; height: ${8 * scale}px; background: linear-gradient(to left, #666 0%, #999 50%, #ddd 100%); transform: rotate(45deg); border-radius: 2px; box-shadow: 0 0 10px rgba(255, 0, 0, 0.5);"></div>
            
            <!-- HP Bar above enemy -->
            <div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); width: 100px; height: 8px; background: #333; border-radius: 4px; border: 2px solid #fff;">
                <div id="enemy-combat-hp" style="width: 100%; height: 100%; background: linear-gradient(to right, #f00 0%, #a00 100%); border-radius: 2px; transition: width 0.5s ease;"></div>
            </div>
            
            <!-- Enemy name -->
            <div style="position: absolute; top: -50px; left: 50%; transform: translateX(-50%); color: #fff; font-weight: bold; font-size: 14px; text-shadow: 0 0 5px #000; white-space: nowrap;">
                <span id="enemy-sprite-name">${enemyName}</span>
            </div>
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
    
    // Scroll to bottom
    const messagesPanel = document.getElementById('messages-panel');
    messagesPanel.scrollTop = messagesPanel.scrollHeight;
}

// Clear messages
function clearMessages() {
    document.getElementById('messages').innerHTML = '';
}

// Explore current location
async function explore() {
    clearMessages();
    addMessage('🔍 Searching for enemies...');
    
    try {
        const response = await fetch('/api/explore', { method: 'POST' });
        const data = await response.json();
        
        if (data.success) {
            gameState = data.game_state;
            updateGameUI();
            
            if (data.combat_started) {
                // Flash the screen for combat start
                document.getElementById('combat-panel').style.animation = 'none';
                setTimeout(() => {
                    document.getElementById('combat-panel').style.animation = 'pulse 0.5s ease-in-out';
                }, 10);
            }
        } else {
            addMessage('❌ ' + (data.error || 'Error exploring area'));
        }
    } catch (error) {
        console.error('Error exploring:', error);
        addMessage('❌ Error exploring area. Check console for details.');
    }
}

// Combat action
async function combatAction(action) {
    if (!window.visualEffects) {
        console.error('Visual effects not loaded!');
        return;
    }
    
    const effects = window.visualEffects;
    
    clearMessages();
    
    try {
        const response = await fetch('/api/combat_action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action })
        });
        
        const data = await response.json();
        
        if (data.success) {
            gameState = data.game_state;
            
            // SHOW VISUAL ATTACK ANIMATION!
            if (action === 'attack') {
                effects.playerAttack();
            } else if (action === 'defend') {
                // Show shield effect
                const player = document.getElementById('player-sprite');
                if (player) {
                    player.style.filter = 'brightness(1.3) drop-shadow(0 0 20px #4af)';
                    setTimeout(() => player.style.filter = '', 500);
                }
            }
            
            // Wait for player animation to finish
            await new Promise(resolve => setTimeout(resolve, 600));
            
            // Check for weather events in messages
            const messages = data.game_state.messages || [];
            for (const msg of messages) {
                if (msg.includes('🌩️')) {
                    // Weather event triggered!
                    if (msg.includes('Lightning Strike') || msg.includes('Chain Lightning')) {
                        effects.showLightningStrike('enemy');
                        await new Promise(resolve => setTimeout(resolve, 800));
                    } else if (msg.includes('Thunder Crash')) {
                        effects.showThunderCrash();
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Solar Flare') || msg.includes('Fire') || msg.includes('Heat Wave')) {
                        effects.showFireBlast(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Blizzard') || msg.includes('Ice') || msg.includes('Frostbite')) {
                        effects.showIceBlast(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1500));
                    } else if (msg.includes('Wind') || msg.includes('Gale') || msg.includes('Sandstorm')) {
                        effects.showWindGust(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 800));
                    } else if (msg.includes('Heal') || msg.includes('Regenerat') || msg.includes('Rain')) {
                        effects.showHealEffect(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Crystal') || msg.includes('Prismatic')) {
                        effects.showCrystalShower(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Shadow') || msg.includes('Eclipse') || msg.includes('Void') || msg.includes('Dark')) {
                        effects.showDarknessPulse(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1200));
                    }
                }
            }
            
            // Enemy turn animation if combat continues
            if (gameState.combat_active && !data.victory && !data.defeat) {
                await new Promise(resolve => setTimeout(resolve, 400));
                effects.enemyAttack();
                await new Promise(resolve => setTimeout(resolve, 600));
            }
            
            // Update HP bars with animation
            if (gameState.player) {
                effects.animateHPDrain('player-combat-hp', gameState.player.hp, gameState.player.max_hp);
                effects.animateHPDrain('hp-bar', gameState.player.hp, gameState.player.max_hp);
            }
            if (gameState.enemy) {
                effects.animateHPDrain('enemy-combat-hp', gameState.enemy.hp, gameState.enemy.max_hp);
                effects.animateHPDrain('enemy-hp-bar', gameState.enemy.hp, gameState.enemy.max_hp);
            }
            
            updateGameUI();
            
            if (data.victory) {
                // Victory animation!
                setTimeout(() => {
                    const enemy = document.getElementById('enemy-sprite');
                    if (enemy) {
                        enemy.style.transition = 'all 1s ease-out';
                        enemy.style.transform = 'translateY(100px) rotate(90deg)';
                        enemy.style.opacity = '0';
                    }
                    
                    // Victory flash
                    effects.screenFlash('#ffd700', 0.5);
                    
                    // Confetti!
                    for (let i = 0; i < 50; i++) {
                        setTimeout(() => {
                            effects.createParticles(
                                window.innerWidth / 2,
                                window.innerHeight / 4,
                                5,
                                ['#ffd700', '#ff6600', '#4af', '#f0f'][Math.floor(Math.random() * 4)]
                            );
                        }, i * 50);
                    }
                    
                    // Victory modal
                    setTimeout(() => {
                        const modal = document.createElement('div');
                        modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:linear-gradient(135deg,#2ecc71,#27ae60);padding:40px;border-radius:20px;border:4px solid #ffd700;z-index:9999;text-align:center;box-shadow:0 0 50px rgba(46,204,113,0.5);';
                        modal.innerHTML = `
                            <h2 style="color:#fff;font-size:3em;margin:0;">🎉 VICTORY! 🎉</h2>
                            <p style="color:#fff;font-size:1.5em;margin:20px 0;">You defeated the enemy!</p>
                            <button onclick="this.parentElement.remove()" style="padding:15px 30px;font-size:1.2em;background:#ffd700;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">Continue</button>
                        `;
                        document.body.appendChild(modal);
                    }, 2000);
                }, 100);
            }
            
            if (data.defeat) {
                // Defeat animation
                setTimeout(() => {
                    const player = document.getElementById('player-sprite');
                    if (player) {
                        player.style.transition = 'all 1s ease-out';
                        player.style.transform = 'translateY(50px) rotate(-45deg)';
                        player.style.opacity = '0.3';
                    }
                    effects.screenFlash('#000', 1);
                    
                    setTimeout(() => {
                        const modal = document.createElement('div');
                        modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:linear-gradient(135deg,#e74c3c,#c0392b);padding:40px;border-radius:20px;border:4px solid #000;z-index:9999;text-align:center;box-shadow:0 0 50px rgba(231,76,60,0.5);';
                        modal.innerHTML = `
                            <h2 style="color:#fff;font-size:3em;margin:0;">💀 DEFEATED 💀</h2>
                            <p style="color:#fff;font-size:1.5em;margin:20px 0;">You have been defeated...</p>
                            <button onclick="location.reload()" style="padding:15px 30px;font-size:1.2em;background:#ffd700;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">Try Again</button>
                        `;
                        document.body.appendChild(modal);
                    }, 1000);
                }, 100);
            }
            
            if (data.escaped) {
                // Escape animation
                const player = document.getElementById('player-sprite');
                if (player) {
                    player.style.transition = 'all 0.5s ease-out';
                    player.style.transform = 'translateX(-200px)';
                    player.style.opacity = '0';
                }
                addMessage('💨 You successfully escaped!');
            }
        }
    } catch (error) {
        console.error('Error in combat:', error);
        addMessage('❌ Error performing action');
    }
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
    let html = '<h4>Choose an Ability:</h4><div class="ability-grid">';
    
    abilities.forEach(ability => {
        html += `<button onclick="useAbility('${ability}')" class="btn">${ability}</button>`;
    });
    
    html += '</div>';
    panel.innerHTML = html;
}

// Use ability with visual effects!
async function useAbility(abilityName) {
    if (!window.visualEffects) {
        console.error('Visual effects not loaded!');
        return;
    }
    
    const effects = window.visualEffects;
    
    clearMessages();
    
    // SHOW ABILITY ANIMATION BASED ON ABILITY!
    const abilityAnimations = {
        // Warrior abilities
        'Shield Bash': () => effects.warriorBash(),
        'Power Strike': () => effects.warriorBash(),
        'Whirlwind': () => effects.warriorCleave(),
        
        // Mage abilities
        'Fireball': () => effects.mageFireball(),
        'Ice Blast': () => effects.mageIceBlast(),
        'Lightning Strike': () => effects.mageLightningBolt(),
        
        // Rogue abilities
        'Backstab': () => effects.rogueBackstab(),
        'Poison Strike': () => effects.roguePoisonStrike(),
        'Shadow Step': () => effects.rogueShadowStrike(),
        
        // Cleric abilities
        'Heal': () => effects.showHealEffect('player'),
        'Smite': () => effects.mageLightningBolt(),
        'Divine Shield': () => {
            const player = document.getElementById('player-sprite');
            if (player) {
                player.style.filter = 'brightness(1.5) drop-shadow(0 0 30px #ffd700)';
                effects.screenFlash('#ffd700', 0.5);
                setTimeout(() => player.style.filter = '', 1000);
            }
        }
    };
    
    // Play the animation!
    if (abilityAnimations[abilityName]) {
        abilityAnimations[abilityName]();
        await new Promise(resolve => setTimeout(resolve, 800));
    }
    
    try {
        const response = await fetch('/api/combat_action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action: 'ability', ability: abilityName })
        });
        
        // Check if response is actually JSON
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
            console.error('Server returned non-JSON response');
            addMessage('❌ Server error. Please refresh the page.');
            return;
        }
        
        const data = await response.json();
        
        if (data.success) {
            gameState = data.game_state;
            
            // Check for weather events
            const messages = data.game_state.messages || [];
            for (const msg of messages) {
                if (msg.includes('🌩️')) {
                    // Weather event triggered!
                    if (msg.includes('Lightning Strike') || msg.includes('Chain Lightning')) {
                        effects.showLightningStrike('enemy');
                        await new Promise(resolve => setTimeout(resolve, 800));
                    } else if (msg.includes('Thunder Crash')) {
                        effects.showThunderCrash();
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Solar Flare') || msg.includes('Fire') || msg.includes('Heat Wave')) {
                        effects.showFireBlast(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Blizzard') || msg.includes('Ice') || msg.includes('Frostbite')) {
                        effects.showIceBlast(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1500));
                    } else if (msg.includes('Wind') || msg.includes('Gale') || msg.includes('Sandstorm')) {
                        effects.showWindGust(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 800));
                    } else if (msg.includes('Heal') || msg.includes('Regenerat') || msg.includes('Rain')) {
                        effects.showHealEffect(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Crystal') || msg.includes('Prismatic')) {
                        effects.showCrystalShower(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1000));
                    } else if (msg.includes('Shadow') || msg.includes('Eclipse') || msg.includes('Void') || msg.includes('Dark')) {
                        effects.showDarknessPulse(msg.includes('enemy') ? 'enemy' : 'player');
                        await new Promise(resolve => setTimeout(resolve, 1200));
                    }
                }
            }
            
            // Enemy turn animation if combat continues
            if (gameState.combat_active && !data.victory && !data.defeat) {
                await new Promise(resolve => setTimeout(resolve, 400));
                effects.enemyAttack();
                await new Promise(resolve => setTimeout(resolve, 600));
            }
            
            // Update HP bars with animation
            if (gameState.player) {
                effects.animateHPDrain('player-combat-hp', gameState.player.hp, gameState.player.max_hp);
                effects.animateHPDrain('hp-bar', gameState.player.hp, gameState.player.max_hp);
            }
            if (gameState.enemy) {
                effects.animateHPDrain('enemy-combat-hp', gameState.enemy.hp, gameState.enemy.max_hp);
                effects.animateHPDrain('enemy-hp-bar', gameState.enemy.hp, gameState.enemy.max_hp);
            }
            
            updateGameUI();
            document.getElementById('ability-panel').classList.add('hidden');
            
            if (data.victory) {
                // Victory animation!
                setTimeout(() => {
                    const enemy = document.getElementById('enemy-sprite');
                    if (enemy) {
                        enemy.style.transition = 'all 1s ease-out';
                        enemy.style.transform = 'translateY(100px) rotate(90deg)';
                        enemy.style.opacity = '0';
                    }
                    
                    effects.screenFlash('#ffd700', 0.5);
                    
                    // Confetti!
                    for (let i = 0; i < 50; i++) {
                        setTimeout(() => {
                            effects.createParticles(
                                window.innerWidth / 2,
                                window.innerHeight / 4,
                                5,
                                ['#ffd700', '#ff6600', '#4af', '#f0f'][Math.floor(Math.random() * 4)]
                            );
                        }, i * 50);
                    }
                    
                    setTimeout(() => {
                        const modal = document.createElement('div');
                        modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:linear-gradient(135deg,#2ecc71,#27ae60);padding:40px;border-radius:20px;border:4px solid #ffd700;z-index:9999;text-align:center;box-shadow:0 0 50px rgba(46,204,113,0.5);';
                        modal.innerHTML = `
                            <h2 style="color:#fff;font-size:3em;margin:0;">🎉 VICTORY! 🎉</h2>
                            <p style="color:#fff;font-size:1.5em;margin:20px 0;">You defeated the enemy!</p>
                            <button onclick="this.parentElement.remove()" style="padding:15px 30px;font-size:1.2em;background:#ffd700;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">Continue</button>
                        `;
                        document.body.appendChild(modal);
                    }, 2000);
                }, 100);
            }
            
            if (data.defeat) {
                setTimeout(() => {
                    const player = document.getElementById('player-sprite');
                    if (player) {
                        player.style.transition = 'all 1s ease-out';
                        player.style.transform = 'translateY(50px) rotate(-45deg)';
                        player.style.opacity = '0.3';
                    }
                    effects.screenFlash('#000', 1);
                    
                    setTimeout(() => {
                        const modal = document.createElement('div');
                        modal.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:linear-gradient(135deg,#e74c3c,#c0392b);padding:40px;border-radius:20px;border:4px solid #000;z-index:9999;text-align:center;box-shadow:0 0 50px rgba(231,76,60,0.5);';
                        modal.innerHTML = `
                            <h2 style="color:#fff;font-size:3em;margin:0;">💀 DEFEATED 💀</h2>
                            <p style="color:#fff;font-size:1.5em;margin:20px 0;">You have been defeated...</p>
                            <button onclick="location.reload()" style="padding:15px 30px;font-size:1.2em;background:#ffd700;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">Try Again</button>
                        `;
                        document.body.appendChild(modal);
                    }, 1000);
                }, 100);
            }
        }
    } catch (error) {
        console.error('Error using ability:', error);
        addMessage('❌ Error using ability');
    }
}

// Show combat inventory
function showCombatInventory() {
    showInventory(true);
}

// Show inventory
async function showInventory(inCombat = false) {
    try {
        const response = await fetch('/api/inventory');
        const data = await response.json();
        
        if (data.success) {
            let html = '';
            
            if (data.inventory.length === 0) {
                html = '<p class="text-center">Your inventory is empty.</p>';
            } else {
                html = '<div class="inventory-grid">';
                
                data.inventory.forEach(item => {
                    html += '<div class="item-card">';
                    html += `<h4>${item.name}</h4>`;
                    html += `<p>${item.description}</p>`;
                    
                    if (item.type === 'Weapon') {
                        html += `<p class="item-stats">⚔️ +${item.attack_bonus} Attack</p>`;
                        if (item.equipped) {
                            html += '<p class="equipped">✓ Equipped</p>';
                        }
                    } else if (item.type === 'Armor') {
                        html += `<p class="item-stats">🛡️ +${item.defense_bonus} Defense</p>`;
                        if (item.equipped) {
                            html += '<p class="equipped">✓ Equipped</p>';
                        }
                    }
                    
                    html += `<button onclick="useItem(${item.index}, ${inCombat})" class="btn">Use</button>`;
                    html += '</div>';
                });
                
                html += '</div>';
            }
            
            showModal('🎒 Inventory', html);
        }
    } catch (error) {
        console.error('Error loading inventory:', error);
    }
}

// Use item
async function useItem(itemIndex, inCombat = false) {
    try {
        const response = await fetch('/api/use_item', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ item_index: itemIndex })
        });
        
        const data = await response.json();
        
        if (data.success) {
            gameState = data.game_state;
            updateGameUI();
            closeModal();
            
            if (!inCombat) {
                showInventory();
            }
        }
    } catch (error) {
        console.error('Error using item:', error);
    }
}

// Show travel options
function showTravel() {
    const location = gameState.location;
    
    let html = '<div class="travel-grid">';
    
    location.connections.forEach(destination => {
        html += `<div class="travel-option" onclick="travelTo('${destination}')">`;
        html += `<h4>🚶 ${destination}</h4>`;
        html += '</div>';
    });
    
    html += '</div>';
    
    showModal('🚶 Travel', html);
}

// Travel to location
async function travelTo(destination) {
    try {
        const response = await fetch('/api/travel', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ destination })
        });
        
        const data = await response.json();
        
        if (data.success) {
            gameState = data.game_state;
            clearMessages();
            updateGameUI();
            closeModal();
        }
    } catch (error) {
        console.error('Error traveling:', error);
    }
}

// Show quests
async function showQuests() {
    try {
        const response = await fetch('/api/quests');
        const data = await response.json();
        
        if (data.success) {
            let html = '';
            
            if (data.active_quests.length === 0 && data.completed_quests.length === 0) {
                html = '<p class="text-center">No quests available.</p>';
            } else {
                if (data.active_quests.length > 0) {
                    html += '<h4 style="color: #ffd700; margin-bottom: 15px;">Active Quests:</h4>';
                    html += '<div class="quest-list">';
                    
                    data.active_quests.forEach(quest => {
                        html += '<div class="quest-card">';
                        html += `<h4>${quest.name}</h4>`;
                        html += `<p>${quest.description}</p>`;
                        html += '<ul class="quest-objectives">';
                        
                        quest.objectives.forEach(obj => {
                            const status = obj.completed ? '✓' : '○';
                            const className = obj.completed ? 'completed' : '';
                            html += `<li class="${className}">${status} ${obj.name}</li>`;
                        });
                        
                        html += '</ul>';
                        
                        if (quest.complete) {
                            html += '<p style="color: #2ecc71; margin-top: 10px;">✓ Ready to complete!</p>';
                        }
                        
                        html += '</div>';
                    });
                    
                    html += '</div>';
                }
                
                if (data.completed_quests.length > 0) {
                    html += '<h4 style="color: #ffd700; margin: 25px 0 15px;">Completed Quests:</h4>';
                    html += '<div class="quest-list">';
                    
                    data.completed_quests.forEach(quest => {
                        html += '<div class="quest-card" style="opacity: 0.7;">';
                        html += `<h4>✓ ${quest.name}</h4>`;
                        html += `<p>${quest.description}</p>`;
                        html += '</div>';
                    });
                    
                    html += '</div>';
                }
            }
            
            // Update game state with any messages
            if (data.messages && data.messages.length > 0) {
                data.messages.forEach(msg => addMessage(msg));
                // Refresh game state
                const stateResponse = await fetch('/api/game_state');
                const stateData = await stateResponse.json();
                gameState = stateData;
                updateGameUI();
            }
            
            showModal('📜 Quests', html);
        }
    } catch (error) {
        console.error('Error loading quests:', error);
    }
}

// Show shop
async function showShop() {
    try {
        const response = await fetch('/api/shop');
        const data = await response.json();
        
        if (data.success) {
            let html = `<p style="color: #2ecc71; font-size: 1.2em; margin-bottom: 20px;">💰 Your Gold: ${gameState.player.gold}</p>`;
            html += '<div class="shop-grid">';
            
            data.items.forEach(item => {
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
    } catch (error) {
        console.error('Error loading shop:', error);
    }
}

// Buy item from shop
async function buyItem(itemKey) {
    try {
        const response = await fetch('/api/shop/buy', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ item_key: itemKey })
        });
        
        const data = await response.json();
        
        if (data.success) {
            gameState = data.game_state;
            updateGameUI();
            closeModal();
            showShop();
        } else {
            alert(data.error || 'Cannot buy this item');
        }
    } catch (error) {
        console.error('Error buying item:', error);
    }
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



