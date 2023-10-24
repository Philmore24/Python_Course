"""
7.1 Write a program that prompts for a file name, then opens that file
and reads through the file, and print the contents of the file in upper case.
 Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""


fname = input("Enter file name: ")
fh = open(fname)
#fh = file handler

for line in fh:
    no_blank_line = line.rstrip() # use this to get rid of the nonprinting characters
    # rstrip removes the extra space from the read lines
    print (no_blank_line.upper())
