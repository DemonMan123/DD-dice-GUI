import secrets

NegativeEffects = ['Maws Corruption', 'Unending Void', 'Maws Wrath']
PositiveEffects = ['Consuming Power', 'Maws Embrace', 'Eternal Hunger']

def TheMawNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheMawPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll