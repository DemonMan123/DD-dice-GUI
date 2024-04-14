import secrets

NegativeEffects = ['Unstable Ground', 'Maws Hunger', 'Dimensional Instability']
PositiveEffects = ['Maw Adaptation', 'Eternal Flux', 'Maws Swiftness']

def TheShiftingMawNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheShiftingMawPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll