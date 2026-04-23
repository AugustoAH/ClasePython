'''
TUPLAS EN PYTHON

Conjunto de elementos ordenados e inmutables que pueden contener datos de diferentes tipos, por ejemplo pueden contener números, cadenas de texto, otras tuplas, etc.

Las tuplas se presentan por una serie de elementos separados por comas y delimitados entre paréntesis () .

──▶ Sintaxis de una tupla
    Tupla = (elemento1, elemento2, elemento3, ..., elementoN)

──▶ Una tupla de textos
    colores = ("rojo", "verde", "azul")

──▶ Una tupla mezclada
    Tupla = (56,"Python",3.14,[1,2,3],True)

──▶ Una tupla vacía (tupla para ser llenada después)
    mochila = ()
                    [  TUPLA  ]
    _________________
   |  0  |  1  |  2  |  <-- Posición (Índice)
   | (A) | (B) | (C) |  <-- Contenido (Valor)
   |_____|_____|_____|
      |     |     |
      ▼     ▼     ▼                     

En las tuplas, cada elemento tiene una posición o índice que comienza desde 0. Por ejemplo, en la tupla colores, 
"rojo" está en la posición 0, "verde" en la posición 1 y "azul" en la posición 2.

Indice Negativo: También se pueden usar índices negativos para acceder a los elementos desde el final de la tupla. 
Por ejemplo, en la tupla colores, "azul" se puede acceder con el índice -1, "verde" con el índice -2 y "rojo" con el índice -3. 

1. Funciones para trabajar con tuplas:
    - count(): Cuenta cuántas veces aparece un elemento en la tupla.
    - index(): te dice la posición (índice) de la primera aparición de un elemento en la tupla.
    - len(): Devuelve la cantidad de elementos en la tupla.
    - max(): Devuelve el valor máximo de la tupla (si los elementos son comparables).
    - min(): Devuelve el valor mínimo de la tupla (si los elementos son comparables).
'''
# Ejemplo de uso de count()
colores = ("rojo", "verde", "azul", "rojo")
print(colores.count("rojo"))  # Salida: 2   / .count(elemento)

# Ejemplo de uso de index()
print(colores.index("verde"))  # Salida: 1. / .index(elemento)

# Ejemplo de uso de len()
print(len(colores))  # Salida: 4 / .len(tupla)

# Ejemplo de uso de max() y min()
numeros = (3, 1, 4, 1, 5)
print(max(numeros))  # Salida: 5 / .max(tupla)
print(min(numeros))  # Salida: 1 / .min(tupla)



