import secrets

NegativeEffects = ['Unjust Verdict', 'Adjudicators Wrath', 'Twisted Justice']
PositiveEffects = ['Judgements Favor', 'Fair Trial', 'Adjudicators Guidance']

def TheAdjudicationNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheAdjudicationPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll