from Dice.D90 import D90Roll
from Dice.D20 import D20Roll
from Dice.D12 import D12Roll
#from Dice.D9 import D9Roll
#from Dice.D8 import D8Roll
#from Dice.D6 import D6Roll
#from Dice.D4 import D4Roll
import pyfiglet
import os

'''
I created another program called "ADRollMenu.py" (Stands for Advantage Disadvantage roll menu)
I'd recommend using that instead of this. Has the same function just in a GUI.

'''

Title = pyfiglet.figlet_format("Demin's dice")

def main():
    input("Press any key to continue... ")
    os.system('cls' if os.name=='nt' else 'clear')
    print(Title)
    print("Roll types: ")
    print("A = Advantage")
    print("D = Disadvantage")
    print("N = Normal (D20 roll)")
    print("E to Exit\n")
    RollType = input("What type of roll would you like to do? ")
    if RollType.lower() == "a":
        AdvantageRoll()
    if RollType.lower() == "d":
        DisadvantageRoll()
    if RollType.lower() == "n":
        Roll = D20Roll()
        print(f"You rolled... {Roll}")
    if RollType.lower() == "e":
        exit()
        
        
def DisadvantageRoll():
    D12R = D12Roll()
    D20R = D20Roll()
    print("Values: ")
    print("D20: ", D20R)
    print("D12: ", D12R)
    if D12R < D20R:
        print("D12 is lower...")
    if D20R < D12R:
        print("D20 is lower...")
    else:
        print("Even")


def AdvantageRoll():
    D20R = D20Roll()
    D90R = D90Roll()
    print("Values: ")
    print("D20: ", D20R)
    print("D90: ", D90R)
    if D20R < D90R:
        print("D90 is higher")
    if D20R > D90R:
        print("D20 is higher")
    else:
        print("Even")

while True:
    main()