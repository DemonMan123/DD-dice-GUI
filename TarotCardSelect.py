# Important imports (DO NOT MESS WITH THIS)
import secrets
from Cards.CardEffects.TheFool import FoolNegativeEffectRoll, FoolPositiveEffectRoll
from Cards.CardEffects.TheMagician import MagicianNegativeEffectRoll, MagicianPositiveEffectRoll
from Cards.CardEffects.TheEmpress import EmpressNegativeEffectRoll, EmpressPositiveEffectRoll
from Cards.CardEffects.HighPriestess import PriestessNegativeEffectRoll, PriestessPositiveEffectRoll
from Cards.CardEffects.TheEmperor import EmperorNegativeEffectRoll, EmperorPositiveEffectRoll
from Cards.CardEffects.TheHierophant import HierophantNegativeEffectRoll, HierophantPositiveEffectRoll
from Cards.CardEffects.TheLovers import LoversNegativeEffectRoll, LoversPositiveEffectRoll
from Cards.CardEffects.TheChariot import ChariotNegativeEffectRoll, ChariotPositiveEffectRoll
#End of imports

Cards = [
        'The Fool',
         'The Magician',
         'The High Priestess', 
         'The Empress', 
         'The Emperor', 
         'The Hierophant', 
         'The Lovers', 
         'The Chariot', 
         'Strength', 
         'The Hermit', 
         'The Wheel of Fortune', 
         'Justice', 
         'The Hanged Man', 
         'Death', 
         'Temperance', 
         'The Devil', 
         'The Tower', 
         'The Star', 
         'The Moon', 
         'The Sun', 
         'Judgement', 
         'The World'
         ]


def SelectCards():
    #SelectIN = input("Would you like to select a card? (Y,N) ")
    #f SelectIN.lower() == "y":
    RandCard = secrets.choice(Cards) #Selects random card from list
        #SelectedCardFormat = pyfiglet.figlet_format(RandCard) #Puts card in a format for PyFiglet (Looks cool)
    
    return(RandCard)
    #else:
        #exit()
    
    
# Define the function to select cards effects
def selectEffect(RollResult, Card):
    card_effects = {
        "The High Priestess": [PriestessNegativeEffectRoll, PriestessPositiveEffectRoll],
        "The Emperor": [EmperorNegativeEffectRoll, EmperorPositiveEffectRoll],
        "The Empress": [EmpressNegativeEffectRoll, EmpressPositiveEffectRoll],
        "The Fool": [FoolNegativeEffectRoll, FoolPositiveEffectRoll],
        "The Magician": [MagicianNegativeEffectRoll, MagicianPositiveEffectRoll],
        "The Hierophant": [HierophantNegativeEffectRoll, HierophantPositiveEffectRoll],
        "The Lovers": [LoversNegativeEffectRoll, LoversPositiveEffectRoll],
        "The Chariot": [ChariotNegativeEffectRoll, ChariotPositiveEffectRoll]
    }

    if Card in card_effects:
        if RollResult < 10:
            return card_effects[Card][0]()
        else:
            return card_effects[Card][1]()
    else:
        return "Card not in list"