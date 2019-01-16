def steuer(uebergabe_gehalt):
    if gehalt_wert > 2500:
        ergebnis = gehalt_wert*0.22
    else:
        ergebnis = gehalt_wert*0.18
    # Ausgabe
    print "Es ergibt sich ein Steuerbetrag von", ergebnis, "Euro"

fehler = 1
while fehler != 0:
    try:
        # Eingaben
        print "Geben Sie Ihr Bruttogehalt in Euro ein:"
        eingabe = input()
        # Berechnung
        gehalt_wert = float(eingabe)
        steuer(gehalt_wert)
        fehler = 0
    except:
        print "Der eingegebene Wert war keine Zahl"
