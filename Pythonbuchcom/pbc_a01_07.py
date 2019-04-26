# !/usr/bin/env python
# -*- coding:utf-8 -*-

def get_float(msg = "Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

def get_bin(msg = "Bitte eine Zahl zwischen 0 und 1 eingeben: "):
    while True:
        try:
            f = int(input(msg))
            if f == 0 or f == 1:
                return f
            else:
                print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

def round_dot_half(ue_zahl):
    return round(ue_zahl * 2) / 2

def main():
    eingabe_erfolgreich = False
    print("-----Abschlussnoten Hilfe-----")
    note = get_float("Bitte Prüfungsnote mit einer Nachkommastelle eingeben: ")
    augenfarbe = get_bin("Augenfarbe (dunkel=1, hell=0): ")
    frisur = get_bin("Bitte Frisur eingeben (kurze Haare=1, lange Haare=0): ")
    wetter = get_bin("Bitte Wetter eingeben (schön=1, nicht schön=0): ")

    if augenfarbe == 1: # Augenfarbe dunkel
        if frisur == 1: # Haare kurz
            temp_note = note + 0.1 * note
        else: # Haare lang
            temp_note = note - 0.1 * note
    else: # Augenfarbe hell
        if frisur == 1: # Haare kurz
            temp_note = note - 0.1 * note
        else: # Haare lang
            temp_note = note + 0.1 * note
    if wetter == 1: # Wetter ist schön
        temp_note -= 1
    temp_note = round_dot_half(temp_note)
    if temp_note < 1:
        temp_note = 1
    print("Berechnete Abschlussnote: " + str(temp_note))

if __name__ == '__main__':
    main()
