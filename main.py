#ivri korem 2020
"""
Infection is a python based simulation using the SIR model,
It lets you create plagues and sandboxes to test and see the plague creates national disasters!
"""

#init
#import
from tkinter import *
from tkinter.font import Font
from Sandbox import Sandbox

#creating gui
popup = Tk()
popup.title("My Plague")
popup.geometry('380x420')

#creating fonts
textFont = Font(popup, size=10, weight="bold")
qFont = Font(popup, size=9, weight="bold")

#creating the gui
Text = Label(popup, text="Welcome to Infaction!\n here you can create a plague,\n and test it in the Sandbox.", font = textFont).grid(row=0)

Label(popup).grid(row=1, ipady=1, ipadx=25)
Label(popup, text="Enter the population of the sandbox (recommended under 1000):", font=qFont).grid(row=2,column=0, sticky=W, ipady=1)
Population = Entry(popup)
Population.grid(row=3, sticky=W, ipady=1, ipadx=25)
Label(popup, text="Enter how many ppl are already infected (recommended under 10):", font=qFont).grid(row=4, sticky=W, ipady=1)
Start = Entry(popup)
Start.grid(row=5, sticky=W, ipady=1, ipadx=25)
Label(popup, text="Enter the plague infaction radius (recommended under 200):", font=qFont).grid(row=6, sticky=W, ipady=1)
Radius = Entry(popup)
Radius.grid(row=7, sticky=W, ipady=1, ipadx=25)
Label(popup, text="Enter the plague infection rate (out of 100):", font=qFont).grid(row=8, sticky=W, ipady=1)
Infection = Entry(popup)
Infection.grid(row=9, sticky=W, ipady=1, ipadx=25)
Label(popup, text="Enter the plague recovery rate (out of 100):", font=qFont).grid(row=10, sticky=W, ipady=1)
Recovery = Entry(popup)
Recovery.grid(row=11, sticky=W, ipady=1, ipadx=25)
Label(popup, text="Enter the plague death rate (out of 100):", font=qFont).grid(row=12, sticky=W, ipady=1)
Death = Entry(popup)
Death.grid(row=13, sticky=W, ipady=1, ipadx=25)
Label(popup).grid(row=14, ipady=1, ipadx=25)

SubmitButton = Button(popup, text="Submit", font=textFont, command=lambda: createSandbox(int(Population.get()), int(Start.get()), int(Radius.get()), int(Infection.get()), int(Recovery.get()), int(Death.get())), padx=50, pady=5).grid(row=15)

#defining createSandbox
def createSandbox(population, start, radius, infection, recovery, death):
    plague = {
        'infection_radius': radius,
        'infection_rate': infection,
        'recovery_rate': recovery,
        'death_rate': death
    }
    mySandbox = Sandbox(population, plague, start)
    popup.destroy()
    mySandbox.run()

#mainloop
popup.mainloop()