# *** LEVEL 1 - FUNKTIONEN *** #
# Hier finden wir mehrere Aufgaben zum Schreiben und Aufrufen von Funktionen.
# Funktionen ermöglichen es uns, wiederverwendbaren Code zu schreiben!

sample_string = "Loctimize is a market-leading expert for language logistics."
# Ein Beispiel-String, den wir in unseren Funktionen verwenden werden

sample_int_1 = 50
# Eine erste Ganzzahl (Integer) für unsere Berechnungen

sample_int_2 = 500
# Eine zweite Ganzzahl für unsere Berechnungen


# AUFGABE 1
# Schreiben wir eine Funktion, die zwei positionelle Argumente nimmt.
# Beide Argumente sollten vom Datentyp int sein!
# Die Funktion soll die Summe der beiden positionellen Argumente berechnen und zurückgeben.
# z.B. sum = a + b
# Speichern wir den Rückgabewert der Funktion in einer separaten Variable und geben ihn aus!
# Rufen wir die Funktion auf, indem wir sample_int_1 und sample_int_2 als Argumente übergeben.

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

def function(a, b):
    # def leitet die Definition einer Funktion ein
    # 'function' ist der Name unserer Funktion (wir könnten jeden beliebigen Namen wählen)
    # (a, b) sind die Parameter - Platzhalter für die Werte, die wir später übergeben
    # Diese Funktion erwartet zwei positionelle Argumente

    result = a + b
    # Wir addieren die beiden Parameter und speichern das Ergebnis in der Variable 'result'

    return result
    # return gibt den Wert zurück an die Stelle, wo die Funktion aufgerufen wurde
    # Nach return endet die Funktion automatisch


# Wir können Variablen innerhalb und außerhalb von Funktionen denselben Namen geben,
# ohne dass sie sich gegenseitig überschreiben
# Das liegt an einem Konzept in Programmiersprachen namens "Scope" (Gültigkeitsbereich),
# von dem es "global scope" und "local scopes" gibt
# Stellen wir uns unser Skript als ein Haus vor und jede einzelne Funktion als ihr
# eigenes Zimmer. Jedes Zimmer kann Kisten haben, die identisch benannt und geformt sind,
# aber dennoch unterschiedliche Gegenstände enthalten!
result = function(sample_int_1, sample_int_2)
# Hier rufen wir die Funktion auf und übergeben die beiden Beispiel-Integers als Argumente
# Der Rückgabewert der Funktion wird in der Variable 'result' gespeichert
# Wichtig: Diese 'result' Variable ist NICHT dieselbe wie die 'result' Variable
# innerhalb der Funktion!

print(result)
# Ausgabe des Ergebnisses (sollte 550 sein: 50 + 500)


# AUFGABE 2
# Schreiben wir eine Funktion, die ein positionelles Argument und ein
# Schlüsselwort-Argument (keyword argument) nimmt.
# Das positionelle Argument sollte ein String sein.
# Das Schlüsselwort-Argument sollte den Datentyp int haben mit einem Standardwert von 100.
# Die Funktion soll die Zeichenlänge des Strings ermitteln, der als positionelles
# Argument übergeben wurde.
# Sie soll diese dann mit der Ganzzahl vergleichen, die als Schlüsselwort-Argument
# übergeben wurde.
# Wenn die Länge des Strings kleiner ist als die übergebene Ganzzahl, geben wir True zurück.
# Wenn die Länge des Strings größer ist als die übergebene Ganzzahl, geben wir False zurück.
# Rufen wir die Funktion zweimal auf:
# Einmal ohne das Schlüsselwort-Argument (nutzt dann den Standardwert)
# Einmal mit sample_int_2 als Schlüsselwort-Argument

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

def function(arg, kwarg=100):
    # Diese Funktion hat zwei Parameter:
    # 'arg' ist ein positionelles Argument (muss immer übergeben werden)
    # 'kwarg=100' ist ein Schlüsselwort-Argument mit Standardwert 100
    # Wenn wir beim Aufruf keinen Wert für kwarg angeben, wird automatisch 100 verwendet

    string_length = len(arg)
    # len() ermittelt die Anzahl der Zeichen im String

    if string_length < kwarg:
        # Vergleichen wir: Ist die String-Länge kleiner als der kwarg-Wert?

        return True
        # Wenn ja, geben wir True zurück und die Funktion endet hier

    else:
        # Wenn die Bedingung False ist (String ist nicht kleiner)

        return False
        # Geben wir False zurück


result = function(sample_string)
# Erster Aufruf: Wir übergeben nur sample_string
# Das Schlüsselwort-Argument 'kwarg' wird nicht angegeben, also wird der Standardwert
# 100 verwendet
# sample_string hat 60 Zeichen, 60 < 100, also sollte True zurückgegeben werden

print(result)
# Ausgabe: True

result = function(sample_string, kwarg=sample_int_2)
# Zweiter Aufruf: Wir übergeben sample_string UND ein Schlüsselwort-Argument
# kwarg=sample_int_2 bedeutet: Verwende 500 statt des Standardwerts 100
# sample_string hat 60 Zeichen, 60 < 500, also sollte True zurückgegeben werden
# Wichtig: Beim Übergeben müssen wir 'kwarg=' schreiben, um anzugeben, welcher
# Parameter gemeint ist

print(result)
# Ausgabe: True

