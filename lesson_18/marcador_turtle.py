from turtle import Turtle

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.penup()
        self.hideturtle()
        self.puntaje_derecho = 0
        self.puntaje_izquierdo = 0
        self.fuente = ('Courier',70,'normal')
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.puntaje_izquierdo,align='center',font= self.fuente)
        self.goto(100,200)
        self.write(self.puntaje_derecho,align='center',font= self.fuente)

    def sumar_puntaje_derecho(self):
        self.puntaje_derecho += 1
        self.actualizar_marcador()

    def sumar_puntaje_izquierdo(self):
        self.puntaje_izquierdo += 1
        self.actualizar_marcador()