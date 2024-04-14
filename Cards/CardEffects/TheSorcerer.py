import secrets

NegativeEffects = ['Mawic Backlack', 'Chaos Surge', 'Sorcerers Curse']
PositiveEffects = ['Arcane Revelation', 'Mawic Attunement', 'Sorcerers Insight']

def TheSorcererNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheSorcererPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll