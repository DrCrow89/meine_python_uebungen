# !/usr/bin/env python
# -*- coding:utf-8 -*-

def quersumme_dritter_potenzen(ue_zahl):
    temp_summe = 0
    temp_zahl = ue_zahl
    while True:
        temp_summe = temp_summe + (temp_zahl%10) ** 3
        temp_zahl = temp_zahl//10
        if temp_zahl == 0:
            break
    return temp_summe

def main():
    while True:
        try:
            eingabe = int(input("Bitte Zahl eingeben (ganze Zahl>0 und durch 3 teilbar): "))
            if (eingabe <= 0):
                print("Es muss eine Zahl größer 0 eingegeben werden!")
            else:
                if eingabe%3 == 0:
                    break
                else:
                    print("Es muss eine Zahl die durch drei teilbar ist eingegeben werden!")
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")
    pruefe_zahl = eingabe
    zaehler = 0
    while True:
        pruefe_zahl = quersumme_dritter_potenzen(pruefe_zahl)
        if pruefe_zahl == 153:
            print(f"Die Zahl {eingabe} endet mit der Quersumme dritter Potenzen auch in 153 nach {zaehler} Durchläufen.")
            break
        else:
            zaehler += 1

if __name__ == '__main__':
    main()
