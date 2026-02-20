# *** KOMPLEXE DATENTYPEN - LISTEN  *** #
# Listen werden genutzt, um Sequenz-Datenstrukturen in Python abzubilden.
# Dienen dazu, mehrere Werte in einer einzigen Variablen zu speichern.
# Sie werden Variablen zugewiesen als kommagetrente Werte innerhalb von eckigen Klammern.
# Können unterschiedliche Datentypen enthalten (selbst weitere Listen -> nesting) und erlauben Doubletten.
# Die Elemente einer Liste werden immer in derselben Reihenfolge angezeigt und können verändert werden,
# d.h. Elemente können geändert, neu hinzugefügt oder entfernt werden, nachdem die Liste erstellt wurde.
# Syntax: <Variablenname> = [<element>, <element>] ODER <Variablenname> = list

"""
# Legen Sie eine neue Liste mit mindestens fünf Elementen in sample_list an!
# Verwenden Sie dazu alle bisher gelernten Datentypen inklusive weiterer Listen!
sample_list =

sample_list_type = type(sample_list)
sample_list_length = len(sample_list)

print(sample_list)
print(sample_list_type)
print(sample_list_length)
"""


# *** EINGEBAUTE METHODEN - LISTEN *** #
# So wie Strings verfügen auch Listen über ihre eigenen eingebaute Methoden.
# .pop() entfernt das letzte Element einer Liste.
# .append() fügt der Liste in Element als letztes Element hinzu.
# Beispiele für weitere Listenmethoden:
# - .clear() – entfernt alle Elemente aus einer Liste
# - .remove() – entfernt ein Element basierend auf seinem Wert aus der Liste
# - .sort() - sortiert die Liste aufsteigend nach Länge der Elemente für Strings oder absolutem Wert für Zahlen
# - ACHTUNG: sort funktioniert nicht, wenn in einer Liste Strings mit anderen Datentypen gemischt werden!
# Wenn sie eine Listenmethode ausführen wird das Ergebnis automatisch in der bearbeiteten Variable gespeichert.
# Syntax: <liste>.<Methodenname>()

"""
# Entfernen Sie das letzte Element von sample_list und fügen Sie ein Neues hinzu!
sample_list
sample_list

print(sample_list)
"""


# *** INDEXING *** #
# Jedes Element hat einen festen Platz in der Liste und kann anhand seiner Position ausgewählt werden (Indexing).
# Beim Zählen fängt man bei 0 an, d.h. das erste Element ist an Position 0, das zweite an Position 1, usw.
# Dieses Verhalten ist in fast allen Progammiersprachen identisch (Ausnahmen sind etwa Fortran, Lua oder COBOL).
# Um ein Element auszuwählen, muss man die Liste spezifizieren und den Index in eckigen Klammern angeben.
# Das letzte Element kann mit dem Index [-1] abgerufen werden.
# Elemente können dementsprechend auch in umgekehrter Reihenfolge abgefragt werden ([-1], [-2], ...).
# Indexing funktioniert auch mit Strings!
# Dabei werden allerdings nicht Wörter oder Satzteile durchnummeriert, sondern Zeichen (inklusive Leerzeichen).
# Syntax: <Liste oder String>[<Index>]

"""
# Generieren Sie eine Liste aus sample_string und speichern Sie sie in sample_word! 
# Greifen Sie auf das erste Wort von sample_words zu und speichern Sie es in first_word!
# Greifen Sie außerdem auf der letzte Wort von sample_words zu und speichern Sie es in last_word!
# first_word_type und last_word_type sollen am Ende String sein!
sample_string = "Hello John! Nice to meet you!"
sample_words =
first_word =
last_word =

first_word_type = type(first_element)
last_word_type = type(last_element)

print(first_word)
print(first_word_type)
print(last_word)
print(last_word_type)
"""


# *** SLICING *** #
# Durch das Indexing können wir also auf bestimmte Elemente einer Liste oder eines Strings zugreifen.
# Was aber, wenn wir auf einen ganzen Ausschnitt eines Strings oder einer Liste zugreifen möchten?
# Dafür gibt es die Slice-Notation, bzw. Slicing.
# Slicing funktioniert auf der Basis von Indexen:
# Variable[Startindex:Endindex+1]
# Wenn man also die ersten 100 Zeichen haben möchte, muss 101 als Endindex angegeben werden.
# Wird der Endindex ausgelassen, wird ein Slice inklusive letztem Element zurückgegeben
# Wenn -1 als Endindex angegeben wird, ist das letzte Element nicht enthalten!
# Syntax: <Variable>[<Startindex>:<Endindex>+1]

"""
# Isolieren Sie unterschiedliche Teile von sample_words!
# Vom ersten bis zum dritten Element
first_slice = sample_words
# Vom dritten bis zum letzten Element
second_slice = sample_words
# Vom zweiten bis zum vorletzten Element
third slice = sample_words

print(first_slice)
print(second_slice)
print(third_slice)
"""


# *** EINGEBAUTE METHODEN - JOIN *** #
# Wir können Listen per Datentypkonvertierung wieder in einen String umwandeln.
# Die so entstehende Formatierung entspricht allerdings der Syntax der Liste.
# Listenelemente können stattdessen mit der Methode .join() zu einem String zusammengesetzt werden.
# .join() ist allerdings keine Listenmethode! Sie wird auf einen String angewendet.
# Die Elemente werden im entstehenden String durch das Zeichen abterennt, das vor dem Aufruf von .join() steht.
# Syntax: "<Trennzeichen>".join(<Liste>)

"""
# Setzen Sie sample_words wieder zu einem String zusammen!
result_string = 

print(sample_string)
"""
