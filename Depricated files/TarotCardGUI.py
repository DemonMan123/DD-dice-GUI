from tkinter import *
from tkinter import ttk
from TarotCardSelect import SelectCards
# FUCK gui's. Also yes, I'm too lazy to delete code.

MainWindow = Tk()

MainWindow.title("Demin's Card Selector")
MainWindow.resizable(False,False)
MainWindow.geometry('300x80')

# Create columns and rows
#MainWindow.columnconfigure((0,1,2,3,4,5,6), weight=1)
#MainWindow.rowconfigure((0,1,2,3,4,5,6), weight=1)
def Select():
    NewCard = SelectCards()
    SelectedCard.set(NewCard)

SelectedCard = StringVar()
lbl = Label(MainWindow, textvariable=SelectedCard)
lbl.pack()
#lbl.grid(column=4, row=2, sticky="NWSE")

CardButton = ttk.Button(text="New Card?", command=Select)
CloseButton = ttk.Button(text="Close", command=quit)
CardButton.pack()
CloseButton.pack()

# Place button in Grid
#CardButton.grid(column=4, row=3, sticky='nwse')
MainWindow.mainloop()