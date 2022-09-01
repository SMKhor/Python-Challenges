#Exercise 1
import random
mynumber = random.uniform(0.1,9.9)
print(mynumber)

#Exercise 2
Choose_Name = ["James", "John", "Mark", "Rick"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print(chosen)
    pick = input("Do you want to keep this person in the list?")
    if pick in ["y","Y","Yes","yes"]:
        print(Choose_Name)
    else:
        Choose_Name.remove(chosen)
        print(Choose_Name)

