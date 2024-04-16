import secrets

NegativeEffects = ['Sealed Fate', 'Gateway to Oblivion', 'Toll of the Gate']
PositiveEffects = ['Portal of Opportunity', 'Guardian of the Gate', 'Gatekeepers Knowledge']

def TheGateNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheGatePositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll