import secrets

NegativeEffects = ['Cursed Eclipse', 'Moons Malice', 'Tides of Darkness']
PositiveEffects = ['Shadowy Veil', 'Umbral Shield', 'Umbral Conduit']

def BlackMoonNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def BlackMoonPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll