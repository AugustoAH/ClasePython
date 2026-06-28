'''
Ejercicio trabajar con argumentos en funciones


OBJETIVO
Crear una función que utilice *args y **kwargs para procesar datos de estudiantes

INSTRUCCIONES
Crea una función llamada procesar_estudiantes que reciba un parámetro obligatorio escuela (string) seguido de un número variable de nombres de estudiantes como argumentos posicionales (*args) y datos adicionales como argumentos con nombre (**kwargs).

La función debe:

Devolver un diccionario con la siguiente estructura:
Una clave 'escuela' con el valor del parámetro obligatorio
Una clave 'estudiantes' con la lista de nombres recibidos en *args
Una clave 'datos_adicionales' con un diccionario que contenga todos los argumentos con nombre recibidos
Ejemplo de uso:

resultado = procesar_estudiantes("IES Tecnológico", "Ana", "Carlos", "Elena", curso="1º DAW", turno="mañana")
print(resultado)
# Debería imprimir:
# {'escuela': 'IES Tecnológico', 'estudiantes': ['Ana', 'Carlos', 'Elena'], 'datos_adicionales': {'curso': '1º DAW', 'turno': 'mañana'}}

'''

def procesar_estudiantes(escuela, *args, **kwargs):
    return {
        'escuela': escuela,
        'estudiantes': list(args),
        'datos_adicionales': kwargs
    }


# Ejemplo de uso
resultado = procesar_estudiantes("IES Tecnológico", "Ana", "Carlos", "Elena", curso="1º DAW", turno="mañana")
print(resultado)