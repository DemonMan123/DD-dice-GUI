import secrets

NegativeEffects = ['Shields Burden', 'Guardians Judgement', 'Waning Protection']
PositiveEffects = ['Shield of Protection', 'Guardians Vigilance', 'Sentinels Aid']

def TheGuardianShieldNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheGuardianShieldPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll