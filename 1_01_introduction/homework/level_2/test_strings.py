#!/usr/bin/env python
# -*- coding: utf-8 -*-

sample_string_1 = """Python is an interpreted, high-level and general-purpose programming language. 
Python's design philosophy emphasizes code readability with its notable use of significant indentation."""

sample_string_2 = """Its language constructs and object-oriented approach aim to help programmers write clear, 
logical code for small and large-scale projects."""

sample_string_combined = sample_string_1 + " " + sample_string_2

first_space_index = sample_string_combined.index(" ")
print("First space index:", first_space_index)

first_word = sample_string_combined[0:first_space_index]
print("First word:", first_word)

length_sample_string_1 = len(sample_string_1)
length_sample_string_2 = len(sample_string_2)
length_sample_string_sum = length_sample_string_1 + length_sample_string_2

print("Length of string 1:", length_sample_string_1)
print("Length of string 2:", length_sample_string_2)
print("Total length:", length_sample_string_sum)

print("\nALL TASKS COMPLETED SUCCESSFULLY!")

