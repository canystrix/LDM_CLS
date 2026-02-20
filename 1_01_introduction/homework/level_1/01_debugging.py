# *** LEVEL 1 - DEBUGGING *** #
# Der folgende Code enthält einige absichtlich eingebaute Fehler.
# Nutzen Sie die Traceback-Nachrichten und das PyCharm Syntax-Highlighting um diese Fehler zu finden und zu beheben!
# Erklären Sie außerdem in Kommentaren, wodurch der Fehler ausgelöst wird!
# Die Aufgabe ist erfolgreich abgeschlossen, wenn beim Ausführen des Codes keine Fehler auftreten.


# AUFGABE 1 - VARIABLEN

int = 1
float = 1.0
boolean = True
var_lambda = 11

# "lambda" is a Python keyword for anonymous functions, so it should not be used as a variable name; rename it.

sample_int = 1
sample_int = 2
sample_int != 3
# Use != for inequality; the incorrect token =! would raise a SyntaxError.
sample_int == 4
# The equality operator is '==' (two equal signs). A single '=' is assignment, not comparison.

sample_string = "hello world!"
sample_string = 'hello world!'
sample_string = "hello world!"
# Opening and closing quotation marks must match (single, double or triple quotes).
sample_string = """hello world!"""
sample_string = "hello world!"
# A missing closing quotation mark would cause a SyntaxError.
sample_string = "hello world!"
# Punctuation like '!' must be inside the quotes to be part of the string.
sample_string = "hello world!"
sample_string = "hello world!"
sample_string = "hello world!"

sample_list = [1, 2, 3, 4, 5]
sample_list = [1, 2, 3, 4, 5.5]
sample_list = [1.2, 2, 03.22, 4, 5]
# Numeric literals must be valid: leading zeros and incorrect decimals will cause errors.
sample_list = [1.123, 2.434, 3.334, 4.343, 5.552]
sample_list = ["Hello", "world!"]
sample_list = ["Hello", "world!", "Nice", "to", "meet", "you!"]
sample_list = ["Hello", "world!", "Nice", "to", "meet", "you", 2, "!"]
sample_list = ["Hello", "world!", ["Nice", "to", "meet", "you", 2, "!"]]
sample_list = [["Hello", "world!"], ["Nice", "to", "meet", "you", 2, "!"]]
# An extra or missing bracket will cause a SyntaxError.
sample_list = [["Hello", "world!"], ["Nice", ["to", "meet"], "you", 2, "!"]]

sample_dict = {"Hello": 1, "world!": 2}
sample_dict = {"Hello": 1, "world!": 2, "Hi": 1, "John!": 3.5}
# Use a decimal point (.) in floating-point literals, not a comma.
sample_dict = {"Hello": 1, "world!": 2, "Hi": 1, "John!": 3.5}
sample_dict = {"Hello": 1, "world!": 2, "Hello": 1, "John!": 3.5}


# AUFGABE 2 - EINGEBAUTE FUNKTIONEN

# sample_int_length = len(sample_int)
# len() does not work on integers; it expects a sequence (like a string, list or dict).
sample_string_length = len(sample_string)
sample_list_length = len(sample_list)
sample_dict_length = len(sample_dict)

print(sample_int)
print(sample_string)
# The print() function requires parentheses in Python 3.
print(sample_list)

type(sample_string)
type(sample_dict)
#type(sample_string + sample_int)
type(sample_string + "sample_int")
### You cannot concatenate a string and an integer directly; convert the int to str() first.
#! --> type(sample_string + str(sample_int))

# AUFGABE 3 - EINGEBAUTE METHODEN

"Hello world!".split()
"Hello world!".split()
# split() accepts a string separator or None, not an integer.
"Hello, World".split()
# You can only split strings, not lists (split() is a string method).

[1, 2, 3, 4, 5].sort()
[1, 2, 3.3, 4, 5].sort()
[1, 2, 3.3, 4.22, 5].sort()
# list.sort() sorts the list in place and returns None; use sorted() if you need a new list.
[1, 2, 3.3, 4.22, 5*2].sort()
["Hello", "world!"].sort()
["Hello", "world!", "Nice", "to", "meet", "you!"].sort()
["Hello", "world!", "Nice", "to", "meet", "you", "2"].sort()
["Hello", "world!", "Nice", "to", "meet", "you!", "2"].sort()
# You cannot sort a list containing both strings and integers in Python 3 (incompatible types).


# AUFGABE 4 - INDEX OPERATIONEN

sample_string[0]
# Use square brackets for indexing: obj[index]. Parentheses would be a call, not indexing.
sample_string[-1]
sample_string[5]
sample_string[3]
# Accessing an index that does not exist raises an IndexError.

sample_list[0]
sample_list[-1]
# Make sure bracket pairs match when indexing nested structures; mismatched brackets cause SyntaxError.
sample_list[1]
# Accessing an index that does not exist raises an IndexError.
sample_list[1]

sample_string[0:2]
sample_string[:]
# Slicing uses the syntax obj[start:stop:step]; ensure variable names and case are correct (Python is case-sensitive).

#sample_string[len(sample_string)]
sample_string[:len(sample_string)]
# Slicing out of range does not raise an error; it just returns a shorter string.
## Falsch! 1. Kann nicht out of range sein da len
##         2. Es sind genau 5 Zeichen

sample_list[0:2]
sample_list[:]
sample_list[:len(sample_list)]