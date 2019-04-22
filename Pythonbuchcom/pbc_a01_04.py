# !/usr/bin/env python
# -*- coding:utf-8 -*-
import doctest

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
    """
    Umrechnung der Temperatur von Celsius in Kelvin

    >>> celsius_in_kelvin(0)
    273.15
    >>> celsius_in_kelvin(-273.15)
    0.0
    >>> celsius_in_kelvin(11.5)
    284.65
    >>>
    """
    if ue_celsius >= ABSOLUTER_NP_C:
        return round(ue_celsius - ABSOLUTER_NP_C,2)
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def celsius_in_fahrenheit(ue_celsius):
    """
    Umrechnung der Temperatur von Celsius in Fahrenheit

    >>> celsius_in_fahrenheit(0)
    32.0
    >>> celsius_in_fahrenheit(-273.15)
    -459.67
    >>> celsius_in_fahrenheit(11.5)
    52.7
    >>>
    """
    if ue_celsius >= ABSOLUTER_NP_C:
        return round((ue_celsius/(CONST_F_1)) + CONST_F_2,2)
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def kelvin_in_celsius(ue_kelvin):
    """
    Umrechnung der Temperatur von Kelvin in Celsius

    >>> kelvin_in_celsius(0)
    -273.15
    >>> kelvin_in_celsius(11.5)
    -261.65
    >>>
    """

    if ue_kelvin >= ABSOLUTER_NP_K:
        return round(ue_kelvin + ABSOLUTER_NP_C,2)
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def kelvin_in_fahrenheit(ue_kelvin):
    """
    Umrechnung der Temperatur von Kelvin in Fahrenheit

    >>> kelvin_in_fahrenheit(0)
    -459.67
    >>> kelvin_in_fahrenheit(11.5)
    -438.97
    >>>
    """
    if ue_kelvin >= ABSOLUTER_NP_K:
        return round(((ue_kelvin + ABSOLUTER_NP_C)/(CONST_F_1)) + CONST_F_2,2)
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def fahrenheit_in_celsius(ue_fahrenheit):
    """
    Umrechnung der Temperatur von Fahrenheit in Celsius

    >>> fahrenheit_in_celsius(0)
    -17.78
    >>> fahrenheit_in_celsius(-459.67)
    -273.15
    >>> fahrenheit_in_celsius(11.5)
    -11.39
    >>>
    """
    if ue_fahrenheit >= ABSOLUTER_NP_F:
        return round(CONST_F_1 * (ue_fahrenheit - CONST_F_2),2)
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def fahrenheit_in_kelvin(ue_fahrenheit):
    """
    Umrechnung der Temperatur von Fahrenheit in Kelvin

    >>> fahrenheit_in_kelvin(0)
    255.37
    >>> fahrenheit_in_kelvin(-459.67)
    0.0
    >>> fahrenheit_in_kelvin(11.5)
    261.76
    >>>
    """
    if ue_fahrenheit >= ABSOLUTER_NP_F:
        return abs(round((CONST_F_1 * (ue_fahrenheit - CONST_F_2)) - ABSOLUTER_NP_C,2))
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

def programm_testen():
    print("-------------------------------------------------------")
    print("Fehlgeschlagene Test:")
    doctest.testmod()
    print("-------------------------------------------------------")

def main():
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
        print("(7) Programm testen")
        print("(8) Programm beenden")
    #print("-----------------Info---------------------")
    #print("Die Umrechnungen berücksichtigen immer den absoluten Nullpunkt von 0K")

        eingabe = get_menue_eintrag(8)
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
            programm_testen()

        elif eingabe == 8:
            beenden = True
            print("Programm beenden")

        else:
            print("Eintrag ist nicht vorhanden")

if __name__ == '__main__':
    main()
