#	AS76	MINIMUM DIFFERENCE	Output the minimum differences between any two numbers in an array:
#Lets the user input an array and converts the values from string to integer
userint = input("Array: ").split()
for i in range(len(userint)):
    userint[i] = int(userint[i])

def mindifference(x):
    minny = 100000000
    for i in range(len(x)-1):
        for j in range(len(x)-1-i):
            num1 = x[i]
            num2 = x[j+i+1]
            difference = abs(num2 - num1)
            if difference < minny:
                minny = difference
    return print("Minimum difference:", minny)

mindifference(userint)
