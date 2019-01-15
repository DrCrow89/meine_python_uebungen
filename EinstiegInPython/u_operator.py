# Eingaben
print "Geben Sie Ihr Bruttogehalt in Euro ein:"
roh_eingabe_gehalt = input()

print "Sind Sie ledig (1) oder verheiratet (2):"
roh_eingabe_familienstand = input()

# Berechnung
gehalt = float(roh_eingabe_gehalt)
familienstand = int(roh_eingabe_familienstand)

if gehalt > 4000 and familienstand == 1:
    ergebnis = gehalt*0.26
elif gehalt > 4000 and familienstand == 2:
    ergebnis = gehalt*0.22
elif gehalt <= 4000 and familienstand == 1:
    ergebnis = gehalt*0.22
elif gehalt <= 4000 and familienstand == 2:
    ergebnis = gehalt*0.18

# Ausgabe
print "Es ergibt sich ein Steuerbetrag von", ergebnis, "Euro"
