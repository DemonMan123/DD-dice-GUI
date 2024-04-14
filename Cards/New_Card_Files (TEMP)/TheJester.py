import secrets

NegativeEffects = ['Jesters Gambit', 'Fools Misfortune', 'Mocking Mirage']
PositiveEffects = ['Fools Fortune', 'Tricksters Bounty', 'Laughters Blessing']

def TheJesterNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheJesterPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll