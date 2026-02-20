# *** LEVEL 3 - CONVERT PDF TO TXT *** #

# There is one sample PDF file located in the subdirectory "files"
# Create a function for reading the contents of sample.pdf and for writing it into a new file named sample_converted.txt
# Save this new file in the "files" subdirectory
# The function should only take the path of sample.pdf as an argument
# Each sentence from the original PDF file should be written to a new line in the final TXT file!

# TODO: Write your code here! Feel free to delete this comment!

import textract

text = None


# IMPORTANT! To solve this task you will need to use a new concept called "import"
# We have not yet talked about this in the course. However, we will learn more about it in the next module.
# Don't worry if you can't solve this task yet!
# If you want to try it anyway, you can install and then import the requires package "textract" as follows:

# In your terminal window or command line write:
# pip install textract

# Then, in this script, use:
# import textract

# From there you can easily process a wide variety of files!

# For example, to read text from a DOCX file:
# textract.process("sample.docx")

# As you work on this task you will probably notice, that you can't save the text you extracted to a TXT file as is
# You may have to do some research on the string method .decode() to solve this problem!
# If you would like to know more about imports you can refer to the following link:
# https://realpython.com/python-import/#basic-python-import
# If you want to learn more about textract, you can read the official documentation:
# https://textract.readthedocs.io/en/stable/python_package.html
