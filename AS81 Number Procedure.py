#AS81	NUMBER PROCEDURE	Create a procedure that outputs the sum and product of all the numbers in a list
#Lets the user input an array and converts the values from string to integer
userint = input("Array: ").split()
for i in range(len(userint)):
    userint[i] = int(userint[i])

def calculate(x):
    sum1 = sum(x)
    product = 1
    for i in range(len(x)):
        product = product*x[i]
    print("Sum of all the numbers:",sum1)
    print("Product of all the numbers:",product)

calculate(userint)
