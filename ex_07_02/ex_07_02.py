''''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce
 an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count= 0  # keeps tracks of the count
total = 0.0 # stores the sum of the float values initialize to 0.0 for FLOAT
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
     # ipos = index postition in the part_string
     # used the find function to look for the character in the line and store postition(index #)
    ipos = line.find(':')
    #starting from the postition stored + 1 to the next string and keep on going
    #starting with + 1 remove the ':' from the return value
    piece = line[ipos+1:]
    #converted the string into float so calculations on it can be done
    Line_value = float(piece)
    count = count + 1
    total = float(total + Line_value)
    average_num = float(total / count)
print("Average spam confidence:",average_num)
