'''
Trabajo 1: Sintaxis Python

¿QUÉ HAY QUE HACER?
Desarrollo de una calculadora de promedios escolares en Python utilizando variables, operadores, estructuras de control y funciones básicas.

PASOS A SEGUIR
Crea un nuevo archivo Python llamado calculadora_promedios.py que contendrá todo el código de tu programa.

Implementa una función llamada ingresar_calificaciones() que permita al usuario introducir el nombre de una materia y su calificación correspondiente. Esta función debe:

Solicitar al usuario que ingrese el nombre de la materia
Solicitar la calificación (validando que sea un número entre 0 y 10)
Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
Preguntar si desea continuar ingresando más materias
Retornar ambas listas cuando el usuario decida terminar
Crea una función calcular_promedio(calificaciones) que reciba una lista de calificaciones y devuelva el promedio de todas ellas.

Desarrolla una función determinar_estado(calificaciones, umbral) que reciba la lista de calificaciones y un valor umbral (por defecto 5.0), y devuelva dos listas: una con los índices de las materias aprobadas y otra con los índices de las reprobadas.

Implementa una función encontrar_extremos(calificaciones) que identifique el índice de la calificación más alta y el índice de la más baja en la lista de calificaciones.

En la función principal (main), llama a la función ingresar_calificaciones() para obtener los datos del usuario.

Utiliza las funciones creadas para calcular el promedio general, determinar materias aprobadas/reprobadas y encontrar las materias con calificaciones extremas.

Muestra un resumen final que incluya:

Todas las materias con sus calificaciones
El promedio general
Las materias aprobadas y reprobadas
La materia con mejor calificación y su valor
La materia con peor calificación y su valor
Asegúrate de manejar casos especiales, como cuando no se ingresa ninguna materia, utilizando estructuras condicionales apropiadas.

Finaliza el programa con un mensaje de despedida e implementa la estructura if __name__ == "__main__": para ejecutar la función principal.

REQUISITOS
Crear un programa que permita al usuario ingresar nombres de materias y sus calificaciones correspondientes (valores entre 0 y 10).
Almacenar las materias y calificaciones en estructuras de datos adecuadas (listas).
Calcular y mostrar el promedio general de todas las calificaciones ingresadas.
Determinar qué materias están aprobadas y reprobadas según un umbral definido (5.0).
Identificar y mostrar la materia con la calificación más alta y la más baja.
Permitir al usuario agregar tantas materias como desee, con opción para finalizar la entrada de datos.
Mostrar un resumen final con toda la información procesada de forma clara.
Utilizar exclusivamente programación estructurada (sin clases ni POO).
Implementar al menos 3 funciones diferentes para organizar el código.
Incluir validación básica de entradas para evitar errores.

'''

"""
calculadora_promedios.py

Calculadora de promedios escolares.
Permite ingresar materias y calificaciones, calcular el promedio general,
determinar materias aprobadas/reprobadas e identificar las calificaciones
extremas (mejor y peor).

Programación estructurada (sin clases ni POO).
"""


def ingresar_calificaciones():
    """
    Solicita al usuario el nombre de cada materia y su calificacion.
    Valida que la calificacion sea un numero entre 0 y 10.
    Devuelve dos listas: nombres de materias y calificaciones.
    """
    materias = []
    calificaciones = []

    print("=== INGRESO DE CALIFICACIONES ===\n")

    while True:
        # Nombre de la materia (no puede estar vacio)
        nombre = input("Nombre de la materia: ").strip()
        while nombre == "":
            print("  El nombre no puede estar vacio.")
            nombre = input("Nombre de la materia: ").strip()

        # Calificacion con validacion: debe ser un numero entre 0 y 10
        while True:
            entrada = input(f"Calificacion de '{nombre}' (0 a 10): ").strip()
            try:
                nota = float(entrada)
            except ValueError:
                print("  Error: debes introducir un numero. Intentalo de nuevo.")
                continue

            if 0 <= nota <= 10:
                break
            else:
                print("  Error: la calificacion debe estar entre 0 y 10.")

        # Almacenar ambos datos en sus listas correspondientes
        materias.append(nombre)
        calificaciones.append(nota)

        # Preguntar si desea continuar
        continuar = input("¿Deseas ingresar otra materia? (s/n): ").strip().lower()
        print()
        if continuar != "s":
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Recibe una lista de calificaciones y devuelve su promedio.
    Devuelve 0 si la lista esta vacia (evita la division por cero).
    """
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Recibe la lista de calificaciones y un umbral (por defecto 5.0).
    Devuelve dos listas de indices: aprobadas y reprobadas.
    """
    aprobadas = []
    reprobadas = []

    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Identifica el indice de la calificacion mas alta y el de la mas baja.
    Devuelve una tupla (indice_mejor, indice_peor).
    Devuelve (None, None) si la lista esta vacia.
    """
    if not calificaciones:
        return None, None

    indice_mejor = 0
    indice_peor = 0

    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_mejor]:
            indice_mejor = i
        if calificaciones[i] < calificaciones[indice_peor]:
            indice_peor = i

    return indice_mejor, indice_peor


def main():
    """Funcion principal que coordina todo el programa."""
    print("BIENVENIDO A LA CALCULADORA DE PROMEDIOS ESCOLARES\n")

    # Obtener los datos del usuario
    materias, calificaciones = ingresar_calificaciones()

    # Caso especial: no se ingreso ninguna materia
    if len(calificaciones) == 0:
        print("No se ingreso ninguna materia. No hay nada que calcular.")
        print("\n¡Hasta pronto!")
        return

    umbral = 5.0

    # Usar las funciones para procesar los datos
    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones, umbral)
    indice_mejor, indice_peor = encontrar_extremos(calificaciones)

    # Mostrar el resumen final
    print("=" * 40)
    print("              RESUMEN FINAL")
    print("=" * 40)

    print("\nMaterias y calificaciones:")
    for i in range(len(materias)):
        print(f"  - {materias[i]}: {calificaciones[i]}")

    print(f"\nPromedio general: {promedio:.2f}")

    print(f"\nMaterias aprobadas (>= {umbral}):")
    if aprobadas:
        for i in aprobadas:
            print(f"  - {materias[i]}: {calificaciones[i]}")
    else:
        print("  (ninguna)")

    print(f"\nMaterias reprobadas (< {umbral}):")
    if reprobadas:
        for i in reprobadas:
            print(f"  - {materias[i]}: {calificaciones[i]}")
    else:
        print("  (ninguna)")

    print(f"\nMejor calificacion: {materias[indice_mejor]} ({calificaciones[indice_mejor]})")
    print(f"Peor calificacion:  {materias[indice_peor]} ({calificaciones[indice_peor]})")

    # Mensaje de despedida
    print("\n" + "=" * 40)
    print("¡Gracias por usar la calculadora! ¡Hasta pronto!")


if __name__ == "__main__":
    main()