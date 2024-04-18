import secrets

NegativeEffects = ['Astral Runes', 'Celestial Anguish', 'NOTHING']
PositiveEffects = ['Cosmic Insight', 'Astral Projection', 'NOTHING']

def AstralRealmNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def AstralRealmPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll