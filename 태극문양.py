import turtle

def draw_shape(r,color):
    t.left(270)
    t.width(3)
    t.color("black",color)
    t.begin_fill()
    t.circle(r/2.0,-180)
    t.circle(r,180)
    t.left(180)
    t.circle(-r/2.0,-180)
    t.end_fill()

t = turtle.Turtle()
t.reset()

draw_shape(200,"red")
t.setheading(180)
draw_shape(200,"blue")
