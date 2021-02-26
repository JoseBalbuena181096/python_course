import time
from turtle import Screen
from jugador_turtle import Jugador
from meteoritos_turtle import Meteoritos
from marcador_turtle import Marcador

#creamos la ventana
ventana = Screen()
ventana.setup(width=600,height=600)
ventana.bgcolor('black')
ventana.title('Meteoro')
ventana.tracer(0)

#creamos un jugador
jugador = Jugador()
#creamos los meteoros
meteoritos =  Meteoritos()
#creamos un marcador
marcador = Marcador()

#empezamos a escuchar eventos del teclado
ventana.listen()
ventana.onkey(jugador.arriba,'Up')
ventana.onkey(jugador.abajo,'Down')
ventana.onkey(jugador.izquierda,'Left')
ventana.onkey(jugador.derecha,'Right')

velocidad_juego = 0.1
fin_juego = False
while not fin_juego:
    #pequeño retardo para que nuestro juego para que nos sea tan rapido
    time.sleep(velocidad_juego)
    ventana.update()
    #crear un meteoro a la vez
    meteoritos.crear_meteorito()
    meteoritos.mover_meteoritos()
    #Detectectar choque con algun meteoro
    for meteorito in meteoritos.meteoritos_lista:
        if meteorito.distance(jugador) < 25:
            fin_juego = True
            marcador.fin_juego()

    if jugador.llegar_meta():
        marcador.incrementar_nivel()
        velocidad_juego *= 0.9 
        jugador.ir_inicio()
        

ventana.exitonclick()
