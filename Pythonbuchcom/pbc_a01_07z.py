# !/usr/bin/env python
# -*- coding:utf-8 -*-
from tkinter import * #Nicht empfohlen

FENSTERBREITE = 550
FENSTERHOEHE = 250
ABSTAND_X = 25
ABSTAND_Y = 50
BREITE = 150

AUGENFARBE = [
    "dunkel",
    "hell"
]

FRISUR = [
    "kurze Haare",
    "lange Haare"
]

WETTER = [
    "schön",
    "nicht schön"
]

def get_float(msg = "Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

def round_dot_half(ue_zahl):
    return float(round(ue_zahl * 2) / 2)

def beenden():
    fenster.destroy()

def handler_eingabe():
    try:
        note = float(eingabe_feld.get())
        ergebnis_label.config(text = note)
        if var_augenfarbe.get() == "dunkel": # Augenfarbe dunkel
            if var_frisur.get() == "kurze Haare": # Haare kurz
                temp_note = note + 0.1 * note
                #print("1: " + str(note) + " + 0.1 * " + str(note) + " = " + str(temp_note))
            else: # Haare lang
                temp_note = note - 0.1 * note
                #print("2: " + str(note) + " - 0.1 * " + str(note) + " = " + str(temp_note))
        else: # Augenfarbe hell
            if var_frisur.get() == "kurze Haare": # Haare kurz
                temp_note = note - 0.1 * note
                #print("3: " + str(note) + " - 0.1 * " + str(note) + " = " + str(temp_note))
            else: # Haare lang
                temp_note = note + 0.1 * note
                #print("4: " + str(note) + " + 0.1 * " + str(note) + " = " + str(temp_note))
        if var_wetter.get() == "schön": # Wetter ist schön
            temp_note -= 1
            #print("5: Wetter ist schön " + str(temp_note))
        if temp_note < 1:
            temp_note = 1.0
        elif temp_note > 6:
            temp_note = 6.0
        temp_note = round_dot_half(temp_note)
        temp_ergebnis = "Berechnete Abschlussnote: " + str(temp_note)
        ergebnis_label.config(text = temp_ergebnis)

    except:
        ergebnis_label.config(text = "Bitte eine Gleitkommazahl eingeben und mit Punkt trennen.")

# Fenster
fenster = Tk()
fenster.title("Abschlussnoten Hilfe")
fenstergroesse = str(FENSTERBREITE) + "x" + str(FENSTERHOEHE)
fenster.geometry(fenstergroesse)

# Menü
mBar = Menu(fenster)
mFile = Menu(mBar)
mFile.add_command(label="Beenden", command=beenden)
mBar.add_cascade(label="Datei",menu=mFile)
fenster["menu"] = mBar

# Allgemeine Variablen im Fenster
var_augenfarbe = StringVar(fenster)
var_augenfarbe.set(AUGENFARBE[0]) # default value
var_frisur = StringVar(fenster)
var_frisur.set(FRISUR[0])
var_wetter = StringVar(fenster)
var_wetter.set(WETTER[0])

# Berechnungsliste
liste_augenfarbe = OptionMenu(fenster, var_augenfarbe, *AUGENFARBE)
liste_frisur = OptionMenu(fenster, var_frisur, *FRISUR)
liste_wetter = OptionMenu(fenster, var_wetter, *WETTER)

# Labels
info_label = Label(fenster, justify = LEFT, text="******************** Abschlussnoten Hilfe ********************\n"\
"**************************************************************")
note_label = Label(fenster, text="Note: ")
ergebnis_label = Label(fenster, justify = LEFT, text="Ergebnis: ")

# Eingabefeld
eingabe_feld = Entry(fenster, bd=5, width=20)

# Buttons
berechnen_button = Button(fenster, text="Umrechnen", command=handler_eingabe)

# Elemente in Fenster legen
info_label.place(anchor=N, x=FENSTERBREITE/2, y=0)
liste_augenfarbe.place(x=ABSTAND_X, width=BREITE, y=ABSTAND_Y)
liste_frisur.place(x=ABSTAND_X*2+BREITE, width=BREITE, y=ABSTAND_Y)
liste_wetter.place(x=ABSTAND_X*3+BREITE*2, width=BREITE, y=ABSTAND_Y)
note_label.place(x=ABSTAND_X, width=BREITE, y=ABSTAND_Y*2)
eingabe_feld.place(x=ABSTAND_X*2+BREITE, width=BREITE, y=ABSTAND_Y*2)
berechnen_button.place(x=ABSTAND_X, width=BREITE, y=ABSTAND_Y*3)
ergebnis_label.place(anchor=W, x=ABSTAND_X, y=ABSTAND_Y*4)

def main():
    fenster.mainloop()

if __name__ == '__main__':
    main()
