import secrets

NegativeEffects = ['Martyrs Burden', 'Forgotten Martyr', 'Martyrs Fall']
PositiveEffects = ['Sacrificial Blessing', 'Martyrs Redemption', 'Martyrs Legacy']

def TheMartyrNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheMartyrPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll