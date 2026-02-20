# *** LEVEL 1 - DEBUGGING *** #
# Der folgende Code enthält einige absichtlich eingebaute Fehler.
# Nutzen Sie die Traceback-Nachrichten und das PyCharm Syntax-Highlighting um diese Fehler zu finden und zu beheben!
# Erklären Sie außerdem in Kommentaren, wodurch der Fehler ausgelöst wird!
# Die Aufgabe ist erfolgreich abgeschlossen, wenn beim Ausführen des Codes keine Fehler auftreten.
from calendar import day_abbr

# AUFGABE 1 - VARIABLEN

int = 1
# Syntaktisch korrekt, aber überschreibt den eingebauten Typnamen "int".
# Dadurch ist der eingebaute Typname int in diesem Skript überschrieben; int() ist hier nicht mehr aufrufbar.
# daher ⮟
my_int = 1

float = 1.0
# Syntaktisch korrekt, aber überschreibt den eingebauten Typnamen float; float() ist hier nicht mehr aufrufbar.
# daher ⮟
my_float = 1.0

boolean = True
# Korrekt. boolean ist kein Keyword und kein eingebauter Typname; daher kann es als Variablenname verwendet werden.

# lambda = 11
# "lambda" ist ein Keyword in Python und kann nicht als Variablenname verwendet werden.
# daher ⮟
my_lambda = 11

sample_int = 1
# korrekt

sample_int = 2
# korrekt

# sample_int =! 3
# =! ist kein gültiger Operator. Das Zeichenpaar != ist der Ungleich-Operator. Damit prüfen wir zwei Werte auf
# Ungleichheit.
# daher ⮟
sample_int != 3

# sample_int === 4
# === existiert in Python nicht. Der Vergleichsoperator ist ==
# daher ⮟
sample_int == 4

sample_string = "hello world!"
# korrekt

sample_string = 'hello world!'
# Korrekt, wir können einfache oder doppelte Anführungszeichen verwenden, solange sie am Anfang und Ende des Strings
# übereinstimmen.

# sample_string = 'hello world!"
# Anführungszeichen dürfen nicht gemischt werden.
# daher ⮟
sample_string = "hello world!"

# sample_string = """hello world!"""
# Triple-Quotes sind in Python syntaktisch korrekt und können auch für einzeilige Strings verwendet werden.
# Sie werden jedoch typischerweise für mehrzeilige Strings oder Docstrings eingesetzt.
# In diesem Fall sind sie nicht notwendig, aber kein Fehler.
# daher ⮟
sample_string = "hello world!"

# sample_string = "hello world!
# Schließendes Anführungszeichen fehlt. String muss mit demselben Anführungszeichen geschlossen werden.
# daher ⮟
sample_string = "hello world!"

# sample_string = "hello world"!
# Inhalte des Strings müssen innerhalb der Anführungszeichen stehen.
# daher ⮟
sample_string = "hello world!"

sample_list = [1, 2, 3, 4, 5]
# korrekt

sample_list = [1, 2, 3, 4, 5.5]
# korrekt, floats und ints können in derselben Liste gemischt werden.

# sample_list = [1.2, 2, 03.22, 4, 5)
# Listenklammern müssen korrekt geöffnet [ und geschlossen ] werden.
# # Führende Null in einer Dezimal-Zahlliteral ist in Python 3 nicht zulässig (z. B. 03 oder 03.22).
# daher ⮟
sample_list = [1.2, 2, 3.22, 4, 5]

sample_list = ["Hello", "world!"]
# korrekt

sample_list = ["Hello", "world!", "Nice", "to", "meet", "you!"]
# korrekt

sample_list = ["Hello", "world!", "Nice", "to", "meet", "you", 2, "!"]
# korrekt, Strings und Zahlen können in derselben Liste gemischt werden.

sample_list = ["Hello", "world!", ["Nice", "to", "meet", "you", 2, "!"]]
# korrekt, Listen können auch verschachtelt sein (Listen in Listen).

# sample_list = [["Hello", "world!"], ["Nice", "to", "meet", "you", 2, "!"]]]
# Zu viele schließende Klammern - jede öffnende Klammer braucht genau eine schließende.
# daher ⮟
sample_list = [["Hello", "world!"], ["Nice", ["to", "meet"], "you", 2, "!"]]

sample_dict = {"Hello": 1, "world!": 2}
# korrekt

# sample_dict = {"Hello": 1, "world!": 2, "Hi": 1, "John!": 3,5}
# Dezimalzahlen verwenden Punkt (.), nicht Komma (,).
# daher ⮟
sample_dict = {"Hello": 1, "world!": 2, "Hi": 1, "John!": 3.5}

sample_dict = {"Hello": 1, "world!": 2, "Hi": 1, "John!": 3.5}
# korrekt

sample_dict = {"Hello": 1, "world!": 2, "Hello": 1, "John!": 3.5}
# Doppelte Schlüssel im Dictionary - der letzte Wert überschreibt den ersten.


# AUFGABE 2 - EINGEBAUTE FUNKTIONEN

# sample_int_length = len(sample_int)
# len() funktioniert nicht auf int-Objekten.
# len(sample_int) würde einen TypeError auslösen,
# len() kann nur auf iterierbaren Objekten wie Strings, Listen oder Dictionaries angewendet werden.
# daher ⮟
sample_string_length = len(sample_string)

sample_list_length = len(sample_list)
# korrekt, aber: len(sample_list) gibt die Anzahl der Elemente in der Liste zurück, nicht die Anzahl
# der Zeichen in den Strings der Liste.

sample_dict_length = len(sample_dict)
# korrekt, aber: len(sample_dict) gibt die Anzahl der Schlüssel im Dictionary zurück, nicht die Anzahl
# der Werte oder die Länge der Schlüssel.

print(sample_int)
# korrekt

# print[sample_string]
print(sample_string)
# Funktionen verwenden runde Klammern (), nicht eckige Klammern []. Eckige Klammern werden für Indexierung oder Zugriff
# auf Elemente verwendet.

print(sample_list)
# korrekt

type(sample_string)
# korrekt

type(sample_dict)
# korrekt

# type(sample_string + sample_int)
# Strings und Zahlen können nicht direkt miteinander addiert werden, da sie unterschiedliche Datentypen sind.
# Python weiß nicht, wie es einen String und eine Zahl kombinieren soll, was zu einem TypeError führt.
# daher ⮟
type(sample_string + str(sample_int))

# AUFGABE 3 - EINGEBAUTE METHODEN

"Hello world!".split()
# korrekt, ohne Argument (Angabe in der Klammer) wird standardmäßig an Leerzeichen gesplittet.

# "Hello world!".split(2)
# split() erwartet einen String als Argument, nicht eine Zahl.
# daher ⮟
"Hello world!".split(" ")

# ["Hello", "World"].split()
# split() ist eine String-Methode und funktioniert nicht auf Listen. Methodoen müssen auf Objekten des entsprechenden
# Typs aufgerufen werden.
# daher ⮟
"Hello, World".split()

[1, 2, 3, 4, 5].sort()
# korrekt

[1, 2, 3.3, 4, 5].sort()
# korrekt, ints und floats können in derselben Liste sortiert werden, da sie beide zu den Zahlen
# gehören und vergleichbar sind.

[1, 2, 3.3, 4.22, 5].sort()
# korrekt

# [1, 2, 3.3, 4.22, 5].sorted()
# Es gibt keine Listenmethode ".sorted()".
# sorted() ist eine eingebaute Funktion, die ein iterierbares Objekt als Argument erhält
# und eine neue sortierte Liste zurückgibt.
# Listen besitzen stattdessen die Methode ".sort()", die die Liste direkt (in-place) sortiert.
# daher ⮟
[1, 2, 3.3, 4.22, 5].sort()

[1, 2, 3.3, 4.22, 5 * 2].sort()
# korrekt, mathematische Ausdrücke werden vor der Sortierung ausgewertet, daher wird 5*2 zu 10 und die Liste wird
# korrekt sortiert.

["Hello", "world!"].sort()
# korrekt, Strings können alphabetisch sortiert werden.

["Hello", "world!", "Nice", "to", "meet", "you!"].sort()
# korrekt, Strings werden alphabetisch sortiert; Großbuchstaben kommen vor Kleinbuchstaben.

["Hello", "world!", "Nice", "to", "meet", "you", "2"].sort()
# korrekt, Strings werden alphabetisch sortiert, wobei "2" vor den Buchstaben kommt.

# ["Hello", "world!", "Nice", "to", "meet", "you!", 2].sort()
# Strings und Zahlen können nicht in derselben Liste sortiert werden, da sie unterschiedliche Datentypen sind und
# nicht direkt miteinander verglichen werden können. Dies führt zu einem TypeError.
# daher ⮟
["Hello", "world!", "Nice", "to", "meet", "you!", "2"].sort()

# AUFGABE 4 - INDEX OPERATIONEN

# sample_string(0)
# Indexierung erfolgt mit eckigen Klammern [], nicht mit runden Klammern ().
# daher ⮟
sample_string[0]

sample_string[-1]
# korrekt, negative Indizes zählen von hinten, -1 ist das letzte Zeichen.

sample_string[5]
# korrekt, Indizes beginnen bei 0, daher ist sample_string[5] das 6. Zeichen, was ein Leerzeichen ist.

sample_list[0]
# korrekt, Indizes beginnen bei 0, daher ist sample_list[0] das erste Element der Liste.

# sample_list[[-1]]
# Python interpretiert sample_list[[-1]] als: Nimm das Element an der Position [-1]. Aber [-1] ist selbst eine Liste,
# und Indizes müssen Zahlen sein, nicht Listen. Dies führt zu einem TypeError.
# Wenn wir das letzte Element haben wollen, brauchen wir nur eine Indexierung: sample_list[-1]
# daher ⮟
sample_list[-1]


# sample_list[5]
# Indizes beginnen bei 0, daher ist sample_list[5] das 6. Element der Liste. Da die Liste nur 5 Elemente hat
# (Index 0-4), führt dies zu einem IndexError.
# daher ⮟
sample_list[4] # z.B.


# sample_list[len(sample_string)]
# Indizes müssen innerhalb der Grenzen der Liste liegen. len(sample_string) gibt die Länge des Strings zurück, die größer
# als die Anzahl der Elemente in sample_list ist, was zu einem IndexError führt.
# daher ⮟
sample_list[len(sample_list) - 1] # z.B.


sample_string[0:2]
# korrekt, gibt die ersten beiden Zeichen des Strings zurück (Index 0 und 1).

sample_string[:]
# Python erlaubt es, den Start- und Endindex in einem Slice wegzulassen. sample_string[:] gibt den gesamten
# String zurück


sample_string[:len(sample_string)]
# Korrekt, gibt den gesamten String zurück, da der Endindex exklusiv ist und len(sample_string) die Länge des Strings
# zurückgibt.

sample_list[0:2]
# Korrekt, gibt die ersten beiden Elemente der Liste zurück (Index 0 und 1).

sample_list[:]
# Korrekt. sample_list[:] erstellt eine Kopie der Liste.
# Die Kopie und das Original sind zwei separate Objekte:
# - Änderungen an sample_list beeinflussen die Kopie nicht
# - Änderungen an der Kopie beeinflussen sample_list nicht

sample_list[:len(sample_list)]
# Korrekt, gibt die gesamte Liste zurück, da der Endindex exklusiv ist und len(sample_list) die Anzahl der Elemente
# in der Liste zurückgibt.
