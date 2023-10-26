

fname = input("Enter file:")
if len(fname) < 1:
    fname= "mbox-short.txt"
fhand = open(fname)
dict_list = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    #print(wds)
    for word in words:
        if len(word) < 1:
            continue
        if words[0] != 'From:':
           continue
        if words[1] in dict_list:
            dict_list[word] = dict_list[word] + 1
        else:
            dict_list[word] = 1

            #print("This is NEW")

# now we want to find the most common word
Largest_count = 0
Key_word = None
for k,v in dict_list.items():
    if v > Largest_count:
        Largest_count = v
        Key_word = k  # captures/remember the word that was largest
print(Key_word,Largest_count)
