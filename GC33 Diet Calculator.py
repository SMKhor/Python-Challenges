foodlist = []
totalkcal = 0
gender = input("Are you male (M) or female (F)? ")
if gender == "M":
    healthykcal = 2500
else:
    healthykcal = 2000

while True:
    food = input("What food have you consumed? ")
    if food == "end day":
        print("Diet Calculator Report:")
        print("All the food you have consumed today:", foodlist)
        print("The amount of calories you consumed today:", totalkcal)
        print("The amount of calories you needed to consume more of to stay healthy:", healthykcal-totalkcal)
        foodlist.clear()
        totalkcal = 0
        continue
    foodlist.append(food)
    try:
        kcal = int(input("How many calories was in the food? "))
    except ValueError:
        print("Please enter a numerical value")
        kcal = input("How many calories was in the food? ")
    totalkcal = totalkcal + int(kcal)
    print("The food you have eaten today:", foodlist)
    print("The amount of calories you need to consume to stay healthy for the day:", healthykcal - totalkcal)
