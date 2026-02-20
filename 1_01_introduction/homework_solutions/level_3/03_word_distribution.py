# *** LEVEL 3 - WORTVERTEILUNG *** #
# Im Folgenden finden Sie einen einzelnen, aber langen String.

sample_text = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected. 
It supports multiple programming paradigms, including structured (particularly, procedural), 
object-oriented and functional programming. Python is often described as a "batteries included" language due to its 
comprehensive standard library. Guido van Rossum began working on Python in the late 1980's, 
as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.1. 
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
# .lower() wandelt alle Großbuchstaben in Kleinbuchstaben um.
# Das ist wichtig, damit wir "Python", "PYTHON" und "python" als dasselbe Wort zählen.
# .split() teilt den Text dann in einzelne Wörter auf (trennt wieder bei Leerzeichen).
# Das Ergebnis ist eine Liste aller Wörter, die wir in der Variable "words" speichern.

distribution = {}
# Wir erstellen ein leeres Dictionary {}.
# Das ist wie eine Tabelle: In jeder Reihe speichern wir ein Wort und einen Zähler.
# Der Zähler zeigt, wie oft das Wort im Text vorkommt.
# Beispiel: "Python" : 6 bedeutet, das Wort "Python" kommt 6-mal vor.
# Anfangs ist das Dictionary leer, wir werden es mit jedem Wort füllen.

for word in words:
# Diese for-Schleife durchläuft jedes Wort in der Liste "words" nacheinander.
# Die Variable "word" enthält jeweils das aktuelle Wort, das wir gerade verarbeiten.

    word = word.rstrip('.,!?;:')
    # .rstrip() entfernt Satzzeichen am Ende des Wortes (., , ! ? ; :)
    # Das ist wichtig, weil "Python." und "Python" sonst als verschiedene Wörter gezählt werden.
    # Wir überschreiben die Variable "word" mit der bereinigten Version.

    if word in distribution:
    # Diese Bedingung prüft, ob das Wort schon als Schlüssel im Dictionary existiert.
    # "in" prüft, ob etwas vorhanden ist.
    # Wenn "ja" (True): führe den nächsten Block aus.

        distribution[word] = distribution[word] + 1  # Langform
        # Ginge auch kürzer >>> distribution[word] += 1
        # += bedeutet "addiere 1 dazu".
        # Wir erhöhen den Zähler des Wortes um 1.
        # Das bedeutet: Wir haben das Wort ein weiteres Mal gefunden, also zählen wir es.

    else:
    # "else" bedeutet:
    # Wenn das Wort nicht im Dictionary existiert, führe diesen Block aus.

        distribution[word] = 1
        # Wir fügen das Wort zum Dictionary hinzu und setzen seinen Zähler auf 1.
        # Das bedeutet: Wir haben dieses Wort zum ersten Mal gefunden, also ist der Zähler 1.

print(distribution)
