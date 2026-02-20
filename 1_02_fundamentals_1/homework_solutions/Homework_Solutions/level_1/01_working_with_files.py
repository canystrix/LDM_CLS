# *** LEVEL 1 - ARBEITEN MIT DATEIEN *** #
# Hier findest du mehrere Aufgaben zum Lesen von Inhalten aus einfachen Textdateien.
# Vergiss nicht, die Dateien nach dem Lesen zu schließen!

# AUFGABE 1
# In diesem Verzeichnis befinden sich zwei TXT-Beispieldateien.
# Lesen wir den Inhalt von sample1.txt als String und speichern ihn in einer Variable
# Geben wir dann den Inhalt dieser neuen Variable aus!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

# Schritt 1: Öffnen der Datei sample1.txt
file = open('./sample1.txt')
# Die open()-Funktion gibt uns ein File-Objekt zurück, das wir in der Variable 'file' speichern
# './' bedeutet "im aktuellen Verzeichnis" - das ist ein relativer Pfad
# Achtung: Unter Windows müssen Pfade stattdessen so aussehen: file = open('.\\sample1.txt')
# Das liegt daran, dass Linux-basierte Betriebssysteme und Windows unterschiedliche Pfadtrennzeichen verwenden!
# In Python-Strings müssen wir außerdem alle \ maskieren, wenn wir sie anzeigen wollen, oder wir verwenden einen
# Raw-String. Tatsächlich könnten wir in diesem Fall './' weglassen und einfach open('sample1.txt') schreiben,
# da unser Skript sich im gleichen Ordner wie die Datei sample1.txt befindet. So wie es jetzt geschrieben ist,
# wird nur deutlich, dass wir einen relativen Pfad verwenden!

# Schritt 2: Lesen des gesamten Dateiinhalts
sample_text = file.read()
# Die .read()-Methode liest den kompletten Inhalt der Datei als einen einzigen String
# Dieser String wird in der Variable sample_text gespeichert

# Schritt 3: Schließen der Datei
file.close()
# Sehr wichtig! file.close() gibt die Datei-Ressource wieder frei
# Vergessen wir nie, unsere Datei zu schließen, wenn wir fertig sind! Mit "with" müssen wir uns darum nicht kümmern

# Schritt 4: Ausgabe des Inhalts
print(sample_text)
# print() zeigt uns den gelesenen Text in der Konsole an


# AUFGABE 2
# Lesen wir den Inhalt von sample1.txt als Liste von Zeilen und speichern ihn in einer Variable
# Geben wir dann den Inhalt dieser neuen Variable aus!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

# Schritt 1: Öffnen der Datei sample1.txt (wie in Aufgabe 1)
file = open('./sample1.txt')

# Schritt 2: Lesen des Dateiinhalts als Liste
sample_text = file.readlines()
# Die .readlines()-Methode gibt uns eine Liste zurück, in der jede Zeile ein Element ist
# Jedes Element behält das Zeilenumbruchzeichen (\n) am Ende
# Das ist nützlich, wenn wir mit einzelnen Zeilen arbeiten wollen

# Schritt 3: Schließen der Datei
file.close()
# Wieder sehr wichtig - wir geben die Ressource frei!

# Schritt 4: Ausgabe der Liste
print(sample_text)
# print() zeigt uns die Liste mit allen Zeilen an
# Wir sehen eckige Klammern [ ] und Anführungszeichen, weil es eine Liste von Strings ist


# AUFGABE 3
# Lesen wir den Inhalt von sample1.txt und sample2.txt als Strings.
# Kombinieren wir die Strings und speichern sie in einer neuen Datei namens sample_combined.txt!
# TIPP: Wir können String-Formatierung verwenden, um die Strings zu kombinieren!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

# Schritt 1: Lesen der ersten Datei
file = open('./sample1.txt')
# Wir öffnen sample1.txt und speichern das File-Objekt

sample_text = file.read()
# Wir lesen den kompletten Inhalt als String

file.close()
# Wir schließen die erste Datei - wichtig, bevor wir die nächste öffnen!

# Schritt 2: Lesen der zweiten Datei und Kombinieren
file = open('./sample2.txt')
# Wir öffnen jetzt sample2.txt

sample_text = f'{sample_text}\n{file.read()}'
# Hier kombinieren wir beide Texte mit einem f-String (formatierter String)
# {sample_text} fügt den Text aus der ersten Datei ein
# \n ist ein Zeilenumbruchzeichen - damit die Absätze nicht direkt aneinander kleben
# {file.read()} liest und fügt den Inhalt der zweiten Datei direkt ein
# Das Ergebnis überschreibt die Variable sample_text mit dem kombinierten Text

file.close()
# Wir schließen die zweite Datei

# Schritt 3: Schreiben in eine neue Datei
file = open('./sample_combined.txt', 'w')
# Um in eine Datei zu schreiben, müssen wir daran denken, sie im Schreibmodus zu öffnen!
# Das zweite Argument 'w' (write) sagt Python: "Öffne diese Datei zum Schreiben"
# Wichtig: Wenn die Datei schon existiert, wird sie überschrieben! Für Anhängen nutzen wir 'a' (append)

file.write(sample_text)
# Die .write()-Methode schreibt unseren kombinierten Text in die Datei
# Anders als print() fügt write() kein Zeilenumbruchzeichen am Ende hinzu

file.close()
# Wir schließen die Datei - besonders wichtig beim Schreiben!
# Erst beim Schließen wird alles wirklich auf die Festplatte geschrieben
