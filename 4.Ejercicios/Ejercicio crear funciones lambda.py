'''
Ejercicio crear funciones lambda


OBJETIVO
Crear funciones lambda para procesar una lista de números

INSTRUCCIONES
Crea tres funciones lambda y asígnalas a variables con los siguientes nombres y comportamientos:

cuadrado: una función que reciba un número y devuelva su cuadrado.
es_par: una función que reciba un número y devuelva True si es par o False si es impar.
suma: una función que reciba dos números y devuelva su suma.
Luego, crea una lista llamada números con los valores [1, 2, 3, 4, 5] y utiliza la función map() con tu lambda cuadrado para crear una nueva lista llamada cuadrados que contenga el cuadrado de cada número.

Finalmente, utiliza la función filter() con tu lambda es_par para crear una lista llamada pares que contenga solo los números pares de la lista original.
'''

# Tres funciones lambda
cuadrado = lambda n: n ** 2
es_par = lambda n: n % 2 == 0
suma = lambda a, b: a + b

# Lista original
números = [1, 2, 3, 4, 5]

# map() con cuadrado para obtener los cuadrados
cuadrados = list(map(cuadrado, números))

# filter() con es_par para obtener solo los pares
pares = list(filter(es_par, números))

# Comprobamos los resultados
print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Suma de 3 y 7:", suma(3, 7))
