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

totalPuntos = 27
caracteristicaInicial = 8
fuerza = caracteristicaInicial
destreza = caracteristicaInicial
constitución = caracteristicaInicial
inteligencia = caracteristicaInicial
sabiduria = caracteristicaInicial
carisma = caracteristicaInicial  



while totalPuntos != 0:
    print("Contador:", totalPuntos)
    totalPuntos -= 1

print("Te has quedado sin puntos")
