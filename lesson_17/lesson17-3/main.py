import turtle as t
from serpiente_turtle import Serpiente
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

serpiente = Serpiente()

fin_juego = False

while not fin_juego:
    #actualizamos la ventana del juego
    ventana.update()
    time.sleep(0.1)    
    serpiente.mover()
ventana.exitonclick()