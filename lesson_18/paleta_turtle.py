from turtle import Turtle

class Paleta(Turtle):
    
    def __init__(self,posicion): 
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(posicion)
    
    def arriba(self):
        nueva_posicion_y = self.ycor() + 40
        self.goto(self.xcor(),nueva_posicion_y) 
    
    def abajo(self):
        nueva_posicion_y = self.ycor() - 40
        self.goto(self.xcor(),nueva_posicion_y) 
        