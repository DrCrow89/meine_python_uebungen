# !/usr/bin/env python
# -*- coding:utf-8 -*-

ABSOLUTER_NP_C = -273.15
ABSOLUTER_NP_F = -459.67
CONST_F_1 = 5/9
CONST_F_2 = 32
ABSOLUTER_NP_K = 0
FEHLERMELDUNG_TEMP = "Ungültiger Bereich der eingegebenen Temperatur"

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

def celsius_in_kelvin(ue_celsius):
    if ue_celsius >= ABSOLUTER_NP_C:
        return ue_celsius - ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def celsius_in_fahrenheit(ue_celsius):
    if ue_celsius >= ABSOLUTER_NP_C:
        return (ue_celsius/(CONST_F_1)) + CONST_F_2
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def kelvin_in_celsius(ue_kelvin):
    if ue_kelvin >= ABSOLUTER_NP_K:
        return ue_kelvin + ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def kelvin_in_fahrenheit(ue_kelvin):
    if ue_kelvin >= ABSOLUTER_NP_K:
        return ((ue_kelvin + ABSOLUTER_NP_C)/(CONST_F_1)) + CONST_F_2
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def fahrenheit_in_celsius(ue_fahrenheit):
    if ue_fahrenheit >= ABSOLUTER_NP_F:
        return CONST_F_1 * (ue_fahrenheit - CONST_F_2)
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def fahrenheit_in_kelvin(ue_fahrenheit):
    if ue_fahrenheit >= ABSOLUTER_NP_F:
        return (CONST_F_1 * (ue_fahrenheit - CONST_F_2)) - ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

beenden = False
while beenden == False:
    print("          Temperatur Umwandler")
    print("-----------------Menü---------------------")
    print("(1) Umrechnung von Celsius nach Kelvin")
    print("(2) Umrechnung von Celsius nach Fahrenheit")
    print("(3) Umrechnung von Kelvin nach Celsius")
    print("(4) Umrechnung von Kelvin nach Fahrenheit")
    print("(5) Umrechnung von Fahrenheit nach Celsius")
    print("(6) Umrechnung von Fahrenheit nach Kelvin")
    print("(7) Programm beenden")
    #print("-----------------Info---------------------")
    #print("Die Umrechnungen berücksichtigen immer den absoluten Nullpunkt von 0K")

    eingabe = get_menue_eintrag(7)
    if eingabe == 1:
        temp_celsius = get_float("Bitte Temperatur in °C eingeben: ")
        temp_ausgabe = celsius_in_kelvin(temp_celsius)
        print(f"{round(temp_celsius,2)}°C sind umgerechnet {round(temp_ausgabe,2)}K")

    elif eingabe == 2:
        temp_celsius = get_float("Bitte Temperatur in °C eingeben: ")
        temp_ausgabe = celsius_in_fahrenheit(temp_celsius)
        print(f"{round(temp_celsius,2)}°C sind umgerechnet {round(temp_ausgabe,2)}°F")

    elif eingabe == 3:
        temp_kelvin = get_float("Bitte Temperatur in K eingeben: ")
        temp_ausgabe = kelvin_in_celsius(temp_kelvin)
        print(f"{round(temp_kelvin,2)}K sind umgerechnet {round(temp_ausgabe,2)}°C")

    elif eingabe == 4:
        temp_kelvin = get_float("Bitte Temperatur in K eingeben: ")
        temp_ausgabe = kelvin_in_fahrenheit(temp_kelvin)
        print(f"{round(temp_kelvin,2)}K sind umgerechnet {round(temp_ausgabe,2)}°F")

    elif eingabe == 5:
        temp_fahrenheit = get_float("Bitte Temperatur in °F eingeben: ")
        temp_ausgabe = fahrenheit_in_celsius(temp_fahrenheit)
        print(f"{round(temp_fahrenheit,2)}°F sind umgerechnet {round(temp_ausgabe,2)}°C")

    elif eingabe == 6:
        temp_fahrenheit = get_float("Bitte Temperatur in °F eingeben: ")
        temp_ausgabe = fahrenheit_in_kelvin(temp_fahrenheit)
        print(f"{round(temp_fahrenheit,2)}°F sind umgerechnet {round(temp_ausgabe,2)}°C")

    elif eingabe == 7:
        beenden = True
        print("Programm beenden")

    else:
        print("Eintrag ist nicht vorhanden")
