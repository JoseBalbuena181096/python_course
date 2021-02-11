import os

logo = '''
 ______         __               __            __
|      |.---.-.|  |.----..--.--.|  |.---.-..--|  |.-----..----..---.-.
|   ---||  _  ||  ||  __||  |  ||  ||  _  ||  _  ||  _  ||   _||  _  |
|______||___._||__||____||_____||__||___._||_____||_____||__|  |___._|
                                                                          
                                                       by Iron Makers.
'''

def limpiar_consola():
  if os.name == "posix":
    var = "clear"
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
  os.system(var)