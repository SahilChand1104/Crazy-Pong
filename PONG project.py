#PONG
#Made by Sahil Chand


import turtle
import os
import time



wn = turtle.Screen()
wn.title(" SMALL PONG 2022")
wn.bgcolor("black")
wn.setup(width=1200, height=600)
wn.tracer(0)

# Score
score1 = 0
score2 = 0

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=1,stretch_len=1)
paddle1.penup()
paddle1.goto(-550, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=1,stretch_len=1)
paddle2.penup()
paddle2.goto(550, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle1_up():
    y = paddle1.ycor()
    y += 40
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 40
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 40
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 40
    paddle2.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 535:
        score1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -535:
        score2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -530 and ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50:
        ball.dx *= -1
        #ball.dx += 1
        ball.dy += 0.1
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 530 and ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50:
        ball.dx *= -1
        #ball.dx += 1
        ball.dy += 0.1
        os.system("afplay bounce.wav&")
    
