from turtle import Turtle

class Pelota(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.movimiento_x = 10
        self.movimiento_y = 10
        self.velocidad_movimiento = 0.1
     
    def mover(self):
        posicion_x = self.xcor() + self.movimiento_x
        posicion_y = self.ycor() + self.movimiento_y
        self.goto(posicion_x,posicion_y)
    
    def rebote_y(self):
        self.movimiento_y *= -1

    def rebote_x(self):
        self.movimiento_x *= -1
        self.velocidad_movimiento *= 0.9
        
    def reiniciar_posicion(self):
        self.goto(0, 0)
        self.rebote_x()
        self.velocidad_movimiento = 0.1