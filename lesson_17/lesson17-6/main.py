import turtle as t
from serpiente_turtle import Serpiente
from comida_turtle import Comida
from marcador_turtle import Marcador
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
comida = Comida()
marcador = Marcador()

ventana.listen()
ventana.onkey(serpiente.derecha,'Right')
ventana.onkey(serpiente.izquierda,'Left')
ventana.onkey(serpiente.arriba,'Up')
ventana.onkey(serpiente.abajo,'Down')

fin_juego = False

while not fin_juego:
    #actualizamos la ventana del juego
    ventana.update()
    time.sleep(0.1)    
    serpiente.mover()
    #Serpiente detecta comida
    if serpiente.head.distance(comida) < 15:
        #print('comi')
        comida.nueva_posicion()
        serpiente.crecer()
        marcador.incrementar_marcador()

    posicion_x = serpiente.head.xcor()
    posicion_y = serpiente.head.ycor()
    if posicion_x > 280.0 or posicion_x < -280.0 or posicion_y > 280.0 or posicion_y < -280.0:
        marcador.fin_juego()
        fin_juego = True
    #detectar si la serpiente se come asi misma
    for parte in serpiente.partes[1:]:
        if serpiente.head.distance(parte)<10:
            marcador.fin_juego()
            fin_juego = True
        
ventana.exitonclick()