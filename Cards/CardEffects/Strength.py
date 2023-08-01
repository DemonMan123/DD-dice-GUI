import secrets

NegativeEffects = ['Self-Destructive Bravery', "Physical Strain", 'Vulnerability Exploitation']
PositiveEffects = ["Heroic Acts", "Fear Dispelling Aura", 'Inner Harmony']

def StrengthNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def StrengthPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll