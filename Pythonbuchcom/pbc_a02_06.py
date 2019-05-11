# !/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, '/home/roland/git/meine_python_uebungen/')
import allg_func
from math import sqrt

def sieb(ue_n):
    list = []
    # Es muss nur bis zur Zahl geprüft werden der größer oder
    # gleich der Wurzel des zu überprüfenden Bereich ist
    # Beispiel: N = 990 -> sqrt(990) = 31.4642654451 --> 32
    bereich = int(sqrt(ue_n)) + 1
    # Liste wird gefüllt mit gültigen Werten
    for i in range(0, ue_n + 1, 1):
        list.append(True)

    list[0] = False # Zahl 0 keine Primzahl
    list[1] = False # Zahl 1 keine Primzahl

    for i in range(2, bereich + 1, 1):
        #print("Index: " + str(i) + " Eintrag: " + str(list[i]))
        if list[i] == True:
            for j in range(2*i, ue_n + 1, i):
                list[j] = False
    return list


def main():
    while True:
        eingabe = int(allg_func.get_eingabe_float("Bitte eine Zahl >= 2 eingeben: "))
        if eingabe >= 2:
            break

    list_sieb = sieb(eingabe)

    temp_zaehler = 0
    for i, val in enumerate(list_sieb):
        if list_sieb[i] == True:
            temp_zaehler += 1

    print("Es gibt " + str(temp_zaehler) + " Primzahlen, welche kleiner sind als " + str(eingabe))

if __name__ == '__main__':
    main()
