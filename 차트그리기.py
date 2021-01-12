import turtle

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height),font = ("굴림",16,"bold"))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

data = [120,300,30,70,85,100]
t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)

for d in data:
    drawBar(d)
