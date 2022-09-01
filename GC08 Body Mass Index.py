weight = float(input("How much do you weigh in kilograms? "))
height = float(input("How tall are you in metres? "))
BMI = round(weight/height **2, 3)
print("Your BMI is:%f" % BMI)
if BMI < 18.5:
    print("You are underweight")
if 18.5 <= BMI < 25.0:
    print("You are normal weight")
if 25.0 <= BMI < 30.0:
    print("You are overweight")
if 30.0 <= BMI:
    print("You are obese")
