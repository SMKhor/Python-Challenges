import turtle
turtle.speed(10)
turtle.bgcolor("cornflower blue")
for i in range(300,-300,-20):
    turtle.penup()
    turtle.goto(-400,i)
    turtle.pendown()
    turtle.forward(600)

turtle.left(90)
for i in range(-400,220,20):
    turtle.penup()
    turtle.goto(i, -280)
    turtle.pendown()
    turtle.forward(580)
    
turtle.done()
