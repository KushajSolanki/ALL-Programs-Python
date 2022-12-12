from turtle import *
from freegames import square, vector

xy1 = vector(-100, 0)
aim1 = vector(4, 0)
body1 = set()

xy2 = vector(100, 0)
aim2 = vector(-4, 0)
body2 = set()

def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    xy1.move(aim1)
    head1 = xy1.copy()
    xy2.move(aim2)
    head2 = xy2.copy()

    if not inside(head1) or head1 in body2:
        print('Blue Player Wins!')
        return

    if not inside(head2) or head2 in body1:
        print('Red Player Wins')
        return

    body1.add(head1)
    body2.add(head2)
    square(xy1.x, xy1.y, 3, 'red')
    square(xy2.x, xy2.y, 3, 'blue')
    update()
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: aim1.rotate(90), 'a')
onkey(lambda: aim1.rotate(-90), 'd')
onkey(lambda: aim2.rotate(90), 'j')
onkey(lambda: aim2.rotate(-90), 'l')
draw()
done()