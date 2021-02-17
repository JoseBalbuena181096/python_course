from turtle import Turtle,colormode,done
import random

tortuga = Turtle()
colormode(255)


def color_random():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


direcciones = [0,90,180,270]
tortuga.pensize(20)
tortuga.speed('fastest')

for _ in range(200):
    tortuga.color(color_random())
    tortuga.forward(40)
    tortuga.setheading(random.choice(direcciones))

done()