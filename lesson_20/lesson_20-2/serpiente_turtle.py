from turtle import Turtle

class Serpiente:

    def __init__(self):
        #lista para almacenar las partes
        self.partes = []
        #crear el cuerpo de la serpuente cada cuadro mide 20x20 pixeles
        self.posiciones_iniciales = [(0,0),(-20,0),(-40,0)]
        self.crear_serpiente()
        #cabeza de la serpiente 
        self.head = self.partes[0] 
        self.direccion = {'arriba':90,'abajo':270,'derecha':0,'izquierda':180}   

    def crear_serpiente(self):
        for posicion in self.posiciones_iniciales:
            self.aumentar_partes(posicion)

    def aumentar_partes(self,posicion):
        parte = Turtle()
        parte.shape('square')
        parte.color('red')
        parte.penup()
        parte.goto(posicion)
        self.partes.append(parte)
    
    def crecer(self):
        self.aumentar_partes(self.partes[-1].position())
    
    def mover(self):
        for parte in range(len(self.partes)-1,0,-1):
            posicion_x = self.partes[parte-1].xcor()
            posicion_y = self.partes[parte-1].ycor()
            self.partes[parte].goto(posicion_x,posicion_y)
    
        self.head.forward(20)

    #girar arriba
    def arriba(self):
        if self.head.heading() != self.direccion['abajo']:
            self.head.setheading(self.direccion['arriba'])
    
    #girar abajo
    def abajo(self):
        if self.head.heading() != self.direccion['arriba']:
            self.head.setheading(self.direccion['abajo'])    

   #girar derecha
    def derecha(self):
        if self.head.heading() != self.direccion['izquierda']:
            self.head.setheading(self.direccion['derecha'])

    #girar izquierda
    def izquierda(self):
        if self.head.heading() != self.direccion['derecha']:
            self.head.setheading(self.direccion['izquierda'])
    
    def reiniciar(self):
        for parte in self.partes:
            parte.hideturtle()
        self.partes.clear()
        self.crear_serpiente()
        self.head = self.partes[0] 