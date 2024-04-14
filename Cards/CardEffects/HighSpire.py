import secrets

NegativeEffects = ['EFFECT', 'EFFECT', 'EFFECT']
PositiveEffects = ['EFFECT', 'EFFECT', 'EFFECT']

def NegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def PositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll