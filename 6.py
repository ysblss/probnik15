
from turtle import *
tracer(15)
k = 17
screensize(1000, 1000)
pensize(1)
for i in range(9):
    fd(22 * k)
    right(90)
    fd(6 * k)
    right(90)
up()
fd(1 * k)
right(90)
fd(5*k)
left(90)
down()
for i in range(9):
    fd(53 * k)
    right(90)
    fd(75 * k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x *k, y * k)
        dot(3, "green")
done
