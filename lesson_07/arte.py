import os
logo = """

Herramienta de        
       _   __                   _
      (_) / _|                 | |
  ___  _ | |_  _ __   __ _   __| |  ___     ___   ___  ___   __ _  _ __
 / __|| ||  _|| '__| / _` | / _` | / _ \   / __| / _ \/ __| / _` || '__|
| (__ | || |  | |   | (_| || (_| || (_) | | (__ |  __/\__ \| (_| || |
 \___||_||_|  |_|    \__,_| \__,_| \___/   \___| \___||___/ \__,_||_|
                                            
                                                       by Iron Makers.

"""
def limpiar_consola():
  if os.name == "posix":
    var = "clear"
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
  os.system(var)