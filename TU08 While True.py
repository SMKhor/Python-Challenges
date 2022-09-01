#Exercise 1
while True:
    favClass = input ('What is your favourite subject?')
    if favClass in ["cs","computer science","Computer Science","CS"] :
        break

#Exercise 2
number = 0
while number < 15 or number > 20 :
    print("Please enter a number between 15 and 20")
    number = float(input("enter a number:"))
