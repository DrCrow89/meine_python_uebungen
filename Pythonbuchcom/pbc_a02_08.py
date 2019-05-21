# !/usr/bin/env python3.6
# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, '/home/roland/git/meine_python_uebungen/')
import allg_func, rkmath

def main():

    while True:
        eingabe = int(allg_func.get_eingabe_float("Bitte eine natürliche Zahl für die Primfaktorzerlegung eingeben: "))
        if eingabe >= 2:
            break

    zer_liste = rkmath.get_primfaktorzerlegung(eingabe)
    print(zer_liste)

if __name__ == '__main__':
    main()
