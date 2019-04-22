# !/usr/bin/env python
# -*- coding:utf-8 -*-
ABSOLUTER_NP_C = -273.15
ABSOLUTER_NP_F = -459.67
CONST_F_1 = 5/9
CONST_F_2 = 32
ABSOLUTER_NP_K = 0
FEHLERMELDUNG_TEMP = "Ungültiger Bereich der eingegebenen Temperatur"

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
        return True, round(ue_celsius - ABSOLUTER_NP_C,2)
    else:
        return False, 0

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
        return True, round((ue_celsius/(CONST_F_1)) + CONST_F_2,2)
    else:
        return False, 0

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
        return True, round(ue_kelvin + ABSOLUTER_NP_C,2)
    else:
        return False, 0

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
        return True, round(((ue_kelvin + ABSOLUTER_NP_C)/(CONST_F_1)) + CONST_F_2,2)
    else:
        return False, 0

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
        return True, round(CONST_F_1 * (ue_fahrenheit - CONST_F_2),2)
    else:
        return False, 0

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
        return True, abs(round((CONST_F_1 * (ue_fahrenheit - CONST_F_2)) - ABSOLUTER_NP_C,2))
    else:
        return False, 0

def main():
    # Sollen die Testergebnisse angezeigt werden, muss das Modul mit
    # python3.6 temperaturen.py -v
    # ausgeführt werden. Ohne das -v werden nur die fehlgeschlagenen Tests ausgegeben.
    doctest.testmod()

if __name__ == '__main__':
    import doctest
    main()
