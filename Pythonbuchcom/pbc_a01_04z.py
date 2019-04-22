# !/usr/bin/env python
# -*- coding:utf-8 -*-
import doctest
from math import pi as PI

def get_float(msg = "Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

def get_menue_eintrag(ue_max_eintraege):
    while True:
        try:
            eingabe = int(input("Bitte Menüeintrag auswählen: "))
            if (eingabe > 0) and (eingabe <= ue_max_eintraege):
                return eingabe
            else:
                print(f"Bitte Eintrag zwischen 0 und {ue_max_eintraege+1} auswählen!")
        except ValueError:
            print("Bitte gültigen Menüeintrag eingeben")


def gradmass_in_bogenmass(ue_gradmass):
    """
    Umrechnung des Gradmasses eines Winkels in Bogenmass

    >>> gradmass_in_bogenmass(51.5662)
    0.9
    >>> gradmass_in_bogenmass(90)
    1.57
    >>>
    """
    return round(ue_gradmass*PI/180,2)

def bogenmass_in_gradmass(ue_bogenmass):
    """
    Umrechnung des Bogenmass eines Winkels in Gradmass

    >>> bogenmass_in_gradmass(0.8941321747749998)
    51.23
    >>> bogenmass_in_gradmass(1.570796327)
    90.0
    >>>
    """
    return round(ue_bogenmass*180/PI,2)

def bogenmass_in_gradmass_zeit(ue_bogenmass):
    """
    Umrechnung des Bogenmass eines Winkels in Gradmass
    mit den Rückgabewerten Grad, Minute, Sekunde

    >>> bogenmass_in_gradmass_zeit(0.8942107145912499)
    (51, 14, 4.2)
    >>>
    """
    gm_gesamt = 180*ue_bogenmass/PI
    gm_dez = int(gm_gesamt) #Ausgabe Grad °
    gm_komma = gm_gesamt - gm_dez
    gm_min_gesamt = gm_komma * 60
    gm_min_dez = int(gm_min_gesamt) #Ausgabe Minute '
    gm_min_komma = gm_min_gesamt - gm_min_dez
    gm_sek_gesamt = round(gm_min_komma * 60,2) #Ausgabe Sekunden ''
    return gm_dez, gm_min_dez, gm_sek_gesamt

def programm_testen():
    print("\n-------------------------------------------------------")
    print("Fehlgeschlagene Test:")
    doctest.testmod()
    print("-------------------------------------------------------\n")

def main():
    beenden = False
    while beenden == False:
        print("           Winkel Umwandler")
        print("-----------------Menü---------------------")
        print("(1) Gradmass in Bogenmass")
        print("(2) Bogenmass in Gradmass")
        print("(3) Bogenmass in Grad, Minute, Sekunde")
        print("(4) Programm testen")
        print("(5) Programm beenden")

        eingabe = get_menue_eintrag(5)
        if eingabe == 1:
            temp_gradmass = get_float("Winkel im Gradmass eingeben: ")
            temp_ausgabe = gradmass_in_bogenmass(temp_gradmass)
            print(f"{round(temp_gradmass,2)}° sind umgerechnet {temp_ausgabe}rad")

        elif eingabe == 2:
            temp_bogenmass = get_float("Winkel im Bogenmass eingeben: ")
            temp_ausgabe = bogenmass_in_gradmass(temp_bogenmass)
            print(f"{round(temp_bogenmass,2)}rad sind umgerechnet {temp_ausgabe}°")

        elif eingabe == 3:
            temp_bogenmass = get_float("Winkel im Bogenmass eingeben: ")
            grad, minute, sekunde = bogenmass_in_gradmass_zeit(temp_bogenmass)
            print(f"{round(temp_bogenmass,2)}rad entspricht {grad}° {minute}` {sekunde}`` ")

        elif eingabe == 4:
            programm_testen()

        elif eingabe == 5:
            beenden = True
            print("Programm beenden")

        else:
            print("Eintrag ist nicht vorhanden")

if __name__ == '__main__':
    main()
