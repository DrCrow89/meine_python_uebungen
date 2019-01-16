def steuer(uebergabe_gehalt):
    if uebergabe_gehalt > 2500:
        ergebnis = uebergabe_gehalt*0.22
    else:
        ergebnis = uebergabe_gehalt*0.18
    return uebergabe_gehalt

# Ausgabe
print "Es ergibt sich ein Steuerbetrag von", steuer(1800), "Euro"
print "Es ergibt sich ein Steuerbetrag von", steuer(2200), "Euro"
print "Es ergibt sich ein Steuerbetrag von", steuer(2500), "Euro"
print "Es ergibt sich ein Steuerbetrag von", steuer(2900), "Euro"
