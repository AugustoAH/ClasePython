'''
Ejercicio módulo os


OBJETIVO
Crear un script que liste archivos por tamaño en un directorio

INSTRUCCIONES
Crea un script en Python que utilice el módulo os para listar todos los archivos (no directorios) en el directorio actual, ordenados por tamaño (de mayor a menor). Para cada archivo, muestra su nombre y tamaño en bytes.

El script debe:

Obtener la lista de todos los elementos en el directorio actual
Filtrar solo los archivos (no directorios)
Obtener el tamaño de cada archivo usando las funciones apropiadas
Ordenar la lista de archivos por tamaño de forma descendente
Mostrar el nombre y tamaño de cada archivo
Puedes empezar importando el módulo os y utilizando os.listdir() para obtener los elementos del directorio actual.
'''

import os

# 1. Obtener la lista de todos los elementos del directorio actual
elementos = os.listdir('.')

# 2 y 3. Filtrar solo archivos y obtener su tamaño
archivos = []
for elemento in elementos:
    if os.path.isfile(elemento):
        tamaño = os.path.getsize(elemento)
        archivos.append((elemento, tamaño))

# 4. Ordenar por tamaño de forma descendente
archivos.sort(key=lambda x: x[1], reverse=True)

# 5. Mostrar nombre y tamaño de cada archivo
for nombre, tamaño in archivos:
    print(f"{nombre}: {tamaño} bytes")

'''------------------'''

directorio = '.'
archivos = []

for elemento in os.listdir(directorio):
    ruta = os.path.join(directorio, elemento)
    if os.path.isfile(ruta):
        archivos.append((elemento, os.path.getsize(ruta)))

archivos.sort(key=lambda x: x[1], reverse=True)

for nombre, tamaño in archivos:
    print(f"{nombre}: {tamaño} bytes")