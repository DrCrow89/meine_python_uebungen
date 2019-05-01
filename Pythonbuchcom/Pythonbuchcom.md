# Quelle
Die Aufgabenstellungen habe ich von: https://pythonbuch.com/aufgabensammlung.html  
# Kapitel 1
## Übung 1
**Dateiname:** pbc_a01_01.py  
**Aufgabenstellung:**  
Erstelle ein Programm, das deinen Vorname, Nachname und dein Geburtsdatum auf der Konsole ausgibt.  
## Übung 2
**Dateiname:** pbc_a01_02.py  
**Aufgabenstellung:**  
Schreibe ein Programm, das zu einem gegebenen Winkel im Bogenmass (Eingabe in der Konsole durch den Benutzer), den entsprechenden Winkel im Gradmass berechnet. Die Ausgabe soll mit Grad (°), Bogenminuten (‚) und Bogensekunden („) ausgegeben werden.  
**Test:**  
Eingabe: 0.8942107145912499rad  
Ausgabe: 51° 14' 4.2''  
## Übung 2z
**Dateiname:** pbc_a01_02z.py  
**Aufgabenstellung:**  
Schreibe ein Programm, welches die Umrechnung vom Gradmass ins Bogenmass übernimmt.  
**Test:**  
Eingabe: 51.2345°  
Ausgabe: 0.89rad  
## Übung 3
**Dateiname:** pbc_a01_03.py  
**Aufgabenstellung:**  
Schreibe ein Programm, das Temperaturen in verschiedene Skalensystemen ineinander umwandelt. Das Programm soll zu Beginn eine Auswahl mit den verschiedenen Möglichkeiten anbieten:  
(1) Umrechnung von Celsius nach Kelvin  
(2) Umrechnung von Celsius nach Fahrenheit  
(3) Umrechnung von Kelvin nach Celsius  
(4) Umrechnung von Kelvin nach Fahrenheit  
(5) Umrechnung von Fahrenheit nach Celsius  
(6) Umrechnung von Fahrenheit nach Kelvin  
## Übung 3z
**Dateiname:** pbc_a01_03z.py  
**Aufgabenstellung:**  
Passe deine Lösung aus der Aufgabe Winkelmass Umwandler so an, dass beide Umrechnungen (Bogen- nach Gradmass und umgekehrt) in einem einzelnen Programm möglich sind.  
## Übung 4
**Dateiname:** pbc_a01_04.py  
**Aufgabenstellung:**  
Erweitere deine Lösung der vorherigen Aufgabe, indem du für die Umrechnung 6 verschiedene Funktionen definierst. Passe ausserdem dein Programm so an, dass der Benutzer mehrere Temperaturen nacheinander umrechnen kann und den Zeitpunkt zum Beenden des Programms selber bestimmt.  
## Übung 4z
**Dateiname:** pbc_a01_04z.py  
**Aufgabenstellung:**  
Erweitere die Lösung der vorherigen Zusatzaufgabe (Winkelmass Umwandler), indem du Funktionen implementierst.  
## Übung 5
**Dateiname:** pbc_a01_05.py  
**Aufgabenstellung:**  
Versuche deine Lösungen von den vorherigen Aufgaben mit einer graphische Benutzeroberfläche zu erweitern. Das Fenster soll folgende Elemente enthalten:  
* ein OptionMenu Widget für die Wahl der Umrechnung (Celsius nach Kelvin, …).
* ein Entry Widget, für die Eingabe der Temperatur.
* ein Label Widget, für die Ausgabe.
* ein Button Widget, der die Umrechnung startet.
## Übung 5z
**Dateiname:** pbc_a01_05z.py  
**Aufgabenstellung:**  
Erstelle auch für den Winkelmass Umwandler ein GUI.  
## Übung 6
**Dateiname:** pbc_a01_06.py  
**Aufgabenstellung:**  
Schreibe ein Programm, welches eine Liste bestehend aus ganzen Zahlen aufsteigend sortiert. Der Benutzer soll per Eingabe entscheiden, welche Elemente in die Liste kommen und er soll so viele Elementen eingeben können, wie er will. Wenn er mit der Eingabe fertig ist, soll er mit einem Befehl (zum Beispiel q) die Eingabe beenden.  
## Übung 6z
**Dateiname:** pbc_a01_06z.py  
**Aufgabenstellung:**  
Schreibe ein anderes Programm, welches eine Liste aus Zeichenketten alphabetisch sortiert.  
## Übung 7
**Dateiname:** pbc_a01_07.py  
**Aufgabenstellung:**  
Professor Ungerechtmann der Kantonsschule Unfairdorf braucht ein Programm für die Notenvergabe der Abschlussprüfung. Die Abschlussnote hängt von den folgenden Parametern ab:  
* Prüfungsnote (von 1 bis 6 mit Halbpunkten);
* Augenfarbe (z.B. dunkel=1, hell=0);
* Frisur (z.B. kurze Haare=1, lange Haare=0);
* Wetter (z.B. schön=1, nicht schön=0).
Es gilt folgendes:  
* Hat der Prüfling dunkle Augen und…
  * kurze Haare, so wird die Abschlussnote um 10% erhöht (d.h. Abschlussnote = Prüfungsnote + 10% Prüfungsnote).
  * lange Haare, so wird die Abschlussnote um 10% reduziert.
* Hat der Prüfling helle Augen und…
  * kurze Haare, so wird die Abschlussnote um 10% reduziert.
  * lange Haare, so wird die Abschlussnote um 10% erhöht.
* Ist das Wetter schön, so wird die Abschlussnote um eine Einheit reduziert.
* Die Abschlussnoten müssen auf halbe Noten gerundet werden.
## Übung 7z
**Dateiname:** pbc_a01_07z.py  
**Aufgabenstellung:**  
Erfinde und implementiere einige neue Bedingungen, von denen die Abschlussnote abhängt.  
## Übung 8
**Dateiname:** pbc_a01_08.py  
**Aufgabenstellung:**  
Der Steueramtchef von Flächenland stellt dich an, um ein einfaches Programm in Python zu schreiben. Dieses Programm soll den Steuersatz jedes Steuerzahlers berechnen. Die Eingabeparameter sind:  
* Vorname und Nachname des Steuerzahlers
* Einkommen (in Dublonen, die Währung von Flächenland)
## Übung 8z
**Dateiname:** pbc_a01_08z.py  
**Aufgabenstellung:**  
Berücksichtige in deinem Programm neben dem Einkommen auch das Vermögen.  

# Kapitel 2
## Übung 1
Erstelle ein Programm, das die Summe aller natürliche Zahlen n≤10000 mit 7∣n und 5∤n berechnet.  
## Übung 1z
List comprehension ist ein syntaktisches Konstrukt, um Listen zu erzeugen. Versuche nachher mit diesem Konstrukt ein äquivalentes Programm zu schreiben.  
## Übung 2
Erstelle ein Programm zur Lösung von quadratische Gleichungen:
```
ax^2+bx+c = 0
```
Die reellen Koeffizienten a,b,c werden vom Benutzer eingegeben.
## Übung 2z
Sei eine quadratische Funktion f(x)=ax2+bx+c durch ihre Koeffizienten a, b, c und eine lineare Funktion g(x)=mx+q durch m und q gegeben. Erstelle ein Programm, das die Schnittpunkte der Graphen von f und g berechnet.
## Übung 3
Sei n∈N. Es gelten folgende Regeln:  
Falls 3∣n, dann soll n um 4 erhöht werden.  
Falls 3∤n aber 4∣n, dann soll n halbiert werden.  
Falls 3∤n und 4∤n, dann soll n um 1 verkleinert werden.  
Diese Regeln sollen nun sukzessive angewendet werden bis n=0 ist. Schreibe ein Programm, welches zu zwei gegebenen natürliche Zahlen a und b mit a < b, auf der Konsole die Anzahl benötigte Schritte für jedes n (a≤n≤b) ausgibt.  
## Übung 3z
Das Collatz-Problem ist ein ungelöstes mathematisches Problem. Es handelt sich dabei um eine Zahlenfolge, die im Zyklus 4-2-1 mündet, unabhängig davon, welche Startzahl n gewählt wird. Schaue dir zuerst an, wie die Folge definiert ist und erstelle dann ein Programm, welches bei einer gegeben Startzahl die Anzahl benötigte Schritte für die Erreichung des Zyklus 4-2-1 ausgibt.  
## Übung 4
Schreibe ein Programm, welches alle PPDIs mit drei Ziffern bestimmt.  
## Übung 5
Sei n>0 eine ganze Zahl, die durch 3 teilbar ist (zum Beispiel 86145). Die Summe der dritten Potenzen der Ziffern ist wieder eine Zahl, die durch 3 teilbar ist: 83+63+13+43+53=918.  
Von dieser neuen Zahl kann man nochmals die Summe der dritten Potenzen der Ziffern berechnen und diese ist wieder durch 3 teilbar (93+13+83=1242), usw. Man kann beweisen, dass dieser Vorgang irgendwann zur 153 gelangt und bei dieser Zahl auch bleibt. Man bemerke, dass 153 eine PPDI ist (13+53+33=153).  
Erstelle ein Programm, das diese Tatsache verifiziert. Im Programm musst du eine Funktion quersumme_dritter_potenzen() definieren. Diese Funktion nimmt als Argument eine ganze Zahl und gibt als Rückgabewert die Summe der dritten Potenzen der Ziffern dieser Zahl.  
## Übung 6
Das Sieb des Eratosthenes ist ein Algorithmus zur Bestimmung einer Liste oder Tabelle aller Primzahlen kleiner oder gleich einer vorgegebenen Zahl.  
Schreibe ein Programm, das bei einer gegebenen natürliche Zahl N≥2, die Liste aller Primzahlen kleiner oder gleich N erzeugt.  
Das Programm soll folgende Struktur haben:  
Eine Funktion sieb() mit N als Eingabeparameter und welche die Liste der Primzahlen kleiner oder gleich N zurückgibt. Eine Funktion main(), in der der Benutzer zur Eingabe aufgefordert wird und die Funktion sieb() aufruft. Der Aufruf der main()-Funktion.  
Als Test für dein Programm benutze folgende Tatsache: Es gibt 78’498 Primzahlen, welche kleiner als 1’000’000 sind.  
## Übung 7
Passe deine Lösung aus der Aufgabe 6 (Sieb des Eratosthenes) so an, dass das Programm neben der Liste der Primzahlen, auch die von der Funktion sieb() benötigte Zeit ausgibt.  
## Übung 8
Mit Hilfe des Siebs des Eratosthenes sollst du nun ein Programm erstellen, weches die Primfaktorzerlegung einer natürliche Zahl berechnet.  
## Übung 8z
Mit Hilfe der bisherigen Programme, welche du geschrieben hast, erstelle nun ein weiteres Programm, welches zu einer gegebenen Zahl n, alle vollkommenen Zahlen kleiner oder gleich n findet.  
