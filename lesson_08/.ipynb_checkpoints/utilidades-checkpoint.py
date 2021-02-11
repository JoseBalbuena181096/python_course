import os

logo = ''' _    _  _______   ____    _____          __  __  ______ __   __ _____   _____   ____
    /\    | |  | ||__   __| / __ \  / ____|        |  \/  ||  ____|\ \ / /|_   _| / ____| / __ \
   /  \   | |  | |   | |   | |  | || (___   ______ | \  / || |__    \ V /   | |  | |     | |  | |
  / /\ \  | |  | |   | |   | |  | | \___ \ |______|| |\/| ||  __|    > <    | |  | |     | |  | |
 / ____ \ | |__| |   | |   | |__| | ____) |        | |  | || |____  / . \  _| |_ | |____ | |__| |
/_/    \_\ \____/    |_|    \____/ |_____/         |_|  |_||______|/_/ \_\|_____| \_____| \____/
'''

def limpiar_consola():
  if os.name == "posix":
    var = "clear"
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
  os.system(var)