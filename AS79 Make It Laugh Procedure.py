string = input("String input: ")

def make_it_laugh(x):
    newstring = ""
    for i in range(len(string)):
        check = string[i]
        if check not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            newstring = newstring + check
        else:
            newstring = newstring + "haha"
    print("Modified string: ", newstring)

make_it_laugh(string)
