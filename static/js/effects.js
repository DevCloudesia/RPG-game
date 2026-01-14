// ===================================
// VISUAL EFFECTS SYSTEM - NO TEXT!
// ===================================

class VisualEffects {
    constructor() {
        this.container = document.getElementById('weather-effects') || this.createContainer();
        this.playerSprite = null;
        this.enemySprite = null;
    }

    createContainer() {
        const container = document.createElement('div');
        container.id = 'weather-effects';
        document.body.appendChild(container);
        return container;
    }

    // ===================================
    // LIGHTNING STRIKE - Show actual lightning!
    // ===================================
    showLightningStrike(target = 'enemy') {
        const targetEl = target === 'enemy' ? 
            document.getElementById('enemy-sprite') : 
            document.getElementById('player-sprite');
        
        if (!targetEl) return;

        const rect = targetEl.getBoundingClientRect();
        
        // Create 3-5 lightning bolts
        const numBolts = 3 + Math.floor(Math.random() * 3);
        
        for (let i = 0; i < numBolts; i++) {
            setTimeout(() => {
                const lightning = document.createElement('div');
                lightning.className = 'lightning-effect';
                lightning.style.left = (rect.left + Math.random() * rect.width) + 'px';
                lightning.style.top = '0';
                this.container.appendChild(lightning);
                
                // Thunder flash
                this.screenFlash('#4af', 0.3);
                this.screenShake();
                
                // Remove after animation
                setTimeout(() => lightning.remove(), 400);
            }, i * 100);
        }

        // Damage number
        setTimeout(() => {
            this.showDamageNumber(rect.left + rect.width/2, rect.top, 25, 'lightning');
        }, 300);
    }

    // ===================================
    // FIRE/SOLAR BLAST - Show flames!
    // ===================================
    showFireBlast(target = 'enemy') {
        const targetEl = target === 'enemy' ? 
            document.getElementById('enemy-sprite') : 
            document.getElementById('player-sprite');
        
        if (!targetEl) return;

        const rect = targetEl.getBoundingClientRect();
        
        // Create expanding fire effect
        const fire = document.createElement('div');
        fire.className = 'fire-effect';
        fire.style.left = (rect.left + rect.width/2 - 100) + 'px';
        fire.style.top = (rect.top + rect.height/2 - 100) + 'px';
        this.container.appendChild(fire);
        
        // Screen flash
        this.screenFlash('#ff6600', 0.4);
        
        // Particles
        this.createParticles(rect.left + rect.width/2, rect.top + rect.height/2, 20, '#ff6600');
        
        setTimeout(() => fire.remove(), 1000);
        
        // Damage number
        setTimeout(() => {
            this.showDamageNumber(rect.left + rect.width/2, rect.top, 30, 'fire');
        }, 500);
    }

    // ===================================
    // ICE/FROST - Show ice shards falling!
    // ===================================
    showIceBlast(target = 'enemy') {
        const targetEl = target === 'enemy' ? 
            document.getElementById('enemy-sprite') : 
            document.getElementById('player-sprite');
        
        if (!targetEl) return;

        const rect = targetEl.getBoundingClientRect();
        
        // Create multiple ice shards
        for (let i = 0; i < 15; i++) {
            setTimeout(() => {
                const shard = document.createElement('div');
                shard.className = 'ice-shard';
                shard.style.left = (rect.left + Math.random() * rect.width) + 'px';
                shard.style.top = '-50px';
                this.container.appendChild(shard);
                
                setTimeout(() => shard.remove(), 1500);
            }, i * 50);
        }
        
        // Freeze effect
        if (targetEl) {
            targetEl.style.filter = 'brightness(0.5) hue-rotate(180deg)';
            setTimeout(() => {
                targetEl.style.filter = '';
            }, 1500);
        }
        
        // Damage number
        setTimeout(() => {
            this.showDamageNumber(rect.left + rect.width/2, rect.top, 20, 'ice');
        }, 800);
    }

    // ===================================
    // WIND GUST - Show wind blowing!
    // ===================================
    showWindGust(target = 'enemy') {
        const targetEl = target === 'enemy' ? 
            document.getElementById('enemy-sprite') : 
            document.getElementById('player-sprite');
        
        if (!targetEl) return;

        const rect = targetEl.getBoundingClientRect();
        
        // Create wind lines
        for (let i = 0; i < 5; i++) {
            const wind = document.createElement('div');
            wind.className = 'wind-effect';
            wind.style.top = (rect.top + i * 30) + 'px';
            this.container.appendChild(wind);
            
            setTimeout(() => wind.remove(), 800);
        }
        
        // Push target
        if (targetEl) {
            const originalTransform = targetEl.style.transform;
            targetEl.style.transform = 'translateX(50px) rotate(10deg)';
            setTimeout(() => {
                targetEl.style.transform = originalTransform;
            }, 300);
        }
        
        // Damage number
        setTimeout(() => {
            this.showDamageNumber(rect.left + rect.width/2, rect.top, 22, 'wind');
        }, 400);
    }

    // ===================================
    // HEALING EFFECT - Show green pulse!
    // ===================================
    showHealEffect(target = 'player') {
        const targetEl = target === 'player' ? 
            document.getElementById('player-sprite') : 
            document.getElementById('enemy-sprite');
        
        if (!targetEl) return;

        const rect = targetEl.getBoundingClientRect();
        
        // Healing pulse
        const heal = document.createElement('div');
        heal.className = 'heal-effect';
        heal.style.left = (rect.left + rect.width/2 - 150) + 'px';
        heal.style.top = (rect.top + rect.height/2 - 150) + 'px';
        this.container.appendChild(heal);
        
        // Green flash
        this.screenFlash('#0f0', 0.3);
        
        // Particles
        this.createParticles(rect.left + rect.width/2, rect.top + rect.height/2, 15, '#0f0');
        
        // Glow effect on target
        if (targetEl) {
            targetEl.style.filter = 'brightness(1.5) drop-shadow(0 0 20px #0f0)';
            setTimeout(() => {
                targetEl.style.filter = '';
            }, 1000);
        }
        
        setTimeout(() => heal.remove(), 1000);
        
        // Heal number
        setTimeout(() => {
            this.showDamageNumber(rect.left + rect.width/2, rect.top, 25, 'heal');
        }, 500);
    }

    // ===================================
    // THUNDER CRASH - Screen flash + shake!
    // ===================================
    showThunderCrash() {
        // Multiple lightning bolts everywhere
        for (let i = 0; i < 8; i++) {
            setTimeout(() => {
                const lightning = document.createElement('div');
                lightning.className = 'lightning-effect';
                lightning.style.left = (Math.random() * window.innerWidth) + 'px';
                lightning.style.top = '0';
                this.container.appendChild(lightning);
                
                setTimeout(() => lightning.remove(), 400);
            }, i * 80);
        }
        
        // Thunder flash
        const thunder = document.createElement('div');
        thunder.className = 'thunder-effect';
        this.container.appendChild(thunder);
        setTimeout(() => thunder.remove(), 600);
        
        // Massive screen shake
        this.screenShake(15);
        
        // Damage both
        setTimeout(() => {
            const player = document.getElementById('player-sprite');
            const enemy = document.getElementById('enemy-sprite');
            if (player) {
                const rect = player.getBoundingClientRect();
                this.showDamageNumber(rect.left + rect.width/2, rect.top, 30, 'lightning');
            }
            if (enemy) {
                const rect = enemy.getBoundingClientRect();
                this.showDamageNumber(rect.left + rect.width/2, rect.top, 30, 'lightning');
            }
        }, 300);
    }

    // ===================================
    // CRYSTAL EFFECTS - Shimmering crystals!
    // ===================================
    showCrystalShower(target = 'enemy') {
        const targetEl = target === 'enemy' ? 
            document.getElementById('enemy-sprite') : 
            document.getElementById('player-sprite');
        
        if (!targetEl) return;

        const rect = targetEl.getBoundingClientRect();
        
        // Create crystal shards
        for (let i = 0; i < 20; i++) {
            setTimeout(() => {
                const crystal = document.createElement('div');
                crystal.className = 'crystal-effect';
                crystal.style.left = (rect.left + Math.random() * rect.width) + 'px';
                crystal.style.top = (rect.top + Math.random() * rect.height) + 'px';
                this.container.appendChild(crystal);
                
                setTimeout(() => crystal.remove(), 1000);
            }, i * 40);
        }
        
        // Rainbow flash
        this.screenFlash('#f0f', 0.5);
        
        // Damage number
        setTimeout(() => {
            this.showDamageNumber(rect.left + rect.width/2, rect.top, 50, 'crit');
        }, 600);
    }

    // ===================================
    // DARKNESS/ECLIPSE - Dark pulse!
    // ===================================
    showDarknessPulse(target = 'enemy') {
        const dark = document.createElement('div');
        dark.className = 'dark-effect';
        this.container.appendChild(dark);
        
        setTimeout(() => dark.remove(), 1200);
        
        const targetEl = target === 'enemy' ? 
            document.getElementById('enemy-sprite') : 
            document.getElementById('player-sprite');
        
        if (targetEl) {
            const rect = targetEl.getBoundingClientRect();
            setTimeout(() => {
                this.showDamageNumber(rect.left + rect.width/2, rect.top, 45, 'dark');
            }, 600);
        }
    }

    // ===================================
    // PLAYER ATTACK ANIMATION
    // ===================================
    playerAttack() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const playerRect = player.getBoundingClientRect();
        const enemyRect = enemy.getBoundingClientRect();
        
        // Move player forward
        player.style.transition = 'transform 0.2s ease-out';
        player.style.transform = 'translateX(100px) scale(1.1)';
        
        // Slash effect
        setTimeout(() => {
            this.createSlashEffect(enemyRect.left - 50, enemyRect.top + enemyRect.height/2);
            
            // Enemy recoil
            enemy.style.transition = 'transform 0.1s ease-out';
            enemy.style.transform = 'translateX(30px) rotate(-10deg)';
            enemy.style.filter = 'brightness(1.5)';
            
            // Damage number
            const damage = 15 + Math.floor(Math.random() * 20);
            this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, damage, 'physical');
            
            // Blood particles
            this.createParticles(enemyRect.left + enemyRect.width/2, enemyRect.top + enemyRect.height/2, 10, '#ff0000');
        }, 200);
        
        // Return player
        setTimeout(() => {
            player.style.transform = 'translateX(0) scale(1)';
            enemy.style.transform = 'translateX(0) rotate(0)';
            enemy.style.filter = '';
        }, 400);
    }

    // ===================================
    // WARRIOR ABILITIES
    // ===================================
    warriorBash() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const enemyRect = enemy.getBoundingClientRect();
        
        // Player charges forward FAST
        player.style.transition = 'transform 0.15s ease-out';
        player.style.transform = 'translateX(120px) scale(1.2)';
        
        setTimeout(() => {
            // BASH impact!
            this.screenShake(15);
            this.screenFlash('#ffaa00', 0.3);
            
            // Shockwave
            const shockwave = document.createElement('div');
            shockwave.style.cssText = `
                position: absolute;
                left: ${enemyRect.left + enemyRect.width/2 - 50}px;
                top: ${enemyRect.top + enemyRect.height/2 - 50}px;
                width: 100px;
                height: 100px;
                border: 5px solid #ffaa00;
                border-radius: 50%;
                opacity: 1;
                transition: all 0.5s ease-out;
            `;
            this.container.appendChild(shockwave);
            
            setTimeout(() => {
                shockwave.style.width = '300px';
                shockwave.style.height = '300px';
                shockwave.style.left = (enemyRect.left + enemyRect.width/2 - 150) + 'px';
                shockwave.style.top = (enemyRect.top + enemyRect.height/2 - 150) + 'px';
                shockwave.style.opacity = '0';
            }, 50);
            
            setTimeout(() => shockwave.remove(), 600);
            
            // Enemy flies back!
            enemy.style.transition = 'transform 0.3s ease-out';
            enemy.style.transform = 'translateX(80px) rotate(-30deg)';
            
            this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, 35, 'physical');
            this.createParticles(enemyRect.left + enemyRect.width/2, enemyRect.top + enemyRect.height/2, 20, '#ffaa00');
        }, 150);
        
        setTimeout(() => {
            player.style.transform = 'translateX(0) scale(1)';
            enemy.style.transform = 'translateX(0) rotate(0)';
        }, 600);
    }

    warriorCleave() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const enemyRect = enemy.getBoundingClientRect();
        
        // Player spins!
        player.style.transition = 'transform 0.4s ease-out';
        player.style.transform = 'translateX(80px) rotate(360deg) scale(1.2)';
        
        // Create spinning slash trails
        setTimeout(() => {
            for (let i = 0; i < 8; i++) {
                setTimeout(() => {
                    const angle = (i * 45) * Math.PI / 180;
                    const x = enemyRect.left + enemyRect.width/2 + Math.cos(angle) * 60;
                    const y = enemyRect.top + enemyRect.height/2 + Math.sin(angle) * 60;
                    this.createSlashEffect(x, y);
                }, i * 50);
            }
            
            this.screenFlash('#ff6600', 0.4);
            this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, 45, 'crit');
            this.createParticles(enemyRect.left + enemyRect.width/2, enemyRect.top + enemyRect.height/2, 25, '#ff6600');
            
            enemy.style.filter = 'brightness(2) hue-rotate(30deg)';
        }, 200);
        
        setTimeout(() => {
            player.style.transform = 'translateX(0) rotate(0) scale(1)';
            enemy.style.filter = '';
        }, 600);
    }

    // ===================================
    // MAGE ABILITIES
    // ===================================
    mageFireball() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const playerRect = player.getBoundingClientRect();
        const enemyRect = enemy.getBoundingClientRect();
        
        // Mage raises hand (scale up)
        player.style.transition = 'transform 0.3s ease-out';
        player.style.transform = 'scale(1.15)';
        player.style.filter = 'brightness(1.5) drop-shadow(0 0 20px #ff6600)';
        
        // Create fireball
        setTimeout(() => {
            const fireball = document.createElement('div');
            fireball.style.cssText = `
                position: absolute;
                left: ${playerRect.left + playerRect.width}px;
                top: ${playerRect.top + playerRect.height/2}px;
                width: 40px;
                height: 40px;
                background: radial-gradient(circle, #ff0 0%, #ff6600 50%, #ff0000 100%);
                border-radius: 50%;
                box-shadow: 0 0 30px #ff6600;
                transition: all 0.5s ease-out;
            `;
            this.container.appendChild(fireball);
            
            // Create fire trail particles
            const trailInterval = setInterval(() => {
                const rect = fireball.getBoundingClientRect();
                this.createParticles(rect.left + 20, rect.top + 20, 3, '#ff6600');
            }, 50);
            
            // Move fireball to enemy
            setTimeout(() => {
                fireball.style.left = (enemyRect.left + enemyRect.width/2) + 'px';
                fireball.style.top = (enemyRect.top + enemyRect.height/2) + 'px';
                fireball.style.transform = 'scale(2)';
            }, 50);
            
            // Impact!
            setTimeout(() => {
                clearInterval(trailInterval);
                fireball.remove();
                this.showFireBlast('enemy');
                this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, 40, 'fire');
            }, 550);
        }, 300);
        
        setTimeout(() => {
            player.style.transform = 'scale(1)';
            player.style.filter = '';
        }, 900);
    }

    mageIceBlast() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const playerRect = player.getBoundingClientRect();
        const enemyRect = enemy.getBoundingClientRect();
        
        // Mage channels ice
        player.style.filter = 'brightness(1.3) hue-rotate(180deg) drop-shadow(0 0 20px #4af)';
        
        // Create ice beam
        setTimeout(() => {
            const beam = document.createElement('div');
            beam.style.cssText = `
                position: absolute;
                left: ${playerRect.left + playerRect.width}px;
                top: ${playerRect.top + playerRect.height/2 - 10}px;
                width: 0px;
                height: 20px;
                background: linear-gradient(to right, #4af, #0af, #4af);
                box-shadow: 0 0 20px #4af;
                transition: width 0.3s ease-out;
            `;
            this.container.appendChild(beam);
            
            // Expand beam
            setTimeout(() => {
                beam.style.width = (enemyRect.left - playerRect.left - playerRect.width) + 'px';
            }, 50);
            
            // Hit enemy
            setTimeout(() => {
                beam.remove();
                this.showIceBlast('enemy');
                this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, 38, 'ice');
                
                // Freeze effect
                enemy.style.filter = 'brightness(0.5) hue-rotate(180deg)';
                setTimeout(() => enemy.style.filter = '', 2000);
            }, 400);
        }, 300);
        
        setTimeout(() => {
            player.style.filter = '';
        }, 1000);
    }

    mageLightningBolt() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const enemyRect = enemy.getBoundingClientRect();
        
        // Mage glows with electricity
        player.style.filter = 'brightness(1.5) drop-shadow(0 0 30px #ff0)';
        
        setTimeout(() => {
            // Cast lightning
            this.showLightningStrike('enemy');
            this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, 42, 'lightning');
        }, 300);
        
        setTimeout(() => {
            player.style.filter = '';
        }, 1200);
    }

    // ===================================
    // ROGUE ABILITIES
    // ===================================
    rogueBackstab() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const enemyRect = enemy.getBoundingClientRect();
        
        // Player disappears (stealth)
        player.style.transition = 'opacity 0.2s ease-out, transform 0.2s ease-out';
        player.style.opacity = '0.2';
        player.style.transform = 'translateX(150px)';
        
        setTimeout(() => {
            // Appear behind enemy!
            player.style.transition = 'none';
            player.style.transform = 'translateX(200px)';
            
            setTimeout(() => {
                player.style.transition = 'opacity 0.1s ease-out';
                player.style.opacity = '1';
                
                // BACKSTAB!
                this.screenFlash('#a0f', 0.2);
                
                // Multiple rapid slashes
                for (let i = 0; i < 5; i++) {
                    setTimeout(() => {
                        this.createSlashEffect(
                            enemyRect.left + enemyRect.width + Math.random() * 30,
                            enemyRect.top + enemyRect.height/2 + (Math.random() - 0.5) * 40
                        );
                    }, i * 50);
                }
                
                enemy.style.filter = 'brightness(1.8)';
                this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top - 20, 55, 'crit');
                this.createParticles(enemyRect.left + enemyRect.width, enemyRect.top + enemyRect.height/2, 30, '#ff0000');
            }, 100);
        }, 200);
        
        // Return to position
        setTimeout(() => {
            player.style.transition = 'transform 0.3s ease-out, opacity 0.3s ease-out';
            player.style.transform = 'translateX(0)';
            player.style.opacity = '1';
            enemy.style.filter = '';
        }, 700);
    }

    roguePoisonStrike() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const enemyRect = enemy.getBoundingClientRect();
        
        // Quick dash attack
        player.style.transition = 'transform 0.15s ease-out';
        player.style.transform = 'translateX(100px)';
        player.style.filter = 'hue-rotate(120deg)';
        
        setTimeout(() => {
            // Poison splash!
            for (let i = 0; i < 20; i++) {
                setTimeout(() => {
                    const x = enemyRect.left + enemyRect.width/2 + (Math.random() - 0.5) * 60;
                    const y = enemyRect.top + enemyRect.height/2 + (Math.random() - 0.5) * 60;
                    
                    const drop = document.createElement('div');
                    drop.style.cssText = `
                        position: absolute;
                        left: ${x}px;
                        top: ${y}px;
                        width: 8px;
                        height: 8px;
                        background: #0f0;
                        border-radius: 50%;
                        box-shadow: 0 0 10px #0f0;
                        animation: particleFade 1s ease-out forwards;
                    `;
                    this.container.appendChild(drop);
                    setTimeout(() => drop.remove(), 1000);
                }, i * 30);
            }
            
            enemy.style.filter = 'hue-rotate(120deg) brightness(1.3)';
            this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, 32, 'poison');
            
            // Poison lingers
            setTimeout(() => {
                enemy.style.filter = 'hue-rotate(120deg) brightness(0.8)';
            }, 500);
        }, 150);
        
        setTimeout(() => {
            player.style.transform = 'translateX(0)';
            player.style.filter = '';
            enemy.style.filter = '';
        }, 1500);
    }

    rogueShadowStrike() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const enemyRect = enemy.getBoundingClientRect();
        
        // Create shadow clones
        for (let i = 0; i < 3; i++) {
            const clone = player.cloneNode(true);
            clone.style.position = 'absolute';
            clone.style.left = player.style.left;
            clone.style.bottom = player.style.bottom;
            clone.style.opacity = '0.5';
            clone.style.filter = 'brightness(0.3)';
            clone.id = 'shadow-clone-' + i;
            document.getElementById('battle-arena').appendChild(clone);
            
            setTimeout(() => {
                clone.style.transition = 'all 0.5s ease-out';
                clone.style.transform = `translateX(${80 + i * 30}px) translateY(${(i - 1) * 30}px)`;
                clone.style.opacity = '0';
            }, 50);
            
            setTimeout(() => clone.remove(), 600);
        }
        
        // Main attack
        player.style.transition = 'transform 0.2s ease-out';
        player.style.transform = 'translateX(100px)';
        
        setTimeout(() => {
            this.showDarknessPulse('enemy');
            this.showDamageNumber(enemyRect.left + enemyRect.width/2, enemyRect.top, 48, 'dark');
        }, 200);
        
        setTimeout(() => {
            player.style.transform = 'translateX(0)';
        }, 600);
    }

    // Add poison color
    showDamageNumber(x, y, damage, type = 'physical') {
        const num = document.createElement('div');
        num.className = 'damage-number';
        
        if (type === 'heal') {
            num.classList.add('heal-number');
            num.textContent = '+' + damage;
        } else if (type === 'crit') {
            num.classList.add('crit-number');
            num.textContent = damage + '!';
        } else {
            num.textContent = damage;
            
            // Color based on type
            if (type === 'fire') num.style.color = '#ff6600';
            if (type === 'ice') num.style.color = '#4af';
            if (type === 'lightning') num.style.color = '#ff0';
            if (type === 'dark') num.style.color = '#a0f';
            if (type === 'wind') num.style.color = '#fff';
            if (type === 'poison') num.style.color = '#0f0';
        }
        
        num.style.left = (x - 30) + 'px';
        num.style.top = y + 'px';
        
        this.container.appendChild(num);
        
        setTimeout(() => num.remove(), 1500);
    }

    // ===================================
    // ENEMY ATTACK ANIMATION
    // ===================================
    enemyAttack() {
        const player = document.getElementById('player-sprite');
        const enemy = document.getElementById('enemy-sprite');
        
        if (!player || !enemy) return;
        
        const playerRect = player.getBoundingClientRect();
        const enemyRect = enemy.getBoundingClientRect();
        
        // Move enemy forward
        enemy.style.transition = 'transform 0.2s ease-out';
        enemy.style.transform = 'translateX(-100px) scale(1.1)';
        
        // Attack effect
        setTimeout(() => {
            this.createSlashEffect(playerRect.left + playerRect.width, playerRect.top + playerRect.height/2);
            
            // Player recoil
            player.style.transition = 'transform 0.1s ease-out';
            player.style.transform = 'translateX(-30px) rotate(10deg)';
            player.style.filter = 'brightness(1.5)';
            
            // Screen shake
            this.screenShake(5);
            
            // Damage number
            const damage = 10 + Math.floor(Math.random() * 15);
            this.showDamageNumber(playerRect.left + playerRect.width/2, playerRect.top, damage, 'physical');
            
            // Blood particles
            this.createParticles(playerRect.left + playerRect.width/2, playerRect.top + playerRect.height/2, 10, '#ff0000');
            
            // Flash red
            this.screenFlash('#f00', 0.2);
        }, 200);
        
        // Return enemy
        setTimeout(() => {
            enemy.style.transform = 'translateX(0) scale(1)';
            player.style.transform = 'translateX(0) rotate(0)';
            player.style.filter = '';
        }, 400);
    }

    // ===================================
    // SLASH EFFECT
    // ===================================
    createSlashEffect(x, y) {
        const slash = document.createElement('div');
        slash.style.position = 'absolute';
        slash.style.left = x + 'px';
        slash.style.top = y + 'px';
        slash.style.width = '100px';
        slash.style.height = '5px';
        slash.style.background = 'linear-gradient(to right, transparent, #fff, transparent)';
        slash.style.boxShadow = '0 0 20px #fff';
        slash.style.transform = 'rotate(-45deg)';
        slash.style.opacity = '1';
        slash.style.transition = 'opacity 0.3s, transform 0.3s';
        this.container.appendChild(slash);
        
        setTimeout(() => {
            slash.style.opacity = '0';
            slash.style.transform = 'rotate(-45deg) scale(2)';
        }, 50);
        
        setTimeout(() => slash.remove(), 350);
    }

    // ===================================
    // DAMAGE NUMBERS - Floating numbers!
    // ===================================
    showDamageNumber(x, y, damage, type = 'physical') {
        const num = document.createElement('div');
        num.className = 'damage-number';
        
        if (type === 'heal') {
            num.classList.add('heal-number');
            num.textContent = '+' + damage;
        } else if (type === 'crit') {
            num.classList.add('crit-number');
            num.textContent = damage + '!';
        } else {
            num.textContent = damage;
            
            // Color based on type
            if (type === 'fire') num.style.color = '#ff6600';
            if (type === 'ice') num.style.color = '#4af';
            if (type === 'lightning') num.style.color = '#ff0';
            if (type === 'dark') num.style.color = '#a0f';
            if (type === 'wind') num.style.color = '#fff';
        }
        
        num.style.left = (x - 30) + 'px';
        num.style.top = y + 'px';
        
        this.container.appendChild(num);
        
        setTimeout(() => num.remove(), 1500);
    }

    // ===================================
    // PARTICLE SYSTEM
    // ===================================
    createParticles(x, y, count, color) {
        for (let i = 0; i < count; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.background = color;
            particle.style.left = x + 'px';
            particle.style.top = y + 'px';
            
            const angle = Math.random() * Math.PI * 2;
            const speed = 50 + Math.random() * 100;
            const dx = Math.cos(angle) * speed;
            const dy = Math.sin(angle) * speed;
            
            particle.style.transform = `translate(${dx}px, ${dy}px)`;
            
            this.container.appendChild(particle);
            
            setTimeout(() => particle.remove(), 1000);
        }
    }

    // ===================================
    // SCREEN EFFECTS
    // ===================================
    screenFlash(color, duration = 0.3) {
        const flash = document.createElement('div');
        flash.style.position = 'fixed';
        flash.style.top = '0';
        flash.style.left = '0';
        flash.style.width = '100%';
        flash.style.height = '100%';
        flash.style.background = color;
        flash.style.opacity = '0.5';
        flash.style.pointerEvents = 'none';
        flash.style.zIndex = '9998';
        flash.style.transition = `opacity ${duration}s`;
        document.body.appendChild(flash);
        
        setTimeout(() => {
            flash.style.opacity = '0';
        }, 50);
        
        setTimeout(() => flash.remove(), duration * 1000);
    }

    screenShake(intensity = 10) {
        const gameScreen = document.getElementById('game-screen');
        if (!gameScreen) return;
        
        gameScreen.style.animation = 'screenShake 0.5s ease-in-out';
        setTimeout(() => {
            gameScreen.style.animation = '';
        }, 500);
    }

    // ===================================
    // HP BAR DRAIN ANIMATION
    // ===================================
    animateHPDrain(barId, currentHP, maxHP) {
        const bar = document.getElementById(barId);
        if (!bar) return;
        
        const percent = (currentHP / maxHP) * 100;
        bar.style.width = percent + '%';
        
        // Color based on HP
        if (percent < 25) {
            bar.style.background = '#ff0000';
        } else if (percent < 50) {
            bar.style.background = '#ff6600';
        } else {
            bar.style.background = '#00ff00';
        }
    }
}

// Initialize effects system
const effects = new VisualEffects();

// Export for use in other scripts
window.visualEffects = effects;

