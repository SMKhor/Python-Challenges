while True:
    try:
        user = input("Please enter a singular character: ")
        store = user[1]
    except LookupError:
        print ("Thank you!")
        break
    else:
        print ("You have inputted more than one character.")
