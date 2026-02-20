# *** LEVEL 3 - WORTVERTEILUNG *** #
# Im Folgenden finden Sie einen einzelnen, aber langen String.

sample_text = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected. 
It supports multiple programming paradigms, including structured (particularly, procedural), 
object-oriented and functional programming. Python is often described as a "batteries included" language due to its 
comprehensive standard library. Guido van Rossum began working on Python in the late 1980's, 
as a successor to the ABC programming language and first released it in 1991 as Python 0.9.1. 
Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system 
using reference counting and was discontinued with version 2.7.18 in 2020. Python 3.0 was released in 2008 and was a 
major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified 
on Python 3."""


# AUFGABE
# Ermitteln Sie, wie oft jedes Wort im String auftaucht!
# Speichern Sie diese Informationen in einem Dictionary und geben Sie sie mit der Print-Funktion aus!
# VORSICHT! Um diese Aufgabe lösen zu können, benötigen Sie neue Konzepte, nämlich For-Schleife und Bedingungen.
# Dieses wurde noch nicht im Kurs behandelt! Wir werden uns allerdings im nächsten Modul mit ihnen beschäftigen.
# Machen Sie sich also keine Sorgen, wenn Sie diese Aufgabe noch nicht lösen können!
# Falls Sie es dennoch versuchen möchten, können Sie sich unter folgendem Link über beide Themen informieren:
# https://realpython.com/python-for-loop/
# https://realpython.com/python-conditional-statements/

# distribution = dict()

words = sample_text.lower().split()
# Split the text into individual words and convert to lowercase for case-insensitive counting

distribution = dict()
for word in words:
    clean_word = word.strip('.,!?;:\'"')
    # Remove punctuation from each word to ensure accurate word counting

    if clean_word in distribution:
        distribution[clean_word] += 1
    else:
        distribution[clean_word] = 1
# Use a for loop to iterate through all words and build a dictionary where each word is a key and its
# frequency is the value

print(distribution)
