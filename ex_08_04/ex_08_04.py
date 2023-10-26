
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
   print(line.rstrip())

      #solution 1
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

      #solution 2
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for i in line.split():
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)