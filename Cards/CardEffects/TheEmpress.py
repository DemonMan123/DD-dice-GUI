import secrets

NegativeEffects = ['Abundances Curse', 'Blossoms of Envy', 'Blighted Harvest']
PositiveEffects = ['Nurturing Aura', 'Empathic Bond', 'Nurturing Shelter']

def EmpressNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def EmpressPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll