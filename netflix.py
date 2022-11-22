import turtle
from turtle import *
turtle.hideturtle()
turtle.bgcolor('dark grey')
turtle.speed(5)
turtle.color('white')
turtle.goto(-80,180)
turtle.down()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.forward(200)
turtle.setheading(270)

s = 360
for i in range(9):
    s = s-10
    turtle.setheading(s)
    turtle.forward(10)

turtle.forward(180)
s = 270
for i in range(9):
    s = s-10
    turtle.setheading(s)
    turtle.forward(10)

turtle.forward(200)
s = 180
for i in range(9):
    s = s-10
    turtle.setheading(s)
    turtle.forward(10)

turtle.forward(180)
s = 90
for i in range(9):
    s = s-10
    turtle.setheading(s)
    turtle.forward(10)
turtle.forward(30)
turtle.end_fill()
turtle.up()
turtle.color('black')
turtle.setheading(273)
turtle.forward(240)
turtle.setheading(0)
turtle.down()
turtle.color('red')
turtle.fillcolor()
turtle.begin_fill()
turtle.forward(30)
turtle.setheading(90)
turtle.forward(180)
turtle.setheading(180)
turtle.forward(30)
turtle.setheading(270)
turtle.forward(180)
turtle.end_fill()
turtle.setheading(0)
turtle.up()
turtle.forward(75)
turtle.down()
turtle.color('red')
turtle.fillcolor()
turtle.begin_fill()
turtle.forward(30)
turtle.setheading(90)
turtle.forward(180)
turtle.setheading(180)
turtle.forward(30)
turtle.setheading(270)
turtle.forward(180)
turtle.end_fill()
turtle.color('red')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.setheading(113)
turtle.forward(195)
turtle.setheading(0)
turtle.forward(31)
turtle.setheading(293)
turtle.forward(196)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
