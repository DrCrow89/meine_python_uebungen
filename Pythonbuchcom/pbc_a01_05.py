from tkinter import * #Nicht empfohlen
import temperaturen

OPTIONS = [
    "Celsius nach Kelvin",
    "Celsius nach Fahrenheit",
    "Kelvin nach Celsius",
    "Kelvin nach Fahrenheit",
    "Fahrenheit nach Celsius",
    "Fahrenheit nach Kelvin"
]

def beenden():
    fenster.destroy()

def handler_eingabe():
    try:
        auswahl = variable.get()
        eingabe = eingabe_feld.get()
        if auswahl == "Celsius nach Kelvin":
            valid, ergebnis = temperaturen.celsius_in_kelvin(float(eingabe))
            if valid == True:
                temp_ausgabe = "Ergebnis: " + str(ergebnis) + " K"
                ergebnis_label.config(text = temp_ausgabe)
            else:
                ergebnis_label.config(text = "Bitte eine gültige Temperatur eingeben.")
        elif auswahl == "Celsius nach Fahrenheit":
            valid, ergebnis = temperaturen.celsius_in_fahrenheit(float(eingabe))
            if valid == True:
                temp_ausgabe = "Ergebnis: " + str(ergebnis) + " °F"
                ergebnis_label.config(text = temp_ausgabe)
            else:
                ergebnis_label.config(text = "Bitte eine gültige Temperatur eingeben.")
        elif auswahl == "Kelvin nach Celsius":
            valid, ergebnis = temperaturen.kelvin_in_celsius(float(eingabe))
            if valid == True:
                temp_ausgabe = "Ergebnis: " + str(ergebnis) + " °C"
                ergebnis_label.config(text = temp_ausgabe)
            else:
                ergebnis_label.config(text = "Bitte eine gültige Temperatur eingeben.")
        elif auswahl == "Kelvin nach Fahrenheit":
            valid, ergebnis = temperaturen.kelvin_in_fahrenheit(float(eingabe))
            if valid == True:
                temp_ausgabe = "Ergebnis: " + str(ergebnis) + " °F"
                ergebnis_label.config(text = temp_ausgabe)
            else:
                ergebnis_label.config(text = "Bitte eine gültige Temperatur eingeben.")
        elif auswahl == "Fahrenheit nach Celsius":
            valid, ergebnis = temperaturen.fahrenheit_in_celsius(float(eingabe))
            if valid == True:
                temp_ausgabe = "Ergebnis: " + str(ergebnis) + " °C"
                ergebnis_label.config(text = temp_ausgabe)
            else:
                ergebnis_label.config(text = "Bitte eine gültige Temperatur eingeben.")
        elif auswahl == "Fahrenheit nach Kelvin":
            valid, ergebnis = temperaturen.fahrenheit_in_kelvin(float(eingabe))
            if valid == True:
                temp_ausgabe = "Ergebnis: " + str(ergebnis) + " K"
                ergebnis_label.config(text = temp_ausgabe)
            else:
                ergebnis_label.config(text = "Bitte eine gültige Temperatur eingeben.")
    except:
        ergebnis_label.config(text = "Bitte eine Kommazahl eingeben")
# Fenster
fenster = Tk()
fenster.title("Temperatur Rechner")
fenster.geometry("500x250")

# Menü
mBar = Menu(fenster)
mFile = Menu(mBar)
mFile.add_command(label="Beenden", command=beenden)
mBar.add_cascade(label="Datei",menu=mFile)
fenster["menu"] = mBar

# Allgemeine Variable im Fenster
variable = StringVar(fenster)
variable.set(OPTIONS[0]) # default value
# Berechnungsliste
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
ergebnis_label.grid(row = 3, column = 0, pady = 10)

fenster.mainloop()
