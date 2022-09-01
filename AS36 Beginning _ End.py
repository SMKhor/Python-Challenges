	#AS36	BEGINNING & END 	Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
    #makes a new list of only the first and last elements of the given list.

userlist = input("Enter a list of numbers: ").split()
for i in range(len(userlist)):
    userlist[i] = int(userlist[i])

new_list = []
new_list.append(userlist[0])
new_list.append(userlist[len(userlist)-1])
print(new_list)
