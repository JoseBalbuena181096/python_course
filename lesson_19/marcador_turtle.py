from turtle import Turtle

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        #ocultamos la tortuga
        self.font = ('Courier',24,'normal')
        self.color('white')
        self.nivel = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.write(f'Nivel: {self.nivel}',align='left',font=self.font)

    def incrementar_nivel(self):
        self.nivel += 1
        self.actualizar_marcador()

    def fin_juego(self):
        self.goto(0, 0)
        self.write(f'Fin del juego.',align='center',font=self.font)

