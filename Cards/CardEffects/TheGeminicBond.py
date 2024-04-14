import secrets

NegativeEffects = ['Fractured Unity', 'Divided Loyalties', 'Bonds Betrayal']
PositiveEffects = ['Dual Unity', 'Shared Knowledge', 'Twin Protection']

def TheGeminicBondNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheGeminicBondPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll