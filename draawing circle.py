import turtle as t
from itertools import cycle

counter = 1
color =cycle(['green','yellow','purple','orange','blue','violet','indigo'])
def draw_circle(size,angle,shift):
    t.bgcolor(next(color))
    t.pencolor(next(color))
    t.pensize(5)
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size,angle+3,shift+3)




t.speed('fast')
draw_circle(50,0,1)

