from utilidades import logo
from utilidades import limpiar_consola
from random import randint
from time import sleep

VIDAS_FACIL = 10
VIDAS_DIFICIL = 5

def elegir_dificultad():
    dificultad = input('¿Qué dificultad deseas?, F para fácil y D para difícil.\n').upper()
    if dificultad == 'F':
        return VIDAS_FACIL
    elif dificultad == 'D':
        return VIDAS_DIFICIL
    else:
        return -1

def verificar_numero(numero_usr,numero_mqn,turnos):
    if numero_usr > numero_mqn:
        print('‘Tu  número es grande’')
        print('Reintente adivinar...')
        sleep(3)
        return turnos-1
    elif numero_usr < numero_mqn:
        print('Tu número es pequeño')
        print('Reintente adivinar...')
        sleep(3)
        return turnos-1
    elif numero_usr == numero_mqn:
        print(f'Felicidades ganaste tu número {numero_usr} el número secreto {numero_mqn}')
        sleep(3)
        return -1

def juego():
    limpiar_consola()
    print('Bienvenido al juego de \n')
    print(logo)
    print('Piensa un número entre 0 y 100\n')
    numero_maquina = randint(0,100)
    turnos =  elegir_dificultad()
    numero_usuario = -1
    while numero_maquina != numero_usuario and turnos >= 0:
        limpiar_consola()
        #test
        #print(numero_maquina)
        print(f'Tu tienes {turnos} turnos para adivinar el número')
        numero_usuario = int(input('Ingresa un posible número .\n'))
        turnos = verificar_numero(numero_usuario,numero_maquina,turnos)
        if turnos == 0:
            limpiar_consola()
            print('Ya no tienes turnos disponibles  perdiste.')
            sleep(3)
            return

juego()
limpiar_consola()