def steuer(uebergabe_gehalt):
    if uebergabe_gehalt > 2500:
        ergebnis = uebergabe_gehalt*0.22
    else:
        ergebnis = uebergabe_gehalt*0.18
    return uebergabe_gehalt
