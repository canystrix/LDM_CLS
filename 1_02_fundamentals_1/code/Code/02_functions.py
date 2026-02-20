# *** DEFINING FUNCTIONS *** #
# Defining and calling a function

"""
def sample_function():
    new_sentence = "hello world!"
    return new_sentence

sample_return_value = sample_function()
print(sample_return_value)
"""


# *** FUNCTION ARGUMENTS *** #
# Adding positional arguments to a function and passing them to the function during the function call

"""
def sample_function(phrase):
    new_sentence = phrase + " world!"
    return new_sentence

sample_return_value = sample_function("Goodbye")
print(sample_return_value)
"""


# *** KEYWORDED ARGUMENTS *** #
# Adding named arguments and default values to a defined function

"""
def sample_function(phrase, name="world!"):
    new_sentence = phrase + " " + name + "!"
    return new_sentence
    
    
sample_return_value = sample_function("Goodbye", name="Jimmy")
print(sample_return_value)
sample_return_value = sample_function("Top of the morning", name="me lads")
print(sample_return_value)
"""


# *** STRING FORMATTING *** #
# Embedding variable values into strings

"""
def sample_function(phrase, name="world!"):
    new_sentence = f"{phrase} {name}!"
    return new_sentence


sample_return_value = sample_function("Goodbye", name="Jimmy")
print(sample_return_value)
sample_return_value = sample_function("Top of the morning", name="me lads")
print(sample_return_value)
"""


# *** DOCSTRINGS *** #
# Adding documentation to a function


# def sample_function(phrase, name="Hello"):
#     """
#     This function takes two string arguments and returns a sentence combined from the first and second argument.
#     :param phrase: A phrase making up the first part of the sentence.
#     :type phrase: str
#     :param name: A phrase making up the second part of the sentence.
#     :type name: str
#     :return: Resulting sentence from the combination of phrase and name.
#     :rtype: str
#     """
#     return f"{phrase} {name}!"
#
# sample_return_value = sample_function("Jimmy", name="Goodbye")
# print(sample_return_value)
# sample_return_value = sample_function("me lads", name="Top of the morning")
# print(sample_return_value)
