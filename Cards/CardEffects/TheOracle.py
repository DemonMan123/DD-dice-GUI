import secrets

NegativeEffects = ['Cryptic Visions', 'Twisted Fate', 'Oracles Curse']
PositiveEffects = ['Divine Insight', 'Oracles Eye', 'Fates Intervention']

def TheOracleNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheOraclePositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll