

# esto es un comentario de una sola linea

"""Esto es un comentario
de multiples lineas 
en Python
"""

# Condicionales 

"""
Simples: Si()              |   if():
Dobles:  Si() Si() Sino()  |   if(): elif():
Multiples: Switch          |   No Existe

"""

# Python Trabaje con IF Simple 
"""
Palabrareservada (Condición):
    SentenciaUno
    SentenciaDos
"""
if (True):
    print("Hola")
    print("Como estas")

if (False):
    print("Bien")
    print("Y usted")
# Comparación de números enteros en Python
a = 5;b = 3
if(a>b):
    print("A es mayor que B")
#Comparación de datos Booleanos en Python
c = False
if (c == True):
    print("C es VERDADERO")
#Comparación de Caracteres en Python
caracter = 'a'
if(caracter == 'b'):
    print("El caracter es:", caracter)
#Compación de Palabras o String en Python
palabra = "Hola"
if (palabra=="Chao"):
    print("La palabra es:",palabra)

#Python trabaje con si Doble
"""
Palabrareservada (Condición):
    SentenciaUno
    SentenciaDos
SINO(Condición):
    SentenciaUno
    SentenciaDos
"""
nota = 1

if (nota >= 4): # Condición de inicio
    print("Excelente")
elif (nota >= 2 and nota <= 3): #Condicion Anidada
    print("Necesita recuperar")
elif (nota >= 1 and nota<2):
    print("Reprobo")
else: # Condicion de Cierre
    print("Su nota fue 0")

