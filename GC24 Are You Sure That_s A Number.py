test = input("Input a float: ")
try:
    float(test)
    res = True
except:
    print("Error: This is not a float")
    res = False

if res == True:
    print(test, "is a float")
