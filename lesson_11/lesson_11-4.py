#problema debug 
def doble(lista):
    lista_doble = []
    for numero in lista:
        doble_numero = numero*2
    lista_doble.append(doble_numero)
    print(lista_doble)
doble([1,2,3,4,5,6])