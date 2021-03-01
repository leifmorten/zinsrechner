from tkinter import *

window = Tk()

window.title("ZR")

main_lbl = Label(window, text="Bitte Zeugs eingeben", font=("Arial Bold", 10))
main_lbl.grid(column=0, row=1)

kapital_lbl = Label(window,text="Startkapital:")
kapital_lbl.grid(column=0, row=2)
kapital_entry = Entry(window, width=10)
kapital_entry.grid(column=2, row=2)

zinsen_lbl = Label(window,text="Zinssatz:")
zinsen_lbl.grid(column=0, row=3)
zinsen_entry = Entry(window, width=10)
zinsen_entry.grid(column=2, row=3)

jahre_lbl = Label(window,text="Jahre:")
jahre_lbl.grid(column=0, row=4)
jahre_entry = Entry(window, width=10)
jahre_entry.grid(column=2, row=4)

ergebnis_lbl = Label(window, text="", font=("Arial Bold", 18))
ergebnis_lbl.grid(column=0, row=6)

def clicked():
    
    kapital = float(kapital_entry.get())
    zinsen = float(zinsen_entry.get())
    jahre = float(jahre_entry.get())

    zinsen = zinsen / 100 + 1
    ergebnis = kapital * (zinsen) ** jahre
    ergebnis = round(ergebnis, 2)
    
    ergebnis_lbl.configure(text=ergebnis)

btn = Button(window, text="Rechnen!", command=clicked)
btn.grid(column=2, row=5)

window.mainloop()