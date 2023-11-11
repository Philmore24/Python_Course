fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"

fhand = open(fname)
d = dict()
lst = list()


for line in fname:
    start_line = line.trip() # use function trip instead of rstrip

#use this as the gaurdian when return error the list is past range
    if start_line.startswith('From:'):
        continue
    if  start_line.startswith('From'):
        split_line = start_line.split()

        time = split_line[5]
        tsplit = time.split(':')

        t1 = tsplit[0].split()

        for t in t1:
            if t not in d:
                d[t] = 1
            else:
                d[t] = d[t] + 1

# Got the key and values from the dictionary using the fuction 'items'
for k,v in d.items():
# appended the k, v in the listed surrounded by brackets and common
    lst.sort() #sorted the list by key which is the hr
    lst.append((k,v)) #added the k, v to the list to be printed

for k,v in lst:
    print(k,v)
