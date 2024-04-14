import secrets

NegativeEffects = ['Betrayal', 'Reckless Fortune', 'Unpredictable Equipment']
PositiveEffects = ['Lucky Break', 'Bold Charisma', 'Synchronistic Guidance']

def FoolNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def FoolPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll