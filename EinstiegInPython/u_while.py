eingabe = 99
while eingabe != 0:
    # Eingaben
    print("Bitte geben Sie den Inch-Wert ein:")
    eingabe = input()

    # Berechnung
    # 1-Inch sind 2.54cm
    inch_wert = float(eingabe)
    ergebnis = inch_wert*2.54

    # Ausgabe
    print inch_wert, "Inch sind", ergebnis, "cm" 
