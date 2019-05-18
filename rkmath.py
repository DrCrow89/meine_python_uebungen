# !/usr/bin/env python
# -*- coding:utf-8 -*-
from math import sqrt
import doctest

def teile_dreier_zahl(ue_zahl):
    """
    Funktion gibt die 

    >>> teile_dreier_zahl(1)
    (0, 0, 1)
    >>> teile_dreier_zahl(29)
    (0, 2, 9)
    >>> teile_dreier_zahl(153)
    (1, 5, 3)
    >>>
    """

    hunderter = int(ue_zahl/100)*100
    zehner = int((ue_zahl - hunderter)/10)*10
    einer = ue_zahl - hunderter - zehner
    hunderte_stelle = int(hunderter/100)
    zehner_stelle = int(zehner/10)

    return hunderte_stelle, zehner_stelle, einer


def quersumme_dritter_potenzen(ue_zahl):
    """
    Algorithmus zur Bestimmung einer Liste aller Primzahlen kleiner oder gleich einer vorgegebenen Zahl.

    >>> quersumme_dritter_potenzen(1)
    1
    >>> quersumme_dritter_potenzen(153)
    153
    >>>
    """
    temp_summe = 0
    temp_zahl = ue_zahl
    while True:
        temp_summe = temp_summe + (temp_zahl%10) ** 3
        temp_zahl = temp_zahl//10
        if temp_zahl == 0:
            break
    return temp_summe

def sieb_eratosthenes(ue_n):
    """
    Algorithmus zur Bestimmung einer Liste aller Primzahlen kleiner oder gleich einer vorgegebenen Zahl.

    >>> sieb_eratosthenes(1)
    []
    >>> sieb_eratosthenes(2)
    [False, False, True]
    >>>
    """

    list = []
    if ue_n <= 1:
        pass
    else:
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
    print("\n-------------------------------------------------------")
    print("Fehlgeschlagene Test:")
    doctest.testmod()
    print("-------------------------------------------------------\n")

if __name__ == '__main__':
    main()
