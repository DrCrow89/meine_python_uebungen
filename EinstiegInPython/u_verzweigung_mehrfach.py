# Eingaben
print "Geben Sie Ihr Bruttogehalt in Euro ein:"
eingabe = input()

# Berechnung
gehalt_wert = float(eingabe)
if gehalt_wert > 4000:
    ergebnis = gehalt_wert*0.26
elif gehalt_wert >= 2500:
    ergebnis = gehalt_wert*0.22
else:
    ergebnis = gehalt_wert*0.18

# Ausgabe
print "Es ergibt sich ein Steuerbetrag von", ergebnis, "Euro"
