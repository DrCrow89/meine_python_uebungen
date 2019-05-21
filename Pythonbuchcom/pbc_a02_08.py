# !/usr/bin/env python3.6
# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, '/home/roland/git/meine_python_uebungen/')
import allg_func, rkmath

def main():
    zer_liste = []

    while True:
        eingabe = int(allg_func.get_eingabe_float("Bitte eine natürliche Zahl für die Primfaktorzerlegung eingeben: "))
        if eingabe >= 2:
            break

    prim_liste = rkmath.sieb_eratosthenes(100)

    for i, val in enumerate(prim_liste):
        if prim_liste[i] == True:
            while eingabe%i == 0:
                eingabe = eingabe/i;
                zer_liste.append(i)
                
    print(zer_liste)

if __name__ == '__main__':
    main()
