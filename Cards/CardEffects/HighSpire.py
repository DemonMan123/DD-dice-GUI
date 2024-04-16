import secrets

NegativeEffects = ['Abyssal Fall', 'Storms Wrath', 'Lonely Heights']
PositiveEffects = ['Aerial Advantage', 'Eagles Eye', 'Tactical Jump']

def HighSpireNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def HighSpirePositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll