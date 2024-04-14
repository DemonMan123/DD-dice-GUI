import secrets

NegativeEffects = ['Forbidden Secrets', 'Cursed Insight', 'Guardians of Secrecy']
PositiveEffects = ['Mystical Resilience', 'Ancestral Guidance', 'Mystical Diplomacy']

def PriestessNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def PriestessPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll