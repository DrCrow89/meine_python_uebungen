# !/usr/bin/env python
# -*- coding:utf-8 -*-
from math import pi as PI

print("Umrechner Gradmass in Bogenmass")
winkel_gradmass = float(input("Winkel im Gradmass eingeben: "))
bm_gesamt = round(winkel_gradmass*PI/180,2)

print(f"{winkel_gradmass}° entspricht {bm_gesamt}rad")
