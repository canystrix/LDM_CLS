# *** LEVEL 2 - ARBEITEN MIT LISTEN *** #
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
# split() ohne Argument trennt den String an Whitespace (Leerzeichen, Zeilenumbrüche, Tabs).
# Das Ergebnis ist eine Liste mit einzelnen Wörtern.

print(sample_words)

# Spalten Sie den String zusätzlich in einzelne Sätze, die Sie in sample_sentences speichern!

# sample_sentences = []
sample_sentences = sample_string.split(".")
# split(".") trennt den String an jedem Punkt. Das Ergebnis ist eine Liste mit einzelnen Sätzen.

print(sample_sentences)


# AUFGABE 2
# Ersetzen Sie das erste Element von sample_words durch einen beliebigen String!

# sample_words
sample_words[0] = "JavaScript"
# [0] ist der Index des ersten Elements der Liste (die Zählung beginnt bei 0, nicht bei 1).
# Mit = weisen wir einen neuen Wert zu. So ändern wir das erste Wort in der Liste.

print(sample_words)

# Entfernen Sie das letzte Element von sample_words!

# sample_words
sample_words.pop()
# pop() ohne Argument entfernt das letzte Element der Liste und gibt es zurück.

print(sample_words)

# Fügen Sie am Ende von sample_words ein neues Element hinzu!

# sample_words
sample_words.append("new_word")
# append() fügt ein Element am Ende der Liste hinzu.

print(sample_words)


# AUFGABE 3
# Ermitteln Sie die Anzahl der Zeichen, Wörter und Sätze von sample_string!
# Die Zeichen manuell zu zählen ist dabei natürlich nicht erlaubt!

# sample_string_chars_count = 0
sample_string_chars_count = len(sample_string)
# len() zählt alle Zeichen im String (inkl. Leerzeichen, Zeilenumbrüche, Satzzeichen).

# sample_string_sentence_count = 0
sample_string_sentence_count = len(sample_sentences)
# len() auf eine Liste gibt die Anzahl der Elemente zurück.
# Achtung: Falls der String mit "." endet, ist das letzte Element leer.

# sample_string_word_count = 0
sample_string_word_count = len(sample_words)
# len() auf eine Liste gibt die Anzahl der Elemente zurück.

print(sample_string_chars_count)
print(sample_string_sentence_count)
print(sample_string_word_count)


# AUFGABE 4
# Setzen Sie die sample_words und sample_sentences wieder zu einem String zusammen!
# joined_sentences und joined_words sollten am Ende den Datentyp str haben!

# joined_sentences = ""
joined_sentences = ".".join(sample_sentences)
# join() verbindet alle Listenelemente mit "." als Trennzeichen zu einem String.
# Das ist das Gegenteil von split() - wir machen aus einer Liste wieder einen String.

# joined_words = ""
joined_words = " ".join(sample_words)
# s.o.

joined_sentences_type = type(joined_sentences)
joined_words_type = type(joined_words)

print(joined_sentences)
print(joined_words)
