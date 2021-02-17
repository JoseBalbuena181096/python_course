#!/usr/bin/env python3
#importamos el módulo turtle
import turtle
#creamos un escenario para colocar nuestra tortuga 
escenario  = turtle.Screen()
#escenario de color azul
escenario .bgcolor("light blue")
#creamos el objeto de nuestra tortuga  
tortuga = turtle.Turtle()
#creamos una tortuga verde
tortuga.shape('turtle')
tortuga.color('green')
#movemos 150 píxeles hacia enfrente la tortuga 
tortuga.forward(150)
#giramos 90  grados hacia la derecha
tortuga.right(90)
#movemos 150 píxeles hacia enfrente la tortuga 
tortuga.forward(150)
#detenemos la ejecución para que no se cierre inmediatamente
turtle.done()