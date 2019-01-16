# Kapitel 3
## Übung 1
**Dateiname:** u_eingabe_inch.py  
**Aufgabenstellung:**  
Schreiben Sie ein Programm zur Eingabe und Umrechnung von beliebigen Inch-Werten in Zentimeter.  
**Test**  
Bitte geben Sie den Inch-Wert ein:  
3.5  
3.5 Inch sind 8.89cm  

## Übung 2
**Dateiname:** u_eingabe_gehalt.py  
**Aufgabenstellung:**  
Schreiben Sie ein Programm zur Berechnung des monatlich zu zahlenden Steuerbetrags. Der Anwender wird dazu aufgefordert, sein monatliches Bruttogehalt einzugeben. Anschließend werden 18% dieses Betrags berechnet und ausgegeben.  
**Test**  
Geben Sie Ihr Bruttogehalt in Euro ein:  
2500  
Es ergibt sich ein Steuerbetrag von 450.0 Euro  

## Übung 3
**Dateiname:** u_verzweigung_einfach.py  
**Aufgabenstellung:**  
Das Programm zur Berechnung des Steuerbetrags wird verändert. Der Anwender soll dazu aufgefordet werden, sein monatliches Bruttogehalt einzugeben. Liegt das Gehalt über 2.500€, sind 22% Steuern zu zahlen, ansonsten 18%.  
**Test 1**  
Geben Sie Ihr Bruttogehalt in Euro ein:  
3000  
Es ergibt sich ein Steuerbetrag von 660.0 Euro  
**Test 2**  
Geben Sie Ihr Bruttogehalt in Euro ein:  
2000  
Es ergibt sich ein Steuerbetrag von 360.0 Euro  

## Übung 4
**Dateiname:** u_verzweigung_mehrfach.py  
**Aufgabenstellung:**  
Das Programm zur Berechnung des Steuerbetrags soll weiter verändert werden. Der Anwender soll dazu aufgefordet werden, sein monatliches Bruttogehalt einzugeben. Anschließend wird sein Steuerbetrag nach folgender Tabelle berechnet:  
| Gehalt | Steuersatz |
|---|---|
| mehr als 4.000 € | 26% |
| 2.500 bis 4.000€ | 22% |
| weniger als 2.500€ | 18% |

## Übung 5
**Dateiname:** u_operator.py  
**Aufgabenstellung:**  
Das Programm zur Berechnung des Steuerbetrags soll weiter verändert werden. Der Anwender soll dazu aufgefordet werden, sein monatliches Bruttogehalt und Familienstand einzugeben. Anschließend wird sein Steuerbetrag nach folgender Tabelle berechnet:  
| Gehalt | Familienstand | Steuersatz |
|---|---|---|
| > 4.000 € | ledig | 26% |
| > 4.000 € | verheiratet | 22% |
| <= 4.000 € | ledig | 22% |
| <= 4.000 € | verheiratet | 18% |

## Übung 6
**Dateiname:** -   
**Aufgabenstellung:**  
Ermitteln Sie durch Überlegen die Ausgaben des folgenden Programms:  
print("Schleife 1")  
for i in 2,3,6.5,-7:  
  print(i)

print("Schleife 2")  
for i in range(3,11,3):  
  print(i)  

print("Schleife 3")  
for i in range(-3,14,4):  
  print(i)  

print("Schleife 4")  
for i in range(3,-11,-3):  
  print(i)  

**Lösung:**  
print("Schleife 1")  
2  
3  
6.5  
-7  

print("Schleife 2")  
3  
6  
9  

print("Schleife 3")  
-3  
1  
5  
9  
13  

print("Schleife 4")  
3  
0  
-3  
-6  
-9  

## Übung 7
**Dateiname:** u_range_inch.py  
**Aufgabenstellung:**  
Schreiben Sie ein Programm, das die folgenden Ausgaben erzeugt:  
15 Inch = 38.1 cm  
20 Inch = 50.8 cm  
25 Inch = 63.5 cm  
30 Inch = 76.2 cm  
35 Inch = 88.9 cm  
40 Inch = 101.6 cm  

## Übung 8
**Dateiname:** u_while.py  
**Aufgabenstellung:**  
Schreiben Sie ein Programm, das den Anwender wiederholt dazu auffordert, einen Wert in Inch einzugeben. Der eingegebene Wert soll anschließend in Zentimeter Umgerechnet und ausgegeben werden. Das Programm soll nach Eingabe des Werts 0 beendet werden.  

## Übung 9
**Dateiname:** u_feher.py  
**Aufgabenstellung:**  
Verbessern Sie das Programm zu Eingabe und Umrechnung eines beliebigen Inch-Werts in Zentimeter. Eingabefehler des Anwenders sollen abgefangen werden. Das Programm soll den Anwender so lange zur Eingabe auffordern, bis sie erfolgreich war.  
