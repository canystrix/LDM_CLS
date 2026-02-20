# *** LEVEL 2 - ARBEITEN MIT DICTIONARIES *** #
# Dictionaries sind Datenstrukturen, mit deren Hilfe wir komplexe Beziehungen abbilden können.
# Beispielsweise können wir in einem Dictionary speichern, wie oft jedes Wort in einem Text vorkommt.
# Im Folgenden finden Sie ein Dictionary, an dem wir unterschiedliche Operationen testen wollen.

sample_dictionary = {1: "Python", 2: "programming", 5: "language"}


# AUFGABE 1
# Bestimmen Sie die Anzahl der Keys in sample_dictionary!
# Speichern Sie das Ergebnis in sample_dictionary_key_num!

# sample_dictionary_key_num = 0
sample_dictionary_key_num = len(sample_dictionary)
# len() auf ein Dictionary angewendet zählt die Anzahl der Schlüssel (Keys).
# Das ist nützlich, um zu wissen, wie viele Key-Value-Paare in unserem Dictionary gespeichert sind.

print(sample_dictionary_key_num)


# AUFGABE 2
# Ersetzen Sie jeden Wert in sample_dictionary!
# Nutzen Sie dazu die folgenden Datentypen:
# - Float
# - Liste mit mindestens zwei Elementen
# - Dictionary mit mindestens zwei Key-Value-Paaren

# sample_dictionary[1] = "Python"
# Der ursprüngliche Wert ist ein String, gefordert ist ein Float (eine Dezimalzahl).
# Mit dictionary[key] = value ersetzen wir den alten Wert durch einen neuen.
# daher ⮟
sample_dictionary[1] = 5.5

# sample_dictionary[2] = "programming"
# Der ursprüngliche Wert ist ein String, gefordert ist eine Liste mit mindestens zwei Elementen.
# Eine Liste ermöglicht es, mehrere Werte unter einem Key zu speichern.
# daher ⮟
sample_dictionary[2] = [1, 2]

# sample_dictionary[5] = "language"
# Der ursprüngliche Wert ist ein String, gefordert ist ein Dictionary mit mindestens zwei Key-Value-Paaren.
# Dictionaries können verschachtelt werden (Dictionary im Dictionary)..
# daher ⮟
sample_dictionary[5] = {1: 2, 3: 4}


print(sample_dictionary)


# AUFGABE 3
# Fügen Sie sample_dictionary zwei neue Werte hinzu!

# sample_dictionary
sample_dictionary[3] = "new_value_1"
# Mit dictionary[key] = value wird ein neues Key-Value-Paar erstellt, falls der Key noch nicht existiert.

# sample_dictionary
sample_dictionary[4] = "new_value_2"
# s.o.

print(sample_dictionary)


# AUFGABE 4
# Wandeln Sie die Keys aus sample_dictionary in eine Liste um und speichern Sie sie in sample_dictionary_keys!
# Speichern Sie außerdem eine Liste der Values aus sample_dictionary in sample_dictionary_values.
# sample_dictionary_keys_type und sample_dictionary_values_type sollten als Datentyp list ausgeben!

# sample_dictionary_keys = sample_dictionary.keys()
# .keys() gibt ein dict_keys-Objekt zurück, nicht eine echte Liste.
# dict_keys-Objekte können nicht indexiert werden (z.B. mit [0]) und haben nicht alle List-Methoden.
# Daher konvertieren wir es mit list() in eine echte Liste, um damit flexibler arbeiten zu können.
# daher ⮟
sample_dictionary_keys = list(sample_dictionary.keys())


# sample_dictionary_values = sample_dictionary.values()
# .values() gibt alle Werte aus dem Dictionary zurück, aber nicht als echte Liste.
# Daher konvertieren wir es mit list() in eine Liste, um damit besser arbeiten zu können.
# daher ⮟
sample_dictionary_values = list(sample_dictionary.values())
# list() konvertiert das Ergebnis von .values() in eine echte Liste.

sample_dictionary_keys_type = type(sample_dictionary_keys)
sample_dictionary_values_type = type(sample_dictionary_values)

print(sample_dictionary_keys)
print(sample_dictionary_keys_type)
print(sample_dictionary_values)
print(sample_dictionary_values_type)
