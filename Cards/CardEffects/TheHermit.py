import secrets

NegativeEffects = ['Loss of Direction', "Excessive Self-Reflection", 'Spiritual Crisis']
PositiveEffects = ["Mentor or Guardian", "Astral Projection", 'Psychic Warding']

def HermitNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def HermitPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll