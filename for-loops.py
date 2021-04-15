# while loops are used when you don't know how many results are going to appear

import turtle

qazi_turtle = turtle.Turtle()
qazi_turtle.speed(15)

elephant_weight = 3000
ant_weight = .01

def square():
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)

qazi = "happy"

for count in range(4):
    square()