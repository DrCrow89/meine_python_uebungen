# !/usr/bin/env python3.6
# -*- coding:utf-8 -*-
from math import sqrt
import doctest

def loese_quad_gleichung_pq(ue_a, ue_b, ue_c, ue_d):
    """
    Funktion löst eine quadratische Gleichung der Form ax^2+bx+c = d

    Rückgabewert ist eine Liste:
    [0] -> Anzahl der Lösungen (Null, eine oder zwei reelle Lösungen)
    [1] -> x1
    [2] -> x2

    >>> loese_quad_gleichung_pq(4, 2, -6, 0)
    [2, 1.0, -1.5]
    >>> loese_quad_gleichung_pq(0, -3, 7, 0)
    [1, 2.3333333333333335, 2.3333333333333335]
    >>> loese_quad_gleichung_pq(-4, 2, 6, 2)
    [2, 1.2807764064044151, -0.7807764064044151]
    >>> loese_quad_gleichung_pq(4, 2, 6, 2)
    [0, 0, 0]
    >>>
    """
    if ue_d == 0.0:
        a = ue_a
        b = ue_b
        c = ue_c
    else:
        a = ue_a
        b = ue_b
        c = ue_c - ue_d

    if a == 0.0:
        x = -c/b
        list = [1, x, x]
        return list
    else:
        p = b/a
        q = c/a
        diskriminante = ((p/2)*(p/2)) - q

        #Es gibt zwei verschiedene reelle Lösungen
        if diskriminante > 0:
            x1 = -p/2 + sqrt(diskriminante)
            x2 = -p/2 - sqrt(diskriminante)
            list = [2, x1, x2]
            return list
        #Es gibt eine reelle Lösung
        elif diskriminante == 0:
            x = -p/2
            list = list = [1, x, x]
            return list
        #Es gibt keine reelle Lösungen
        else: #diskriminante < 0
            list = [0, 0, 0]
            return list

def stellenwert_hundert(ue_zahl):
    """
    Funktion gibt zu einer Zahl, welche kleiner 1000 sein muss, die Einer-, Zehner- und Hunderterstelle zurück.

    >>> stellenwert_hundert(1)
    (0, 0, 1)
    >>> stellenwert_hundert(29)
    (0, 2, 9)
    >>> stellenwert_hundert(153)
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
