#Exercise 1
MyList = ["apples", "bananas", "carrots", "donuts", "eggs", "fish fingers"]
print(*MyList[0:4], sep= ", ")

#Exercise 2
VidGameCharacters = ["Mario", "Luigi", "Yoshi", "Princess Peach"]
while True:
    check = input("Do you want to add a new character?")
    if check in ["y","yes","Yes","Y"]:
        NewCharacter = input("Please add a new character:")
        VidGameCharacters.append(NewCharacter)
        VidGameCharacters.sort()
        print(*VidGameCharacters, sep = ", ")
    else:
        VidGameCharacters.sort()
        print(*VidGameCharacters, sep = ", ")
        break
