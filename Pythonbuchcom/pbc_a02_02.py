# !/usr/bin/env python
# -*- coding:utf-8 -*-
from math import sqrt

def get_float(msg = "Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

def main():
    print("-----Quadratische Gleichungen lösen-----")
    print("------------ ax^2+bx+c = 0 -------------")
    a = get_float(msg = "Bitte Koeffizienten a eingeben: ")
    b = get_float(msg = "Bitte Koeffizienten b eingeben: ")
    c = get_float(msg = "Bitte Koeffizienten c eingeben: ")

    if a == 0.0:
        x = -c/b
        print(f"Es gibt eine reelle Lösung: x = {x}")
    else:
        p = b/a
        q = c/a
        diskriminante = ((p/2)*(p/2)) - q

        #Es gibt zwei verschiedene reelle Lösungen
        if diskriminante > 0:
            x1 = -p/2 + sqrt(diskriminante)
            x2 = -p/2 - sqrt(diskriminante)
            print(f"Es gibt zwei reelle Lösungen: x1 = {x1}, x2 = {x2}")
        #Es gibt eine reelle Lösung
        elif diskriminante == 0:
            x = -p/2
            print(f"Es gibt eine reelle Lösung: x = {x}")
        #Es gibt keine reelle Lösungen
        else: #diskriminante < 0
            print(f"Es keine reelle Lösung")

if __name__ == '__main__':
    main()
