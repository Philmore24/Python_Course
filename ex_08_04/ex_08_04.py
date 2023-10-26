
fname = input("Enter file name: ")
if len(fname) == 0:
    fname ='romeo.txt'

fh = open(fname)
newList = list()
for line in fh:
   line =line.rstrip()
   words = line.split()
   for word in words:
       if word not in newList:
           newList.append(word)
       elif word in newList:
           continue

newList.sort()
print(newList)
#worked and submitted


fname = input("Enter file name: ")
if len(fname) < 0:
    fname= "romeo.txt"
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

'''
if len(fname) == 0:
    fname = open('romeo.txt')

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
'''
