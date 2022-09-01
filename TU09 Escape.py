ErrorCount = 0
while True:
    MyNumber = input("Please enter a number:")
    print("You have made %d errors occur" % ErrorCount)
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        print("Seriously, don't you read the instructions. \nI asked for a number...")
        ErrorCount += 1
print(valid_number)
