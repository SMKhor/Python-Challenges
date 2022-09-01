myHeight = 143
PersonHeight = int(input("What is your height in cm?"))
if myHeight < PersonHeight:
    print("Hey! You're taller than me.")
elif myHeight == PersonHeight:
    print("You're the same height as me!")
elif myHeight > PersonHeight:
    print("Wow you're pretty short.")
