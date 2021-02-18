import turtle as t

#creamos nuestra ventana 
ventana = t.Screen()
#definimos el tamaño de la ventana
ventana.setup(width=600,height=600)
#definir el color de fondo de la ventana
ventana.bgcolor('black')
#nombre de la ventana
ventana.title('Juego de la serpiente')

#crear el cuerpo de la serpuente cada cuadro mide 20x20 pixeles
posiciones_iniciales = [(0,0),(-20,0),(-40,0)]
for posicion in posiciones_iniciales:
    parte = t.Turtle()
    parte.shape('square')
    parte.color('white')
    parte.goto(posicion)

ventana.exitonclick()