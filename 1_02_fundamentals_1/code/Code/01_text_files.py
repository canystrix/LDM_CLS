# *** READING TEXT FILES *** #
# Opening plain text files and reading their contents

"""
file_path = "sample_en.txt"
file_object = open(file_path)
file_content = file_object.read()
file_object.close()

print(file_content)
"""


# *** WRITING TEXT FILES *** #
# Creating a new plain text file and writing data to it

"""
new_file_content = "Hello world!"
file_path = "sample_output.txt"
file_object = open(file_path, "w")
file_object.write(new_file_content)
file_object.close()
"""


# *** APPENDING TO TEXT FILES *** #
# Adding contents to an existing plain text file

"""
new_file_content = "Hello world!"
file_path = "sample_output.txt"
file_object = open(file_path, "a")
file_object.write(new_file_content)
file_object.close()
"""