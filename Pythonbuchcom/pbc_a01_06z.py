# !/usr/bin/env python
# -*- coding:utf-8 -*-
buchstaben_liste = []
print("Bitte nacheinander Zeichen eingeben. Zum Abschließen ein \"quit\" eingeben.")
beenden = False
while beenden == False:
    eingabe = input("Eingabe: ")
    if eingabe == "quit":
        beenden = True
    else:
        buchstaben_liste.append(eingabe)

buchstaben_liste.sort()
print(buchstaben_liste)
