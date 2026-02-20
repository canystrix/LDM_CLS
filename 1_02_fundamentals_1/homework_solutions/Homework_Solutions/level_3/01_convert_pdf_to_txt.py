# *** LEVEL 3 - PDF IN TXT KONVERTIEREN *** #

# HINWEIS: Ursprünglich wurde für diese Aufgabe die textract-Bibliothek verwendet.
# Diese musste jedoch durch pypdf ersetzt werden, da textract komplexe externe
# Systemabhängigkeiten hat, die auf unseren Computern schwierig zu installieren sind.
#
# Stattdessen nutzen wir jetzt die pypdf-Bibliothek. Sie ist eine reine Python-Bibliothek
# ohne externe Systemabhängigkeiten und lässt sich problemlos installieren.
#
# Einschränkung von pypdf im Vergleich zu textract:
# - pypdf kann KEINE OCR durchführen (keine gescannten PDFs oder Bilder erkennbar)
# - pypdf verarbeitet nur PDFs (textract kann auch DOCX, DOC, RTF, etc.)
# textract würde mehr Funktionalität bieten, aber die Installation ist deutlich aufwändiger.
# Daher verwenden wir pypdf für diese Lerneinheit.

# INSTALLATION DES PAKETS:
# Wenn du diesen Code ausführst, wirst du einen Fehler sehen.
# Er bedeutet, dass das pypdf-Paket noch nicht installiert ist.
# Um es zu installieren:
# 1. Hovere über "PdfReader" in der Zeile 41 (der Text mit der roten Wellenlinie)
# 2. Rechtsklick auf "PdfReader"
# 3. Klicke auf "Show Context Actions"
# 4. Klicke auf "Install package pypdf" (oder ähnlich)
# Das IDE installiert das Paket automatisch für dich!
#
# Alternativ kannst du auch im Terminal eingeben: pip install pypdf



# Aufgabe
# Im Unterverzeichnis "files" befindet sich eine PDF-Beispieldatei
# Erstellen wir eine Funktion zum Lesen des Inhalts von sample.pdf und zum Schreiben
# in eine neue Datei namens output.txt
# Speichern wir diese neue Datei im Unterverzeichnis "files"
# Die Funktion soll nur den Pfad von sample.pdf als Argument nehmen
# Jeder Satz aus der ursprünglichen PDF-Datei sollte in einer neuen Zeile in der
# finalen TXT-Datei geschrieben werden!

# TODO: Schreibe hier deinen Code! Du kannst diesen Kommentar gerne löschen!

from pypdf import PdfReader
# import lädt externe Bibliotheken (Module), die zusätzliche Funktionalität bereitstellen
# pypdf ist eine reine Python-Bibliothek zum Lesen und Verarbeiten von PDF-Dateien
# from pypdf import PdfReader bedeutet: Importiere die Klasse PdfReader aus dem pypdf-Modul
# Wir werden im nächsten Modul mehr über Imports lernen!

path = "./files/sample.pdf"
# Wir speichern den Pfad zur PDF-Datei in einer Variable
# ./ bedeutet "aktuelles Verzeichnis", dann gehen wir in den Ordner "files"


def pdf_to_txt(pdf_path):
    # Diese Funktion konvertiert eine PDF-Datei in eine TXT-Datei
    # Parameter: pdf_path - der Pfad zur PDF-Datei, die konvertiert werden soll

    reader = PdfReader(pdf_path)
    # PdfReader() öffnet und liest die PDF-Datei

    text = ""
    # Wir erstellen einen leeren String, in dem wir den gesamten Text sammeln werden

    for page in reader.pages:
        # Wir iterieren über jede Seite in der PDF
        text += page.extract_text()
        # extract_text() extrahiert den Text von der aktuellen Seite

    # Wir teilen den Text in Sätze auf und fügen jeden auf einer neuen Zeile ein
    sentences = text.split('. ')
    text = '\n'.join(sentences)
    # Jeder Satz steht jetzt auf einer eigenen Zeile

    output_dir = './files/'
    # Das Zielverzeichnis (Folder), in dem die neue Datei gespeichert werden soll

    output_file = 'output.txt'
    # Der Name der neuen Datei, die wir erstellen werden

    file = open(output_dir + output_file, 'w')
    # Wir öffnen die Datei im Schreibmodus ('w')
    # output_dir + output_file kombiniert die Strings: './files/' + 'output.txt' = './files/output.txt'
    # Diese neue Datei wird erstellt, falls sie nicht existiert

    file.write(text)
    # Wir schreiben den extrahierten Text (mit Sätzen auf neuen Zeilen) in die Datei

    file.close()
    # Wir schließen die Datei - sehr wichtig! Erst dann wird alles gespeichert


pdf_to_txt(path)
# Wir rufen die Funktion auf und übergeben den Pfad zur PDF-Datei
# Die Funktion wird ausgeführt und erstellt die output.txt Datei

# HINWEIS: pypdf gibt manchmal Warnungen wie "Ignoring wrong pointing object..."
# aus. Dies sind nur informative Meldungen über Formatierungsprobleme in der PDF-Datei
# und verhindern nicht, dass der Code funktioniert. Die Warnung kann man ignorieren!

# Weitere Informationen:
# https://realpython.com/python-import/#basic-python-import
# https://pypdf.readthedocs.io/en/stable/
