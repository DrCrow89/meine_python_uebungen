print(f"{'Inch':>7}{'cm':>7}") # Schreibe Inch rechtsbündig und lasse insgesamt Platz für 7 Zeichen
for i in range(15,45,5): # Starte mit dem Wert 15 für i und erhöhe Schrittweise um 5 bis 40
    print( f"{i:>7.2f}{i*2.54:>7.2f}") # Ausgabe von i, das Rechtsbündig ist, 7 Stellen insgesamt hat mit 2 Nachkommastellen
