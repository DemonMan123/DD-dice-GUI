import secrets

NegativeEffects = ['Blind Faith', 'Religious Pilgrimage', 'Revelations & Prophecies']
PositiveEffects = ['Revenant', 'Spiritual Ascendance', 'Divine Aegis']

def HierophantNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def HierophantPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll