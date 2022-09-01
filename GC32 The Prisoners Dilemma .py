import random
import time
Achoice = ""
Bchoice = ""
select = ["silent", "confess"]

def restart():
    time.sleep(2)
    menu = input("Do you want to play again? Y/N ")
    if menu == "Y":
        gamestart()

def gamestart():
    print("Welcome to the prisoner's dilemma! You are prisoner A and the computer is prisoner B.")
    Achoice = input("Now, do you chose to stay silent or confess?\nAnswer either 'silent' or 'confess': ")
    Bchoice = random.choice(select)
    print("Prisoner A chooses:", Achoice)
    print("Prisoner B chooses:", Bchoice)
    if Achoice == "silent" and Bchoice == "silent":
        print("Prisoner A stays in prison for 1 year")
        print("Prisoner B stays in prison for 1 year")
        restart()
    if Achoice == "confess" and Bchoice == "confess":
        print("Prisoner A stays in prison for 5 years")
        print("Prisoner B stays in prison for 5 years")
        restart()
    if Achoice == "confess" and Bchoice == "silent":
        print("Prisoner A is released! Congrats!")
        print("Prisoner B stays in prison for 20 years")
        restart()
    if Achoice == "silent" and Bchoice == "confess":
        print("Prisoner A stays in prison for 20 years")
        print("Prisoner B is released! Congrats!")
        restart()

while True:
    gamestart()
    break
