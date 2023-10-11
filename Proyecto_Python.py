# La idea es realizar una aplicación que te monte un personaje de DnD
# en base a tu selección

import requests

# Aqui importaremos la api de la clase que seleccionas

urlclases = 'https://www.dnd5eapi.co/api/classes'
urlrazas = 'https://www.dnd5eapi.co/api/races'

clasesdata = requests.get(urlclases)
razasdata = requests.get(urlrazas)

# Comencemos por el nombre

print('Bienvenido a la creacion de personaje')
print('Elije el nombre del mismo: ')

nombre = input()

# A continuación, definiremos la raza
if razasdata.status_code == 200:
    data = razasdata.json()
    for e in data['results']:
        print(e['index'])


# Aqui elegiremos la clase

#if data.status_code == 200:
#   data = data.json()
#    for e in data['results']:
#        resultado = e + e['index']
#        print (resultado)