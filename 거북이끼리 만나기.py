#내가 만든 조건문 문제2
import turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape("turtle")
t2.shape("turtle")

t2.penup()
t2.goto(200,200)

count = 4

while count > 0 :
    control = input("입력(l,r) : ")
    if control == "l" :
        t1.left(90)
        t1.forward(100)
    elif control == "r" :
        t1.right(90)
        t1.forward(100)
    count -= 1

if t1.pos() == t2.pos() :
    t1.write("안녕!")
else :
    t1.write("어디있니?")
