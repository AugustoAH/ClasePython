'''
CONJUNTOS EN PYTHON
Un conjunto es una colección de elementos únicos y no ordenados. En Python, los conjuntos se representan mediante la 
clase `set`. Los conjuntos son útiles para realizar operaciones como la unión, intersección, diferencia y diferencia 
simétrica entre conjuntos.


──▶ Sintaxis de un conjunto
    conjunto = {elemento1, elemento2, elemento3, ..., elementoN}
──▶ Un conjunto de números
    numeros = {1, 2, 3, 4, 5}       
──▶ Un conjunto de textos
    frutas = {"manzana", "banana", "cereza"}
──▶ Un conjunto mezclado
    conjunto = {56, "Python", 3.14, True}   
──▶ Un conjunto vacío (conjunto para ser llenado después)
    conjunto_vacio = set()  # No se pueden usar {} para crear un conjunto vacío

En los conjuntos, no se pueden tener elementos duplicados. Si intentas agregar un elemento que ya existe en el conjunto, 
no se agregará nuevamente. Además, los conjuntos no mantienen un orden específico de los elementos.

1) Funciones para agregar elementos a un conjunto:

- add(): Agrega un elemento al conjunto.
- remove(): Elimina un elemento del conjunto. Si el elemento no existe, se genera un error.
- discard(): Elimina un elemento del conjunto. Si el elemento no existe, no se genera un error.
- update(): Agrega los elementos de otro conjunto o iterable al conjunto actual.
- copy(): Crea una copia del conjunto actual.   
-clear(): Elimina todos los elementos del conjunto, dejándolo vacío.

- Union: La unión de dos conjuntos A y B es un nuevo conjunto que contiene todos los elementos de A y B, sin duplicados.
- Intersección: La intersección de dos conjuntos A y B es un nuevo conjunto que contiene solo los elementos que están presentes en ambos conjuntos.
- Diferencia: La diferencia de dos conjuntos A y B es un nuevo conjunto que contiene los elementos que están presentes en A pero no en B.
- Diferencia Simétrica: La diferencia simétrica de dos conjuntos A y B es un nuevo conjunto que contiene los elementos que están presentes en A o en B, pero no en ambos conjuntos.  

- in: El operador `in` se utiliza para verificar si un elemento está presente en un conjunto. Devuelve `True` si el elemento está en el conjunto y `False` si no lo está.
- len(): La función `len()` se utiliza para obtener el número de elementos en un conjunto. Devuelve un entero que representa la cantidad de elementos únicos en el conjunto.

'''
# Ejemplo de uso de add()
numeros = {1, 2, 3}
numeros.add(4) # .add(elemento)         
print(numeros)  # Salida: {1, 2, 3, 4}  

# Ejemplo de uso de remove()
numeros.remove(2) # .remove(elemento)
print(numeros)  # Salida: {1, 3, 4}

# Ejemplo de uso de discard()
numeros.discard(3) # .discard(elemento)
print(numeros)  # Salida: {1, 4}
numeros.discard(5) # .discard(elemento) (no genera error si el elemento no existe)
print(numeros)  # Salida: {1, 4}

# Ejemplo de uso de update()
otros_numeros = {5, 6}
numeros.update(otros_numeros) # .update(conjunto o iterable)
print(numeros)  # Salida: {1, 4, 5, 6}

# Ejemplo de uso de copy()
numeros_copia = numeros.copy() # .copy()
print(numeros_copia)  # Salida: {1, 4, 5, 6}

# Ejemplo de uso de clear()
numeros.clear() # .clear()
print(numeros)  # Salida: set() (conjunto vacío)        
# Ejemplo de operaciones entre conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión
union = A.union(B) # A | B
print(union)  # Salida: {1, 2, 3, 4, 5, 6}

# Intersección
interseccion = A.intersection(B) # A & B
print(interseccion)  # Salida: {3, 4}

# Diferencia
diferencia = A.difference(B) # A - B
print(diferencia)  # Salida: {1, 2}

# Diferencia Simétrica
diferencia_simetrica = A.symmetric_difference(B) # A ^ B
print(diferencia_simetrica)  # Salida: {1, 2, 5, 6}

# Ejemplo de uso de in
print(3 in A)  # Salida: True
print(5 in A)  # Salida: False

# Ejemplo de uso de len()
print(len(A))  # Salida: 4  

# Ejemplo de uso de len() con conjuntos
conjunto_vacio = set()
print(len(conjunto_vacio))  # Salida: 0 
