# Create a Parity Byte entry system generator that uses even parity.
print("Parity Byte entry system generator that uses even parity")
parity = input("Enter 7 bits which will form an even parity: ")
bits = 0
output = ""

for i in range(7):
    check = parity[i]
    if check == "1":
        bits = bits + 1

if int(bits) % 2 == 0:
    output = parity + "0"
else:
    output = parity + "1"

print("Parity Byte with Even Parity: ", output)
