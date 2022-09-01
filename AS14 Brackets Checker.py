#Create a program to make sure that the number of brackets is balanced.
brackk = input("Enter the brackets to check: ")
left = 0
right = 0
check = ""

for i in range(len(brackk)):
    char = brackk[i]
    if char == "(":
        left = left + 1
    if char == ")":
        right = right + 1

print("Number of ( : ", left)
print("Number of ) : ", right)

if left == right:
    check = "balanced"
else:
    check = "not balanced"

print("Number of brackets is", check)
