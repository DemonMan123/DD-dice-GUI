import secrets

NegativeEffects = ['Broken Oath', 'Fallen Comrades', 'Creeds Judgement']
PositiveEffects = ['Code of Honor', 'Oathsworn Alliance', 'Creeds Protection']

def TheCreedsmenNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheCreedsmenPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll