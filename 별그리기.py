import turtle
t = turtle.Turtle()
t.shape("turtle")

size = int(input("별의 크기는 얼마로 할까요? "))
angle = 144 # 별 안의 각도는 36도이다.

t.forward(size)
t.right(angle)
t.forward(size)
t.right(angle)
t.forward(size)
t.right(angle)
t.forward(size)
t.right(angle)
t.forward(size)
t.right(angle)
