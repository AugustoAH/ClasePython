'''
Ejercicio crear funciones

OBJETIVO
Crear una función que calcule el área de un rectángulo

INSTRUCCIONES
Crea una función llamada calcular_area_rectangulo que reciba dos parámetros: base y altura. La función debe calcular y retornar el 
área del rectángulo (base × altura).

Luego, llama a la función con los valores 5 y 3, y almacena el resultado en una variable llamada area. Finalmente, imprime el resultado 
con un mensaje descriptivo.

'''

def calcular_area_rectangulo(base, altura):
    return base * altura


# Llamamos a la función con los valores 5 y 3
area = calcular_area_rectangulo(5, 3)

# Imprimimos el resultado con un mensaje descriptivo
print(f"El área del rectángulo es: {area}")