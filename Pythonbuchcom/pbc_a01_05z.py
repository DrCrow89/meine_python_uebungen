from tkinter import * #Nicht empfohlen
from math import pi as PI
import temperaturen

OPTIONS = [
    "Gradmass in Bogenmass",
    "Bogenmass in Gradmass",
    "Bogenmass in Grad, Minute, Sekunde"
]

def beenden():
    fenster.destroy()

def gradmass_in_bogenmass(ue_gradmass):
    return round(ue_gradmass*PI/180,2)

def bogenmass_in_gradmass(ue_bogenmass):
    return round(ue_bogenmass*180/PI,2)

def bogenmass_in_gradmass_zeit(ue_bogenmass):
    gm_gesamt = 180*ue_bogenmass/PI
    gm_dez = int(gm_gesamt) #Ausgabe Grad °
    gm_komma = gm_gesamt - gm_dez
    gm_min_gesamt = gm_komma * 60
    gm_min_dez = int(gm_min_gesamt) #Ausgabe Minute '
    gm_min_komma = gm_min_gesamt - gm_min_dez
    gm_sek_gesamt = round(gm_min_komma * 60,2) #Ausgabe Sekunden ''
    return gm_dez, gm_min_dez, gm_sek_gesamt

def handler_eingabe():
    auswahl = variable.get()
    eingabe = eingabe_feld.get()
    try:
        if auswahl == "Gradmass in Bogenmass":
            ergebnis = gradmass_in_bogenmass(float(eingabe))
            temp_ausgabe = "Ergebnis: " + str(ergebnis) + "rad"
            ergebnis_label.config(text = temp_ausgabe)

        elif auswahl == "Bogenmass in Gradmass":
            ergebnis = bogenmass_in_gradmass(float(eingabe))
            temp_ausgabe = "Ergebnis: " + str(ergebnis) + "°"
            ergebnis_label.config(text = temp_ausgabe)

        elif auswahl == "Bogenmass in Grad, Minute, Sekunde":
            grad, minute, sekunde = bogenmass_in_gradmass_zeit(float(eingabe))
            temp_ausgabe = "Ergebnis: " + str(grad) + "° " + str(minute) + "' " + str(sekunde) + "'' "
            ergebnis_label.config(text = temp_ausgabe)

    except:
        ergebnis_label.config(text = "Bitte eine Kommazahl eingeben")
# Fenster
fenster = Tk()
fenster.title("Winkel Rechner")
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
info_label = Label(fenster, justify = LEFT, text="******************** Winkel Rechner ********************\n\
1) Gewünschte Umrechnungsart auswählen\n\
2) Winkel eingeben\n\
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
