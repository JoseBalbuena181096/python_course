from utilidades import paises
from utilidades import logo
from utilidades import limpiar_consola
from utilidades import contra
from random import randint
from time import sleep

def obtener_pais():
    pais = randint(0,len(paises))
    return paises[pais]
def nombre_pais(pais):
    for nombre in pais:
        return nombre
def validar_eleccion(eleccion,poblacion_a,poblacion_b):
    if poblacion_a > poblacion_b:
        return eleccion == "A"
    else:
        return eleccion == "B"
   
def juego():
    limpiar_consola()
    print("Bienvenido al juego acierta qué país tiene ")
    print(logo)
    vidas = 3
    marcador = 0
    continuar_juego = True
    while continuar_juego and vidas > 0:
        pais_aleatorio_a = obtener_pais()    
        pais_aleatorio_b = obtener_pais()  
        while pais_aleatorio_a == pais_aleatorio_b:
            pais_aleatorio_b = obtener_pais()
        nombre_pais_a = nombre_pais(pais_aleatorio_a)
        nombre_pais_b = nombre_pais(pais_aleatorio_b)
        print(f'País A: {nombre_pais_a}.')
        print(contra)
        print(f'País B: {nombre_pais_b}.')
        eleccion = input('¿Qué país tiene mayor población? Escribe A ó B.\n').upper()
        poblacion_a = pais_aleatorio_a[nombre_pais_a]
        poblacion_b = pais_aleatorio_b[nombre_pais_b]
        eleccion = validar_eleccion(eleccion,poblacion_a,poblacion_b)
        if eleccion:
            marcador += 1
            print(f"!Correcto!, {nombre_pais_a} tiene {poblacion_a} habitantes y {nombre_pais_b} tiene {poblacion_b} habitantes.")
            print(f'Marcador {marcador}  -  Vidas {vidas}')

        else:
            vidas -= 1
            print(f"!Incorrecto!, {nombre_pais_a} tiene {poblacion_a} habitantes y {nombre_pais_b} tiene {poblacion_b} habitantes.")
            print(f'Marcador {marcador}  -  Vidas {vidas}')
        if vidas == 0:   
            print('Fin del juego ya no tienes vidas.')
            sleep(2) 
            return
        sleep(6)   
        limpiar_consola()
juego()



