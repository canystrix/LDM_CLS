# *** KOMEPLEXE DATENTYPEN - DICTIONARIES *** #
# Ein Dictionary ist eine Sammlung von Daten, die keine Duplikate enthält.
# Die Daten werden in sog. Key:Value-Pairs gespeichert, sie sind geordnet* und veränderbar. (*seit Python-Version 3.7)
# Dictionaries werden mit geschweiften Klammern geschrieben und jedem Key wird ein Value zugeordnet.
# - Keys sind einzigartig, Values können sich wiederholen.
# - Values können zum Beispiel Strings, Zahlen, Booleans, Listen oder weitere Dictionaries sein (nesting).
# Die Erstellung funktioniert wie bei Listen.
# man kann das Dictionary bei der Erstellung manuell befüllen
# oder ein leeres Dictionary erstellen und die Key:Value-Pairs durch Code hinzufügen und updaten.
# Syntax: <Variablenname> = {<key>: <value>, <key>: <value>} ODER <Variablenname> = dict()

"""
# Legen Sie ein neues Dictionary in sample_dict an!
# Verwenden Sie dazu alle bisher gelernten Datentypen inklusive Dictionaries!
sample_dict =

sample_dict_type = type(sample_dict)

print(sample_list)
print(sample_dict_type)
"""


# *** DICTIONARY KEYS *** #
# Auf Dictionary-Elemente kann nicht wie auf Strings oder Listen durch nummerierten Index zugegriffen werden.
# Stattdessen können wir auf ihre Values über den dazugehörigen Key zugreifen.
# Auf diese Weise können - ähnlich wie bei Listen - auch Werte im Dictionary ersetzt werden,
# zum Beispiel: Dictionary["key"] = "value"
# Auf diese Weise können auch neue Werte hinzugefügt werden, wenn der verwendete Key noch nicht existiert.
# Syntax: <Dictionary>[<key>]

"""
# Greifen Sie auf einen der Keys in sample_dict zu und speichern Sie ihn in sample_dict_value! 
sample_dict_value = 
print(sample_dict_value)

# Ändern sie den Wert, der diesem Key zugewiesen ist!
sample_dict =
print(sample_dict)
"""


# *** EINGEBAUT METHODEN - DICTIONARIES *** #
# Auch Dictionaries verfügen über eigene eingebaute Methoden.
# .keys() gibt die Keys eines Dictionary als listenähnliches Objekt zurück.
# .values() gibt die Values eines Dictionary als listenähnliches Objekt zurück.
# Die Rückgabewerte aus keys() und values() sind keine eigenständigen Listen.
# um sie als Listen zu speichern, müssen sie zusätzlich mit der list() Funktion konvertiert werden.
# Beispiele für weitere Dictionary-Methoden:
# - .clear() – entfernt alle Elemente aus einem Dictionary.
# - .pop() – entfernt ein Element basierend auf seinem Key aus dem Dictionary.
# - .popitem() - entfernt das letzte hinzugefügte Key-Value-Paar.
# Wenn sie eine Listenmethode ausführen wird das Ergebnis automatisch in der bearbeiteten Variable gespeichert.
# Syntax: <liste>.<Methodenname>()

"""
# Nutzen sie Methoden, um jeweils eine Liste für Keys und Values von sample_dict zu erhalten!
# speichern Sie die generierten Keys in sample_dict_keys!
# die generierten Values werden in sample_dict_values gespeichert!
sample_dict_keys =
sample_dict_values = 

sample_dict_keys_type = type(sample_dict_keys)
sample_dict_values_type = type(sample_dict_values)

print(sample_dict_keys)
print(sample_dict_key_type)
print(sample_dict_values)
print(sample_dict_values_type)
"""


# *** AUSBLICK AUF MODUL 2 *** #
# Im nächsten Modul werden wir und mit Funktionen, Bedingungen und Schleifen beschäftigen.
# Mit diesem Wissen werden Sie in der Lage sein, komplexer Logiken für die Sprachdatenverarbeitung zu schreiben!
# Wenn Sie sich bereits über die nächsten Themen informieren möchten, finden Sie weitere Informationen hier:
# Bedingungen: https://realpython.com/python-conditional-statements/
# For-Schleifen: https://realpython.com/python-for-loop/
# While-Schleifen: https://realpython.com/python-while-loop/
# Funktionen: https://realpython.com/defining-your-own-python-function/
