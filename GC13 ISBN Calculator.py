choice = input("Choose a or b:\na) Calculate the ISBN check digit\nb) Check if the ISBN 13 code is correct\nAnswer: ")

if choice == "a":
    num = int(input("Enter the ISBN without the check digit: "))
    oddigits = [(int(str(num)[0])), (int(str(num)[2])), (int(str(num)[4])), (int(str(num)[6])), (int(str(num)[8])), (int(str(num)[10]))]
    evendigits = [(int(str(num)[1])), (int(str(num)[3])), (int(str(num)[5])), (int(str(num)[7])), (int(str(num)[9])), (int(str(num)[11]))]
    sumodd = sum(oddigits)
    sumeven = (sum(evendigits))*3
    checkdigit = 10 - ((sumeven+sumodd)%10)
    print("%d is the check digit" % checkdigit)

if choice == "b":
    num = int(input("Enter the ISBN 13 digit code you want to check: "))
    oddigits = [(int(str(num)[0])), (int(str(num)[2])), (int(str(num)[4])), (int(str(num)[6])), (int(str(num)[8])), (int(str(num)[10])), (int(str(num)[12]))]
    evendigits = [(int(str(num)[1])), (int(str(num)[3])), (int(str(num)[5])), (int(str(num)[7])), (int(str(num)[9])), (int(str(num)[11]))]
    sumodd = sum(oddigits)
    sumeven = (sum(evendigits))*3
    checkdigit = (sumeven+sumodd)%10
    if checkdigit == 0:
        print("The ISBN: %d is correct" % num)
    else:
        print("The ISBN: %d is incorrect" % num)
