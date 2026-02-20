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
as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.1. 
Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system 
using reference counting and was discontinued with version 2.7.18 in 2020. Python 3.0 was released in 2008 and was a 
major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified 
on Python 3."""]



# AUFGABE
# Ermitteln Sie die durchschnittliche Zeichenlänge und Wortlänge der drei Strings!
# Schreiben Sie den Code so, dass er auch dann noch funktioniert, wenn der Liste ein Element hinzugefügt wird!


total_chars = 0
# Wir erstellen einen Zähler, der bei 0 startet.
# Hier speichern wir die Gesamtsumme aller Zeichen (daher auch Summenvariable genannt).
# Diese Variable muss vor der Schleife definiert werden.
# Wenn wir sie innerhalb der Schleife definieren würden, würde sie bei jeder Wiederholung
# auf 0 zurückgesetzt.

# average_segment_words = 0
total_words = 0
# Wir erstellen wieder einen Zähler, der bei 0 startet. Dieses Mal für die Gesamtsumme der Wörter.

for segment in source_segments:
# Eine for-Schleife durchläuft eine Sequenz Schritt für Schritt.
    # Ein Iterable ist ein Objekt, über das man Element für Element laufen kann.
    # Listen und Strings sind beispielsweise iterierbar; hier ist source_segments ein Iterable.
    # In der for-Schleife läuft Python nacheinander über jedes Segment.
    # "for segment in source_segments" bedeutet:
    # Nimm nacheinander jedes Element aus der Liste source_segments
    # und speichere es jeweils temporär in der Variable "segment" (den Namen dieser Variable können wir frei wählen).
    # "segment" ist also die Laufvariable der Schleife.
    # Alles, was eingerückt unter der Schleife steht,
    # wird für jedes einzelne Element erneut ausgeführt.

    segment_chars = len(segment)
    # len(segment) zählt, wie viele Zeichen dieser aktuelle Text (String) hat.
    # Das Ergebnis speichern wir in segment_chars.

    total_chars = total_chars + segment_chars
    # Hier addieren wir die Zeichenzahl dieses Textes zur bisherigen Summe.
    # total_chars = total_chars + segment_chars bedeutet: Nimm die alte Summe, addiere die neue Zahl dazu,
    # speichere das Ergebnis zurück. Beim ersten Durchlauf ist die Variable 0, wie außerhalb der Schleife definiert,
    # beim zweiten Durchlauf enthält sie das Ergebnis des ersten Durchlaufs usw.
    # Tipp: Kürzer geht auch:
    # total_chars += segment_chars ist dasselbe wie total_chars = total_chars + segment_chars.
    # Nach jeder Wiederholung der Schleife wird total_chars größer.

    segment_words = segment.split()
    # split() teilt den Text (String) in einzelne Wörter (standardmäßig an Leerzeichen).
    # Das Ergebnis ist eine Liste mit allen Wörtern dieses Textes.
    # Diese Liste speichern wir in der Variable "segment_words".

    number_of_words = len(segment_words)
    # len(segment_words) zählt, wie viele Wörter dieser Text enthält.
    # Das Ergebnis speichern wir in number_of_words.

    total_words = total_words + number_of_words
    # Hier addieren wir die Wortanzahl dieses Textes zur bisherigen Summe.
    # Nach jeder Wiederholung der Schleife wird total_words größer.

# Nach der Schleife haben wir die Gesamtsumme aller Zeichen und Wörter aus allen Texten.

average_segment_chars = total_chars / len(source_segments)
# Jetzt berechnen wir den Durchschnitt.
# total_chars ist die Gesamtsumme aller Zeichen (aus der Schleife oben).
# len(source_segments) zählt, wie viele Segmente (Listenelemente) in der Liste sind (hier: 3).
# Division (/) teilt die Gesamtsumme durch die Anzahl der Texte.
# Das Ergebnis ist die durchschnittliche Länge pro Text in Zeichen.

average_segment_words = total_words / len(source_segments)
# Jetzt berechnen wir den Durchschnitt der Wörter pro Text.
# total_words ist die Gesamtsumme aller Wörter (aus der Schleife oben).
# len(source_segments) zählt, wie viele Segmente (Listenelemente) in der Liste sind (hier: 3).
# Division (/) teilt die Gesamtsumme durch die Anzahl der Texte.
# Das Ergebnis ist die durchschnittliche Anzahl von Wörtern pro Text.

print(average_segment_chars)
print(average_segment_words)