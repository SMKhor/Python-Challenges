phrase = "Hello! Everyday is a good day and a good day it is. 365 days in a year."
print(phrase)
check1 = input("Can you type out this phrase:")
check2 = ""

while check2 != phrase:
    if check1 == phrase:
        check2 = input("Can you type out the phrase again: ")
        if check2 == phrase:
            print("Congratulations! You are cleared to operate!")
        else:
            print("Incorrect. Please type out the phrase again.")
            check2 = input("Can you type out the phrase again: ")
    else:
        print("Incorrect. Please type out the phrase again.")
        check1 = input("Can you type out this phrase:")
        
