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
print('****************************')     

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

while totalPuntos != 0 or totalPuntos < 0:
    print("Aquí está tu total de puntos:", totalPuntos)
    print("para construir tu personaje tendras que asignarle estadisticas")
    print("Puedes elegir entre: Fuerza, Destreza, Inteligencia, Sabiduria, Constitución, Carisma")
    print('¿En qué quieres gastartelos?')
    compra = input()
    if compra.lower() == 'fuerza':
        diccionarioCaracteristicas['fuerza'] = diccionarioCaracteristicas['fuerza'] + 1
        totalPuntos -=1
        if diccionarioCaracteristicas['fuerza'] == 10:
            totalPuntos -=2
        if diccionarioCaracteristicas['fuerza'] == 11:
            totalPuntos -=3 
        if diccionarioCaracteristicas['fuerza'] == 12:
            totalPuntos -=4
        if diccionarioCaracteristicas['fuerza'] == 13:
            totalPuntos -=5
        if diccionarioCaracteristicas['fuerza'] == 14:
            totalPuntos -=7
        if diccionarioCaracteristicas['fuerza'] == 15:
            totalPuntos -=9
    if compra.lower() == 'destreza':
        diccionarioCaracteristicas['destreza'] = diccionarioCaracteristicas['destreza'] + 1
        totalPuntos -=1
        if diccionarioCaracteristicas['destreza'] == 10:
            totalPuntos -=2
        if diccionarioCaracteristicas['destreza'] == 11:
            totalPuntos -=3 
        if diccionarioCaracteristicas['destreza'] == 12:
            totalPuntos -=4
        if diccionarioCaracteristicas['destreza'] == 13:
            totalPuntos -=5
        if diccionarioCaracteristicas['destreza'] == 14:
            totalPuntos -=7
        if diccionarioCaracteristicas['destreza'] == 15:
            totalPuntos -=9    
    if compra.lower() == 'sabiduría':
        diccionarioCaracteristicas['sabiduría'] = diccionarioCaracteristicas['sabiduría'] + 1
        totalPuntos -=1
        if diccionarioCaracteristicas['sabiduría'] == 10:
            totalPuntos -= 2
        if diccionarioCaracteristicas['sabiduría'] == 11:
            totalPuntos -= 3 
        if diccionarioCaracteristicas['sabiduría'] == 12:
            totalPuntos -= 4
        if diccionarioCaracteristicas['sabiduría'] == 13:
            totalPuntos -= 5
        if diccionarioCaracteristicas['sabiduría'] == 14:
            totalPuntos -= 7
        if diccionarioCaracteristicas['sabiduría'] == 15:
            totalPuntos -= 9
    if compra.lower() == 'inteligencia':
        diccionarioCaracteristicas['inteligencia'] = diccionarioCaracteristicas['inteligencia'] + 1
        totalPuntos -=1
        if diccionarioCaracteristicas['inteligencia'] == 10:
            totalPuntos -= 2
        if diccionarioCaracteristicas['inteligencia'] == 11:
            totalPuntos -= 3 
        if diccionarioCaracteristicas['inteligencia'] == 12:
            totalPuntos -= 4
        if diccionarioCaracteristicas['inteligencia'] == 13:
            totalPuntos -= 5
        if diccionarioCaracteristicas['inteligencia'] == 14:
            totalPuntos -= 7
        if diccionarioCaracteristicas['inteligencia'] == 15:
            totalPuntos -= 9
    if compra.lower() == 'constitución':
        diccionarioCaracteristicas['constitución'] = diccionarioCaracteristicas['inteligencia'] + 1
        totalPuntos -=1
        if diccionarioCaracteristicas['constitución'] == 10:
            totalPuntos -= 2
        if diccionarioCaracteristicas['constitución'] == 11:
            totalPuntos -= 3 
        if diccionarioCaracteristicas['constitución'] == 12:
            totalPuntos -= 4
        if diccionarioCaracteristicas['constitución'] == 13:
            totalPuntos -= 5
        if diccionarioCaracteristicas['constitución'] == 14:
            totalPuntos -= 7
        if diccionarioCaracteristicas['constitución'] == 15:
            totalPuntos -= 9        
    if compra.lower() == 'carisma':
        diccionarioCaracteristicas['carisma'] = diccionarioCaracteristicas['inteligencia'] + 1
        totalPuntos -=1
        if diccionarioCaracteristicas['carisma'] == 10:
            totalPuntos -= 2
        if diccionarioCaracteristicas['carisma'] == 11:
            totalPuntos -= 3 
        if diccionarioCaracteristicas['carisma'] == 12:
            totalPuntos -= 4
        if diccionarioCaracteristicas['carisma'] == 13:
            totalPuntos -= 5
        if diccionarioCaracteristicas['carisma'] == 14:
            totalPuntos -= 7
        if diccionarioCaracteristicas['carisma'] == 15:
            totalPuntos -= 9                             
    

print("Te has quedado sin puntos")
print("Tus estadisticas son: ")
print('****************************')
print('')
print('FUERZA: '+ str(diccionarioCaracteristicas['fuerza']))
print('DESTREZA: '+ str(diccionarioCaracteristicas['destreza']))
print('INTELIGENCIA: '+ str(diccionarioCaracteristicas['inteligencia']))
print('SABIDURIA: '+ str(diccionarioCaracteristicas['sabiduria']))
print('CARISMA: '+ str(diccionarioCaracteristicas['carisma']))
print('CONSTITUCIÓN: '+ str(diccionarioCaracteristicas['constitución']))
print('')
print('****************************')
