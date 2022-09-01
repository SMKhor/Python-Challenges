PoojaAccountBalance = float(input("Pooja's account balance: $"))
while True:
    withdraw = float(input("How much do you want to withdrawl? $"))
    if withdraw%5 == 0 and withdraw < (PoojaAccountBalance - 0.5):
        PoojaAccountBalance = PoojaAccountBalance - withdraw - 0.5
        print("Pooja's new account balance: $%.2f" % PoojaAccountBalance)
        break
    if withdraw%5 != 0:
        print("The withdrawl amount must be a multiple of 5. Try again.")
    if withdraw > (PoojaAccountBalance - 0.5):
        print("Pooja's account balance is too low for this transaction to be successful. Try again.")
