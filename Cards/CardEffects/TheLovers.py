import secrets

NegativeEffects = ['Karmic Consequences', "Love's Curse Spread", 'Forbidden Union']
PositiveEffects = ['Soul Connection', "Love's Unity", 'Ritual of Unity']

def LoversNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def LoversPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll