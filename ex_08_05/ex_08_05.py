fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    word_list = line.split()
    #print(word_list)

    # Call this a Gaurdian that checks and skip if conflict
    if len(word_list) < 1:
        continue
    if word_list[0] != 'From:':
       continue
    count = count + 1
    print(word_list[1])


print("There were", count, "lines in the file with From as the first word")
