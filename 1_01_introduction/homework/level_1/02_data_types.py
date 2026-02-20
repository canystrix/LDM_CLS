# *** LEVEL 1 - DATENTYPEN *** #
# Im folgenden Code verwenden wir Variablen deren Datentyp nicht sofort ersichtlich ist.
# Das kann zum Beispiel passieren, wenn wir den Code Anderer verwenden.
# Oder etwa unterschiedliche Datenformate importieren.

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.insert(0, ...) tells Python to search for modules in a specific folder
# os.path.dirname(__file__) = get the folder where THIS file is located
# '..' = go up one folder level to the parent directory
# os.path.abspath(...) = convert that path to an absolute path that Python can understand
# Python will now look for the _meta folder in the parent directory


from _meta.ignore_me import test_variable_1
from _meta.ignore_me import test_variable_2
from _meta.ignore_me import test_variable_3
from _meta.ignore_me import test_variable_4
from _meta.ignore_me import test_variable_5
from _meta.ignore_me import test_variable_6
from _meta.ignore_me import test_variable_7

# Moment, das ist neu!
# Keine Angst, in Modul 3 werden wir diese Syntax näher kennenlernen!
# Falls Sie es aber kaum erwarten können, können Sie unter folgendem Link mehr erfahren:
# https://realpython.com/python-import/


# AUFGABE 1
# Geben Sie die Variablen über die Print-Funktion aus um herauszufinden, welche Werte sie beinhalten!

# Print each variable to display its value
print(test_variable_1)
print(test_variable_2)
print(test_variable_3)
print(test_variable_4)
print(test_variable_5)
print(test_variable_6)
print(test_variable_7)


# AUFGABE 2
# Ermitteln Sie die Datentypen der einzelnen Variablen und geben Sie sie mit der Print-Funktion aus!

# Use the type() function to determine the data type of each variable
test_variable_1_type = type(test_variable_1)
test_variable_2_type = type(test_variable_2)
test_variable_3_type = type(test_variable_3)
test_variable_4_type = type(test_variable_4)
test_variable_5_type = type(test_variable_5)
test_variable_6_type = type(test_variable_6)
test_variable_7_type = type(test_variable_7)


print(test_variable_1_type)
print(test_variable_2_type)
print(test_variable_3_type)
print(test_variable_4_type)
print(test_variable_5_type)
print(test_variable_6_type)
print(test_variable_7_type)


# AUFGABE 3
# Verändern Sie jeweils den letzten Wert der folgenden Vergleiche, sodass sie True ergeben!

# Compare the data types with the expected type objects
print(test_variable_1_type == dict)
print(test_variable_2_type == float)
print(test_variable_3_type == int)
print(test_variable_4_type == bool)
print(test_variable_5_type == list)
print(test_variable_6_type == str)

# Don't understand, the comparisons already return True (??)
