import turtle as t
from random import choice

tortuga = t.Turtle()
colores = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

def dibujar_figura(lados):
    angulo = 360/lados
    for _ in range(lados):
        tortuga.forward(100)
        tortuga.right(angulo)

for i in range(3,10):
    tortuga.color(choice(colores))
    dibujar_figura(i)

t.done()