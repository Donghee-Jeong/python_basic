import random
import turtle

def randomPosition():
    t.penup()
    t.goto(random.randrange(-200,200),random.randrange(-200,200))
    t.pendown()

def star(length):
    for i in range(5):
        t.forward(length)
        t.right(144)

t = turtle.Turtle()

n = int(turtle.textinput("","몇 개의 별을 그릴까요? "))

for i in range(n):
    length = random.randrange(50,200)
    randomPosition()
    star(length)
