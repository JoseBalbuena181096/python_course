from turtle import Turtle

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.puntuacion = 0
        self.color('white')
        self.fuente = ('Arial',20,'normal')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.write(f"Puntuación: {self.puntuacion}", align = 'center',font= self.fuente)

    def incrementar_marcador(self):       
        self.puntuacion += 1
        self.actualizar_marcador()

    def fin_juego(self):
        self.goto(0,0)
        self.write('Fin del juego.', align = 'center',font= self.fuente)
