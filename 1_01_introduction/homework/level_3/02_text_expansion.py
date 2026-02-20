# *** LEVEL 3 - TEXTAUSDEHNUNG*** #
# Im Folgenden finden sie zwei Strings mit unterschiedlicher Länge.
# Der erste String ist der Ausgangstext einer Übersetzungseinheit aus einem Translation Memory,
# der zweite String ist der dazugehörige Zieltext.

source_text = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects."""
target_text = """Python - интерпретируемый, высокоуровневый и универсальный язык программирования. 
Философия дизайна Python делает акцент на удобочитаемость кода с заметным использованием значительных отступов. 
Его конструкции языка и объектно-ориентированный подход направлены на то, 
чтобы помочь программистам писать понятный, логичный код для небольших и крупных проектов."""


# AUFGABE
# Ermitteln Sie die Textausdehnung zwischen Ausgangstext und Zieltext,
# also, um wieviel Prozent der zweite String länger ist, als der erste.
# Auch hier gilt: Verwenden Sie nur die Mittel, die im ersten Modul behandelt wurden!

# difference = 0

source_length = len(source_text)
target_length = len(target_text)
# Use the len() function to determine the character count of both strings

difference = ((target_length - source_length) / source_length) * 100
# Calculate the percentage difference: subtract source length from target length, divide by source length and multiply
# by 100 to get the expansion percentage

print(difference)