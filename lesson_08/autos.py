from utilidades import logo
from utilidades import limpiar_consola

#crear funcion para determinar los autos recomendados de acorde al presupuesto 
def autos_posibles(autos,presupuesto):
    print('Los autos recomendados para comprar son: ')
    for auto in autos:
        if autos[auto]['precio'] <= presupuesto:
            print(f"Modelo:{auto} Precio(pesos MxN):{autos[auto]['precio']} Año:{autos[auto]['año']}")

#realizar el registro de los autos 
autos = {}
registro_fin = False
limpiar_consola()
print('Bienvenido al sistema de registro de ')
print(logo)
while not registro_fin:
    datos_auto = input('Ingrese el modelo, el año y el precio del automóvil (Pesos MxN), separados por coma.\n').lower()
    datos_auto = datos_auto.split(',')
    autos[datos_auto[0]] = {'año': int(datos_auto[1]), 'precio':int(datos_auto[2])}
    char_fin = input('Para terminar el registro ingrese s o n para continuar ingresando.\n').lower()
    if char_fin == 's':
        registro_fin = True
    elif char_fin == 'n':
        registro_fin = False
    limpiar_consola()
limpiar_consola()
#preguntar presupuesto y mostrar los autos que podría comprar 
print('Herramienta para seleccionar auto por presupuesto de ')
print(logo)
fin_herramienta = False
autos_recomendados = []
while not fin_herramienta:
    presupuesto = int(input('Ingrese el presupuesto que tiene  para su auto (Pesos MxN).\n'))
    autos_posibles(autos,presupuesto)
    char_fin = input('Para terminar la herramenta s o n para continuar cotizando.\n').lower()
    if char_fin == 's':
        fin_herramienta = True
    elif char_fin == 'n':
        fin_herramienta = False
    limpiar_consola()
    