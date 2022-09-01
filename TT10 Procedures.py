import turtle
turtle.speed(0)

def triangle_draw(x,y,sz):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range (3):
        turtle.forward(sz)
        turtle.right(120)

for y in range (-400, 400, 20):
    for x in range (-800, 600, 20):
        triangle_draw(x,y,10)

turtle.done()
