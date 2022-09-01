#AS08 ROCK PAPER SCISSORS	Create a game of rock, paper, Scissors to play against the computer.
import random
print("Rock, Paper, Scissors Game!")
ulives = 3
clives = 3
choices = ["Rock", "Paper", "Scissors"]
userchoose = ""

while ulives > 0 and clives > 0:
    print("\nYou have", ulives, "lives left.")
    print("The computer has", clives, "lives left.")
    user = input("\nRock (R), Paper (P) or Scissors (S)? ")
    comp = random.choice(choices)
    if user.upper() == "R":
        print("You chose Rock.")
        userchoose = "Rock"
    if user.upper() == "P":
        print("You chose Paper.")
        userchoose = "Paper"
    if user.upper() == "S":
        print("You chose Scissors.")
        userchoose = "Scissors"
    print("Computer chose ", comp, ".")
    if userchoose == comp:
        print("\nIt is a tie!")
    if userchoose == "Rock" and comp == "Scissors":
        print("Rock beats Scissors")
        print("User beats Computer!")
        clives = clives - 1

    if userchoose == "Rock" and comp == "Paper":
        print("Paper beats Rock")
        print("Computer beats User!")
        ulives = ulives - 1

    if userchoose == "Paper" and comp == "Rock":
        print("Paper beats Rock")
        print("User beats Computer!")
        clives = clives - 1

    if userchoose == "Paper" and comp == "Scissors":
        print("Scissors beats Paper")
        print("Computer beats User!")
        ulives = ulives - 1

    if userchoose == "Scissors" and comp == "Rock":
        print("Rock beats Scissors")
        print("Computer beats User!")
        ulives = ulives - 1

    if userchoose == "Scissors" and comp == "Paper":
        print("Scissors beats Paper")
        print("User beats Computer!")
        clives = clives - 1


if ulives == 0:
    print("\nComputer Wins!")
else:
    print("\nUser Wins!")
