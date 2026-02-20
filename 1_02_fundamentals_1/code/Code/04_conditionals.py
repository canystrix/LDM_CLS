# *** IF STATEMENTS *** #
# Running code based on the evaluation results of a condition

"""
sample_string_1 = "Hello!"
sample_string_2 = "Hello!"

if sample_string_1 == sample_string_2:
    print("Strings are the same!")
elif sample_string_1.lower() == sample_string_2:
    print("Strings are the same but different case!")
else:
    print("Strings are different!")
"""


# *** IDENTITY OPERATORS *** #
# Checking whether two elements have the same value or are the same object instance

"""
sample_list_1 = ["What", "a", "wonderful", "day"]
sample_list_2 = ["What", "a", "wonderful", "day"]

if sample_list_1 == sample_list_2:
    print("Lists have the same value!")
elif sample_list_1 != sample_list_2:
    print("Lists do not have the same value!")

if sample_list_1 is sample_list_2:
    print("Lists are the same object!")
elif sample_list_1 is not sample_list_2:
    print("Lists are not the same object!")
"""


# *** MEMBERSHIP OPERATORS *** #
# Checking whether or not an element is part of a sequence

"""
sample_list = ["What", "a", "wonderful", "day"]

search_string_1 = "wonderful"
search_string_2 = "terrible"

if search_string_1 in sample_list_1:
    print(f"{search_string_1} is in the list!")
if search_string_2 not in sample_list_1:
    print(f"{search_string_2} is not in the list!")
"""


# *** BOOLEAN OPERATORS *** #
# Chaining conditions together in order to determine whether a piece of code should be run

"""
sample_string = "What a wonderful day!"

sample_string_length = len(sample_string)

min_length = 5
max_length = 50

if sample_string_length > min_length and sample_string_length < max_length:
    print("Word count ok!")
elif sample_string_length < min_length:
    print("Word count too low!")
else:
    print("Word count too high!")
"""
