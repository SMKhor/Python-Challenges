#	AS01	BUBBLE SORT	Write the Python required for a bubble sort. Test it with 9 randomly assigned numbers.
userlist = input("Enter a list of numbers: ").split()
for i in range(len(userlist)):
    userlist[i] = int(userlist[i])

n = len(userlist)-1
for i in range(len(userlist)-1):
    for j in range(n):
        if userlist[j] > userlist[j+1]:
            temp = userlist[j]
            userlist[j] = userlist[j+1]
            userlist[j+1] = temp
    n = n - 1

print(userlist)
