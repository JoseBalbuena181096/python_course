import os
animales = ['abeja',
'aguila',
'alacran',
'araña',
'avispa',
'ballena', 
'bisonte',
'bufalo',
'burro',
'caballo',
'camello',
'canario',
'cangrejo',
'canguro',
'caracol',
'cebra',
'cerdo',
'chango',
'chimpance',
'ciervo',
'cisne', 
'cocodrilo',
'elefante',
'escarabajo',
'escorpion',
'foca',
'gallina',
'gallo',
'gato',
'golondrina',
'hipopotamo',
'hormiga', 
'jabali',
'jirafa',
'leon',
'loro',
'mosca',
'mosquito',
'oso',
'oveja', 
'perdiz',
'perro',
'pinguino', 
'pollo',
'saltamontes',
'serpiente',
'tigre', 
'topo',
'toro',
'tortuga',
'vaca',
'zorro']

estados = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
titulo = '''
 ______  _           _                                    _
|  ____|| |         | |                                  | |
| |__   | |    __ _ | |__    ___   _ __   ___   __ _   __| |  ___
|  __|  | |   / _` || '_ \  / _ \ | '__| / __| / _` | / _` | / _  
| |____ | |  | (_| || | | || (_) || |   | (__ | (_| || (_| || (_) |
|______||_|   \__,_||_| |_| \___/ |_|    \___| \__,_| \__,_| \___/

                        VERSIÓN ANIMALES 
'''

def limpiar_consola():
  if os.name == "posix":
    var = "clear"
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
  os.system(var)