import turtle as t
import random


tortuga = t.Turtle()
tortuga.speed('fastest')
t.colormode(255)


def color_random():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def dibujar_circulos(numero_circulos):
    incremento = int(360 / numero_circulos)
    for _ in range(incremento):
        tortuga.color(color_random())
        tortuga.circle(100)
        tortuga.setheading(tortuga.heading() + incremento)

dibujar_circulos(5)

screen = t.Screen()
screen.exitonclick()