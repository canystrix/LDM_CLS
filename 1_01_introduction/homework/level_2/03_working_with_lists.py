# *** LEVEL 1 - ARBEITEN MIT LISTEN *** #
# Listen bieten uns eine praktische Möglichkeit, mehrere Elemente in einer Variable zu speichern.
# Das ist zum Beispiel nützlich, wenn wir nicht mit einem ganzen Satz arbeiten wollen, sondern seinen Bestandteilen.
# Im Folgenden finden Sie einen String, an dem wir unterschiedliche Operationen ausführen wollen:

sample_string = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects."""


# AUFGABE 1
# Spalten Sie den String in einzelne Wörter und speichern Sie das Ergebnis in sample_words!

# sample_words = []

sample_words = sample_string.split()
# Split the string into individual words using Python's split() method without arguments

print(sample_words)

# Spalten Sie den String zusätzlich in einzelne Sätze, die Sie in sample_sentences speichern!

# sample_sentences = []

sample_sentences = sample_string.split(".")
# Split the string into individual sentences using the period character as the delimiter

print(sample_sentences)


# AUFGABE 3
# Ermitteln Sie die Anzahl der Zeichen, Wörter und Sätze von sample_string!
# Die Zeichen manuell zu zählen ist dabei natürlich nicht erlaubt!

# sample_string_chars_count = 0
# sample_string_sentence_count = 0
# sample_string_word_count = 0

sample_string_chars_count = len(sample_string)
sample_string_sentence_count = len(sample_sentences)
sample_string_word_count = len(sample_words)
# Use the len() function to count characters in the string and the number of elements in each list

print(sample_string_chars_count)
print(sample_string_sentence_count)
print(sample_string_word_count)


# AUFGABE 2
# Ersetzen Sie das erste Element von sample_words durch einen beliebigen String!

# sample_words

sample_words[0] = "Python 3"
# Replace the first element (index 0) of the list with a new string value

print(sample_words)


# Entfernen Sie das letzte Element von sample_words!

# sample_words

sample_words.remove("projects.")
# Use the remove() method to delete a specific element from the list

print(sample_words)


# Fügen Sie am Ende von sample_words ein neues Element hinzu!

# sample_words

sample_words.append("append")
# Use the append() method to add a new element at the end of the list

print(sample_words)



# AUFGABE 4
# Setzen Sie die sample_words und sample_sentences wieder zu einem String zusammen!
# joined_sentences und joined_words sollten am Ende den Datentyp str haben!

# joined_sentences = ""
# joined_words = ""

joined_sentences = ", ".join(sample_sentences)
joined_words = ", ".join(sample_words)
# Use the join() method to combine list elements into a single string with a delimiter

joined_sentences_type = type(joined_sentences)
joined_words_type = type(joined_words)

print(joined_sentences)
print(joined_words)

