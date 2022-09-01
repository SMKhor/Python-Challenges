import random
check = ""
score = 0

while True:
    check = input("Play/Continue the Multiplication Game? (Y/N) ")
    if check == "N":
        break
    else:
        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        print("Question: ", num1, "x", num2)
        ans = num1 * num2
        userans = int(input("Answer: "))
        if ans == userans:
            score = score + 1
            print("Correct!")
            print("Current score: ", score)
        else:
            print("Incorrect!")
            print("Current score: ", score)

print("Your final score is: ", score, "!")
