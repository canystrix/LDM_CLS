# *** KOMMENTARE *** #
# Kommentare erläutern den Code und werden von Python ignoriert beim Ausführen des Programms.
# Sie werden verwendet, um Python-Code zu erklären und den Code besser lesbar zu machen.
# Sie können auch dafür verwendet werden, Stellen im Code auszublenden.
# Syntax: # <Kommentar Text>

# print("Hello!")

# Mehrzeilige Kommentare werden durch drei einfache oder doppelte Anführungszeichen markiert, 
# wie in den folgenden Code-Beispielen zu sehen ist.


# *** PRINT *** #

# Werte werden im Script nicht automatisch angezeigt, wenn man Variablen oder Funktionen aufruft!
# Um Werte anzeigen zu lassen, verwendet man die Print-Funktion.
# Syntax: print(<Variable>)

# Lassen Sie sich folgenden Wert mithilfe von print() ausgeben:
# True


print("HI")

# *** VARIABLEN *** #
# Variablen sind wie Container, in denen ein Wert gespeichert und wiederverwendet werden kann.
# Variablen können beliebig oft verwendet und später überschrieben werden.
# sie sind der Grundstein jeglicher Programmiersprache!
# Syntax: <Variablenname> = <Wert>


# Weisen Sie der Variable den Wert True zu und lassen Sie sich das Ergebnis mithilfe von print() anzeigen!


sample_boolean = True

print(sample_boolean)


# *** CODESEQUENZ *** #
# Python liest den Code sequenziell von oben nach unten und bricht ab, sobald ein Fehler gefunden wird.
# Beim Kodieren muss also darauf geachtet werden, dass die Variablen definiert sind, bevor man sie aufruft!


# Entfernen Sie die Anführungszeichen und beobachten Sie, welcher Wert von print() ausgegeben wird!

sample_variable = False
sample_variable = sample_boolean
print(sample_variable)


# *** TRACEBACK *** #
# In folgendem Code wird eine Variable aufgerufen, bevor sie definiert wird.
# Dieser Fehler erzeugt einen sogenannten "Traceback".
# Dabei handelt es sich um eine Chronik aller Funktionsaufrufe im Code an einer bestimmten Stelle.
# Im Traceback sind abzulesen:
# - Die aufgerufenen Funktionen
# - Die Zeilen, in denen sie aufgerufen wurden
# - Die Sequenz, in der sie aufgerufen wurden
# - Die Art des Fehlers
# Den Traceback richtig lesen zu können ist eine der wichtigsten Fähigkeiten eines Softwareentwicklers!


# Wenn Sie die Reihenfolge ändern sehen Sie, dass der Code erfolgreich ausgeführt wird!
sample_error = False
print(sample_error)




# *** PRIMITIVE DATENTYPEN - BOOLEAN *** #
# Jedem Wert wird ein sogenannter "Datentyp" zugordnet.
# Boolean ist einer der grundlegenden Datentypen in Python.
# Mit type() kann man den Datentyp einer Variable bestimmen.
# Den entstehenden Wert kann man auch in einer Variable speichern, um ihn später wiederzuverwenden.
# Syntax: type(<variable>)


# Bestimmen sie den Datentyp der zuvor angelegten Variable sample_boolean!

sample_boolean_type = bool

print(sample_boolean_type)



# *** BOOLSCHE OPERATOREN *** #
# Mit Boolschen Operatoren kann man Werte und Variablen miteinander vergleichen.
# Ein solcher Vergleich gibt einen Boolean-Wert zurück.
# Der so zurückgegebene Wert kann auch in einer Variable gespeichert werden.
# Mögliche Vergleichsoperatoren sind:
# - == Exakt gleich
# - != Ungleich
# - < Kleiner als
# - > Größer als
# - <= Kleiner gleich
# - >= Größer gleich
# Syntax: <Wert> <operator> <Wert>

"""
# Verändern Sie nur die hier angegebenen Werte so, dass die folgenden Vergleiche "True" zurückgeben!
# Verändern Sie nicht die Operatoren!

print(True == False) 
print(False > True)
print(sample_variable != sample_boolean)
print(0 == True)
"""
