#Exercise 1
money = float(129)
print(f"RM{money}")

#Example
numcol1 = [1,1003442,5.32222342]
numcol2 = [5.62233,7.364363,9.32747474342]
numcol3 = [9.2634526,7.866832817,10.781237892798]

print("\nLeft Justify")
for i in range(3):
    print(f"{numcol1[i]:<15} {numcol2[i]:<15} {numcol3[i]:<15}")

print("\nRight justify with fixed decimal points")
for i in range(3):
    print(f"{numcol1[i]:>15.2f} {numcol2[i]:>15.2f} {numcol3[i]:>15.2f}")
# Note the order here. >15 and then .2f which is 2 decimal places

print("\nCentred with fixed decimal points")
for i in range(3):
    print(f"{numcol1[i]:^15.2f} {numcol2[i]:^15.2f} {numcol3[i]:^15.2f}")

#Exercise 2
PrimeNum = ["Prime Numbers", 2,3,5,7,11]
SquareNum = ["Square Numbers", 1,4,9,16,25]
EvenNum = ["Even Numbers", 2,4,6,8,10]

print("\nTable of Numbers")
for i in range(6):
    print(f"{PrimeNum[i]:^15} {SquareNum[i]:^15} {EvenNum[i]:^15}")

#Exercise 3
ConVert = int(input("Please enter a number to be converted into binary:"))
print(f"Binary: {ConVert:b}")
