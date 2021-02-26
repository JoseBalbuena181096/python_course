from turtle import Screen
from paleta_turtle import Paleta
from pelota_turtle import Pelota
from marcador_turtle import Marcador
import time

#creamos la ventana del juego de 800x600 pixeles
ventana = Screen()
#color de la ventana en negro
ventana.bgcolor('black')
#tamaño de la ventana 800 x 600
ventana.setup(width=800,height=600)
ventana.title('Ping Pong')

ventana.tracer(0)
paleta_derecha = Paleta((350,0))
paleta_izquirda = Paleta((-350,0))
pelota = Pelota()
marcador = Marcador()
ventana.listen()
ventana.onkey(paleta_derecha.arriba,'Up')
ventana.onkey(paleta_derecha.abajo,'Down')
ventana.onkey(paleta_izquirda.arriba,'w')
ventana.onkey(paleta_izquirda.abajo,'s')

fin_juego = False

while not fin_juego:
    time.sleep(pelota.velocidad_movimiento)
    ventana.update()  
    pelota.mover()

    #detectar cuando la pelota chocque con el muro 
    if pelota.ycor() > 280 or pelota.ycor() <-280:
        pelota.rebote_y()
    if pelota.distance(paleta_derecha) < 50 and pelota.xcor() > 320:
        pelota.rebote_x()
    if pelota.distance(paleta_izquirda) < 50 and pelota.xcor() <- 320:
        pelota.rebote_x()
    #detectar paleta derecha falla
    if pelota.xcor() > 380:
        marcador.sumar_puntaje_izquierdo()
        pelota.reiniciar_posicion()
        
    #detectar paleta izquierda falla
    if pelota.xcor() < -380:
        marcador.sumar_puntaje_derecho()
        pelota.reiniciar_posicion()


ventana.exitonclick()
