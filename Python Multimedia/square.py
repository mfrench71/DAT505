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
    def __init__(self, width, height, obstacle):
        # Assign a random colour
        colour = random.choice(colours)
        # Draw a square with dimensions based on value of results
        self.shape = canvas.create_rectangle(0, 0, width, height, fill=colour)
        # Set a random movement speed from a range
        self.speedx = random.randrange(1, 10)
        self.speedy = random.randrange(1, 10)
        # Draw a label within the square with the value of the result. Centre the label within square
        self.label = canvas.create_text(width/2, height/2, text = width, fill="white", font="Helvetica 18 bold")
        self.obstacle = obstacle
    
    # Check square coords (pos) against obstacle coords
    def hitObstacle(self, pos):
        obstaclePos = canvas.coords(self.obstacle.id)
        # Are square coords within obstacle coords (horizontal)
        if pos[2] >= obstaclePos[0] and pos[0] <= obstaclePos[2]:
            # Are sqaure coords within obstacle coords (vertical) - adjust for obstacle height (+50)
            if pos[3] >= obstaclePos[1] and pos[3] <= obstaclePos[3] + 50:
                # If within, return true (hit)
                 return True
        return False

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
        # Check for obstacle collision and reverse direction of movement if collision occurs
        if self.hitObstacle(pos) == True:
            self.speedx *= -1
            self.speedy *= -1

# Create a class for Obstacle

class Obstacle:
    def __init__(self, width, height, label):
        # Assign a random colour
        colour = random.choice(colours)
        # Draw oval and label. Centre the label within oval
        self.id = canvas.create_oval(0, 0, width, height, fill=colour)
        self.label = canvas.create_text(width/2, height/2, text = label, fill="white", font="Helvetica 14 bold")
        canvas.move(self.id, 340, 175)
        # Move oval and label
        canvas.move(self.label, 340, 175)
        
    def draw(self):
        pass

# Draw obstacle
obstacle = Obstacle(100,100,"DAT 505")
obstacle.draw()

#Create empty list to hold Square objects

square_list = []

#Loop through each result
for i in range(scoreListLength):
    # Instantiate and add Square object to square_list and pass width and height values (same)
    square_list.append(Square(scoreList[i],scoreList[i], obstacle))
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