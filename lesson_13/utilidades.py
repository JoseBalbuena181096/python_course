import os

def limpiar_consola():
  if os.name == "posix":
    var = "clear"
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
  os.system(var)

logo = """
                  ___           ___                    ___           ___           ___           ___           ___     
    ___          /  /\         /  /\                  /  /\         /  /\         /  /\         /  /\         /__/\    
   /  /\        /  /:/        /  /:/_                /  /:/        /  /::\       /  /:/_       /  /::\       |  |::\   
  /  /:/       /  /:/        /  /:/ /\              /  /:/        /  /:/\:\     /  /:/ /\     /  /:/\:\      |  |:|:\  
 /__/::\      /  /:/  ___   /  /:/ /:/_            /  /:/  ___   /  /:/~/:/    /  /:/ /:/_   /  /:/~/::\   __|__|:|\:\ 
 \__\/\:\__  /__/:/  /  /\ /__/:/ /:/ /\          /__/:/  /  /\ /__/:/ /:/___ /__/:/ /:/ /\ /__/:/ /:/\:\ /__/::::| \:
    \  \:\/\ \  \:\ /  /:/ \  \:\/:/ /:/          \  \:\ /  /:/ \  \:\/:::::/ \  \:\/:/ /:/ \  \:\/:/__\/ \  \:\~~\__\/
     \__\::/  \  \:\  /:/   \  \::/ /:/            \  \:\  /:/   \  \::/~~~~   \  \::/ /:/   \  \::/       \  \:\      
     /__/:/    \  \:\/:/     \  \:\/:/              \  \:\/:/     \  \:\        \  \:\/:/     \  \:\        \  \:\     
     \__\/      \  \::/       \  \::/                \  \::/       \  \:\        \  \::/       \  \:\        \  \:\    
                 \__\/         \__\/                  \__\/         \__\/         \__\/         \__\/         \__\/   

                                                                                          By Iron Makers.
"""

ice_cream = """
       ()
      (__)
     (____)
    (______)
   (________)
  (__________)
   \/\/\/\/\/
    \/\/\/\/
     \/\/\/
      \/\/
       \/
"""