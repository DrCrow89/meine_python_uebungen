# !/usr/bin/env python
# -*- coding:utf-8 -*-

print("          Temperatur Umwandler")
print("-----------------Menü---------------------")
print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")
print("-----------------Info---------------------")
print("Die Umrechnungen berücksichtigen immer den absoluten Nullpunkt von 0K")
eingabe = int(input("Bitte Umrechnung wählen: "))

if eingabe == 1:
    eingabe_celsius = float(input("Bitte Temperatur in °C eingeben: "))
    ausgabe_celsius = round(eingabe_celsius, 2)
    ausgabe_kelvin = round(eingabe_celsius + 273.15, 2)
    if ausgabe_kelvin < 0:
        ausgabe_kelvin = 0
    print(f"{ausgabe_celsius}°C sind umgerechnet {ausgabe_kelvin}K")
elif eingabe == 2:
    eingabe_celsius = float(input("Bitte Temperatur in °C eingeben: "))
    ausgabe_celsius = round(eingabe_celsius, 2)
    ausgabe_fahrenheit = round((eingabe_celsius/(5/9))+32,2)
    print(f"{ausgabe_celsius}°C sind umgerechnet {ausgabe_fahrenheit}°F")
elif eingabe == 3:
    eingabe_kelvin = float(input("Bitte Temperatur in K eingeben: "))
    if eingabe_kelvin < 0:
        eingabe_kelvin = 0
    ausgabe_kelvin = round(eingabe_kelvin, 2)
    ausgabe_celsius = round(eingabe_kelvin - 273.15, 2)
    print(f"{ausgabe_kelvin}K sind umgerechnet {ausgabe_celsius}°C")
elif eingabe == 4:
    eingabe_kelvin = float(input("Bitte Temperatur in K eingeben: "))
    if eingabe_kelvin < 0:
        eingabe_kelvin = 0
    ausgabe_kelvin = round(eingabe_kelvin, 2)
    ausgabe_fahrenheit = round(((eingabe_kelvin - 273.15)/(5/9)) + 32, 2)
    print(f"{ausgabe_kelvin}K sind umgerechnet {ausgabe_fahrenheit}°F")
elif eingabe == 5:
    eingabe_fahrenheit = float(input("Bitte Temperatur in °F eingeben: "))
    ausgabe_fahrenheit = round(eingabe_fahrenheit, 2)
    ausgabe_celsius = round(5/9 * (eingabe_fahrenheit - 32), 2)
    print(f"{ausgabe_fahrenheit}°F sind umgerechnet {ausgabe_celsius}°C")
elif eingabe == 6:
    eingabe_fahrenheit = float(input("Bitte Temperatur in °F eingeben: "))
    ausgabe_fahrenheit = round(eingabe_fahrenheit, 2)
    ausgabe_kelvin = round((5/9 * (eingabe_fahrenheit - 32)) + 273.15, 2)
    if ausgabe_kelvin < 0:
        ausgabe_kelvin = 0
    print(f"{ausgabe_fahrenheit}°F sind umgerechnet {ausgabe_kelvin}K")
else:
    print("Eintrag ist nicht vorhanden")
