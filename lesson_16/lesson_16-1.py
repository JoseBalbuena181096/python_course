import turtle as t


tortuga = t.Turtle()
ventana = t.Screen()

#mover adelante
def mover_adelante(): 
    tortuga.forward(10)

#mover atras
def mover_atras(): 
    tortuga.backward(10)

#girar derecha
def girar_derecha():
    giro = tortuga.heading() - 10
    tortuga.setheading(giro)

#girar izquierda
def girar_izquierda():
    giro = tortuga.heading() + 10
    tortuga.setheading(giro)

def limpiar():
    tortuga.clear()
    tortuga.penup()
    tortuga.home()
    tortuga.pendown()

#poner a la ventana a la escucha  
ventana.listen()
ventana.onkey(key = 'Up',fun = mover_adelante)
ventana.onkey(key = 'Down',fun = mover_atras)
ventana.onkey(key = 'Right',fun = girar_derecha)
ventana.onkey(key = 'Left',fun = girar_izquierda)
ventana.onkey(key = 'space',fun = limpiar)
ventana.exitonclick()

