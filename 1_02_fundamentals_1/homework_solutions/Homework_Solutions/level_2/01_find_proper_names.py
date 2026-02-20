# *** LEVEL 2 - EIGENNAMEN FINDEN *** #
# Hier lernen wir, wie wir Eigennamen (Proper Names) in einem Text identifizieren können.
# Eigennamen beginnen in der Regel mit einem Großbuchstaben!

# In diesem Verzeichnis befindet sich eine TXT-Beispieldatei
# Lesen wir den Inhalt von sample.txt als String oder Liste von Absätzen
# Iterieren wir dann über jedes Wort in der Datei
# Überprüfen wir für jedes Wort, ob es mit einem Großbuchstaben beginnt. Wenn ja,
# fügen wir es zu name_set hinzu
# TIPP: Es gibt eine String-Methode, um zu prüfen, ob ein Wort großgeschrieben ist!
# Speichern wir den Inhalt von name_set in einer neuen Datei!
# Jedes Element in name_set sollte in der finalen Datei in einer eigenen Zeile
# angezeigt werden

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

name_set = set()
# Ein Set ist eine Datenstruktur, die nur eindeutige Elemente speichert
# (keine Duplikate!)
# Perfekt für unsere Aufgabe, da manche Eigennamen mehrmals im Text vorkommen könnten

file = open('./sample.txt')
# Wir öffnen die Datei sample.txt im Lesemodus (Standard)

text = file.read()
# Wir lesen den gesamten Inhalt der Datei als einen einzigen String

file.close()
# Wichtig: Wir schließen die Datei wieder

words = text.split()
# Die .split()-Methode teilt den String an jedem Leerzeichen
# Das Ergebnis ist eine Liste mit einzelnen Wörtern
# z.B. "Hello World" wird zu ["Hello", "World"]

# Wir können diese Aufgabe mit der String-Methode "isupper()" lösen
# Achtung: Die Methode selbst prüft, ob der gesamte String großgeschrieben ist,
# deshalb müssen wir nur das erste Zeichen überprüfen
# Es gibt auch andere Wege, dies zu tun, die einen komplexeren und low-level
# Prozess erfordern. Wir könnten zum Beispiel das erste Zeichen jedes Wortes
# extrahieren und in seine numerische Darstellung umwandeln. Dann könnten wir,
# abhängig von der Kodierung, prüfen, ob es im richtigen Zahlenbereich liegt
# (65 bis 90 für ASCII)
for word in words:
    # Wir iterieren über jedes Wort in der Liste

    if word[0].isupper():
        # word[0] greift auf das erste Zeichen des Wortes zu (Index 0)
        # .isupper() prüft, ob dieses Zeichen ein Großbuchstabe ist
        # Gibt True zurück, wenn es ein Großbuchstabe ist, sonst False

        name_set.add(word)
        # Die .add()-Methode fügt das Wort zum Set hinzu
        # Wenn das Wort bereits im Set ist, wird es NICHT doppelt hinzugefügt
        # (Set-Eigenschaft!)

print(name_set)
# Ausgabe des Sets mit allen gefundenen Eigennamen zur Überprüfung

# Jetzt speichern wir die Eigennamen in einer neuen Datei
file = open('./proper_names.txt', 'w')
# Wir öffnen eine neue Datei im Schreibmodus ('w')
# Wenn die Datei nicht existiert, wird sie erstellt
# Wenn sie existiert, wird sie überschrieben!

for name in name_set:
    # Wir iterieren über jedes Element im Set

    file.write(name + '\n')
    # Wir schreiben den Namen in die Datei
    # '\n' ist ein Zeilenumbruchzeichen - damit jeder Name in einer neuen Zeile steht
    # Wichtig: .write() fügt KEINE automatischen Zeilenumbrüche hinzu
    # (anders als print())

file.close()
# Wir schließen die Datei - sehr wichtig beim Schreiben, damit alles gespeichert wird!

