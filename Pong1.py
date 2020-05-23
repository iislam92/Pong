# Simple Pong in Python 3 for Beginners
# Part 4: Moving the ball

import turtle # Module to add graphics

wn = turtle.Screen()
wn.title("Pong by Intisar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle() # turtle - module name Turtle - class name
paddle_a.speed(0) # Sets the animation to maximum speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-375, 0)

# Paddle B
paddle_b = turtle.Turtle() # turtle - module name Turtle - class name
paddle_b.speed(0) # Sets the animation to maximum speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375, 0)

# Ball
ball= turtle.Turtle() # turtle - module name Turtle - class name
ball.speed(0) # Sets the animation to maximum speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5 # Everytime our ball moves, it will move by this amount of pixels
ball.dy = -2.5


# Function to allow for the two paddles to move up and down
def paddle_a_up():
    y = paddle_a.ycor() # .ycor is from turtle module that returns y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # .ycor is from turtle module that returns y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # .ycor is from turtle module that returns y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # .ycor is from turtle module that returns y coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen() # Tells program to listen for keyboard input
wn.onkeypress(paddle_b_up, "Up") # When up arrow is pressed, paddle_b_up function is called
wn.onkeypress(paddle_a_up, "w") # When "w" is pressed, paddle_a_up function is called
wn.onkeypress(paddle_a_down, "s") # When "s" is pressed, paddle_a_down function is called
wn.onkeypress(paddle_b_down, "Down") # When down arrow is pressed, paddle_b_up fucntion is called

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # Reverses the direction of the ball when it hits the top border

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverses the direction of the ball when it hits the bottom border

    if ball.xcor() > 390:
        ball.goto(0, 0) # If ball goes off to the side, ball moves back to center
        ball.dx *= -1 # Reverses direction once ball moves back to center

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
