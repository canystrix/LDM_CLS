# *** PRIMITIVE DATENTYPEN - STRINGS *** #
# String ist der letzte der grundlegenden Datentypen in Python.
# außerdem ist es derjenige Datentyp, mit dem wir uns am meisten beschäftigen werden.
# Mit Strings können wir Zeichenfolgen ausdrücken, etwa die Folge von Buchstaben in natürlicher Sprache.

"""
# Definieren Sie eine neue Variable vom Dateityp String in sample_string!
sample_string =

sample_string_type = type(sample_string)

print(sample_string)
print(sample_string_type)
"""


# *** STRINGS ZUSAMMENFÜGEN *** #
# Wenn wir zwei String haben, können wir sie auch miteinander kombinieren!
# Dafür benötigen wir das Additionszeichen, das wir bereits aus der Arithmetik kennen.
# Jeweils ein String auf beiden Seiten des +-Zeichens kombiniert die beiden String miteinander.
# Diesen zusammengefügten String können wir ebenfalls in einer Variable speichern.
# Syntax: <Variable> = <string> + <string>

"""
# Definieren Sie einen neuen String in der Variable part_string!
# Überschreiben Sie anschließend sample_string, indem sie sample_string und part_string miteinander kombinieren!

part_string = 

sample_string = 

print()
"""


# *** EINGEBAUTE FUNKTIONEN *** #
# Python verfügt über verschiedene eingebaute Funktionen,
# z.B. len(), mit der sich die Zeichenlänge eines Strings bestimmen lässt.
# Die zuvor verwendeten Funktionen type() und print() zählen ebenfalls dazu.
# Funktionen werden mit ihrem Namen, runden Klammern und sogenannten Parametern aufgerufen.
# Syntax: <Funktionsname>(<Variable>)

"""
# Ermitteln Sie die Länge von sample_string!
sample_string_length =

print(sample_string_length)
"""


# *** EINGEBAUT METHODEN - STRINGS *** #
# Einige Datentypen wie strings verfügen über eingebaute Methoden.
# So lassen sich öft benötigte Operationen an einzelnen Variablen des jeweiligen Datentyps durchführen.
# Es muss also kein zusätzlicher Code dafür geschrieben werden.
# Strings können in Python auch schnell und einfach in einzelne Wörter zerlegt werden.
# dazu kann die Methode string.split() verwendet werden.
# Die einzelnen Teile werden automatisch in Form einer Liste gespeichert.
# In den Klammern kann man angeben, an welchen Zeichen der String geteilt werden soll.
# Viele Methoden akzeptieren solche Parameter, um unterschiedliche Ergebnisse zurückzugeben.
# Ohne Angaben (also bei leeren Klammern) orientiert sich Python beim Teilen standardmäßig an den Leerzeichen.
# Beispiele für weitere Stringmethoden:
# - .lower() - Konvertiert alle Großbuchstaben im String zu Kleinbuchstaben
# - .upper() – Konvertiert alle Kleinbuchstaben im String zu Großbuchstaben
# - .isdigit() - Gibt True zurück, wenn alle Zeichen im String Ziffern sind
# - .find() - Durchsucht den String nach einem Wert und gibt die erste Stelle zurück, an der er gefunden wurde
# Syntax: <Variable>.<Methodenname>()

"""
# Teilen Sie sample_string in einzelne Wörter!
sample_words = sample_string

sample_words_type = type(sample_words)

print(sample_words)
print(sample_words_type)
"""
