import secrets

NegativeEffects = ['Corrupted Soul', 'Haunted by Shadows', 'Bargain of the Abyss']
PositiveEffects = ['Dominion Over Darkness', 'Consuming Avatar', 'Maws Sovereignty']

def PossessorOfTheMawNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def PossessorOfTheMawPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll