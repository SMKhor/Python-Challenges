list = []
n = int(input("Enter number of elements: "))

for i in range(0, n):
    elements = int(input())
    list.append(elements)

def histogram(x):
    for i in range(len(x)):
        print("*" * x[i])

histogram(list)
