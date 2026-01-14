# 💫 STATUS AILMENTS SYSTEM ADDED! 🔥❄️⚡

## New Feature: Status Effects in Combat!

Your RPG now has a **complete status ailment system** with buffs and debuffs that last multiple turns!

---

## 🔥 HARMFUL STATUS EFFECTS (Debuffs)

### Damage Over Time:
1. **🔥 Burning** (3 turns)
   - Deals fire damage each turn
   - Inflicted by: Fireball (30% chance)
   - Stacks with other effects

2. **☠️ Poisoned** (4 turns)
   - Damage INCREASES each turn (3, 6, 9, 12...)
   - Inflicted by: Poison Strike (50% chance)
   - Deadly if not cured quickly!

3. **🩸 Bleeding** (3 turns)
   - Constant damage per turn
   - Reduces healing effectiveness
   - Inflicted by: Backstab (40% chance)

### Crowd Control:
4. **❄️ Frozen** (2 turns)
   - **CANNOT ACT!**
   - Takes +50% damage from attacks
   - 30% chance to break free each turn
   - Inflicted by: Ice Blast (25% chance)

5. **💫 Stunned** (1 turn)
   - Cannot move for one turn
   - Inflicted by: Shield Bash (40% chance)

6. **⚡ Paralyzed** (3 turns)
   - 50% chance to MISS attacks
   - Inflicted by: Lightning Strike (35% chance)

7. **😵 Confused** (2 turns)
   - 40% chance to attack yourself!
   - Unpredictable in battle

---

## 💪 BENEFICIAL STATUS EFFECTS (Buffs)

### Healing:
1. **💚 Regeneration** (4 turns)
   - Restores 8 HP per turn
   - Inflicted by: Heal ability (100% chance on self)

### Power Ups:
2. **💪 Empowered** (3 turns)
   - +10 attack damage
   - Stack with equipment bonuses

3. **🛡️ Shielded** (3 turns)
   - +8 defense
   - Reduces incoming damage
   - Inflicted by: Divine Shield (100% on self)

4. **⚡ Hasted** (3 turns)
   - 50% chance for DOUBLE ATTACK!
   - Attack twice in one turn

5. **😡 Berserk** (3 turns)
   - +50% attack damage
   - -30% defense (high risk, high reward!)
   - Inflicted by: Berserker Rage

6. **✨ Invulnerable** (2 turns) - RARE!
   - 80% damage reduction!
   - Nearly unkillable for 2 turns

---

## 🎮 How Status Effects Work

### Duration System:
- Effects last 1-4 turns
- Countdown at START of each turn
- Effects expire automatically
- Multiple effects can stack!

### Application:
- **Abilities** have % chance to inflict status
- **Weather** can boost status chances
- **Critical hits** may apply status
- Some enemies have innate status attacks

### Status Display:
```
Status: 🔥 Burning (2) | 💪 Empowered (3) | ⚡ Hasted (2)
```
Shows all active effects with turns remaining

---

## ⚔️ Combat Integration

### Turn Order:
1. **Status effects process** (damage/healing applied)
2. **Player chooses action**
3. **Status effects influence** (bonuses, penalties)
4. **Actions resolve**
5. **New effects may apply**

### Status Effect Stacking:
- **Same effect**: Refreshes duration
- **Different effects**: Stack fully
- **Buffs + Debuffs**: Can have both simultaneously

### Strategic Depth:
- **Freeze** enemies to prevent attacks
- **Poison** for long battles
- **Buff** yourself before big hits
- **Haste** for burst damage
- **Regen** for sustain

---

## 📊 Status Effect Math

### Attack Modifiers:
```
Base Attack: 15
+ Weapon: +10 = 25
+ Empowered: +10 = 35
× Berserk: ×1.5 = 52.5 → 52 damage!
```

### Defense Modifiers:
```
Base Defense: 10
+ Armor: +15 = 25
+ Shielded: +8 = 33
- Berserk: ×0.7 = 23 defense
```

### Damage Taken:
```
Incoming: 30 damage
× Frozen: ×1.5 = 45 damage!
× Invulnerable: ×0.2 = 6 damage!
```

---

## 🎯 Ability Status Chart

| Ability | Status Effect | Chance | Target |
|---------|--------------|--------|--------|
| Fireball | 🔥 Burning | 30% | Enemy |
| Ice Blast | ❄️ Frozen | 25% | Enemy |
| Lightning Strike | ⚡ Paralyzed | 35% | Enemy |
| Poison Strike | ☠️ Poisoned | 50% | Enemy |
| Backstab | 🩸 Bleeding | 40% | Enemy |
| Shield Bash | 💫 Stunned | 40% | Enemy |
| Heal | 💚 Regen | 100% | Self |
| Divine Shield | 🛡️ Shielded | 100% | Self |
| Berserker Rage | 😡 Berserk | 100% | Self |

---

## 💡 Strategy Tips

### Offensive:
- 🔥 **Burn + Poison** = Maximum damage over time
- ❄️ **Freeze** then attack for +50% damage
- 😡 **Berserk** for quick kills
- ⚡ **Haste** with high attack weapons

### Defensive:
- 🛡️ **Shield** before enemy strong attacks
- 💚 **Regen** for long battles
- ✨ **Invulnerable** to tank boss attacks
- ❄️ **Freeze** dangerous enemies

### Combos:
- **Empowered + Berserk + Haste** = Devastating!
- **Shielded + Regen + Invulnerable** = Unkillable!
- **Poison + Burn + Bleeding** = Triple DoT death!

---

## 🌦️ Weather + Status Synergy

Weather can boost status application:
- ⛈️ **Stormy** → Paralysis +20% chance
- ❄️ **Snowy** → Freeze duration +1 turn
- ☀️ **Sunny** → Burn damage +30%
- 🌌 **Aurora** → All effects +50% potency!

---

## 🎮 In-Game Examples

### Example 1: Warrior vs Enemy
```
Turn 1: Use Shield Bash
→ 💫 Enemy is Stunned! Cannot act!

Turn 2: Enemy Stunned, you attack freely
→ Critical hit! 🩸 Enemy is Bleeding!

Turn 3: Bleeding deals 4 damage
→ Enemy attacks, you use Berserker Rage
→ 😡 You're Berserk! +50% attack!

Turn 4: Super-powered attack finishes enemy!
```

### Example 2: Mage vs Boss
```
Turn 1: Cast Ice Blast
→ ❄️ Boss is Frozen!

Turn 2: Boss cannot act
→ Cast Lightning Strike
→ Critical! ⚡ Boss is Paralyzed!

Turn 3: Boss misses due to Paralysis
→ Cast Fireball
→ 🔥 Boss is Burning!

Turn 4: Boss takes burn damage
→ Win with status effects!
```

---

## 📝 Files Modified

✅ `status_effects.py` - Complete status system (NEW!)
✅ `character.py` - Status manager integration
✅ `enemy.py` - Enemies can have status effects
✅ `combat.py` - Status processing (updating...)

---

## 🌐 Play Now!

**URL:** http://localhost:8080

**New Features:**
✅ 13 status effects (7 debuffs, 6 buffs)
✅ Multi-turn duration system
✅ Status effect stacking
✅ Ability-based status infliction
✅ Strategic combat depth
✅ All previous features preserved!

---

**Your game now has DEEP strategic combat!** 🔥❄️💫⚡

Use status effects wisely to dominate battles! Try freezing enemies, poisoning bosses, and buffing yourself for epic fights!

