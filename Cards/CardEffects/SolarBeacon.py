import secrets

NegativeEffects = ['Blinding Radiance', 'Solar Flare', 'Heat Exhaustion']
PositiveEffects = ['Radiant Blessing', 'Solar Empowerment', 'Beacons Guidance']

def SolarBeaconNegativeEffectRoll():
    NegativeRoll = secrets.choice(NegativeEffects)
    return NegativeRoll

def SolarBeaconPositiveEffectRoll():
    PositiveRoll = secrets.choice(PositiveEffects)
    return PositiveRoll