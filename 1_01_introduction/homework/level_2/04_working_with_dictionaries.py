# *** LEVEL 1 - ARBEITEN MIT DICTIONARIES *** #
# Dictionaries sind Datenstrukturen, mit deren Hilfe wir komplexe Beziehungen abbilden können.
# Beispielsweise können wir in einem Dictionary speichern, wie oft jedes Wort in einem Text vorkommt.
# Im Folgenden finden Sie ein Dictionary, an dem wir unterschiedliche Operationen testen wollen.

sample_dictionary = {1: "Python", 2: "programming", 5: "language"}


# AUFGABE 1
# Bestimmen Sie die Anzahl der Keys in sample_dictionary!
# Speichern Sie das Ergebnis in sample_dictionary_key_num!

# sample_dictionary_key_num = len(sample_dictionary.keys())

sample_dictionary_key_num = len(sample_dictionary.keys())
sample_dictionary_value_num = len(sample_dictionary.values())
# Use the len() function with .keys() and .values() methods to count the number of keys and values in the dictionary

print(sample_dictionary_key_num)
print(sample_dictionary_value_num)

# AUFGABE 2
# Ersetzen Sie jeden Wert in sample_dictionary!
# Nutzen Sie dazu die folgenden Datentypen:
# - Float
# - Liste mit mindestens zwei Elementen
# - Dictionary mit mindestens zwei Key-Value-Paaren

# sample_dictionary[1] = 5.5
# sample_dictionary[2] = [1, 2, 3]
# sample_dictionary[5] = {1: 2}

sample_dictionary[1] = 5.5
sample_dictionary[2] = [1, 2, 3]
sample_dictionary[5] = {1: 2, 2: 4}
# Replace each value in the dictionary with the required data types: float, list and nested dictionary

print(sample_dictionary)


# AUFGABE 3
# Fügen Sie sample_dictionary zwei neue Werte hinzu!

# sample_dictionary[3] = 1
# sample_dictionary[4] = 2

sample_dictionary[3] = 1
sample_dictionary[4] = 2
# Add two new key-value pairs to the dictionary using direct assignment

print(sample_dictionary)


# AUFGABE 4
# Wandeln Sie die Keys aus sample_dictionary in eine Liste um und speichern Sie sie in sample_dicationary_keys!
# Speichern Sie außerdem eine Liste der Values aus sample_dictionary in sample_dictionary values.
# sample_dictionary_keys_type und sample_dictionary_values_type sollten als Datentyp list ausgeben!

# sample_dictionary_keys = list(sample_dictionary.keys())
# sample_dictionary_values = list(sample_dictionary.values())

sample_dictionary_keys = list(sample_dictionary.keys())
sample_dictionary_values = list(sample_dictionary.values())
# Convert dictionary keys and values to lists using the list() function combined with .keys() and .values() methods

sample_dictionary_keys_type = type(sample_dictionary_keys)
sample_dictionary_values_type = type(sample_dictionary_values)

print(sample_dictionary_keys)
print(sample_dictionary_keys_type)
print(sample_dictionary_values)
print(sample_dictionary_values_type)
