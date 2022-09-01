import random
numbers = []
mean = 0
total = 0

for i in range(50):
    randomnum = random.randint(0,1000)
    numbers.append(randomnum)

maxvalue = numbers[0]
minvalue = numbers[0]

for i in range(50):
    if numbers[i] > maxvalue:
        maxvalue = numbers[i]
    if numbers[i] < minvalue:
        minvalue = numbers[i]
    total = total + numbers[i]
    mean = total/(len(numbers))


print("List: ", numbers)
print("Minimum:", minvalue)
print("Maximum:", maxvalue)
print("Mean average:", mean)
