from turtle import Turtle
import random

#Creamos la clase Meteoritos
class Meteoritos(Turtle):

    def __init__(self):
        self.colores = ['red','gray','orange','brown']
        self.meteoritos_lista = []

    def crear_meteorito(self):
        crear_random = random.randint(1, 6)
        if crear_random == 1:
            nuevo_meteorito = Turtle('circle')
            #definimos el tamaño del meteorito
            nuevo_meteorito.shapesize(stretch_wid=1.5,stretch_len=1.5)
            nuevo_meteorito.penup()
            nuevo_meteorito.color(random.choice(self.colores))
            #definimos una poscicion al azar
            random_x = random.randint(-250,250)
            nuevo_meteorito.goto(random_x, 300)
            self.meteoritos_lista.append(nuevo_meteorito)
    
    def mover_meteoritos(self):
        i = 0
        for meteorito in self.meteoritos_lista:
            nueva_posicion_y = meteorito.ycor() - 10
            meteorito.goto(meteorito.xcor(),nueva_posicion_y)
            #si el meteorito llego al otro lado se elimina
            if nueva_posicion_y < -250:
                self.meteoritos_lista[i].hideturtle()
                self.meteoritos_lista.pop(i)
                continue
            i += 1 
                
