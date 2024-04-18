import secrets

NegativeEffects = ['Whispers of Madness', 'Abyssal Hunger', 'Voids Embrace']
PositiveEffects = ['Beckoning Shadows', 'Echoes of the Abyss', 'Maws Favor']

def CallOfTheMawNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def CallOfTheMawPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll