# !/usr/bin/env python
# -*- coding:utf-8 -*-
from math import pi

print("Umrechner Bogenmass in Gradmass")
winkel_bogenmass = float(input("Winkel im Bogenmass eingeben: "))
gm_gesamt = 180*winkel_bogenmass/pi
gm_dez = int(gm_gesamt) #Ausgabe Grad °
gm_komma = gm_gesamt - gm_dez

gm_min_gesamt = gm_komma * 60
gm_min_dez = int(gm_min_gesamt) #Ausgabe Minute '
gm_min_komma = gm_min_gesamt - gm_min_dez

gm_sek_gesamt = round(gm_min_komma * 60,2) #Ausgabe Sekunden ''

print(f"{winkel_bogenmass}rad entspricht {gm_dez}° {gm_min_dez}` {gm_sek_gesamt}`` ")
