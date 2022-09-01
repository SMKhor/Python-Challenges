#	AS41	PARITY BIT CHECKER GAME	Create a Parity Bit Checker Quiz that challenges students on odd and even bit checking. The computer should correct wrong answers.
import random
bit = ["0", "1"]
parity = ["Even", "Odd"]
question = ""
cont = "Y"
num0 = 0
num1 = 0
correctbit = ""

print("Parity Bit Checker Game")
print("The computer will generate 7-bits, enter the 8th bit according to the parity given by the computer.")

while cont == "Y":
    cont = input("\nContinue? (Y/N) ")
    if cont != "Y":
        break
    for i in range(7):
        bitchoice = random.choice(bit)
        question = question + bitchoice
    print("Bits: ", question)
    paritychoice = random.choice(parity)
    print("Parity: ", paritychoice)
    userbit = input("What's the 8th bit? ")

    for i in range(7):
        char = question[i]
        if char == "0":
            num0 = num0 + 1
        if char == "1":
            num1 = num1 + 1

    if paritychoice == "Even":
        if num1 % 2 == 0:
            correctbit = "0"
        else:
            correctbit = "1"
    if paritychoice == "Odd":
        if num1 % 2 == 0:
            correctbit = "1"
        else:
            correctbit = "0"

    if userbit == correctbit:
        print("That was correct!")
    else:
        print("Incorrect. The correct bit was", correctbit, ".")

    question = ""
    num0 = 0
    num1 = 0
