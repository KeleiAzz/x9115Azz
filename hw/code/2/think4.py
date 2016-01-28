from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
# print bob
bob.delay = 0.01


def square(turtle, length):
	for i in range(4):
	    fd(bob, length)
	    lt(bob)

def polygon(turtle, length, n):
	angle = 360.0 / n
	polyline(turtle, n, length, angle)

def circle(turtle, r):
	arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def turtleFlower(t, n, r, angle):
	# angle = 180 - 2 * 360.0 / n
	for i in range(n):
		arc(t, r, angle)
		lt(t, 180 - angle)
		arc(t, r, angle)
		lt(t, 360 / n + 180 - angle)

def pie(t, n, length):
	angle = 360.0 / n
	for i in range(n):
		triangle(t, length, angle)
		lt(t, 180)

def triangle(t, length, angle):
	bottom =  2 * length * math.sin(angle / 2 * math.pi / 180)
	fd(t, length)
	lt(t, 180 - (180 - angle) / 2.0)
	fd(t, bottom)
	lt(t, 180 - (180 - angle) / 2.0)
	fd(t, length)

# arc(bob, 60, 50)
# lt(bob, 180 - 50)
# arc(bob, 60, 50)
# turtleFlower(bob, 20, 140, 20)
# triangle(bob, 100, 60)
pie(bob, 6, 100)
# polygon(bob, 60, 5)
# circle(bob, 60)

wait_for_user()

