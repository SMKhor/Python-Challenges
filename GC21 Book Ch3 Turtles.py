#Exercise 1
for i in range(1000):
    print("We like Python turtles!")

#Exercise 2
import turtle
cellphone = turtle.Turtle()
cellphone.color("blue")
cellphone.shape("arrow")
cellphone.speed(1)
cellphone.forward(100)
cellphone.left(90)
cellphone.back(400)

#Exercise 3
for f in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print("One of the months of the year is " + f)

#Exercise 4
wn = turtle.Screen()
tess = turtle.Turtle()
tess.left(3645)
#tess spins around in circles until eventually it stops to face North East, about 45 degrees left

#Exercise 5a
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)

#Exercise 5b
for i in xs:
    print(i)
    print(i*i)

#Exercise 5c
total = 0
for i in xs:
    total += total + 1
print(total)

#Exercise 5d
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply(xs))
#Exerice 6
#An equilateral triangle
ross = turtle.Turtle()
for i in range(3):
    ross.forward(100)
    ross.left(120)

#Square
for i in range(4):
    ross.forward(100)
    ross.left(90)

#A hexagon
for i in range(6):
    ross.forward(100)
    ross.left(60)

#An octagon
for i in range(8):
    ross.forward(100)
    ross.left(15)

turtle.done()
