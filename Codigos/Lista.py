
'''
LISTAS EN PYTHON

Las listas son un conjunto de elementos ordenados y mutables que pueden contener datos de diferentes tipos, por ejemplo pueden contener números, cadenas de texto, otras listas, etc.

Las listas se presentan por una serie de elementos separados por comas y delimitados entre corchetes [] .

──▶ Sintaxis de una lista
    Lista = [elemento1, elemento2, elemento3, ..., elementoN]

──▶ Una lista de textos
    frutas = ["manzana", "banana", "cereza"]

──▶ Una lista mezclada
    Lista = [56,"Python",3.14,[1,2,3],True]

──▶ Una lista vacía (lista para ser llenada después)
    mochila = []

                 [  LISTA  ]
    _________________
   |  0  |  1  |  2  |  <-- Posición (Índice)
   | [A] | [B] | [C] |  <-- Contenido (Valor)
   |_____|_____|_____|
      |     |     |
      ▼     ▼     ▼

En las listas, cada elemento tiene una posición o índice que comienza desde 0. Por ejemplo, en la lista frutas, "manzana" está 
en la posición 0, "banana" en la posición 1 y "cereza" en la posición 2.

Indice Negativo: También se pueden usar índices negativos para acceder a los elementos desde el final de la lista. 
Por ejemplo, en la lista frutas, "cereza" se puede acceder con el índice -1, "banana" con el índice -2 y "manzana" con el índice -3.

1. Funciones para agregar elementos a una lista:
    - append(): Agrega un elemento al final de la lista.
    - insert(): Agrega un elemento en una posición específica de la lista.
    - extend(): Agrega los elementos de otra lista al final de la lista actual.
    - copy(): Crea una copia de la lista actual.
'''
# Ejemplo de uso de append()
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja") # .append(elemento)
print(frutas)  # Salida: ['manzana', 'banana', 'cereza', 'naranja']

# Ejemplo de uso de insert()
frutas.insert(1, "kiwi") # .insert(posición, elemento)
print(frutas)  # Salida: ['manzana', 'kiwi', 'banana', 'cereza', 'naranja']

# Ejemplo de uso de extend()
otras_frutas = ["pera", "uva"]
frutas.extend(otras_frutas) # .extend(lista)
print(frutas)  # Salida: ['manzana', 'kiwi', 'banana', 'cereza', 'naranja', 'pera', 'uva']      

#Ejemplo de uso de copy()
frutas_copia = frutas.copy() # .copy()
print(frutas_copia)  # Salida: ['manzana', 'kiwi', 'banana', 'cereza', 'naranja', 'pera', 'uva']

'''
2. Funciones para eliminar elementos de una lista:
    - remove(): Busca el primer elemento que coincida con el valor especificado y lo elimina de la lista. si no existe el valor, se genera un error.
    - pop(): Elimina y devuelve el elemento en una posición específica de la lista. Si no se especifica la posición, elimina y devuelve el último elemento.
    - clear(): Elimina todos los elementos de la lista.
    - del: Es una palabra reservada que se puede usar para eliminar un elemento en una posición específica de la lista o para eliminar toda la lista.
    '''
# Ejemplo de uso de remove()
frutas.remove("kiwi") # .remove(elemento)
print(frutas)  # Salida: ['manzana', 'banana', 'cereza', 'naranja', 'pera', 'uva']  

# Ejemplo de uso de pop()
ultima_fruta = frutas.pop(1) # .pop(posición)
print(ultima_fruta)  # Salida: 'banana'
print(frutas)  # Salida: ['manzana', 'cereza', 'naranja', 'pera']  

# Ejemplo de uso de clear()
frutas.clear() # .clear()
print(frutas)  # Salida: []

#Ejemplo del uso (del)
del frutas # del lista
# print(frutas)  # Esto generará un error porque la lista ha sido eliminada
del otras_frutas[0] # del lista[posición]
print(otras_frutas)  # Salida: ['uva']

'''
3. Funciones para ordenar y contar elementos en una lista:
    - len(): Devuelve el número de elementos en la lista.
    - sort(): Ordena los elementos de la lista en orden ascendente (de menor a mayor). 
              Si se desea ordenar en orden descendente, se puede usar el argumento reverse=True.
              modifica la lista original.
    - sorted(): Devuelve una nueva lista con los elementos ordenados, sin modificar la lista original.
    - count(): Devuelve el número de veces que un elemento específico aparece en la lista.
    - reverse(): Invierte el orden de los elementos en la lista. modifica la lista original.
'''

# Ejemplo de uso de len()
numeros = [3, 1, 4, 1, 5, 9]
print(len(numeros))  # Salida: 6    

# Ejemplo de uso de sort()
numeros.sort() # .sort()
print(numeros)  # Salida: [1, 1, 3, 4, 5, 9]
numeros.sort(reverse=True) # .sort(reverse=True)
print(numeros)  # Salida: [9, 5, 4, 3, 1, 1]        

# Ejemplo de uso de sorted()
numeros_ordenados = sorted(numeros) # sorted(lista)
print(numeros_ordenados)  # Salida: [1, 1, 3, 4, 5, 9]
print(numeros)  # Salida: [9, 5, 4, 3, 1, 1]

# Ejemplo de uso de count()
print(numeros.count(1))  # Salida: 2

# Ejemplo de uso de reverse()
numeros.reverse() # .reverse()
print(numeros)  # Salida: [1, 1, 3, 4, 5, 9]

'''
4. Funciones para acceder a elementos de una lista:
    - index(): Devuelve el índice de la primera aparición de un elemento específico en la lista. 
    Si el elemento no se encuentra, se genera un error.
    - slicing: Permite acceder a una porción de la lista utilizando la sintaxis lista[inicio:fin:paso].
    - in: Es un operador que se utiliza para verificar si un elemento específico está presente en la lista. 
    Devuelve True si el elemento está presente y False si no lo está.
'''
# Ejemplo de uso de index()
numeros = [1, 2, 3, 4, 5]
print(numeros.index(3))  # Salida: 2

# Ejemplo de uso de slicing()
print(numeros[1:4])  # Salida: [2, 3, 4]
print(numeros[::2])  # Salida: [1, 3, 5]

# Ejemplo de uso de in
print(3 in numeros)  # Salida: True
print(6 in numeros)  # Salida: False

'''5. Funciones estadisticas para listas numéricas:
    - sum(): Devuelve la suma de todos los elementos en la lista.
    - min(): Devuelve el valor mínimo de la lista.
    - max(): Devuelve el valor máximo de la lista.
    '''
# Ejemplo de uso de sum()
numeros = [1, 2, 3, 4, 5]
print(sum(numeros))  # Salida: 15   

# Ejemplo de uso de min()
print(min(numeros))  # Salida: 1

# Ejemplo de uso de max()
print(max(numeros))  # Salida: 5    


