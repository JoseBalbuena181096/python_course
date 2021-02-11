from utilidades import logo
from utilidades import limpiar_consola

def suma(n1,n2):
    return n1 + n2
def resta(n1,n2):
    return n1 - n2
def producto(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2

operaciones = {
    '+' : suma,
    '-' : resta,
    '*' : producto,
    '/' : division
} 

def calculadora():
    limpiar_consola()
    print(logo)
    n_primero = float(input('Ingrese el primer número\n'))
    continuar_operando = True
    while continuar_operando:
        seleccion_operacion = input('¿Qué operación desea realizar? " + , - , * , / "\n')
        operacion = operaciones[seleccion_operacion]
        n_siguiente = float(input('Ingrese el siguiente número\n'))
        resultado = operacion(n_primero,n_siguiente)
        print(f'{n_primero} {seleccion_operacion} {n_siguiente} = {resultado}')
        eleccion = input('Si desea continuar con las operacione con ingrese C , si desea resetear la calculadora ingrese R, si desea finalizar ingrese F.\n').upper()
        if eleccion == 'C':
            n_primero = resultado
        elif eleccion == 'R':
            continuar_operando = False
            limpiar_consola()
            calculadora()
        elif eleccion == 'F':
            continuar_operando = False
            limpiar_consola()

calculadora()

