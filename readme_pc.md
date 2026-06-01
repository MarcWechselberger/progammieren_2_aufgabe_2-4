# Aufgabe: Power-Curve II     

Für diese Aufgabe sollen die in einem CSV-Datensatz (activity.csv) gespeicherten Leistungsdaten einer sportlichen Aktivität als Leistungskurve/Powercurve dargestellt werden.

### Umsetzungsschritte

- read_data: 
    - eine Funktion, die die CSV-Datei auslesen kann und ein Pandas Dataframe der Daten zurückgibt
    - Eingabeparameter: relativer Pfad zur CSV-Datei
    - Ausgabeparameter: Dataframe
- add_time:
    - Funktion, die eine Zeitachse hinzufügt über die Länge des Dataframes. Bei einer Zeile pro Sekunde
    - Eingabeparameter:
    - Ausgabe: