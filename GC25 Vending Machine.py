soda = 3.50
chips = 5.00
cookies = 4.50
candy = 2.00
water = 1.50

print("Vending Machine")
numcol1 = ["Product", "1 Soda", "2 Chips", "3 Cookies", "4 Candy", "5 Water"]
numcol2 = ["Price", "RM3.50", "RM5.00", "RM4.50", "RM2.00", "RM1.50"]

for i in range(6):
    print(f"{numcol1[i]:^15} {numcol2[i]:^15}")

money = float(input("Input money:"))
product= input("What do you want to buy? (enter product number)")
if product == "1":
    bought = "Soda"
    change = money - soda

if product == "2":
    bought = "Chips"
    change = money - chips

if product == "3":
    bought = "Cookies"
    change = money - cookies

if product == "4":
    bought = "Candy"
    change = money - candy

if product == "5":
    bought = "Water"
    change = money - water

print("Product you bought:", bought)
print("Amount of change:", "{0:.2f}".format(change))
