import turtle
t = turtle.Turtle()
t.shape("turtle")

list = ['red','orange','yellow','green']

t.fillcolor(list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(list[1])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(list[2])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(50)
t.fillcolor(list[3])
t.begin_fill()
t.circle(100)
t.end_fill()
