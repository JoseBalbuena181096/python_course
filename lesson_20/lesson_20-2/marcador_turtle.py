from turtle import Turtle

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        #nuevo -2 
        with open('/home/jose/Desktop/python_course/lesson_20/lesson_20-2/datos.txt', mode='r') as file:
            self.mayor_puntaje = int(file.read())
        self.puntuacion = 0
        self.color('brown')
        self.fuente = ('Arial',20,'normal')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.write(f"Puntuación: {self.puntuacion} Mejor Puntuación: {self.mayor_puntaje}", align = 'center',font= self.fuente)

    def incrementar_marcador(self):       
        self.puntuacion += 1
        self.actualizar_marcador()
    #nuevo
    def reiniciar(self):
        if self.puntuacion > self.mayor_puntaje:
            self.mayor_puntaje = self.puntuacion
            #nuevo-2
            with open('/home/jose/Desktop/python_course/lesson_20/lesson_20-2/datos.txt', mode='w') as data:
                data.write(f'{self.mayor_puntaje}')
        self.puntuacion = 0
        self.actualizar_marcador() 
        