import random
tiles = []
vowels = ["A", "E", "I", "O", "U"]
consonant = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
choosenvowels = int(input("How many vowels do you want? "))
tiles.append(random.choices(vowels, k = choosenvowels))
tiles.append(random.choices(consonant, k = 6 - choosenvowels))

print(tiles)
