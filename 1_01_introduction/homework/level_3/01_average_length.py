# *** LEVEL 3 - TEXTAUSDEHNUNG *** #
# Im Folgenden finden sie drei Strings mit unterschiedlicher Länge in einer Liste.
# Die drei Strings repräsentieren Ausgangssegmente eines Translation Memory.
# Sie wurden zuerst ausgelesen und dann als Liste gespeichert.

source_segments = ["""Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects.""",
                   """Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, 
including structured (particularly, procedural), object-oriented and functional programming. 
Python is often described as a "batteries included" language due to its comprehensive standard library.""",
                   """Guido van Rossum began working on Python in the late 1980's, 
as a successor to the ABC programming language and first released it in 1991 as Python 0.9.1. 
Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system 
using reference counting and was discontinued with version 2.7.18 in 2020. Python 3.0 was released in 2008 and was a 
major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified 
on Python 3."""]


# AUFGABE
# Ermitteln Sie die durchschnittliche Zeichenlänge und Wortlänge der drei Strings!
# Schreiben Sie den Code so, dass er auch dann noch funktioniert, wenn der Liste ein Element hinzugefügt wird!

# average_segment_chars = 0
# average_segment_words = 0

total_chars = sum(len(segment) for segment in source_segments)
average_segment_chars = total_chars / len(source_segments)
# Use a generator expression with sum() to calculate total characters, then divide by the number of segments for the average

total_words = sum(len(segment.split()) for segment in source_segments)
average_segment_words = total_words / len(source_segments)
# Use a generator expression with split() to count words in each segment, then divide by the number of segments for the average

print(average_segment_chars)
print(average_segment_words)