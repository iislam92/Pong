# Simple Pong in Python 3 for Beginners

import turtle # Module to add graphics

wn = turtle.Screen()
wn.title("Pong by Intisar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # turtle - module name Turtle - class name
paddle_a.speed(0) # Sets the animation to maximum speed
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-385, 0)

# Paddle B
paddle_b = turtle.Turtle() # turtle - module name Turtle - class name
paddle_b.speed(0) # Sets the animation to maximum speed
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375, 0)

# Ball
ball= turtle.Turtle() # turtle - module name Turtle - class name
ball.speed(0) # Sets the animation to maximum speed
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 3 # Everytime our ball moves, it will move by this amount of pixels
ball.dy = -3

# Pen (To allow for score keeping)
pen = turtle.Turtle()
pen.speed(0) # Animation Speed
pen.color("yellow")
pen.penup() # So that no lines appear when the pen moves
pen.hideturtle() # We don't wanna see the pen. Just wanna see the texts
pen.goto(0, 275) # Screen height is 300, so score should be closer to the top
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


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
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1 # Reverses the direction of the ball when it hits the top border

    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1  # Reverses the direction of the ball when it hits the bottom border

    if ball.xcor() > 400:
        ball.goto(0, 0) # If ball goes off to the side, ball moves back to center
        ball.dx *= -1 # Reverses direction once ball moves back to center
        score_a += 1 # Adds a point to player A
        pen.clear() # Clears the screen before score gets updated
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 # Adds a point to player B
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 365 and ball.xcor() < 375) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(365)
        ball.dx *= -1

    if (ball.xcor() < -375 and ball.xcor() > -385) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-375)
        ball.dx *= -1


