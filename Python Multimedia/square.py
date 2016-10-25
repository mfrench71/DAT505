# Import libraries

from Tkinter import *
import time
import random

# Open text file and read into list

scoreList = []
myFile = open("data.txt", "r")
for myLine in myFile:
   scoreList.append(int(myLine))

# Get number of scores for later

scoreListLength = len(scoreList)

# Set global canvas height and width

WIDTH = 800
HEIGHT = 500

# Create root widget

tk = Tk()

# Create a canvas widget

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("DAT505 - Matthew French")
canvas.pack()

# Define a list of colours

colours = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta', 'turquoise', 'grey', 'gold', 'pink']

# Create a class for Square

class Square:
    def __init__(self, width, height):
        # Assign a random colour
        colour = random.choice(colours)
        # Draw a square with dimensions based on value of results
        self.shape = canvas.create_rectangle(0, 0, width, height, fill=colour)
        # Set a random movement speed from a range
        self.speedx = random.randrange(1, 10)
        self.speedy = random.randrange(1, 10)
        # Draw a label within the square with the value of the result. Centre the label.
        self.label = canvas.create_text(width/2, height/2, text = width, fill="white", font="Helvetica 18 bold")

    def update(self):
        # Move the square
        canvas.move(self.shape, self.speedx, self.speedy)
        # Move the label to match the square
        canvas.move(self.label, self.speedx, self.speedy)
        # Get position of the square
        pos = canvas.coords(self.shape)
        # Check for wall collision and reverse direction of movement if collision occurs
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

#Create empty list to hold Square objects

square_list = []

#Loop through each result
for i in range(scoreListLength):
    # Instantiate and add Square object to square_list and pass width and height values (same)
    square_list.append(Square(scoreList[i],scoreList[i]))
# Infinite loop
while True:
    # Loop through each square
    for square in square_list:
        # Move the squares
        square.update()
    # Update display
    tk.update()
    # Pause to slow movement slightly
    time.sleep(0.01)