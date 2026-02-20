# *** LEVEL 2 - ARBEITEN MIT STRINGS *** #
# Bei der natürlichen Sprachverarbeitung liegt unser Hauptaugenmerk natürlich auf Strings.
# Strings bieten uns unterschiedliche Möglichkeiten, mit ihnen zu interagieren und sie zu manipulieren.
# Im Folgenden finden Sie zwei Strings, an denen wir unterschiedliche Operationen ausführen wollen.

sample_string_1 = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation."""

sample_string_2: str = """Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects."""


# AUFGABE 1
# Kombinieren Sie sample_string_1 und sample_string_2 und speichern Sie das Ergebnis in sample_string_combined.
# Achten Sie darauf, dass die beiden Sätze in sample_string durch ein Leerzeichen getrennt werden!

# sample_string_combined = ""

sample_string_combined = sample_string_1 + " " + sample_string_2
# Concatenate the two strings with a space between them using the + operator


# AUFGABE 2
# Finden Sie den Index des ersten Leerzeichens in sample_string_combined.
# Nutzen Sie dafür eine von Pythons eingebauten Stringmethoden!


# first_space_index = 0

first_space_index = sample_string_combined.index(" ")
# Use Python's built-in .index() method to find the position of the first space character

print(first_space_index)


# AUFGABE 3
# Nutzen sie den Index des ersten Leerzeichens, um durch Slicing das erste Wort des Strings zu erhalten!

# first_word = sample_string_combined

first_word = sample_string_combined[0:first_space_index]
# Use string slicing to extract characters from the start (0) up to the first space index

print(first_word)


# AUFGABE 4
# Finden Sie heraus, wieviele Zeichen in sample_string_1 und sample_string_2 enthalten sind!
# Speichern Sie die Ergebnisse in length_sample_string_1, length_sample_string_2 und length_sample_string_sum!

# length_sample_string_1 = 0
# length_sample_string_2 = 0

length_sample_string_1 = len(sample_string_1)
length_sample_string_2 = len(sample_string_2)
# Use the built-in len() function to count the number of characters (including spaces and newlines) in each string

print(length_sample_string_1)
print(length_sample_string_2)

# length_sample_string_sum = length_sample_string_1 + length_sample_string_2

length_sample_string_sum = length_sample_string_1 + length_sample_string_2
# Add both lengths together to get the total character count

print(length_sample_string_sum)