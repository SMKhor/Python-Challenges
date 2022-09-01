#	AS03	MIRROR TEXT	A jokes shop company wants people to enter in text, but when they display it they want it to be spelt backwards.
usertext = input("Enter in a text: ")
displaytext = ""
textlength = len(usertext)
for i in range(textlength):
    displaytext = displaytext + usertext[textlength-1-i]
print("Display:",displaytext)
