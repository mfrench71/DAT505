from Tkinter import *
import time
import random

scoreList = []
myFile = open("data.txt", "r")
for myLine in myFile:
   scoreList.append(int(myLine))
scoreListLength = len(scoreList)

WIDTH = 800
HEIGHT = 500

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Drawing")
canvas.pack()

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta', 'turquoise', 'grey', 'gold', 'pink']

class Square:
    def __init__(self, width, height):
        color = random.choice(colors)
        self.shape = canvas.create_rectangle(0, 0, width, height, fill=color)
        self.speedx = random.randrange(1, 10)
        self.speedy = random.randrange(1, 10)
        self.label = canvas.create_text(20, 20, text = width, fill="white", font="Helvetica 18 bold")

    def update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        canvas.move(self.label, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

square_list = []
for i in range(scoreListLength):
    square_list.append(Square(scoreList[i],scoreList[i]))
while True:
    for square in square_list:
        square.update()
    tk.update()
    time.sleep(0.01)