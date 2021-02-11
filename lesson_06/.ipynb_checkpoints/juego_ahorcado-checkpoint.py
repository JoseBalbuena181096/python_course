from ahorcado import animales
from ahorcado import estados
from ahorcado import limpiar_consola
from ahorcado import titulo
import random

palabra_secreta = random.choice(animales)
#mostrar los espacios en blaco equivalentes a la longitud de la palabra secreta 
mostrar = []
for letra in palabra_secreta:
    mostrar += '_'
vidas = len(estados)-1
fin_juego = False

print(titulo)

while not fin_juego:
    #selecciona aleatoriamente una palabra de la lista de animales
    #test
    #print(palabra_secreta)
    #cambiar cada espacio en blanco por la letra que coincida con la letra del usuario  
    longitud_palabra = len(palabra_secreta)
    letra_usuario = input('Ingrese una letra del nombre del animal a divinar \n').lower()
    limpiar_consola()
    if letra_usuario in mostrar:
        print(f"Ya has usado la letra {letra_usuario}")
        continue
    for posicion in range(longitud_palabra):
        letra = palabra_secreta[posicion] 
        if letra_usuario == letra:
            mostrar[posicion] = letra
    print(f"{' '.join(mostrar)}")
    
    if not letra_usuario in palabra_secreta:
        print(f"La letra {letra_usuario} que has escogido no se está en el animal a adivinar")
        vidas -= 1
        if vidas == 0:
            fin_juego = True
            print("Perdiste 😭")
            print(f'El animal secreto es {palabra_secreta}')
            print(estados[vidas])
            break
    
    if not '_' in mostrar:
        fin_juego = True
        print("Ganaste 😎")
    print(estados[vidas])
print('Fin del juego.')