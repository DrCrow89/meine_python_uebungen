# !/usr/bin/env python
# -*- coding:utf-8 -*-
from math import pi as PI

print("           Winkel Umwandler")
print("-----------------Menü---------------------")
print("(1) Gradmass in Bogenmass")
print("(2) Bogenmass in Gradmass")

eingabe = int(input("Bitte Umrechnung wählen: "))
if eingabe == 1:
    winkel_gradmass = float(input("Winkel im Gradmass eingeben: "))
    bm_gesamt = round(winkel_gradmass*PI/180,2)
    print(f"{winkel_gradmass}° entspricht {bm_gesamt}rad")
elif eingabe == 2:
    winkel_bogenmass = float(input("Winkel im Bogenmass eingeben: "))
    gm_gesamt = 180*winkel_bogenmass/pi
    gm_dez = int(gm_gesamt) #Ausgabe Grad °
    gm_komma = gm_gesamt - gm_dez
    gm_min_gesamt = gm_komma * 60
    gm_min_dez = int(gm_min_gesamt) #Ausgabe Minute '
    gm_min_komma = gm_min_gesamt - gm_min_dez
    gm_sek_gesamt = round(gm_min_komma * 60,2) #Ausgabe Sekunden ''
    print(f"{winkel_bogenmass}rad entspricht {gm_dez}° {gm_min_dez}` {gm_sek_gesamt}`` ")
else:
    print("Eintrag ist nicht vorhanden")
