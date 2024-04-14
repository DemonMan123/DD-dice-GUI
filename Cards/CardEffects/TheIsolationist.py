import secrets

NegativeEffects = ['Lonelinesss Grip', 'Isolations Madness', 'Desperate Isolation']
PositiveEffects = ['Solitudes Respite', 'Isolations Insight', 'Hermits Revelation']

def TheIsolationistNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheIsolationistPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll