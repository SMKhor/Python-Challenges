import turtle

class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.speed(0)
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()

file = open('patterns.txt','r')
content = file.readlines()
file.close()

num = int(input("Which pattern would you like to print (1-5)? "))
mypattern = pattern(int(content[(num*2)-2].strip()),int(content[(num*2)-1].strip()))
mypattern.draw_pattern()
