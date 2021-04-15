# while loops are used when you don't know how many results are going to appear

import turtle

qazi_turtle = turtle.Turtle()

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

# must use == to check values, other wise python will think you are trying to re-asign the value
while qazi == "sad":
    qazi_turtle.forward(10)

