import turtle

def drawMap():
    
    for i in range(2):
        t.penup()
        if i==0:
            t.goto(-300,50)
            t.pendown()
            t.forward(200)
            t.right(90)
            t.forward(150)
            t.left(90)
            t.forward(200)
            t.left(90)
            t.forward(150)
        else:
            t.goto(-300,-50)
            t.pendown()
            t.forward(100)
            t.right(90)
            t.forward(150)
            t.left(90)
            t.forward(400)
            
            t.left(90)
            t.forward(250)
        t.right(90)

def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

t = turtle.Turtle()
s = turtle.Screen()

drawMap()
t.penup()
t.goto(-300,0)
t.pendown()
s.onkey(turn_left,"Left")
s.onkey(turn_right,"Right")

s.listen()
s.mainloop()
