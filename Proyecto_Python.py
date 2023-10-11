#!/usr/bin/python3Al

# La idea es realizar una aplicación que te monte un personaje de DnD
# en base a tu selección

import requests
import json

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
print('****************************')

if razasdata.status_code == 200:
    dataraz = razasdata.json()
    print('Elija su raza de las presentadas a continuación: ')
    for e in dataraz['results']:
        print(' ' + e['index'])

    razaseleccionada = input('Elija su raza: ')
    
# Aqui elegiremos la clase

print('****************************')
if clasesdata.status_code == 200:
    dataclas = clasesdata.json()
    print('Elija una clase de las presentadas a continuación')
    for i in dataclas['results']:
        print(' ' + i['index'])
    
    
    claseseleccionada = input('Elija su clase: ')
    
# Output de la clase
print('Su personaje es: ', nombre," el ", claseseleccionada, " ", razaseleccionada )     

# Aqui calcularemos las estadisticas del personaje 
# Se calculará siguiente un sistema de point buy
# Es decir, se te asigna un total de puntos
# con el cual comprar el valor de tus estadisticas

# Creamos un diccionario que almacena las caracteristicas

totalPuntos = 27
diccionarioCaracteristicas = {
    "fuerza": 8,
    "destreza": 8,
    "inteligencia": 8,
    "sabiduria": 8,
    "constitución": 8,
    "carisma": 8
}

# Aquí se calculan los puntos

while totalPuntos != 0:
    print("Aquí está tu total de puntos:", totalPuntos)
    print("para construir tu personaje tendras que asignarle estadisticas")
    print("Puedes elegir entre: Fuerza, Destreza, Inteligencia, Sabiduria, Constitución, Carisma")
    print('¿En qué quieres gastartelos?')
    compra = input()
    if compra.lower() == 'fuerza':
        diccionarioCaracteristicas['fuerza'] = diccionarioCaracteristicas['fuerza'] + 1
        if diccionarioCaracteristicas['fuerza'] ==
    totalPuntos -= 1

print("Te has quedado sin puntos")
print("Tus estadisticas son: ")
print('****************************')
print('FUERZA: '+ str(diccionarioCaracteristicas['fuerza']))
print('DESTREZA: '+ str(diccionarioCaracteristicas['destreza']))
print('INTELIGENCIA: '+ str(diccionarioCaracteristicas['inteligencia']))
print('SABIDURIA: '+ str(diccionarioCaracteristicas['sabiduria']))
print('CARISMA: '+ str(diccionarioCaracteristicas['carisma']))
print('CONSTITUCIÓN: '+ str(diccionarioCaracteristicas['constitución']))
