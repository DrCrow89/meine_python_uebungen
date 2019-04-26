# !/usr/bin/env python
# -*- coding:utf-8 -*-
zahlen_liste = []
print("Bitte nacheinander Zahlen eingeben. Zum Abschließen ein \"q\" eingeben.")
beenden = False
while beenden == False:
    eingabe = input("Eingabe: ")
    try:
        zahlen_liste.append(float(eingabe))
    except:
        if eingabe == "q":
            beenden = True
        print("Bitte Zahlen eingeben.")
zahlen_liste.sort()
print(zahlen_liste)
