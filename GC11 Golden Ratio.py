import math
length = int(input("Enter the length of your painting:"))
phi = (1 + math.sqrt(5)) / 2
height = length / phi

print("The height for the landscape: %.2f" % height)
