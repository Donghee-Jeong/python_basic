#두 원을 그리고 한 원이 다른 원 안에 있는지 확인하
import turtle
t = turtle.Turtle()
t.shape("turtle")

x1=int(input("큰 원의 중심좌표 x1: "))
y1=int(input("큰 원의 중심좌표 y1: "))
r1=int(input("큰 원의 반지름: "))

x2=int(input("작은 원의 중심좌표 x2: "))
y2=int(input("작은 원의 중심좌표 y2: "))
r2=int(input("작은 원의 반지름: "))

t.penup()
t.goto(x1,y1-(r1/2))
t.pendown()
t.circle(r1)

t.penup()
t.goto(x2,y2-(r2/2))
t.pendown()
t.circle(r2)

distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

if distance + r2 < r1 :
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
else :
    t.write("두번째 원이 첫번째 원의 내부에 있지 않습니다.")
