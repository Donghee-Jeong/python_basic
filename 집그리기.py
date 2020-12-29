import turtle
t = turtle.Turtle()
t.shape("turtle")

size = int(input("집의 크기는 얼마로 할까요? "))

t.forward(size) #size만큼 거북이를 전진시킨다.
t.right(90) #거북이를 오른쪽으로 90도 회전시킨다.
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

t.right(90)

t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
