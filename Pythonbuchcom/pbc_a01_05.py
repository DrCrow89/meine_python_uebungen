from tkinter import *

OPTIONS = [
    "Celsius nach Kelvin",
    "Celsius nach Fahrenheit",
    "Kelvin nach Celsius",
    "Kelvin nach Fahrenheit",
    "Fahrenheit nach Celsius",
    "Fahrenheit nach Kelvin",
    "Programm beenden"
]

def handler_eingabe():
    print(variable.get())

# Fenster
fenster = Tk()
fenster.title("Temperatur Rechner")
fenster.geometry("500x500")

# Allgemeine Variable im Fenster
variable = StringVar(fenster)
variable.set(OPTIONS[0]) # default value
# Optionsmenü
auswahl_liste = OptionMenu(fenster, variable, *OPTIONS)

# Labels
info_label = Label(fenster, justify = LEFT, text="******************** Temperatur Rechner ********************\n\
1) Gewünschte Umrechnungsart auswählen\n\
2) Temperatur eingeben\n\
3) Taste \"Umrechnen\" drücken")
ergebnis_label = Label(fenster, justify = LEFT, text="Ergebnis: ")

# Eingabefeld
eingabe_feld = Entry(fenster, bd=5, width=20)

# Buttons
berechnen_button = Button(fenster, text="Umrechnen", command=handler_eingabe)

# Elemente in Fenster legen
info_label.grid(row = 0, column = 0, columnspan = 3, padx = 60, pady = 0)
auswahl_liste.grid(row = 1, column = 0, columnspan = 3, padx = 60, pady = 10)
eingabe_feld.grid(row = 2, column = 0, padx = 60, pady = 10)
berechnen_button.grid(row = 2, column = 1, padx = 60, pady = 10)
ergebnis_label.grid(row = 3, column = 0, padx = 60, pady = 10)

fenster.mainloop()
