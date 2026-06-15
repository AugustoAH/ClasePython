import random

# 1. >/ Funciones que no reciben parametros y no devuelven resultados.

def mostrar_bienvenida():
    # No hay parámetros de entrada entre los paréntesis.
    print("¡Bienvenido a la función de bienvenida!")
    print("Por favor, selecciona una opción del menú.")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

# Para Usar la funcion, simplemente la llamamos por su nombre seguido de paréntesis.
mostrar_bienvenida()

#>/ Funciones que reciben parametros y no devuelven resultados.

def saludar_persona(nombre, edad):
    # Recibe "nombre" y "edad" como parámetros de entrada.
    print(f"¡Hola {nombre}, veo que tienes {edad} años!")
    # No tiene return, solo imprime en pantalla el mensaje.

saludar_persona("Estrella", 45)  # Llamamos a la función con argumentos específicos.

#>/ Funciones que no reciben parametros y devuelven resultados.

def tirar_dado():
    # No recibe parámetros de entrada.
    numero_obtenido = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6.
    return numero_obtenido  # Devuelve el número obtenido.

resultado = tirar_dado()  # Llamamos a la función y almacenamos el resultado en una variable.
print(f"Has tirado el dado y obtuviste: {resultado}")  # Imprimimos el resultado.

#>/ Funciones que reciben parametros y devuelven resultados.

def calcular_area_rectangulo(base, altura):
    # Recibe los datos necesarios
    area = base * altura
    # Devuelve el resultado del cálculo
    return area

# Para usarla:
mi_area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {mi_area}")