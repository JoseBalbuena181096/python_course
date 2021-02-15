import os

def limpiar_consola():
  if os.name == "posix":
    var = "clear"
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
  os.system(var)
  
logo = '''                                                                 
                                    \ \     / /                                  
  _ __ ___   __ _ _   _  ___  _ __   \ \   / /   _ __ ___   ___ _ __   ___  _ __ 
 | '_ ` _ \ / _` | | | |/ _ \| '__|   > > < <   | '_ ` _ \ / _ \ '_ \ / _ \| '__|
 | | | | | | (_| | |_| | (_) | |     / /   \ \  | | | | | |  __/ | | | (_) | |   
 |_| |_| |_|\__,_|\__, |\___/|_|    /_/     \_\ |_| |_| |_|\___|_| |_|\___/|_|   
                   __/ |                                                         
                _ |___/            _                                             
               | |   | |          (_)                                            
    _ __   ___ | |__ | | __ _  ___ _  ___  _ __                                  
   | '_ \ / _ \| '_ \| |/ _` |/ __| |/ _ \| '_ \                                 
   | |_) | (_) | |_) | | (_| | (__| | (_) | | | |                                
   | .__/ \___/|_.__/|_|\__,_|\___|_|\___/|_| |_|                                
   | |                                                                           
   |_|                                         
                                                            By Iron Makers.                                  
'''
contra = '''
 __   _____
 \ \ / / __|  
  \ V /\__ \_ 
   \_/ |___(_)
'''

paises = [
{
'China' : 1406828000
},
{
'India' : 1380602000
},
{
'Estados Unidos' : 332977000
},
{
'Indonesia' : 272839000
},
{
'Pakistán' : 227351000
},
{
'Nigeria' : 223307000
},
{
'Brasil' : 212163000
},
{
'Bangladés' : 171211000
},
{
'Rusia' : 146679000
},
{
'México' : 127206000
},
{
'Japón' : 125570000
},
{
'Filipinas' : 109526000
},
{
'República Democrática del Congo' : 103693000
},
{
'Etiopía' : 102176000
},
{
'Egipto' : 101993000
},
{
'Vietnam' : 98153000
},
{
'Turquía' : 84358000
},
{
'Irán' : 84333000
},
{
'Alemania' : 83273000
},
{
'Tailandia' : 68352000
},
{
'Reino Unido' : 67374000
},
{
'Francia' : 65257000
},
{
'Sudáfrica' : 60110000
},
{
'Italia' : 59432000
},
{
'Tanzania' : 56761000
},
{
'Birmania' : 55247000
},
{
'Corea del Sur' : 51836000
},
{
'Colombia' : 50869000
},
{
'Kenia' : 48909000
},
{
'España' : 47557000
},
{
'Argentina' : 45599000
},
{
'Sudán' : 45155000
},
{
'Argelia' : 44636000
},
{
'Uganda' : 42255000
},
{
'Ucrania' : 41612000
},
{
'Irak' : 40674000
},
{
'Polonia' : 38387000
},
{
'Canadá' : 38111000
},
{
'Marruecos' : 36043000
},
{
'Arabia Saudita' : 35467000
},
{
'Uzbekistán' : 34537000
},
{
'Malasia' : 33771000
},
{
'Afganistán' : 33264000
},
{
'Perú' : 33177000
},
{
'Angola' : 31613000
},
{
'Ghana' : 31300000
},
{
'Mozambique' : 30516000
},
{
'Yemen' : 30230000
},
{
'Nepal' : 30193000
},
{
'Venezuela​' : 28597000
},
{
'Costa de Marfil' : 26792000
},
{
'Madagascar' : 26629000
},
{
'Australia' : 25878000
},
{
'Corea del Norte' : 25652000
},
{
'Camerún' : 25259000
},
{
'Níger' : 23653000
},
{
'República de China (o Taiwán)​' : 23649000
},
{
'Sri Lanka' : 21978000
},
{
'Burkina Faso' : 21855000
},
{
'Malí' : 20851000
},
{
'Chile' : 19598000
},
{
'Rumania' : 19249000
},
{
'Kazajistán' : 18875000
},
{
'Malaui' : 18783000
},
{
'Zambia' : 18144000
},
{
'Ecuador' : 17664000
},
{
'Siria' : 17488000
},
{
'Países Bajos' : 17483000
},
{
'Guatemala' : 16988000
},
{
'Senegal' : 16963000
},
{
'Chad' : 16529000
},
{
'Somalia' : 16087000
},
{
'Camboya' : 15629000
},
{
'Zimbabue' : 15599000
},
{
'Sudán del Sur' : 13551000
},
{
'Ruanda' : 12822000
},
{
'Guinea' : 12711000
},
{
'Benín' : 12310000
},
{
'Túnez' : 11841000
},
{
'Haití' : 11827000
},
{
'Bolivia' : 11716000
},
{
'Grecia' : 11713000
},
{
'Bélgica' : 11561000
},
{
'Burundi' : 11350000
},
{
'Cuba' : 11305000
},
{
'Jordania' : 10980000
},
{
'República Checa' : 10712000
},
{
'República Dominicana' : 10496000
},
{
'Suecia' : 10394000
},
{
'Portugal' : 10248000
},
{
'Azerbaiyán' : 10154000
},
{
'Emiratos Árabes Unidos' : 9996000
},
{
'Hungría' : 9760000
},
{
'Tayikistán' : 9505000
},
{
'Bielorrusia' : 9390000
},
{
'Honduras' : 9379000
},
{
'Israel' : 9308000
},
{
'Papúa Nueva Guinea' : 9038000
},
{
'Austria' : 8951000
},
{
'Suiza' : 8690000
},
{
'Sierra Leona' : 8245000
},
{
'Togo' : 7811000
},
{
'Hong Kong (China)' : 7517000
},
{
'Paraguay' : 7303000
},
{
'Laos' : 7302000
},
{
'Líbano' : 6991000
},
{
'Libia' : 6918000
},
{
'Bulgaria' : 6905000
},
{
'Serbia' : 6896000
},
{
'El Salvador' : 6797000
},
{
'Kirguistán' : 6643000
},
{
'Nicaragua' : 6630000
},
{
'Turkmenistán' : 6083000
},
{
'Dinamarca' : 5844000
},
{
'Singapur' : 5677000
},
{
'República del Congo' : 5603000
},
{
'Finlandia' : 5536000
},
{
'Eslovaquia' : 5466000
},
{
'Noruega' : 5398000
},
{
'Palestina​' : 5166000
},
{
'Costa Rica' : 5138000
},
{
'Nueva Zelanda' : 5126000
},
{
'Irlanda' : 5020000
},
{
'República Centroafricana' : 4862000
},
{
'Liberia' : 4620000
},
{
'Kuwait' : 4561000
},
{
'Omán' : 4474000
},
{
'Panamá' : 4309000
},
{
'Mauritania' : 4221000
},
{
'Croacia' : 4095000
},
{
'Georgia​' : 3716000
},
{
'Eritrea' : 3569000
},
{
'Uruguay' : 3538000
},
{
'Bosnia y Herzegovina' : 3265000
},
{
'Puerto Rico (EE. UU.)' : 3191000
},
{
'Mongolia' : 3171000
},
{
'Armenia' : 2951000
},
{
'Catar' : 2861000
},
{
'Albania' : 2834000
},
{
'Lituania' : 2795000
},
{
'Jamaica' : 2725000
},
{
'Moldavia' : 2581000
},
{
'Namibia' : 2529000
},
{
'Botsuana' : 2396000
},
{
'Gambia' : 2262000
},
{
'Gabón' : 2252000
},
{
'Eslovenia' : 2103000
},
{
'Macedonia del Norte' : 2077000
},
{
'Lesoto' : 2072000
},
{
'Letonia' : 1894000
},
{
'Kosovo​' : 1809000
},
{
'Guinea-Bisáu' : 1640000
},
{
'Baréin' : 1630000
},
{
'Guinea Ecuatorial' : 1480000
},
{
'Timor Oriental' : 1446000
},
{
'Trinidad y Tobago' : 1370000
},
{
'Estonia' : 1333000
},
{
'Mauricio' : 1272000
},
{
'Yibuti' : 1124000
},
{
'Suazilandia (o Esuatini)' : 1122000
},
{
'Comoras' : 909000
},
{
'Chipre' : 900000
},
{
'Fiyi' : 897000
},
{
'Reunión (Francia)' : 871000
},
{
'Guyana' : 788000
},
{
'Bután' : 753000
},
{
'Macao (China)' : 706000
},
{
'Islas Salomón' : 705000
},
{
'Luxemburgo' : 639000
},
{
'Montenegro' : 622000
},
{
'República Árabe Saharaui Democrática' : 604000
},
{
'Surinam' : 590000
},
{
'Cabo Verde' : 560000
},
{
'Malta' : 537000
},
{
'Brunéi' : 487000
},
{
'Belice' : 425000
},
{
'Bahamas' : 391000
},
{
'Maldivas' : 388000
},
{
'Guadalupe (Francia)' : 387000
},
{
'Islandia' : 370000
},
{
'Martinica (Francia)' : 364000
},
{
'Vanuatu' : 298000
},
{
'Guayana Francesa' : 296000
},
{
'Mayotte (Francia)' : 290000
},
{
'Barbados' : 287000
},
{
'Polinesia Francesa' : 279000
},
{
'Nueva Caledonia (Francia)' : 273000
},
{
'Santo Tomé y Príncipe' : 213000
},
{
'Samoa' : 199000
},
{
'Santa Lucía' : 185000
},
{
'Guam (EE. UU.)' : 177000
},
{
'Curazao (PB)' : 157000
},
{
'Kiribati' : 120000
},
{
'Aruba (PB)' : 113000
},
{
'Granada' : 113000
},
{
'San Vicente y las Granadinas' : 111000
},
{
'Jersey (RU)' : 109000
},
{
'Micronesia' : 106000
},
{
'Islas Vírgenes de los Estados Unidos' : 104000
},
{
'Tonga' : 100000
},
{
'Antigua y Barbuda' : 99000
},
{
'Seychelles' : 99000
},
{
'Isla de Man (RU)' : 82000
},
{
'Andorra' : 79000
},
{
'Islas Caimán (RU)' : 72000
},
{
'Dominica' : 72000
},
{
'Bermudas (RU)' : 64000
},
{
'Guernsey (RU)' : 63000
},
{
'Samoa Americana (EE. UU.)' : 57000
},
{
'Groenlandia (Dinamarca)' : 56000
},
{
'Islas Marianas del Norte (EE. UU.)' : 56000
},
{
'Islas Marshall' : 55000
},
{
'Islas Feroe (Dinamarca)' : 53000
},
{
'San Cristóbal y Nieves' : 53000
},
{
'Islas Turcas y Caicos (RU)' : 46000
},
{
'San Martín (PB)' : 44000
},
{
'Liechtenstein' : 39000
},
{
'Mónaco' : 38000
},
{
'San Martín (Francia)' : 35000
},
{
'Gibraltar (RU)​' : 34000
},
{
'San Marino' : 34000
},
{
'Åland (Finlandia)' : 30000
},
{
'Islas Vírgenes Británicas (RU)' : 30000
},
{
'Caribe Neerlandés (PB)' : 26000
},
{
'Palaos' : 18000
},
{
'Anguila (RU)' : 15000
},
{
'Islas Cook (NZ)' : 15000
},
{
'Nauru' : 12000
},
{
'San Bartolomé (Francia)' : 11000
},
{
'Tuvalu' : 11000
},
{
'Wallis y Futuna (Francia)' : 11000
},
{
'San Pedro y Miquelón (Francia)' : 6000
},
{
'Santa Elena, Ascensión y Tristán de Acuña (RU)' : 6000
},
{
'Montserrat (RU)' : 5000
},
{
'Islas Malvinas (RU)​' : 4000
},
{
'Svalbard y Jan Mayen (Noruega)' : 3000
},
{
'Isla de Navidad (Australia)' : 2000
},
{
'Niue (NZ)' : 2000
},
{
'Isla Norfolk (Australia)' : 2000
},
{
'Tokelau (NZ)' : 2000
},
{
'Ciudad del Vaticano' : 1000
},
{
'Islas Cocos (Australia)' : 500
},
{
'Islas Ultramarinas Menores de los Estados Unidos' : 100
},
{
'Islas Pitcairn (RU)' : 50
}
]
