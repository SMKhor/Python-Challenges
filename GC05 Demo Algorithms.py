#Demo code to demonstrate the ideas of: sequence, selection, repetition, variable
#Sequence
print("This is a sequence")
print("Step 1")
print("Step 2")
print("Step 3")
print("End of the sequence")

#Selection
ask = input("Is it sunny today?")
if ask in ["yes", "Yes"]:
    print("Yay! We can go out can play!")
elif ask in ["no", "No"]:
    print("Oh no, that's sad")
else:
    print("Look out the window and check!")

#Repetition
for i in range(5):
    print("This is repetition")

#Variable
variable = input("Enter your variable:")
strvariable = "This is a string variable:"
intvariable = 12

print(strvariable + variable)
print(intvariable)
