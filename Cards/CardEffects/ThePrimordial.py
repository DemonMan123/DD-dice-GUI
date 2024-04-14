import secrets

NegativeEffects = ['Raging Elements', 'Primeval Curse', 'Chaos of Creation']
PositiveEffects = ['Ancient Wisdom', 'Primal Blessing', 'Natures Harmony']

def ThePrimordialNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def ThePrimordialPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll