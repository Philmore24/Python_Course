fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"

fhand = open(fname)
d = dict()
lst = list()


for line in fname:
    start_line = line.strip()

    if  start_line.startswith('From'):
        spline = start_line.split()

        time = spline[5]
        tsplit = time.split(':')

        t1 = tsplit[0].split()

        for t in t1:
            if t not in d:
                d[t] = 1
            else:
                d[t] = d[t] + 1

for k,v in d.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)
