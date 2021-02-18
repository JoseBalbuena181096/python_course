from turtle import Turtle

class Serpiente:
    def __init__(self):
        #lista para almacenar las partes
        self.partes = []
        #crear el cuerpo de la serpuente cada cuadro mide 20x20 pixeles
        self.posiciones_iniciales = [(0,0),(-20,0),(-40,0)]

        for posicion in self.posiciones_iniciales:
            parte = Turtle()
            parte.shape('square')
            parte.color('white')
            parte.penup()
            parte.goto(posicion)
            self.partes.append(parte)
        
    def mover(self):
        for parte in range(len(self.partes)-1,0,-1):
            posicion_x = self.partes[parte-1].xcor()
            posicion_y = self.partes[parte-1].ycor()
            self.partes[parte].goto(posicion_x,posicion_y)
    
        self.partes[0].forward(20)
        self.partes[0].left(90)