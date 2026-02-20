# *** LEVEL 2 - WORTHÄUFIGKEITEN ZÄHLEN *** #

# In diesem Verzeichnis befindet sich eine TXT-Beispieldatei.
# Lesen wir den Inhalt von sample.txt als String oder Liste von Absätzen.
# Schreiben wir eine Funktion, um über den Inhalt von sample.txt zu iterieren
# und die Häufigkeit jedes Wortes im Dokument zu zählen.
# Speichern wir jedes einzelne Wort und die Anzahl seiner Vorkommen im Text
# in einem Dictionary!
#
# Beispiel: Wenn das Wort "hello" zweimal im Text gefunden wird und das Wort
# "goodbye" einmal, dann sollte das finale Dictionary so aussehen:
# word_occurrence = {"hello":2, "goodbye":1}
#
# Schreiben wir dieses Dictionary in eine neue Datei namens sample_words.csv
# Die erste Zeile der finalen Datei sollte eine Überschrift sein, die nur "Word"
# und "Occurrences" enthält
# Jedes der Key-Value-Paare in word_occurrences sollte in eine neue Zeile in der
# finalen Datei geschrieben werden.
#
# Die finale Dateistruktur sollte so aussehen:
# Words     Occurrences
# hello     2
# goodbye   1

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

word_occurrence = dict()
# Wir erstellen ein leeres Dictionary, um die Worthäufigkeiten zu speichern
# dict() ist gleichbedeutend mit {}

file = open('./sample.txt')
# Wir öffnen die Datei sample.txt im aktuellen Verzeichnis

text = file.read()
# Wir lesen den gesamten Inhalt als String

file.close()
# Wir schließen die Datei


def count_occurences(text):
    # Diese Funktion zählt, wie oft jedes Wort im Text vorkommt
    # Parameter: text - der String, der analysiert werden soll

    words = text.split()
    # Wir teilen den Text in einzelne Wörter auf

    for word in words:
        # Wir iterieren über jedes Wort in der Liste

        # Wir müssen das Dictionary während der Iteration füllen, deshalb müssen wir
        # prüfen, ob die Wörter bereits darin existieren
        # Wenn ja, wollen wir die Zählung nicht auf 1 zurücksetzen, also verwenden wir
        # eine if-Bedingung, um das nur einmal zu tun
        if word not in word_occurrence:
            # 'not in' prüft, ob das Wort NICHT im Dictionary ist
            # Wenn das Wort neu ist, initialisieren wir es mit dem Wert 1

            word_occurrence[word] = 1
            # Wir erstellen einen neuen Dictionary-Eintrag: Key=Wort, Value=1

        else:
            # Wenn das Wort bereits im Dictionary existiert

            word_occurrence[word] += 1
            # Wir erhöhen den Zähler um 1
            # += 1 ist eine Kurzform für:
            # word_occurrence[word] = word_occurrence[word] + 1

    # Da wir direkt in die globale Variable word_occurrence schreiben,
    # müssen wir nichts zurückgeben


# Der beste Weg, das Dictionary zu konvertieren, ist wahrscheinlich
# eine weitere Funktion
def dict_to_csv(input):
    # Diese Funktion konvertiert ein Dictionary in ein CSV-Format
    # (Comma-Separated Values)
    # Parameter: input - das Dictionary, das konvertiert werden soll
    # Rückgabe: ein String im CSV-Format

    # Um eine CSV-Datei zu erhalten, müssen wir jedes Key-Value-Paar in eine neue
    # Zeile schreiben. Wir müssen auch ein Trennzeichen zwischen Key und Value einfügen
    # und ihnen ein Zeilenumbruchzeichen folgen lassen
    # Wir können andere Trennzeichen verwenden, hier nutzen wir ein Semikolon, da die
    # Wörter Kommas enthalten könnten!
    text = "Words;Occurences\n"
    # Wir beginnen mit der Überschrift (Header)
    # \n fügt einen Zeilenumbruch hinzu

    for key, value in input.items():
        # Wir iterieren über alle Key-Value-Paare im Dictionary
        # .items() gibt uns beide Werte gleichzeitig (Tuple Unpacking)

        text += f"{key};{value}\n"
        # Wir fügen jede Zeile zum Text hinzu
        # += bedeutet: text = text + f"{key};{value}\n"
        # f-String: {key} wird durch das Wort ersetzt, {value} durch die Anzahl
        # ; ist unser Trennzeichen (Semikolon statt Komma)
        # \n sorgt dafür, dass die nächste Zeile in einer neuen Zeile beginnt

    return text
    # Wir geben den fertigen CSV-Text zurück


count_occurences(text)
# Wir rufen die Funktion auf, um die Worthäufigkeiten zu zählen
# Das Ergebnis wird in word_occurrence gespeichert (globale Variable)

text = dict_to_csv(word_occurrence)
# Wir konvertieren das Dictionary in einen CSV-String
# Achtung: Hier überschreiben wir die Variable 'text' mit dem CSV-formatierten Text!

print(text)
# Wir geben den CSV-Text in der Konsole aus (zur Überprüfung)

file = open('./output.csv', 'w')
# Wir öffnen eine neue Datei im Schreibmodus
# Wenn die Datei nicht existiert, wird sie erstellt

file.write(text)
# Wir schreiben den CSV-Text in die Datei

file.close()
# Wir schließen die Datei - sehr wichtig beim Schreiben!

