import turtle

def tree(length):
    if length>0:
        t.forward(length)
        t.left(20)
        tree(length-10)
        t.right(40)
        tree(length-10)
        t.left(20)
        t.backward(length)
    


t = turtle.Turtle()
t.shape("turtle")
t.left(90)
tree(50)
