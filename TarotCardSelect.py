# Important imports (DO NOT MESS WITH THIS)
import secrets
from Cards.CardEffects.AngelOfTheMaw import AngelOfTheMawNegativeEffectRoll, AngelOfTheMawPositiveEffectRoll
# from Cards.CardEffects.AstralRealm import AstralRealmNegativeEffectRoll, AstralRealmPositiveEffectRoll
# from Cards.CardEffects.BlackMoon import BlackMoonNegativeEffectRoll, BlackMoonPositiveEffectRoll
# from Cards.CardEffects.CallOfTheMaw import CallOfTheMawNegativeEffectRoll, CallOfTheMawPositiveEffectRoll
from Cards.CardEffects.HighSpire import HighSpireNegativeEffectRoll, HighSpirePositiveEffectRoll
from Cards.CardEffects.PossessorOfTheMaw import PossessorOfTheMawNegativeEffectRoll, PossessorOfTheMawPositiveEffectRoll
# from Cards.CardEffects.SolarBeacon import SolarBeaconNegativeEffectRoll, SolarBeaconPositiveEffectRoll
from Cards.CardEffects.TheAdjudication import TheAdjudicationNegativeEffectRoll, TheAdjudicationPositiveEffectRoll
from Cards.CardEffects.TheCreedsmen import TheCreedsmenNegativeEffectRoll, TheCreedsmenPositiveEffectRoll
from Cards.CardEffects.TheGate import TheGateNegativeEffectRoll, TheGatePositiveEffectRoll
from Cards.CardEffects.TheGeminicBond import TheGeminicBondNegativeEffectRoll, TheGeminicBondPositiveEffectRoll
from Cards.CardEffects.TheGuardianShield import TheGuardianShieldNegativeEffectRoll, TheGuardianShieldPositiveEffectRoll
from Cards.CardEffects.TheIsolationist import TheIsolationistNegativeEffectRoll, TheIsolationistPositiveEffectRoll
from Cards.CardEffects.TheJester import TheJesterNegativeEffectRoll, TheJesterPositiveEffectRoll
from Cards.CardEffects.TheMartyr import TheMartyrNegativeEffectRoll, TheMartyrPositiveEffectRoll
from Cards.CardEffects.TheMaw import TheMawNegativeEffectRoll, TheMawPositiveEffectRoll
from Cards.CardEffects.TheMistress import TheMistressNegativeEffectRoll, TheMistressPositiveEffectRoll
from Cards.CardEffects.TheOracle import TheOracleNegativeEffectRoll, TheOraclePositiveEffectRoll
from Cards.CardEffects.ThePrimordial import ThePrimordialNegativeEffectRoll, ThePrimordialPositiveEffectRoll
from Cards.CardEffects.TheShiftingMaw import TheShiftingMawNegativeEffectRoll, TheShiftingMawPositiveEffectRoll
from Cards.CardEffects.TheSorcerer import TheSorcererNegativeEffectRoll, TheSorcererPositiveEffectRoll
from Cards.CardEffects.TheWarpDrive import TheWarpDriveNegativeEffectRoll, TheWarpDrivePositiveEffectRoll
# End of imports

# New Cards (Not yet implemented)
Cards = [
    'The Jester',
    'The Sorcerer',
    'The Creedsmen',
    'The Mistress',
    'The Primordial',
    'The Oracle',
    'The Geminic Bond',
    'The Warp Drive',
    'The Guardian Sheld',
    'The Isolationist',
    'The Shifting Maw',
    'The Adjudication',
    'The Martyr',
    'The Maw',
    'Angel of the Maw',
    'Possessor of the Maw',
    'High Spire',
    'The Gate',
    'Black Moon',
    'Solar Beacon',
    'Call of the Maw',
    'Astral Realm'
]

def SelectCards():
    RandCard = secrets.choice(Cards) #Selects random card from list
    return(RandCard)
    
    
# Define the function to select cards effects
def selectEffect(RollResult, Card):
    Effect = ""
    rolltype = ""
    card_effects = {
        'The Jester': [TheJesterNegativeEffectRoll, TheJesterPositiveEffectRoll],
        'The Sorcerer': [TheSorcererNegativeEffectRoll, TheSorcererPositiveEffectRoll],
        'The Creedsmen': [TheCreedsmenNegativeEffectRoll, TheCreedsmenPositiveEffectRoll],
        'The Mistress': [TheMistressNegativeEffectRoll, TheMistressPositiveEffectRoll],
        'The Primordial': [ThePrimordialNegativeEffectRoll, ThePrimordialPositiveEffectRoll],
        'The Oracle': [TheOracleNegativeEffectRoll, TheOraclePositiveEffectRoll],
        'The Geminic Bond': [TheGeminicBondNegativeEffectRoll, TheGeminicBondPositiveEffectRoll],
        'The Warp Drive': [TheWarpDriveNegativeEffectRoll, TheWarpDrivePositiveEffectRoll],
        'The Guardian Sheld': [TheGuardianShieldNegativeEffectRoll, TheGuardianShieldPositiveEffectRoll],
        'The Isolationist': [TheIsolationistNegativeEffectRoll, TheIsolationistPositiveEffectRoll],
        'The Shifting Maw': [TheShiftingMawNegativeEffectRoll, TheShiftingMawPositiveEffectRoll],
        'The Adjudication': [TheAdjudicationNegativeEffectRoll, TheAdjudicationPositiveEffectRoll],
        'The Martyr': [TheMartyrNegativeEffectRoll, TheMartyrPositiveEffectRoll],
        'The Maw': [TheMawNegativeEffectRoll, TheMawPositiveEffectRoll],
        'Angel of the Maw': [AngelOfTheMawNegativeEffectRoll, AngelOfTheMawPositiveEffectRoll],
        'Possessor of the Maw': [PossessorOfTheMawNegativeEffectRoll, PossessorOfTheMawPositiveEffectRoll],
        'High Spire': [HighSpireNegativeEffectRoll, HighSpirePositiveEffectRoll],
        'The Gate': [TheGateNegativeEffectRoll, TheGatePositiveEffectRoll],
        # 'Black Moon': [BlackMoonNegativeEffectRoll, BlackMoonPositiveEffectRoll],
        # 'Solar Beacon': [SolarBeaconNegativeEffectRoll, SolarBeaconPositiveEffectRoll],
        # 'Call of the Maw': [CallOfTheMawNegativeEffectRoll, CallOfTheMawPositiveEffectRoll],
        # 'Astral Realm': [AstralRealmNegativeEffectRoll, AstralRealmPositiveEffectRoll]
    }
    
    if Card in card_effects:
        if RollResult < 10:
            rolltype = "Negative"
            Effect = card_effects[Card][0]()
        else:
            rolltype = "Positive"
            Effect = card_effects[Card][1]()
    else:
        rolltype = "NULL"
        Effect = "Card not in list"

    return Effect, rolltype