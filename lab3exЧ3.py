import turtle
from math import acos, pi

EDGE_LEN = 10
N_TURTLES = 10

RADIUS_COEFF = 20

turtles = [turtle.Turtle(shape='turtle') for _ in range(N_TURTLES)]

for i, trt in enumerate(turtles):
    trt.penup()
    trt.goto((i + 1) * RADIUS_COEFF, 0)
    trt.pendown()
    trt.left(90)

while True:
    for i, trt in enumerate(turtles):
        trt.forward(EDGE_LEN)
        trt.left(180 - 2 * acos(EDGE_LEN / (2 * (i + 1) * RADIUS_COEFF)) * 180 / pi)
 