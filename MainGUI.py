# All the imports required to work
from tkinter import *
from tkinter import ttk
from Dice.D90 import D90Roll
from Dice.D20 import D20Roll
from Dice.D12 import D12Roll
from TarotCardSelect import SelectCards, selectEffect
from Cards.Descriptions import search_word

# Create and setup main root window
root = Tk()
img = PhotoImage(file='icons/Skull.ico')
root.title("Demin's Roll Program")
root.iconphoto(False, img)
root.resizable(False,False)
root.geometry('350x150')

# Create main roll functions
def AdvantageRoll():
    print("Running Advantage Roll")
    D20R = D20Roll()
    D90R = D90Roll()
    if D20R > D90R:
        advantage = "D20 HIGHER"
    elif D90R > D20R:
        advantage = "D90 HIGHER"
    else:
        advantage = "TIE"
    Result.set(f"D20: {D20R}, D90: {D90R}, Result of Advantage: {advantage}")
        
def DisadvantageRoll():
    print("Running Disadvantage Roll")
    D12R = D12Roll()
    D20R = D20Roll()
    if D12R < D20R:
        Disadvantage = "D12 LOWER"
    elif D20R < D12R:
        Disadvantage = "D20 LOWER"
    else:
        Disadvantage = "TIE"
    Result.set(f"D12: {D12R}, D20: {D20R}, Result of Disadvantage: {Disadvantage}")
        
def D20Single():
    print("Running D20 Roll")
    D20R = D20Roll()
    Result.set(f"You rolled... {D20R}")

# Creating a function to create the card description window
CardDesc = None

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def CardDescriptionWindow(Card_Name, cardDesc, effect):
    img = PhotoImage(file='icons/5429974.ico')
    global CardDesc
    if CardDesc is not None and CardDesc.winfo_exists():
        CardDesc.destroy()

    CardDesc = Toplevel()
    CardDesc.title(f"{Card_Name}'s description")
    CardDesc.resizable(False,False)
    CardDesc.iconphoto(False, img) 
    center_window(CardDesc, 300, 90)

    # Display the card description
    label = Label(CardDesc, text=cardDesc)
    Effect = Label(CardDesc, text=f"Your effect: {effect}")
    label.place(x=15, y=10)
    Effect.place(x=15, y=50)

def TarotCardSel():
    TarotCard = SelectCards()
    Result.set(f"Your Tarot card: {TarotCard}")
    CardDescription = search_word(TarotCard)
    Roll = D20Roll()
    Effect = selectEffect(Roll, TarotCard)
    print(f"Rolling D20... {Roll}")
    CardDescriptionWindow(TarotCard, CardDescription, Effect)


# Create text for the output into GUI
Result = StringVar()
MainText = Label(root, textvariable=Result)
OutputLabel = Label(root, text="OUTPUT > ", fg="red")

# Create buttons
AdvantageRollButton = ttk.Button(text="Advantage Roll", command=AdvantageRoll)
DisadvantageRollButton = ttk.Button(text="Disadvantage Roll", command=DisadvantageRoll)
D20Rollbutton = ttk.Button(text="      D20 Roll      ", command=D20Single)
SelectTarotCardButton = ttk.Button(text="      Tarot Card       ", command=TarotCardSel)
ExitButton = ttk.Button(text="Exit", command=exit)

# Place everything on screen
OutputLabel.place(x=0,y=10)
MainText.place(x=60, y=10)
AdvantageRollButton.place(x=60, y=50)
DisadvantageRollButton.place(x=170, y=50)
D20Rollbutton.place(x=60, y=80)
SelectTarotCardButton.place(x=170, y=80)
ExitButton.place(x=122, y=110)

# Start the GUI/loop
root.mainloop()