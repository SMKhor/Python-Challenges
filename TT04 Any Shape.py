import turtle
num = int(input("How many sides do you want your polygon to have?"))
for i in range (num):
    turtle.forward(100)
    turtle.right(360/num)

turtle.done()
