import secrets

NegativeEffects = ['Temptations Trap', 'Lusts Ensnarement', 'Jealous Wrath']
PositiveEffects = ['Enthralling Charm', 'Seductive Veil', 'Mistresss Embrace']

def TheMistressNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheMistressPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll