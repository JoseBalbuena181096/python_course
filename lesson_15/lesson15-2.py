#importamos del módulo turtle : Turtle, done
from turtle import Turtle
from turtle import done

"""
Ejercicio , realizar un cuadrado de 200 pixeles por lado. 
"""
"""
tortuga = Turtle()
tortuga.forward(200)
tortuga.right(90)
tortuga.forward(200)
tortuga.right(90)
tortuga.forward(200)
tortuga.right(90)
tortuga.forward(200)
tortuga.right(90)
"""

"""
tortuga = Turtle()
for i in range(0,4):
    tortuga.forward(200)
    tortuga.right(90)
"""
tortuga = Turtle()
for i in range(0,4):
    for j in range(0,20):
        if j%2 == 0:
            tortuga.forward(10)
            tortuga.penup()
        else:
            tortuga.forward(10)
            tortuga.pendown()
    tortuga.right(90)


for i in range(0,4):
    tortuga.forward(200)
    tortuga.right(90)

done()