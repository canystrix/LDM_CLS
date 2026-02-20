# *** PRIMITIVE DATENTYPEN - INTEGER UND FLOAT *** #
# Integer und Floats gehören ebenfalls zu den grundlegenden Datentypen in Python.
# Mit ihnen lassen sich ebenfalls Vergleiche, aber auch Berechnungen anstellen.
# Sie werden auch genutzt, um Statistiken zu berechnen wie zum Beispiel die durchschnittliche Länge von Strings.

"""
# Definieren Sie eine neue Variable vom Dateityp integer als sample_number!
# Und eine Variable vom Dateityp float als sample_decimal

sample_number =
sample_decimal =

sample_number_type = type(sample_number)
sample_decimal_type = type(sample_decimal)

print(sample_number)
print(sample_number_type)
print(sample_decimal)
print(sample_decimal_type)
"""


# *** ARITHMETIK *** #
# Mit Integers und Floats können einfache Arithmetische Operation durchgeführt werden.
# Eine Arithmetische Operation die einen Float-Wert beinhaltet, hat immer einen Float-Wert als Ergebnis.
# Folgende arithmetische Operatoren stehen zur Verfügung:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*) - Doppelte Sternchen potenzieren einen Wert (Zum Beispiel: 5 ** 2 = 25)
# - Division (/) – ACHTUNG, das Ergebnis einer Division ist immer ein Float-Wert!
# - Modulo (%) – Gibt den verbleibenden Rest einer Division zurück (Zum Beispiel: 5 % 2 = 1)
# Wenn arithmetische Operationen verkettet werden, folgen sie den üblichen Regeln der Arithmetik:
# - Priorität 1: Ausdrücke in Klammern
# - Priorität 2: Exponenten
# - Priorität 2: Multiplikation und Division
# - Priorität 3: Addition und Subtraktion
# Bei gleicher Priorität der Operationen, werden sie ihrer Reihenfolge entsprechend ausgewertet.
# Syntax: <Wert> <Operator> <Wert>

"""
# Führen Sie unterschiedliche arithemtische Operationen aus! Nutzen Sie dabei sowohl Integer als auch Float!
# Sie können auch ihre zuvor definierten Variablen verwenden!
sample_sum = 
sample_difference =
sample_product = 
sample_quotient = 
sample_modulo =

print(sample_sum)
print(sample_difference)
print(sample_product)
print(sample_quotient)
print(sample_modulo)
"""


# *** DATENTYPEN KONVERTIEREN *** #
# Python bestimmt den Datentyp einer Variable automatisch,
# d.h., bei der Erstellung von Variablen wird i.d.R. kein Datentyp angegeben.
# Manchmal muss der Datentyp allerdings zu einem späteren Zeitpunkt mit expliziten Deklarationen geändert werden.
# Dazu verwendet man die Funktionen bool(<Variable>), int(<Variable>), str(<Variable>), float(<Variable>).
# Es ist zu beachten:
# - Float zu Integer – Der Rückgabewert wird automatisch gerundet
# - String zu Integer – Nur möglich, wenn der zu konvertierender Wert ausschließlich eine ganz Zahl enthält
# - String zu Float – Nur möglich, wenn der jeweilige String ausschließlich eine ganze Zahl ODER ein Dezimalzahl enthält
# - Integer zu Boolean – 0 ist FALSE, jede andere Zahl ist TRUE
# - Float zu Boolean – 0.0 ist FALSE, jede andere Zahl ist TRUE
# - String zu Boolean – "" oder leere Strings sind FALSE, jeder andere String ist TRUE

"""
# Konvertieren die Variablen sample_number, sample_decimal und sample_boolean zu anderen Datentypen!
# Speichern Sie die Ergebnisse dabei wie folgt:
# integer_to_boolean: Rückgabewert der Konvertierung von sample_number zu Boolean
# float_to_integer: Rückgabewert der Konvertierung von sample_float zu Integer
# boolean_to_float: Rückgabewert der Konvertierung von sample_boolean zu Float
# integer_to_string: Rückgabewert der Konvertierung von sample_number zu String

sample_boolean = True

integer_to_float =
float_to_integer =
boolean_to_float =

integer_to_string =

integer_to_float_type = type(integer_to_float)
float_to_integer_type = type(float_to_integer)
boolean_to_float_type = type(boolean_to_float)

integer_to_string_type = type(integer_to_string)

print(integer_to_float)
print(integer_to_float_type)
print(float_to_integer)
print(float_to_integer_type)
print(boolean_to_float)
print(float_to_boolean_type)

print(integer_to_string)
print(integer_to_string_type)
"""