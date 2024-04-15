import secrets

NegativeEffects = ['Fallen Angel', 'Betrayed Trust', 'Lost Faith']
PositiveEffects = ['Divine Intervention', 'Redeeming Light', 'Guardian Angel']

def AngelOfTheMawNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def AngelOfTheMawPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll