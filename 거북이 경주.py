import turtle
import random

def forward_turtle(t):  # 거북이가 1~60 사이의 거리만큼 움직이는 함수 선언
    d = random.randint(1,60)
    t.forward(d)

t1 = turtle.Turtle()    # 터틀 두개 생성
t2 = turtle.Turtle()

t1.color("pink")    # 터틀별로 색상 지정
t2.color("blue")

t1.shape("turtle")  # 거북이 모양으로 변경
t2.shape("turtle")

t1.pensize(5)   # 사이즈 설정
t2.pensize(5)

t1.penup()  # 시작점으로 이동하기 위해 penup
t2.penup()

t1.goto(-300,0) # 시작점으로 이동
t2.goto(-300,-100)

t1.pendown()    # 시작점으로 이동 후 pendown
t2.pendown()

for i in range(100):    # 경주는 100회 진행
    forward_turtle(t1)
    forward_turtle(t2)
