import secrets

NegativeEffects = ['Vengeful Eyes', 'Detrimental Void', 'Addictive Power']
PositiveEffects = ['Unleased Power', 'Masterful Skill', 'Arcane Insight']

def MagicianNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def MagicianPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll