# *** LEVEL 1 - CONDITIONALS (BEDINGUNGEN) *** #
# Hier arbeiten wir mit if-Bedingungen, um den Ablauf unseres Programms zu steuern.
# Conditionals ermöglichen es uns, unterschiedliche Aktionen basierend auf bestimmten Bedingungen auszuführen!

sample_list = ["Deutsche", "Post", "DHL", "Group", "is", "the", "world's", "leading", "logistic", "company"]
# Eine Liste mit verschiedenen Wörtern, die wir untersuchen werden

max_length = 10
# Die maximale Länge, die wir als Vergleichswert nutzen

min_length = 5
# Die minimale Länge, die wir als Vergleichswert nutzen


# AUFGABE 1
# Überprüfen wir für jedes Element in sample_list, ob die Länge des Elements größer als max_length ist.
# Wenn ja, geben wir eine Bestätigungsnachricht aus.

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

for element in sample_list:
    # Die for-Schleife iteriert über jedes Element in der Liste
    # In jedem Durchlauf wird das aktuelle Element in der Variable 'element' gespeichert

    if len(element) > max_length:
        # if leitet eine Bedingung ein - der Code darunter wird nur ausgeführt, wenn die Bedingung True ist
        # len(element) gibt uns die Anzahl der Zeichen im String zurück
        # Der Vergleichsoperator > prüft, ob die Länge größer als max_length ist

        print(f"{element} is longer than {max_length}!")
        # f-String: {element} wird durch den tatsächlichen Wert der Variable ersetzt
        # Diese Zeile wird nur ausgeführt, wenn die if-Bedingung wahr ist


# AUFGABE 2
# Überprüfen wir für jedes Element in sample_list, ob die Länge des Elements größer als max_length ist.
# Wenn ja, geben wir eine Bestätigungsnachricht aus.
# Wenn nein, geben wir eine Fehlermeldung aus.
# Wir können den Code aus Aufgabe 1 erweitern!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

for element in sample_list:
    # Wieder iterieren wir über jedes Element in der Liste

    if len(element) > max_length:
        # Erste Bedingung: Ist das Element länger als max_length?

        print(f"{element} is longer than {max_length}!")
        # Ausgabe, wenn die Bedingung True ist

    else:
        # else fängt alle Fälle ab, die nicht durch if abgedeckt wurden
        # Der Code im else-Block wird ausgeführt, wenn die if-Bedingung False ist

        print(f"{element} is not longer than {max_length}!")
        # Ausgabe für alle Elemente, die NICHT länger als max_length sind


# AUFGABE 3
# Überprüfen wir für jedes Element in sample_list, ob die Länge des Elements größer als max_length ist.
# Wenn ja, geben wir eine Bestätigungsnachricht aus.
# Schreiben wir außerdem eine elif-Anweisung, die prüft, ob die Länge des Elements kleiner als min_length ist.
# Wenn ja, geben wir eine andere Bestätigungsnachricht aus.
# Wenn keine der obigen Bedingungen zutrifft, geben wir eine Fehlermeldung aus.
# Wir können den Code aus Aufgabe 2 erweitern!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

for element in sample_list:
    # Wieder iterieren wir über jedes Element in der Liste

    if len(element) > max_length:
        # Erste Bedingung: Ist das Element länger als max_length?

        print(f"{element} is longer than {max_length}!")
        # Ausgabe für sehr lange Wörter

    elif len(element) < min_length:
        # elif (else if) ist eine zusätzliche Bedingung, die nur geprüft wird, wenn die if-Bedingung False war
        # Hier prüfen wir: Ist das Element kürzer als min_length?
        # Der Vergleichsoperator < bedeutet "kleiner als"

        print(f"{element} is shorter than {min_length}!")
        # Ausgabe für sehr kurze Wörter

    else:
        # else fängt alle übrigen Fälle ab
        # Dieser Block wird ausgeführt, wenn das Element weder länger als max_length noch kürzer als min_length ist

        print(f"{element} is between {min_length} and {max_length}!")
        # Ausgabe für Wörter, die in der mittleren Länge liegen
