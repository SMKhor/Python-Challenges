#	A223	NEAT FROM 101 TO 1000	Find all the "neat" 3 digit numbers beginning with 101 up to 1000.
#   A "neat" number is a positive integer which is divisible by the sum of it's digits.
#  The number 720 is a neat number because 7+0+2 = 9 which is a divisor of 720.

num_list = []
neat_list = []

for i in range(101,1000):
    num_list.append(i)

for i in range(899):
    check = num_list[i]
    summy = 0
    for digit in str(check):
      summy += int(digit)
    divisible = int(check) % summy
    if divisible == 0:
        neat_list.append(check)

print("Neat Numbers: ")
print(neat_list)
