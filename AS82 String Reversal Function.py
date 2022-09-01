string = input("Please enter string to reverse: ")

def func(x):
    new = ""
    total = len(x)
    for i in range(len(x)):
        new = new + string[total-i-1]
    return new

print(func(string))
