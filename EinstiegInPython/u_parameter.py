def steuer(uebergabe_gehalt):
    if uebergabe_gehalt > 2500:
        ergebnis = uebergabe_gehalt*0.22
    else:
        ergebnis = uebergabe_gehalt*0.18
    # Ausgabe
    print "Es ergibt sich ein Steuerbetrag von", ergebnis, "Euro"

steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)
