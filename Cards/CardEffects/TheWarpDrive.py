import secrets

NegativeEffects = ['Temporal Distortion', 'Reality Fracture', 'Mawic Corruption']
PositiveEffects = ['Temporal Shift', 'Dimensional Shortcut', 'Maws Protection']

def TheWarpDriveNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def TheWarpDrivePositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll