#importamos los modulos a emplear
from turtle import Turtle

#Creamos la clase de nuestro jugador que hereda de Turtle
class Jugador(Turtle):
    #Metodo constructor
    def __init__(self):
        super().__init__()
        #damos forma a nuestro judagor
        self.shape('classic')
        self.color('white')
        self.shapesize(stretch_wid=3,stretch_len=2)
        self.penup()
        self.distancia_mover = 10
        self.posicion_inicial = (0,-280) 
        self.ir_inicio()
        self.setheading(90)
        self.meta_y = 275

    def arriba(self):
        nueva_posicion_y = self.ycor() + 20
        if nueva_posicion_y < 300:
            self.goto(self.xcor(),nueva_posicion_y) 
    
    def abajo(self):
        nueva_posicion_y = self.ycor() - 20
        if nueva_posicion_y > -300:
            self.goto(self.xcor(),nueva_posicion_y) 

    def derecha(self):
        nueva_posicion_x = self.xcor() + 20 
        if nueva_posicion_x < 300:
            self.goto(nueva_posicion_x,self.ycor()) 
    
    def izquierda(self):
        nueva_posicion_x = self.xcor() - 20
        if nueva_posicion_x > -300:
            self.goto(nueva_posicion_x,self.ycor()) 
    
    def llegar_meta(self):
        if self.ycor() > self.meta_y:
            return True
        else:
            return False
    
    def ir_inicio(self):
        self.goto(self.posicion_inicial)