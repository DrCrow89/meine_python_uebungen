# !/usr/bin/env python
# -*- coding:utf-8 -*-

def get_float(msg = "Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

def main():
    print("-----Flache Steuern-----")
    vorname = input("Bitte Vornamen eingeben: ")
    nachname = input("Bitte Nachname eingeben: ")
    einkommen = get_float("Bitte Einkommen eingeben: ")
    vermoegen = get_float("Bitte Vermögen eingeben: ")

    if (einkommen <= 10000):
        steuern_einkommen = einkommen*0.4
    elif ((einkommen > 10000) and (einkommen <= 30000)):
        steuern_einkommen = einkommen*0.55
        print(steuern_einkommen)
    elif ((einkommen > 30000) and (einkommen <= 70000)):
        steuern_einkommen = einkommen*0.75
    else:
        steuern_einkommen = einkommen*0.82
    print(vermoegen)
    if (vermoegen <= 100000):
        steuern_vermoegen = vermoegen*0.05
    elif ((vermoegen > 100000) and (vermoegen <= 500000)):
        steuern_einkommen = vermoegen*0.08
    elif ((vermoegen > 500000) and (vermoegen <= 1000000)):
        steuern_vermoegen = vermoegen*0.13
    else:
        steuern_vermoegen = vermoegen*0.21

    steuern = steuern_einkommen + steuern_vermoegen

    print(f"Der Steuerzahler {vorname} {nachname} muss für das laufende Jahr {steuern} Dublonen dem Steueramt bezahlen.")

if __name__ == '__main__':
    main()
