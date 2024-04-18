# All the imports required to work
import datetime
import os
import requests
from tkinter import *
from tkinter import ttk
from Dice.D90 import D90Roll
from Dice.D20 import D20Roll
from Dice.D12 import D12Roll
from TarotCardSelect import SelectCards, selectEffect
from Cards.Descriptions import search_word
from GetEffectDescriptions import getEffectDescription

# Create and setup main root window
root = Tk()
img = PhotoImage(file='icons/Skull.ico')
root.title("Demin's Roll Program")
root.iconphoto(False, img)
root.resizable(False,False)
root.geometry('350x150')

Webhook_url = "YourURL"
current_datetime = datetime.datetime.now()
logs_file_path = ""


def create_log_file():
    global logs_file_path
    # Format the filename with date and 12-hour time (e.g., YYYY-MM-DD-hh-MM-SS)
    logs_filename = current_datetime.strftime("%Y-%m-%d_%I-%M-logs.txt")
    log_dir = "Logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logs_file_path = os.path.join(log_dir, logs_filename)

    with open(logs_file_path, 'w') as file:
        file.write("Log file created on " + current_datetime.strftime("%Y-%m-%d at %I:%M:%S %p\n"))

    print(f"Log file '{logs_filename}' has been created at '{log_dir}'.")
    LogSend("TEST LOG... WORKING","INITIAL")

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
    logFileAppend(f"Advantage roll: {advantage}\nD20 result: {D20R}\nD90 result: {D90R}","ADVANTAGE ROLL")
    LogSend(f"Roll: {advantage}\nD20 result: {D20R}\nD90 result: {D90R}","ADVANTAGE")
    
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
    logFileAppend(f"Disadvantage roll: {Disadvantage}\nD12 result: {D12R}\nD20 result: {D20R}", "DISADVANTAGE ROLL")
    LogSend(f"Roll Result: {Disadvantage}\nD12 result: {D12R}\nD20 result: {D20R}","DISADVANTAGE")
        
def D20Single():
    print("Running D20 Roll")
    D20R = D20Roll()
    Result.set(f"You rolled... {D20R}")
    logFileAppend(f"Rolled {D20R}","D20")
    LogSend(f"ROLLED: {D20R}","D20")

# Creating a function to create the card description window
CardDesc = None

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def CardDescriptionWindow(Card_Name, cardDesc, effect, RollType, EffectDescription):
    global CardDesc
    if CardDesc is not None and CardDesc.winfo_exists():
        CardDesc.destroy()
    
    CardDesc = Toplevel()
    CardDesc.title(f"{Card_Name}'s description")
    CardDesc.resizable(True, False)
    CardDesc.iconphoto(False, PhotoImage(file='icons/5429974.ico')) 
    center_window(CardDesc, 300, 200)  # Make sure this function is properly defined somewhere in your code

    # Display the card description with word wrapping (IDC about making it look nice. It's really a public program anyways)
    label = Label(CardDesc, text=cardDesc)
    Effect = Label(CardDesc, text=f"Your effect: {effect}")
    RollType = Label(CardDesc, text=f"Roll Type: {RollType}")
    Effect_Description = Label(CardDesc, text=f"Effect description:\n{EffectDescription}", wraplength=280)
    label.place(x=15, y=10)
    Effect.place(x=15, y=35)
    RollType.place(x=15, y=60)
    Effect_Description.place(x=15, y=90)
    
def TarotCardSel():
    TarotCard = SelectCards()
    Result.set(f"Your Tarot card: {TarotCard}")
    CardDescription = search_word(TarotCard)
    Roll = D20Roll()
    Effect,RollType = selectEffect(Roll, TarotCard)
    EffectDescription = getEffectDescription(Effect)
    print(f"Rolling D20... {Roll}")
    CardDescriptionWindow(TarotCard, CardDescription, Effect, RollType, EffectDescription)
    LogSend(f"Drew {TarotCard}\nDescription: {CardDescription}\nEffect: {Effect}","TAROT")
    logFileAppend(f"Drew {TarotCard}\nDescription: {CardDescription}\nEffect: {Effect}\nEffect type: {RollType}\nEffect Description: {EffectDescription}","TAROT")
    
def LogSend(message,type):
    data = {
        "username": f"{type} LOG",
        "content": f"{message}\n------------------------------\n"
    }
    
    response = requests.post(Webhook_url, json=data)
    if response.status_code ==  204:
        print("Log sent")
    else:
        print("Something went wrong")
        
def logFileAppend(Data,logname):
    with open(logs_file_path, "a") as logs:
        time = current_datetime.strftime("%I:%M:%S %p")
        logs.write(f"\n[{logname} LOG at {time}]\n{Data}\n")

def openLogs():
    os.startfile(logs_file_path)

# Create text for the output into GUI
Result = StringVar()
MainText = Label(root, textvariable=Result)
OutputLabel = Label(root, text="OUTPUT > ", fg="red")

# Create buttons
AdvantageRollButton = ttk.Button(text="Advantage Roll", command=AdvantageRoll)
DisadvantageRollButton = ttk.Button(text="Disadvantage Roll", command=DisadvantageRoll)
D20Rollbutton = ttk.Button(text="      D20 Roll      ", command=D20Single)
SelectTarotCardButton = ttk.Button(text="      Tarot Card       ", command=TarotCardSel)
ExitButton = ttk.Button(text="          Exit          ", command=exit)
LogButton = ttk.Button(text="            Logs           ", command=openLogs)

# Place everything on screen
OutputLabel.place(x=0,y=10)
MainText.place(x=60, y=10)
AdvantageRollButton.place(x=60, y=50)
DisadvantageRollButton.place(x=170, y=50)
D20Rollbutton.place(x=60, y=80)
SelectTarotCardButton.place(x=170, y=80)
ExitButton.place(x=60, y=110)
LogButton.place(x=170, y=110)

# Start the GUI/loop and create a logfile
if __name__ == "__main__":
    create_log_file()
    root.mainloop()