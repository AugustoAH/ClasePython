'''
</>  Reto código

Objetivo: Crear y manipular una lista de números para calcular estadísticas básicas

Crea una lista llamada números que contenga los valores 10, 20, 30, 40 y 50. A continuación, realiza las siguientes operaciones:

    * Añade el número 60 al final de la lista
    * Inserta el número 15 entre el 10 y el 20
    * Elimina el número 30 de la lista
    * Calcula la suma de todos los números en la lista y guárdala en una variable llamada suma
    * Calcula el promedio de los números en la lista y guárdalo en una variable llamada promedio

    Al final, imprime la lista resultante, la suma y el promedio.

            Solución:
'''
# Ejercicio de listas en Python
# 1. Crear la lista con los valores iniciales
numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)
# 2. Añadir el número 60 al final de la lista
numeros.append(60)
print("Después de añadir 60:", numeros)
# 3. Insertar el número 15 entre el 10 y el 20
numeros.insert(1, 15)
print("Después de insertar 15:", numeros)
# 4. Eliminar el número 30 de la lista
numeros.remove(30)
print("Después de eliminar 30:", numeros)
# 5. Calcular la suma de todos los números en la lista
suma = sum(numeros)
# 6. Calcular el promedio de los números en la lista
promedio = suma / len(numeros)
# Imprimir resultados finales
print("\nResultados finales:")
print("Lista resultante:", numeros)
print("Suma de los números:", suma)
print("Promedio de los números:", promedio)


'''
La solución implementa correctamente todos los pasos solicitados en el enunciado:

    * Creas la lista numeros con [10, 20, 30, 40, 50] de forma adecuada.
    * Usas append(60) para añadir el 60 al final, tal y como se pide.
    * Usas insert(1, 15) para colocar el 15 entre 10 y 20, ya que el índice 1 es la posición correcta tras el 10.
    * Eliminas el 30 con remove(30), que es la forma más clara en este contexto.
    * Calculas la suma con suma = sum(numeros) y el promedio como suma / len(numeros), ambas operaciones son correctas y usan bien las funciones integradas de Python.
    * Imprimes la lista resultante, la suma y el promedio en el orden indicado.

El código es claro, conciso y sigue buenas prácticas básicas de Python. ¡Buen trabajo! Como mejora menor opcional, podrías imprimir 
los resultados con mensajes más descriptivos, por ejemplo: print("Lista:", numeros) o print(f"Promedio: {promedio}") para hacer la 
salida más legible para el usuario.

'''