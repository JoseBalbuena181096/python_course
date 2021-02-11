#problema debug 
año = int(input('¿En qué año naciste ?\n'))
if año > 1980 and año < 1994:
    print('Eres millennial.')
elif año >= 1994:
    print('Eres generación Z.')