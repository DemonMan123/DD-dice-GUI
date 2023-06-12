import secrets

NegativeEffects = ['Fractured Alliances', 'Leadership Paranoia', 'Isolation of Power']
PositiveEffects = ['Just Governance', 'Inspiring Presence', 'Formidable Presence']

def EmperorNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def EmperorPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll