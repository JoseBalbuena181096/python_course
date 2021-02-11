#herramienta de cifrado césar  
from arte import logo
from arte import limpiar_consola

def case(ascii_,direccion,desplazamiento,char,n):
    index = ascii_ - ord(char)
    if direccion == 'encode':
        index_desplazado = (index + desplazamiento) % n
    elif direccion == 'decode':
        index_desplazado = (index - desplazamiento) % n
    nuevo_ascii =  ord(char) + index_desplazado
    nuevo_char = chr(nuevo_ascii)
    return nuevo_char

def cifrado_cesar(data,desplazamiento,direccion):
    data_cifrada = ''
    for char in data:
        ascii_ = ord(char)
        if char.isupper():
            data_cifrada += case(ascii_,direccion,desplazamiento,'A',26)
        elif char.islower():
            data_cifrada += case(ascii_,direccion,desplazamiento,'a',26)
        elif char.isdigit():
            data_cifrada += case(ascii_,direccion,desplazamiento,'0',10)
        else:
            data_cifrada += char
    print(f"{direccion} de {data} es {data_cifrada}")


fin_herramienta   = False
while not fin_herramienta:
    print(logo)
    direccion = input("Ingresa 'encode' para encriptar o ingresa 'decode' para decodificar:\n")
    data = input("Ingresa el mensaje:\n")
    desplazamiento = int(input("Ingrese el número del desplazamiento:\n"))
    cifrado_cesar(data,desplazamiento,direccion)
    reinicio = input('Ingrese s para continuar ó  n para terminar.\n').lower()
    if reinicio == 'n':
        fin_herramienta = True
        print('Gracias por usar la herramienta...')
    limpiar_consola()