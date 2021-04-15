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

if elephant_weight < ant_weight:
    square()
else:
    qazi_turtle.forward(400)