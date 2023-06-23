import secrets

NegativeEffects = ['', '', '']
PositiveEffects = ['', '', '']

def EmperorNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def EmperorPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll