# *** LEVEL 2 - ARBEITEN MIT STRINGS *** #
# Bei der natürlichen Sprachverarbeitung liegt unser Hauptaugenmerk natürlich auf Strings.
# Strings bieten uns unterschiedliche Möglichkeiten, mit ihnen zu interagieren und sie zu manipulieren.
# Im Folgenden finden Sie zwei Strings, an denen wir unterschiedliche Operationen ausführen wollen.

sample_string_1 = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation."""

sample_string_2 = """Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects."""


# AUFGABE 1
# Kombinieren Sie sample_string_1 und sample_string_2 und speichern Sie das Ergebnis in sample_string_combined.
# Achten Sie darauf, dass die beiden Sätze in sample_string_combined durch ein Leerzeichen getrennt werden!

# sample_string_combined = ""
# Mit dem + Operator können wir Strings zusammenfügen (konkatenieren). So können wir mehrere Texte zu einem kombinieren.
# Das Leerzeichen " " in der Mitte sorgt dafür, dass die beiden Strings nicht direkt aneinander kleben.
# daher ⮟
sample_string_combined = sample_string_1 + " " + sample_string_2

print(sample_string_combined)

# AUFGABE 2
# Finden Sie den Index des ersten Leerzeichens in sample_string_combined.
# Nutzen Sie dafür eine von Pythons eingebauten Stringmethoden!

# first_space_index = 0
first_space_index = sample_string_combined.find(" ")
# find(" ") sucht nach dem ersten Leerzeichen im String und gibt dessen Position (Index) zurück.
# Der Index ist die Nummer der Position, an der sich das Leerzeichen befindet (Zählung beginnt bei 0).
# Wir brauchen diese Position später zum Slicing, um das erste Wort zu extrahieren.

print(first_space_index)


# AUFGABE 3
# Nutzen sie den Index des ersten Leerzeichens, um durch Slicing das erste Wort des Strings zu erhalten!

# first_word = sample_string_combined
# Das wäre der komplette String, nicht nur das erste Wort.
# daher ⮟
first_word = sample_string_combined[:first_space_index]
# [:first_space_index] ist ein Slice (Ausschnitt) des Strings. Der : bedeutet "von...bis".
# Wenn links vom : nichts steht, beginnen wir am Anfang des Strings (Index 0).
# first_space_index ist die Position des Leerzeichens. Damit bekomme wir alle Zeichen vor dem Leerzeichen.
# Das Ergebnis ist das erste Wort des Strings.

print(first_word)


# AUFGABE 4
# Finden Sie heraus, wieviele Zeichen in sample_string_1 und sample_string_2 enthalten sind!
# Speichern Sie die Ergebnisse in length_sample_string_1, length_sample_string_2 und length_sample_string_sum!

# length_sample_string_1 = 0
length_sample_string_1 = len(sample_string_1)
# len() zählt alle Zeichen im String (inkl. Leerzeichen, Zeilenumbrüche, Satzzeichen).

# length_sample_string_2 = 0
length_sample_string_2 = len(sample_string_2)
# len() zählt alle Zeichen im String (inkl. Leerzeichen, Zeilenumbrüche, Satzzeichen).

length_sample_string_sum = length_sample_string_1 + length_sample_string_2
# korrekt

print(length_sample_string_1)
print(length_sample_string_2)
print(length_sample_string_sum)
