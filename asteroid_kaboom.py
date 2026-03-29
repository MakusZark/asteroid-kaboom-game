"""

The purpose of this program is to run a game using the turtle window graphics. The game randomly generates asteroids and stars on the screen. The play inputs coordinates to score points and the final score is displayed.

"""

## Modules
import turtle
from pixels import check_pixel_color
import random
import time

## Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Kaboom!!!"

NUM_STAR = 100 # number of stars in the background
NUM_ASTEROID = 10 # number of asteroids
ASTEROID_SIDES = 8 # number of sides of each asteroid
EXPLOSION_RADIUS = 40 # radius of the explosion

BLUE_PTS = 100 # points per blue asteroid
PINK_PTS = 200 # points per pink asteroid

## Turtle set up
# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)

# Create the turtle object
t = turtle.Turtle()

## Start of your code
t.speed(0)
t.screen.bgcolor("black")

## Intro text

t.pencolor("yellow")
t.write("Welcome to Asteroid Kaboom!!!", align = "center", font = ('Courier New', 50, 'normal'))
time.sleep(2)
t.clear()

t.write("Your job is to destroy the asteroids by guessing their coordinates", align = "center", font = ('Courier New', 15, 'normal'))
t.penup()
t.goto(0, -20)
t.write("The blue asteroids are 100pts, the pink ones are 200pts", align = "center", font = ('Courier New', 15, 'normal'))
t.pendown()
time.sleep(5)
t.clear()

t.write("Good Luck!", align = "center", font = ('Courier New', 50, 'normal'))
time.sleep(1)
t.clear()

## Draws star field
t.screen.tracer(0)

for i in range(NUM_STAR): # This for loop repeats 100 times to draw 100 stars

    grayscale = random.random() # Randomly generates the grayscale value
    t.pencolor(grayscale, grayscale, grayscale)
    t.fillcolor(grayscale, grayscale, grayscale)

    t.penup()
    t.goto(random.randint(int(-SCREEN_WIDTH/2),int(+SCREEN_WIDTH/2)),random.randint(int(-SCREEN_HEIGHT/2),int(+SCREEN_HEIGHT/2))) # Moves the turtle to a random location inside the screen
    t.pendown()
    t.begin_fill()
    radius = 3*random.random() # Generates a random number from 0 to 1, scales it up by 3 then assigns that to the variable radius
    t.circle(radius, 360)
    t.end_fill()

t.screen.update()
time.sleep(1)


## Draws asteroids

num_pink = random.randint(1, 8) # Randomly generates a number from 0 - 8 which will be the amount of pink asteroids drawn

# Defines variables and puts first asteroid at (0,0)
x_coord  = 0
y_coord = 0

for i in range(NUM_ASTEROID - num_pink): # loops 10 minus the amount of pink asteroids times which will be the amount of blue asteroids drawn
    length = random.randint(15,50) # Assigns a random integer from 15 to 50 to the variable length
    t.pencolor("black")
    t.fillcolor("blue")
    t.penup()
    t.goto(0 + x_coord - length/2 ,0 + y_coord - length) # Goes to an off set coordiate near 0,0 so that the asteroid is centered at 0,0. Next loop this will be a different random coordinate
    x_coord = random.randint(int(-SCREEN_WIDTH/2),int(+SCREEN_WIDTH/2)) # randomly generates new x coordinate for next loop
    y_coord = random.randint(int(-SCREEN_HEIGHT/2),int(+SCREEN_HEIGHT/2))# randomly generates new y coordinate for next loop
    t.pendown()
    t.begin_fill()
    for n in range(8): # Loops 8 times for the 8 sides of the asteroids. This loop actually draws the asteroids
        t.forward(length)
        t.left(360/8)
    t.end_fill()
    t.left(random.randint(0,360)) # Off sets rotation for next loop
t.screen.update()
time.sleep(1)


for i in range(num_pink): # Loops code num_pink times to draw the remaining asteroids
    length = random.randint(15,50) # Assigns a random integer from 15 to 50 to the varible length
    t.pencolor("black")
    t.fillcolor("pink")
    t.penup()
    x_coord = random.randint(int(-SCREEN_WIDTH/2),int(+SCREEN_WIDTH/2)) # randomly generates new x coordinate
    y_coord = random.randint(int(-SCREEN_HEIGHT/2),int(+SCREEN_HEIGHT/2)) # randomly generates new y coordinate
    t.goto(x_coord - length/2 ,y_coord - length)
    t.pendown()
    t.begin_fill()
    for n in range(8): # Same as other loop, draws the asteroid sides, loops 8 times for 8 sides
        t.forward(length)
        t.left(360/8)
    t.end_fill()
    t.left(random.randint(0,360)) # Off sets rotation for next loop
t.screen.update()
time.sleep(1)


t.penup()
t.home()

## Player guesses

guesses = int(screen.numinput("Kaboom?", "How many shots do you want?")) # Gets amount of guesses from player
points = 0

for i in range(guesses): # This loop draws explosions and counts points, loops for however many guesses player inputed

    # Gets shot location
    x = screen.numinput("Where to shoot?", "What is the x value")
    y = screen.numinput("Where to shoot?", "What is the y value")

    current_points = BLUE_PTS*check_pixel_color(x, y, "blue") + PINK_PTS*check_pixel_color(x, y, "pink") # Calculates the points scored for the guess based on point system
    points += current_points # Keeps track of total points for game

   # Draws explosion
    t.pensize(5)
    t.penup()
    t.goto(x,y - 40)
    t.pendown()
    t.pencolor("red")
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(40, 360)
    t.end_fill()

    # Draws explosion effect
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pencolor("yellow")
    for i in range(20): # This loop draws explosion effect, loop 20 times to randomly draw 20 lines centered at the guessed location
        angle = random.randint(0, 360)
        length = random.randint(20, 60)
        t.setheading(angle)
        t.forward(length)
        t.backward(length)

   # Writes points scored
    t.penup()
    t.home()
    t.goto(x, y)
    t.pendown()
    t.pencolor("black")
    t.write(f"+{current_points} pts!", align = "center", font = ('Arial', 15, 'normal'))
    t.screen.update()
    time.sleep(2)

## Ending message

t.penup()
t.clear()
t.goto(0,0)
t.pencolor("red")
t.write("Game Over", align = "center", font = ('Courier New', 50, 'normal'))
t.screen.update()
time.sleep(1)
t.clear()


# Gives final total points
t.pencolor("Yellow")
t.write(f"You scored {points} points!", align = "center", font = ('Courier New', 50, 'normal'))
t.screen.update()
time.sleep(3)
t.clear()


t.goto(0,0)
t.write("Thanks for Playing!", align = "center", font = ('Courier New', 50, 'normal'))
t.screen.update()


## End of your code

# Make a clean exit
screen.exitonclick()
