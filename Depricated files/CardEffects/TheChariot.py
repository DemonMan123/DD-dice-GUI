import secrets

NegativeEffects = ['Ruthless Competition', "Tyrannical Rule", 'Unending War']
PositiveEffects = ["Victory's Reward", "Resilient Willpower", 'Divine Favor']

def ChariotNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def ChariotPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll