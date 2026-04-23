'''
</>  Reto código

Objetivo: Crear una función que utilice Counter para analizar frecuencias de caracteres en un texto

Implementa una función llamada analizar_texto que reciba como parámetro una cadena de texto y devuelva un diccionario con las siguientes estadísticas:

    caracteres_mas_comunes: Una lista con los 3 caracteres más comunes y su frecuencia, excluyendo espacios en blanco. El formato debe ser una lista de tuplas (caracter, frecuencia).

    total_caracteres: El número total de caracteres en el texto, incluyendo espacios.

    total_sin_espacios: El número total de caracteres excluyendo espacios en blanco.

Utiliza la clase Counter del módulo collections para realizar el análisis de frecuencias.

Ejemplo de uso:

resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)
# Debería imprimir algo como:
# {'caracteres_mas_comunes': [('e', 4), ('o', 3), ('l', 2)], 'total_caracteres': 32, 'total_sin_espacios': 27}


'''
from collections import Counter

def analizar_texto(texto):
    # 1. Calcular el total de caracteres (incluyendo espacios)
    total_caracteres = len(texto)
    
    # 2. Crear una nueva cadena excluyendo TODOS los caracteres de espacio en blanco
    # Se usa una comprensión de generador junto con isspace()
    texto_sin_espacios = "".join(c for c in texto if not c.isspace())
    
    # 3. Calcular el total de caracteres sin espacios
    total_sin_espacios = len(texto_sin_espacios)
    
    # 4. Contar la frecuencia usando el texto ya filtrado
    frecuencias = Counter(texto_sin_espacios)
    
    # 5. Encontrar los 3 caracteres más comunes
    caracteres_mas_comunes = frecuencias.most_common(3)
    
    # Devolver el diccionario con las estadísticas
    return {
        "caracteres_mas_comunes": caracteres_mas_comunes,
        "total_caracteres": total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }

# Ejemplo de uso
resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)

# Otra solución 

#from collections import Counter

def analizar_texto(texto):
    """
    Analiza un texto y devuelve estadísticas sobre sus caracteres.
    
    Args:
        texto (str): El texto a analizar.
        
    Returns:
        dict: Un diccionario con las estadísticas del texto:
            - caracteres_mas_comunes: Lista de tuplas (caracter, frecuencia) de los 3 caracteres más comunes
            - total_caracteres: Número total de caracteres incluyendo espacios
            - total_sin_espacios: Número total de caracteres excluyendo espacios
    """
    # Calcular el total de caracteres incluyendo espacios
    total_caracteres = len(texto)
    
    # Calcular el total de caracteres sin espacios
    total_sin_espacios = len(texto.replace(" ", ""))
    
    # Crear un Counter excluyendo espacios en blanco
    contador = Counter([c for c in texto if c != " "])
    
    # Obtener los 3 caracteres más comunes
    caracteres_mas_comunes = contador.most_common(3)
    
    # Crear y devolver el diccionario con las estadísticas
    return {
        "caracteres_mas_comunes": caracteres_mas_comunes,
        "total_caracteres": total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }
# Ejemplo de uso
if __name__ == "__main__":
    resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
    print(resultado)

