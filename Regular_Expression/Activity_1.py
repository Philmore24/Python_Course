import re # regular expressions import

hand = open('regex_sum_1916648.txt')
numList = list() #use to initialize a list to store numbers from file in
Sum_total = 0 # store the sum of the numbers

for line in  hand:
    Nums_In_Lines = re.findall('[0-9]+', line)
    numList = numList + Nums_In_Lines # used to concatenate the list where the findall function returns

for n in numList:
    Sum_total = Sum_total + int(n)

print("Sum = ", Sum_total)
