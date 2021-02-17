import turtle as t
import random

ventana = t.Screen()
ventana.setup(width=500, height=400)
eleccion = ventana.textinput(title='Carrera de tortugas', prompt='¿Cuál tortuga ganará la carrera?, ingrese el color en ingles')

colores = ['blue','green','red','purple']
posiciones_y = [-120,-40,40,120]
tortugas = []

for i in range(0,4):
    nueva_tortuga = t.Turtle(shape='turtle')
    nueva_tortuga.color(colores[i])
    nueva_tortuga.penup()
    nueva_tortuga.goto(x = -225,y = posiciones_y[i])
    tortugas.append(nueva_tortuga)

if eleccion:
    fin_carrera = False

while not fin_carrera:
    for tortuga in tortugas:
        if tortuga.xcor() > 230:
            fin_carrera = True
            tortuga_ganadora = tortuga.pencolor()
            if eleccion == tortuga_ganadora:
                print(f'Ganaste felicidades la tortuga {tortuga_ganadora} gano.')
                break
            else:
                print(f'Perdiste la tortuga ganadora es {tortuga_ganadora}. ')
                break
        #incrementar posicion en x de cada tortuga
        incremento_distancia = random.randint(0,20)
        tortuga.forward(incremento_distancia)
        

ventana.exitonclick()