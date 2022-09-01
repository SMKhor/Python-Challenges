import random
MysteryNum = random.randint(1,100)
print(MysteryNum)

while True:
    guess = (input("Enter your guess:"))
    try:
        if int(guess) < MysteryNum:
            print("The number is higher than this")
        elif int(guess) > MysteryNum:
            print("The number is lower than this")
        elif int(guess) == MysteryNum:
            print("Congrats you got it right!")
            break
    except ValueError:
        print("Please enter a number.")
