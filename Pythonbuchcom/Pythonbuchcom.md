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
