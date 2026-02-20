# *** WHILE LOOPS *** #
# Looping through a block of code until a condition is no longer met

"""
sample_list = ["What", "a", "wonderful", "day", "what", "a", "beautiful", "day"]

sample_list_len = len(sample_list)

while sample_list_len > 0:
    print(sample_list[0-sample_list_len])
    sample_list_len -= 1
"""


# *** BREAK STATEMENTS *** #
# Leaving a loop immediately

"""
sample_list = ["What", "a", "wonderful", "day", "what", "a", "beautiful", "day"]

sample_list_len = len(sample_list)

while sample_list_len > 0:
    print(sample_list[0-sample_list_len])
    break
    sample_list_len -= 1
"""


# *** FOR LOOPS *** #
# Iterating over a set number of elements until the last element is reached

"""
sample_list = ["What", "a", "wonderful", "day", "what", "a", "beautiful", "day"]

for list_item in sample_list:
    print(list_item)
"""


# *** SETS *** #
# A complex data type holding an unordered collection of unique elements

"""
sample_list = ["What", "a", "wonderful", "day", "what", "a", "beautiful", "day"]

unique_words = set()

for list_item in sample_list:
    unique_words.add(list_item)

print(unique_words)
"""


# *** CONTINUE STATEMENTS *** #
# Jumping to the next iteration of a loop

"""
sample_list = ["What", "a", "wonderful", "day", "what", "a", "beautiful", "day"]

unique_words = set()

for list_item in sample_list:
    continue 
    unique_words.add(list_item)

print(unique_words)
"""
