
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
   print(line.rstrip())


fname = input("Enter file name: ") 
fh = open("romeo.txt")
newlist = list ()
for line in fh:
    words = line.split()
    for word in words:
        if word not in newlist :
            newlist.append (word)
        elif word in newlist :
            continue
newlist.sort ()
print (newlist)