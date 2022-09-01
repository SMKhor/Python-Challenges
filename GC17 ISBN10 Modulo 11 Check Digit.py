stringtocheck = input("Input the number to check (with the checksum in the end): ")
checksumtocheck = stringtocheck[len(stringtocheck)-1]
multiplier = len(stringtocheck)
total = 0

for i in range(len(stringtocheck)-1):
        num = int(stringtocheck[i])
        total = total + (num*multiplier)
        multiplier = multiplier - 1

remainder = total%11
finalchecksum = str(11 - remainder)
if finalchecksum == "11":
    finalchecksum = "0"

if finalchecksum == "10":
    finalchecksum = "X"


if checksumtocheck == finalchecksum:
    result = "Yes"
else:
    result = "No"

print("Checksum given: " + str(checksumtocheck))
print("Checksum calculated: " + str(finalchecksum))
print("Check pass? " + result)
