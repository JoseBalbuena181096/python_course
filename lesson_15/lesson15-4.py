import turtle as t

colores = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

escenario  = t.Screen()
escenario.bgcolor('black')
tortuga = t.Turtle()
tortuga.shape('turtle')
tortuga.speed('fastest')

for i in range(360):
    tortuga.color(colores[i%6])
    tortuga.width(i/50 + 1)
    tortuga.forward(i)
    tortuga.right(59)
t.done()