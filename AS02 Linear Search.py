#	AS02	LINEAR SEARCH	Write the Python required to do a linear search of Python in an array
userlist = input("Enter a list of numbers: ").split()
item = input("Enter the item you're searching for: ")
check = False
for i in range(len(userlist)):
    if item == userlist[i]:
        print("Item", item, "has the index of",str(i))
        check = True

if check == False:
    print("Sorry, Item",item,"could not be found in this array.")
