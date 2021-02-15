from utilidades import logo
from utilidades import limpiar_consola
from utilidades import ice_cream
from time import sleep

menu = {
    'fresa' :  {
        'ingredientes' : {
            'fresa' : 100,
            'conos': 1,
        }, 
        'precio' : 10 
    },
    'chocolate' : {
        'ingredientes' : {
            'chocolate' : 100,
            'conos': 1,
        }, 
        'precio' : 10 
    },
    'combinado' : {
        'ingredientes' : {

            'chocolate' : 50,
            'fresa': 50,
            'conos': 1,
        }, 
        'precio' : 12
    }
}

recursos = {
    'fresa' : 1500,
    'chocolate' : 1000,
    'conos' : 50,
    'chispas' : 450,
    'jarabe' : 300,
    'dinero' : 100,
}

encendida = True


def reporte_recursos():
    """
    esta función reporta los recursos de la máquina de helados 
    """
    print(f'Fresa: {recursos["fresa"]} ml.')
    print(f'Chocolate: {recursos["chocolate"]} ml.')
    print(f'Conos: {recursos["conos"]}')
    print(f'Chispas: {recursos["chispas"]} grs.')
    print(f'Jarabe: {recursos["jarabe"]} ml.')
    print(f'Dinero: ${recursos["dinero"]} pesos.')        

def validar_helado(ingredientes):
    """
    esta función válida si existen suficientes recursos para realizar el helado 
    """
    for elemento in ingredientes:
        if ingredientes[elemento] > recursos[elemento]:
            print(f"No hay suficiente {elemento}")
            return False
    return True

def validar_chispas():
    """
    esta función válida si desea añadir chispas a su helado y si hay suficientes 
    """
    chispas = input('¿Desea agregar chispas a su helado?, s para sí ó n para no\n').lower()
    if chispas == 's':
        if recursos['chispas'] >= 20:
            return True
        else:
            print("No hay suficientes chispas para su helado.")
            return False
    return False

def validar_jarabe():
    """
    esta función válida si desea añadir jarabe a su helado y si hay suficiente
    """
    jarabe = input('¿Desea agregar jarabe a su helado?, s para sí ó n para no\n').lower()
    if jarabe == 's':
        if recursos['jarabe'] >= 30:
            return True
        else:
            print("No hay suficiente jarabe para su helado.")
            return False
    return False

def recibir_monedas():
    """
    Esta función permite permite depositar el dinero.
    """
    total = int(input('¿Cuántas monedas de 1 peso? \n'))
    total += int(input('¿Cuántas monedas de 2 pesos? \n'))*2
    total += int(input('¿Cuántas monedas de 5 pesos? \n'))*5
    total += int(input('¿Cuántas monedas de 10 pesos? \n'))*10
    return total

def validar_pago(pago,precio_helado,chispas,jarabe):
    """
    esta función realizar la validación del pago 
    """
    if chispas:
        precio_helado += 1
    if jarabe:
        precio_helado += 2
    if pago >= precio_helado:
        cambio = pago - precio_helado
        print(f"Su cambio es de ${cambio} pesos.")
        recursos['dinero'] += precio_helado
        return True
    else:
        print("No es suficiente dinero no podemos realizar el helado, le reembolsamos su pago.")
        return False

def hacer_helado(eleccion,helado,chispas,jarabe):
    for elemento in helado['ingredientes']:
        recursos[elemento] -= helado['ingredientes'][elemento]
    print(ice_cream)
    print(f'Aqui esta tu helado de {eleccion}')
    if chispas:
        recursos['chispas'] -= 20
        print("Con chispas.")
    if jarabe:
        recursos['jarabe'] -= 30
        print("Con jarabe.")
    print('¡Disfrutar!')



while encendida:
    limpiar_consola()
    print(logo)
    eleccion = input('¿Qué helado te gustaría? (fresa, chocolate ó combinado):\n').lower()
    if eleccion == 'apagar':
        encendida = False
        limpiar_consola()
        print("Apagando ... hasta pronto.")
        sleep(2)
        limpiar_consola()
    elif eleccion == 'reporte':
        reporte_recursos()
        sleep(7)
    else:
        helado = menu[eleccion]
        if validar_helado(helado['ingredientes']):
            chispas = validar_chispas()
            jarabe = validar_jarabe()
            pago = recibir_monedas()
            if validar_pago(pago,helado['precio'],chispas,jarabe):
                hacer_helado(eleccion,helado,chispas,jarabe)
        sleep(7)
        