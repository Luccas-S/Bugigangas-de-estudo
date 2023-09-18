from turtle import *
from math import *
"""
jeff = turtle.Turtle()

print (jeff)
for i in range(4):
    jeff.fd(100)
    jeff.lt(90)
turtle.mainloop()
"""
jeff = Turtle()

"""
def square(t: turtle, length):
    t = turtle.Turtle()
    for n in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()
"""
"""
def polygon(p: turtle, length_2: int, n: int):
    p = turtle.Turtle()
    for i in range(n):
        p.fd(length_2)
        p.lt(360/n)
    turtle.mainloop()
def circle(t, r: int):
    polygon(t, 1, r)

circle(jeff, 100)
"""
"""
def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    mainloop()
def circle(t, r):
    circumference = 2 * pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
    
circle(jeff, 100)
"""
def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)
    mainloop()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    mainloop()

def circle(t, r):
    arc(t, r, 360)

arc(jeff, 100, 80)