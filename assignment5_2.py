
#5.2
#Print the larget and small integer entered by the user until enter 'done'

largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        intval= int(num)
    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = intval
    elif intval < smallest:
       smallest = intval

    elif intval > largest:
       largest = intval

print("Maximum is", largest)
print("Minimum is", smallest)
