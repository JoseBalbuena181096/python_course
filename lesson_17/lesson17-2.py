import turtle as t
import time

#creamos nuestra ventana 
ventana = t.Screen()
#definimos el tamaño de la ventana
ventana.setup(width=600,height=600)
#definir el color de fondo de la ventana
ventana.bgcolor('black')
#nombre de la ventana
ventana.title('Juego de la serpiente')

#pausamos la ventana del juego
ventana.tracer(0)
#lista para almacenar las partes
partes = []
#crear el cuerpo de la serpuente cada cuadro mide 20x20 pixeles
posiciones_iniciales = [(0,0),(-20,0),(-40,0)]

for posicion in posiciones_iniciales:
    parte = t.Turtle()
    parte.shape('square')
    parte.color('white')
    parte.penup()
    parte.goto(posicion)
    partes.append(parte)


fin_juego = False

while not fin_juego:
    #actualizamos la ventana del juego
    ventana.update()
    time.sleep(0.1)    
    
    for parte in range(len(partes)-1,0,-1):
        posicion_x = partes[parte-1].xcor()
        posicion_y = partes[parte-1].ycor()
        #print(posicion_x)
        #print(posicion_y)
        partes[parte].goto(posicion_x,posicion_y)
    
    partes[0].forward(20)
    partes[0].left(90)
ventana.exitonclick()