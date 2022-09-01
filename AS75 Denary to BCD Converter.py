#Write a piece of code which asks the user to input a denary number and outputs the Binary Coded Decimal conversion of it.
denary = input("Denary number to convert to BCD: ")
length = len(denary)
output = ""

for i in range(length):
    digit = denary[i]
    if digit == "0":
        binary = "0000 "
    if digit == "1":
        binary = "0001 "
    if digit == "2":
        binary = "0010 "
    if digit == "3":
        binary = "0011 "
    if digit == "4":
        binary = "0100 "
    if digit == "5":
        binary = "0101 "
    if digit == "6":
        binary = "0110 "
    if digit == "7":
        binary = "0111 "
    if digit == "8":
        binary = "1000 "
    if digit == "9":
        binary = "1001 "
    output = output + binary

print("Binary Coded Decimal version: ", output)
