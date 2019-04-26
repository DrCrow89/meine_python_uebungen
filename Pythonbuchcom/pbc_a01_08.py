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

    if (einkommen <= 10000):
        steuern = einkommen*0.4
    elif ((einkommen > 10000) and (einkommen <= 30000)):
        steuern = einkommen*0.55
    elif ((einkommen > 30000) and (einkommen <= 70000)):
        steuern = einkommen*0.75
    else:
        steuern = einkommen*0.82

    print(f"Der Steuerzahler {vorname} {nachname} muss für das laufende Jahr {steuern} Dublonen dem Steueramt bezahlen.")

if __name__ == '__main__':
    main()
