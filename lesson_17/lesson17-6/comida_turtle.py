from turtle import Turtle
import random

class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        """
        posicion_x = random.randint(-280,280)
        posicion_y = random.randint(-280,280)
        self.goto(posicion_x,posicion_y)
        """
        self.nueva_posicion()

    def nueva_posicion(self):
        posicion_x = random.randint(-270,270)
        posicion_y = random.randint(-270,270)
        self.goto(posicion_x,posicion_y)
    
