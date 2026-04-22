'''
El condicional if es básicamente el "portero" de tu código: decide si una parte del programa 
debe ejecutarse o no, basándose en si una condición es verdadera o falsa.

Operadores de comparación

Para que el if funcione, necesitas comparar valores. Aquí tienes los más comunes:
 | Operador  |  Significado   |  Ejemplo |
──────────────────────────────────────────
 |    ==     |  Igual a       |  a == b  |
 |    !=     |  Diferente de  |  a != b  |
 |    >      |  Mayor que     |  a > b   |
 |    <      |  Menor que     |  a < b   |
 |    >=     |  Mayor o igual |  a >= b  |
 |    <=     |  Menor o igual |  a <= b  |
 ─────────────────────────────────────────

Condiciones múltiples (and, or, not)

Puedes combinar preguntas en una sola línea:
    and: Ambas deben ser ciertas.
    or: Al menos una debe ser cierta.
    not: Invierte el resultado (lo que es verdad lo hace falso).

IF/ELIF/ELSE
La sentencia (if) forma parte de un conjunto de sentencias encargadas de bifurcar la ejecución 
del código fuente dependiento de una serie de condiciones. Por tanto, la sentencias (if) te permite
tomar decisiones, evaluar una condición de una operación lógica y dependiendo de su resultado, ejecutará
un código fuente u otro.

Comandos relacionados con la sentencia (if) y su significado:

> (if) - permite generar un bloque de codigo que se ejecutará si se cumple la condición de entrada que tiene.

      [Inicio]
         |
El "if" (ej. if x > 10:)
   [¿Condición?]  ─────────(False)───┐
         │                           │
       (True)                        │
         ▼                           ▼
  [Bloque Código] ──────────────▶[ Sigue ]
                                     |
                                   [Fin] 

'''
#Ejecuta el Siguiente Programa en Python
print("Ingrese la temperatura:")
temperatura = int(input())              # Input se utiliza para recibir datos del usuario a través del teclado.
if temperatura > 30: #  ¿ > 30 ? ─(F)─┐   Para cumplirlo la temperatura debe ser mayor de 30 para imprimir Calor 
    print("Calor")   #     │          │   Si es menor no imprime nada
                     #    (V)         │
                     #  [Calor] ──▶ [Fin]
print("Fin del programa")  
print("----------------")  
'''
> (elif) - permite generar un camino alternativo con una condición de entrada

       [Inicio]
          |
El "elif" (ej. if edad >= 18: ... elif edad >= 13: ... else: ...)
          |
    [Condición # 1] ─────────(False)──────────┐
          |                                   |
       (True)                                 ▼
          ▼                            [Condición # 2] ──────(False)──────┐
 [Bloque Código # 1]                          |                           |
          |                                (True)                         |
          |                                   ▼                           |
          |                          [Bloque Código # 2]                  |
          |                                   |                           ▼
          └──────────────────────────────────────────────────────────▶[ Sigue ]
                                                                          |
                                                                        [Fin]
'''
#Ejecuta el Siguiente Programa en Python
print("Ingrese la Edad:")
edad = int(input())

if edad >= 18:                   #  [¿Edad >= 18?] ─(F)─┐
    print("Eres adulto")         #       │              │
                                 #      (V)             ▼
elif edad >= 13:                 #       │        [¿Edad >= 13?] ─(F)─┐
    print("Eres adolescente")    #       │              │             │
                                 #       │             (V)            ▼
                                 #       │              │             │
                                 #    [Adulto]     [Adolecente]       │
                                 #       │              │             │
print("Fin del programa")        #       └──────────────────────▶ [ Sigue ]
print("----------------")
'''
> (else) - permite generar un camino alternativo que se ejecutará siempre que no se haya cumplido las condiciones
de los posibles caminos de las intrucciones (if) y (elif)

      [Inicio]
          |
El "if-else" (ej. if x % 2 == 0: ... else: ...)
          |
    [¿Condición?] ─────────────(False)────────────┐
          |                                       |
       (True)                                     |
          ▼                                       ▼
     [Bloque if]                            [Bloque else]
          |                                       |
          └───────────────────────────────────────┴────▶ [ Sigue ]
                                                             |
                                                           [Fin]
'''
#Ejecuta el Siguiente Programa en Python
print("Ingrese la nota:")
nota = int(input())

if nota >= 60:                 #  [¿Nota >= 60?] ───(F)───┐
    print("Aprobaste")         #       │                  │
                               #      (V)                 ▼
else:                          #       │            [Bloque else]
    print("Reprobaste")        #  [Bloque if]             │
                               #       │                  │
print("Fin del programa")      #       └──────────────────┴──▶ [ Sigue ]
print("----------------")

'''
Estructura cumpleta aplicada (if) ──▶ (elif) ──▶ (else) en python

       [Inicio]
          |
El "if-elif-else" (ej. if x > 0: ... elif x == 0: ... else: ...)
          |
    [¿x > 0?] ─────────────(False)─────────────┐
        |                                      |
     (True)                                    ▼
        ▼                                  [¿x == 0?] ────────(False)───────┐
 [Bloque Positivo]                             |                            |
        |                                   (True)                          |
        |                                      ▼                            ▼
        |                                [Bloque Cero]               [Bloque Negativo]
        |                                      |                            |
        └──────────────────────────────────────┴────────────────────────────┴───▶ [ Sigue ]
                                                                                      |
                                                                                    [Fin]
'''
#Ejecuta el Siguiente Programa en Python
x = -5
if x > 0:                      #   [¿x > 0?] ──(F)──┐
    print("Es positivo")       #       │            │
                               #      (V)           ▼
elif x == 0:                   #       │       [¿x == 0?] ──(F)──┐
    print("Es cero")           #       │            │            │
                               #       │           (V)           ▼
else:                          #       │            │            │
    print("Es negativo")       #  [Positivo]      [Cero]    [Negativo]
                               #       │            │            │
print("Análisis terminado")    #       └────────────┴────────────┴──▶ [ Sigue ]

'''
Un error común: No olvides los dos puntos (:) al final de la condición y asegúrate de que el código de abajo tenga sangría (4 espacios o un Tab), de lo contrario Python te lanzará un error.
'''

#Ejemplos Prácticos
print("----------------")
usuario = "admin"
password = 1234
if usuario == "admin" and password == 1234:
    print("Acceso concedido")
else:
    print("Datos incorrectos")
print("----------------")
#----------------------------------------------------------------------
print("----------------")
print("Escribir un número de 1 a 10")
numero= int(input())
if(numero > 5):
    print("¡Soy mayor que 5!")
elif(numero == 5):
    print("Soy el número 5")
else:
    print("Soy menor o igual que 5")
print("----------------")
#----------------------------------------------------------------------
print("----------------")
edad = int(input("¿Cuántos años tienes? "))
if edad < 4:
    # Si tiene menos de 4 años, entra gratis
    precio = 0
    print("¡Entrada gratis para bebés!")
elif edad <= 12:
    # Si no es menor de 4, pero tiene 12 o menos
    precio = 5
    print("Precio infantil: $5")
elif edad < 65:
    # Si no es niño, pero tiene menos de 65
    precio = 10
    print("Precio estándar: $10")
else:
    # Si no cumplió ninguna de las anteriores (65 o más)
    precio = 7
    print("Precio para adultos mayores: $7")
print(f"Total a pagar: ${precio}")
print("----------------")

'''
Resumen "Para Llevar"
Si puedes recordar estos tres puntos, ya sabes usar condicionales:
    if: Es obligatorio y es el primero que se evalúa.
    elif: Es opcional, puedes poner los que quieras, y solo se miran si el de arriba falló.
    else: Es el plan B. Se ejecuta solo si absolutamente todo lo anterior fue falso.

Checklist de Supervivencia
Antes de dar el tema por cerrado, asegúrate de que tu código siempre cumpla esto:
    [ ] Indentación: ¿El código dentro del if tiene sus 4 espacios de sangría?
    [ ] Los dos puntos: ¿Puse : al final de cada condición?
    [ ] Exclusividad: ¿Recuerdo que en cuanto una condición se cumple, Python ignora el resto del bloque?
    [ ] Orden: ¿Puse las condiciones más específicas al principio? (Por ejemplo, preguntar primero por > 100 antes que por > 10).

Ejercicios Para Realizar
1. La Bola 8 Mágica
Crea un programa que te pida una pregunta y te devuelva una respuesta aleatoria (puedes usar un número al azar del 1 al 4 para decidir qué responder).
    Si es 1: "Sí, definitivamente".
    Si es 2: "No cuentes con ello".
    Si es 3: "Pregunta de nuevo más tarde".
    Si es 4: "Mi instinto dice que sí".

Un truco extra para tus programas:
Para el ejercicio de la Bola 8, puedes usar este código al principio de tu archivo para generar números al azar:
Python
import random
numero = random.randint(1, 4) # Genera un número entre 1 y 4

2. Papel o Tijera (Versión Básica)
Pide a dos usuarios que escriban su elección por teclado.
    Usa if y and para comparar las opciones (ej. if jugador1 == "piedra" and jugador2 == "tijeras":).
    Muestra quién ganó o si hubo un empate.

3. Supervivencia en el Bosque
Haz una mini "aventura de texto". El programa te pregunta: "Ves un zombi a lo lejos, ¿qué haces? (correr / pelear / esconderse)".
    Usa if, elif y else para darle un final diferente a cada elección (¡algunos finales pueden ser trágicos!).

4. El Mezclador de Colores
Pide al usuario que introduzca dos colores primarios (rojo, azul o amarillo) y dile qué color forman.
    Si mete "rojo" y "azul", dile que se forma el "púrpura".
    Si los colores son iguales, dile que el color no cambia.
    Si mete algo que no es un color primario, usa el else para avisarle del error.

5. El Validador de Montaña Rusa
Crea un sistema que decida si alguien puede subir a la atracción más extrema del parque.
    Debe medir estatura (mínimo 1.40m) y edad (mínimo 12 años).
    Si cumple ambas, ¡bienvenido!
    Si solo falla una, dile exactamente cuál es el problema.
    Si tiene una condición especial (ej. "VIP"), entra directo sin importar lo demás.
'''
