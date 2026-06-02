# Aufgabe: Power-Curve II     

Für diese Aufgabe sollen die in einem CSV-Datensatz (activity.csv) gespeicherten Leistungsdaten einer sportlichen Aktivität als Leistungskurve/Powercurve dargestellt werden.     
Der hier beschriebene Code befindet sich in *advanced_powercurve.py*

### Umsetzungsschritte

- read_data: 
    - eine Funktion, die eine CSV-Datei im angebegenen Dateipfad auslesen kann und ein Pandas Dataframe der Daten zurückgibt
    - Eingabeparameter: relativer Pfad zur CSV-Datei
    - Ausgabeparameter: Dataframe
- add_time:
    - Funktion, die eine Zeitachse hinzufügt über die Länge des Dataframes. Hier: eine Zeile (== ein Index) pro Sekunde
    - Eingabeparameter: Dataframe aus read_data
    - Ausgabe: modifizierter Dataframe
- find_best_effort:
    - Funktion, die den Dataframe in einem beliebig großen Intervall (rolling window) durchgeht, für jedes einzelne Window den Mittelwert bestimmt und den größten Wert dieser Mittelwerte für die gewählte Intervallgröße zurückgibt. Die "resolution" bietet die Möglichkeit, Daten zu verarbeiten, die mehr oder weniger als einen Datensatz pro Sekunde erfassen. Da im getesteten "activity.csv" neue Daten einmal pro Sekunde erhoben wurden, ist die "resolution" standardmäßig auf 1 gesetzt.
    - Eingabe: mod. Dataframe, window_size, resolution
    - Ausgabe: größerter Mittelwert als float
- create_pc_df:
    - Diese Funktion erstellt einen neuen Dataframe mit den Spalten "Intervalls" und "Max. avg. Power" um daraus die Leistungskurve zu plotten. In dieser Funktion wird die Funktion find_best_effort in einer for-Schleife aufgerufen, die für die gewählten Windows eine Liste mit der max. Leistung im jeweiligen Window erstellt.
    - Eingabe: mod. Dataframe, window_list
    - Ausgabe: Powercurve Dataframe
- plot_pc:
    - Funktion, um den in create_pc_df erstellten Dataframe zu plotten
    - Eingabe: Powercurve Dataframe
    - Ausgabe: fig (Plot)     
-----
#### Extras
- create_windows:
    - Eine Funktion, eine Liste (window_list) mit Fenstergrößen(window_sizes) von 1 bis über die ganze Länge des mod. Dataframes erstellt.
    - Eingabe: mod. Dataframe
    - Ausgabe: Liste mit allen möglichen window_sizes
-----
### Beispielhafter Plot (activity.csv) mit allen möglichen "window_sizes"

![Hier sollte jetzt ein Plot sein!](/data/activities/newplot.png)
