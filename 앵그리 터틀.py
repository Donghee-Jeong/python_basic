import turtle
import math

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()

def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def fire():
    x,y = 0,0
    v = 50
    a = player.heading()
    vx = v * math.cos(a * 3.14 / 180.0)
    vy = v * math.sin(a * 3.14 / 180.0)

    while player.ycor() >=0:
        vx = vx
        vy = vy -10
        x = x+ vx
        y=y+vy
        player.goto(x,y)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(fire,"space")
screen.listen()
