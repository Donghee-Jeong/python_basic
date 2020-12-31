import turtle
t = turtle.Turtle()

num = int(input("몇각형인가요? "))

for i in range(num) :
    t.forward(100)
    t.right(360/num)
