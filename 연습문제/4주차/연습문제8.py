import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

list = [x1,y1,x2,y2,x3,y3]

t.up()
t.goto(list[0],list[1])
t.down()
t.goto(list[2],list[3])
t.goto(list[4],list[5])
