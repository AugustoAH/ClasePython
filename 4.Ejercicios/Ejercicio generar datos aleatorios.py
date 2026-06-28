'''
Ejercicio generar datos aleatorios

OBJETIVO
Crear una función que genere datos aleatorios para un conjunto de usuarios


INSTRUCCIONES
Crea una función llamada generar_usuarios que genere datos aleatorios para un conjunto de usuarios. La función debe recibir como parámetro el número de usuarios a generar y devolver una lista de diccionarios, donde cada diccionario representa un usuario con los siguientes campos:

id: un número entero único para cada usuario (comenzando desde 1)
nombre: un nombre aleatorio elegido de una lista predefinida
edad: un número entero aleatorio entre 18 y 65
puntuación: un número flotante aleatorio entre 0.0 y 10.0 (con un decimal)
Para implementar esta función, deberás:

Crear una lista de posibles nombres (al menos 5 nombres diferentes)
Utilizar random.randint() para generar las edades
Utilizar random.uniform() para generar las puntuaciones
Redondear las puntuaciones a 1 decimal

Ejemplo de uso:

usuarios = generar_usuarios(3)
print(usuarios)


Ejemplo de salida:

[
  {'id': 1, 'nombre': 'Ana', 'edad': 25, 'puntuacion': 8.7},
  {'id': 2, 'nombre': 'Carlos', 'edad': 42, 'puntuacion': 6.3},
  {'id': 3, 'nombre': 'Elena', 'edad': 31, 'puntuacion': 9.5}
]
'''

import random

def generar_usuarios(cantidad):
    nombres = ['Ana', 'Carlos', 'Elena', 'David', 'Lucía', 'Javier', 'Marta']
    usuarios = []

    for i in range(1, cantidad + 1):
        usuario = {
            'id': i,
            'nombre': random.choice(nombres),
            'edad': random.randint(18, 65),
            'puntuacion': round(random.uniform(0.0, 10.0), 1)
        }
        usuarios.append(usuario)

    return usuarios


# Ejemplo de uso
usuarios = generar_usuarios(3)
print(usuarios)

'''-------------------------------------------------'''

def generar_usuarios_dos(cantidad):
    nombres = ['Ana', 'Carlos', 'Elena', 'David', 'Lucía', 'Javier', 'Marta']
    return [
        {
            'id': i,
            'nombre': random.choice(nombres),
            'edad': random.randint(18, 65),
            'puntuacion': round(random.uniform(0.0, 10.0), 1)
        }
        for i in range(1, cantidad + 1)
    ]
# Ejemplo de uso
usuarios_dos = generar_usuarios_dos(3)
print(usuarios_dos)