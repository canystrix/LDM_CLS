# *** LEVEL 1 - SCHLEIFEN (LOOPS) *** #
# Hier lernen wir, wie wir mit Schleifen über Datenstrukturen iterieren können.
# Schleifen ermöglichen es uns, wiederkehrende Aufgaben effizient zu automatisieren!

sample_string = "The Liebherr Group has a decentralized organizational structure and comprises eleven product divisions."
# Ein String mit mehreren Wörtern, über den wir iterieren werden

sample_list = ['The', 'Liebherr', 'Group', 'has', 'a', 'decentralized', 'organizational', 'structure', 'and', 'comprises', 'eleven', 'product', 'divisions.']
# Eine Liste mit einzelnen Wörtern als Elemente

sample_dict = {"The": 1, "Liebherr": 2, "Group": 3}
# Ein Dictionary mit Wörtern als Keys und Zahlen als Values


# AUFGABE 1
# Verwenden wir eine while-Schleife, um über sample_string und sample_list zu iterieren und jedes Element auszugeben!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

# While-Schleifen mit sample_string:
max_index = len(sample_string)
# len() gibt uns die Gesamtzahl der Zeichen im String zurück
# Diese Zahl speichern wir als maximalen Index

current_index = 0
# Wir starten bei Index 0 (das erste Zeichen)

while current_index < max_index:
    # while leitet eine Schleife ein, die läuft, solange die Bedingung True ist
    # Die Bedingung: current_index < max_index bedeutet "solange der aktuelle Index kleiner als der maximale Index ist"
    # Das ist unsere "Ausstiegsbedingung" - ohne sie würde die Schleife endlos laufen!

    print(sample_string[current_index])
    # Wir greifen mit [current_index] auf das Zeichen an dieser Position zu und geben es aus

    current_index += 1
    # Wichtig! Wir erhöhen den Index um 1, damit wir beim nächsten Durchlauf das nächste Zeichen bekommen
    # += 1 ist eine Kurzform für: current_index = current_index + 1
    # Ohne diese Zeile würde die Schleife endlos laufen, weil die Bedingung nie False wird!

# While-Schleifen mit sample_list:
max_index = len(sample_list)
# len() gibt uns jetzt die Anzahl der Elemente in der Liste zurück

current_index = 0
# Wieder starten wir bei Index 0

while current_index < max_index:
    # Gleiche Logik wie oben: Schleife läuft, solange current_index kleiner als max_index ist

    print(sample_list[current_index])
    # Wir greifen auf das Listenelement an dieser Position zu

    current_index += 1
    # Wieder erhöhen wir den Index, um zum nächsten Element zu gelangen


# AUFGABE 2
# Verwenden wir eine for-Schleife, um über sample_string und sample_list zu iterieren und jedes Element auszugeben!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

# For-Schleifen mit sample_string:
for element in sample_string:
    # for ist viel einfacher als while!
    # Die for-Schleife iteriert automatisch über alle Elemente in einem iterierbaren Objekt (String, Liste, etc.)
    # Wir brauchen keine Ausstiegsbedingung und keinen Index - Python macht das für uns!
    # In jedem Durchlauf wird das aktuelle Zeichen in der Variable 'element' gespeichert

    print(element)
    # Wir geben einfach das aktuelle Element aus - keine komplizierte Index-Logik nötig!

# For-Schleifen mit sample_list:
for element in sample_list:
    # Gleiche Syntax wie oben - for-Schleifen funktionieren für Strings, Listen und viele andere Datentypen
    # In jedem Durchlauf enthält 'element' das nächste Wort aus der Liste

    print(element)
    # Ausgabe des aktuellen Listenelements


# AUFGABE 3
# Verwenden wir eine for-Schleife, um über das Dictionary zu iterieren und jeden Key und den dazugehörigen Value gleichzeitig auszugeben!
# TIPP: Wir brauchen dafür die Dictionary-Methode .items()!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

for key, value in sample_dict.items():
    # .items() gibt uns Key-Value-Paare zurück
    # In jeder Iteration bekommen wir zwei Werte gleichzeitig: den Key und den Value
    # Diese beiden Werte werden automatisch in die Variablen 'key' und 'value' entpackt
    # Das nennt man "Tuple Unpacking" - wir packen ein Paar von Werten in separate Variablen aus

    print(key)
    # Ausgabe des Keys (z.B. "The", "Liebherr", "Group")

    print(value)
    # Ausgabe des zugehörigen Values (z.B. 1, 2, 3)

