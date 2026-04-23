'''
DICCIONARIO EN PYTHON

Los diccionarios son un conjunto de elementos no ordenados, mutables e indexados por claves, que pueden contener datos de diferentes tipos, 
por ejemplo pueden contener números, cadenas de texto, otras listas, etc.

Esta colección de elementos pares llave-valor (key-value) en lugar de indices para acceder a los elementos, se utilizan las claves.

Las claves deben ser únicas dentro del diccionario y pueden ser de cualquier tipo inmutable, como cadenas de texto, números o tuplas.

──▶ Sintaxis de un diccionario
    Diccionario = {clave1: valor1, clave2: valor2, clave3: valor3, ..., claveN: valorN}

──▶ Un diccionario de textos
    persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}    

──▶ Un diccionario mezclado
    Diccionario = {"numero": 56, "lenguaje": "Python", "pi": 3.14, "lista": [1,2,3], "booleano": True}

──▶ Un diccionario vacío (diccionario para ser llenado después)
    mochila = {}   

──▶ Crear un diccionario a partir de una lista de tuplas
    tuplas = [("marca", "APC"), ("voltaje", 120), ("baterias", 4)]
    diccionario = dict(tuplas) # dict(lista_de_tuplas)      

──▶ Crear un diccionario a partir de dos listas (una de claves y otra de valores)
    claves = ["marca", "voltaje", "baterias"]
    valores = ["APC", 120, 4]
    diccionario = dict(zip(claves, valores)) # dict(zip(lista_claves, lista_valores))   

──▶ Crear un diccionario a partir de una lista de claves con un valor predeterminado
    claves = ["marca", "voltaje", "baterias"]
    valor_predeterminado = None
    diccionario = dict.fromkeys(claves, valor_predeterminado) # dict.fromkeys(lista_claves, valor_predeterminado)

──▶ Crear un diccionario a partir de un conjunto de pares clave-valor utilizando argumentos de palabras clave
    diccionario = dict(marca="APC", voltaje=120, baterias=4) # dict(clave1=valor1, clave2=valor2, clave3=valor3, ...)   

──▶ Crear un diccionario a partir de un conjunto de pares clave-valor utilizando una comprensión de diccionario
    claves = ["marca", "voltaje", "baterias"]
    valores = ["APC", 120, 4]
    diccionario = {clave: valor for clave, valor in zip(claves, valores)} # {clave: valor for clave, valor in zip(lista_claves, lista_valores)} 

──▶ Crear un diccionario a partir de un conjunto de pares clave-valor utilizando la función dict() con argumentos de palabras clave
    diccionario = dict(marca="APC", voltaje=120, baterias=4) # dict(clave1=valor1, clave2=valor2, clave3=valor3, ...)    

──▶ Crear un diccionario a partir de un conjunto de pares clave-valor utilizando la función dict() con una lista de tuplas
    tuplas = [("marca", "APC"), ("voltaje", 120), ("baterias", 4)]
    diccionario = dict(tuplas) # dict(lista_de_tuplas)      

──▶  Crear diccionarios vacios utilizando la función dict()
    diccionario_vacio1 = dict() # dict()

1) Reglas sobre las llaves en un diccionario:

* Son unicas: No pueden haber duplicidad en la llave, si se hace la asignación de un valor a una llave que ya existe, 
el valor anterior será sobrescrito por el nuevo valor.

* Son inmutables: Las llaves suelen ser textos (string) o numeros, No se puede usar una lista como llave, 
pero si se puede usar una tupla como llave, siempre y cuando la tupla contenga elementos inmutables.
      

         { DICCIONARIO }
    _______________________
   |   Clave    |   Valor  |  <-- Relación (Mapping)
   |  "marca"   |  "APC"   |  <-- Par 1
   | "voltaje"  |   120    |  <-- Par 2
   | "baterias" |    4     |  <-- Par 3
   |____________|__________|
         |            |
      (Buscas)    (Obtienes)
         ▼            ▼             

En los diccionarios, cada elemento tiene una clave que se utiliza para acceder a su valor correspondiente. 
Por ejemplo, en el diccionario persona, "nombre" es una clave que se utiliza para acceder al valor "Juan", "edad" 
es una clave que se utiliza para acceder al valor 30 y "ciudad" es una clave que se utiliza para acceder al valor "Madrid". 

2) Operaciones básicas con diccionarios:
* Acceder: diccionario["clave"] o diccionario.get("clave")
* Modificar: diccionario["clave"] = nuevo_valor
* Agregar: diccionario["nueva_clave"] = valor
* Eliminar: del diccionario["clave"] o diccionario.pop("clave")
* Verificar existencia: "clave" in diccionario  

3. Funciones para trabajar con diccionarios:
    - keys(): Devuelve una vista de las claves del diccionario.
    - values(): Devuelve una vista de los valores del diccionario.
    - items(): Devuelve una vista de los pares clave-valor del diccionario.
    - get(): Devuelve el valor asociado a una clave específica, o un valor predeterminado si la clave no existe.
    - pop(): Elimina un par clave-valor específico y devuelve su valor.
    - clear(): Elimina todos los elementos del diccionario.

'''
# Ejemplo de uso de keys(), values() e items()
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(persona.keys())   # Salida: dict_keys(['nombre', 'edad', 'ciudad'])
print(persona.values()) # Salida: dict_values(['Juan', 30, 'Madrid'])
print(persona.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])

# Ejemplo de uso de get()
print(persona.get("nombre"))  # Salida: 'Juan'
print(persona.get("profesion", "Desconocida"))  # Salida: 'Desconocida' (porque la clave "profesion" no existe) 

# Ejemplo de uso de pop()
edad = persona.pop("edad") # .pop("clave")
print(edad)  # Salida: 30
print(persona)  # Salida: {'nombre': 'Juan', 'ciudad': 'Madrid'} (porque el par clave-valor con la clave "edad" ha sido eliminado)

# Ejemplo de uso de clear()
persona.clear() # .clear()
print(persona)  # Salida: {} (porque todos los elementos del diccionario han sido eliminados)   

'''
list: devuelve una lista de todas las claves incluidas en un diccionario.
'''
carros = {"marca": "Toyota", "modelo": "Corolla", "año": 2020}
print(list(carros))  # Salida: ['marca', 'modelo', 'año

'''
sorter: devuelve una lista ordenada de todas las claves incluidas en un diccionario.
'''
carros = {"marca": "Toyota", "modelo": "Corolla", "año": 2020}
print(sorted(carros))  # Salida: ['año', 'marca', 'modelo']

'''
in: comprueba si una clave se encuentra en el diccionario y devuelve True o False.
'''
carros = {"marca": "Toyota", "modelo": "Corolla", "año": 2020}
print("marca" in carros)  # Salida: True
print("color" in carros)  # Salida: False           


