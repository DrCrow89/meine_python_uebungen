# !/usr/bin/env python
# -*- coding:utf-8 -*-

def get_eingabe_float(msg = "Bitte Zahl von Typ float eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")
