fehler = 1
while fehler != 0:
    try:
        # Eingaben
        print "Bitte geben Sie den Inch-Wert ein:"
        eingabe = input()
        # Berechnung
        # 1-Inch sind 2.54cm
        inch_wert = float(eingabe)
        ergebnis = inch_wert*2.54
        fehler = 0
    except:
        print "Der eingegebene Wert war keine Zahl"
    # Ausgabe
print inch_wert, "Inch sind", ergebnis, "cm"
