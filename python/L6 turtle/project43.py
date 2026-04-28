import turtle
screen = turtle.Screen()
screen.bgcolor('Aqua')

t = turtle.Turtle()
t.speed(2)

#
t.color("blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()


t.penup()
t.goto(150, 0)
t.pendown()


t.color("green")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()


t.penup()
t.goto(-150, -150)
t.pendown()


t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.right(90)
    t.forward(80)
    t.right(90)
t.end_fill()


t.penup()
t.goto(150, -150)
t.pendown()


t.color("purple")
t.begin_fill()
sides = 6
angle = 360 / sides

for _ in range(sides):
    t.forward(80)
    t.right(angle)
t.end_fill()

turtle.done()