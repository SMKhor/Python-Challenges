import tkinter
import random
window = tkinter.Tk()
names = ["Amy", "Bryan", "Chelsea", "Dylan", "Ethan", "Farah", "Greg"]

def RandomName():
    MyRandom = random.choice(names)
    name_picked.configure(text="Name chosen:" + str(MyRandom))

MyTitle = tkinter.Label(window, text = "Random Name Picker", font = "Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text = "OK", command = RandomName)
MyButton.pack()

name_picked = tkinter.Label(window, font = "Helvetica 16 bold")
name_picked.pack()

window.mainloop()
