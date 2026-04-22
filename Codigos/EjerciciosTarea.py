'''
Nivel 1: Calentamiento (Variables y Condicionales Simples)

Estos ejercicios buscan que el estudiante se familiarice con la captura de datos (input), conversión de tipos y condicionales básicos.

1. El saludo personalizado
Enunciado: Pide al usuario su nombre y su edad. Muestra un mensaje de bienvenida y calcula en qué año nació aproximadamente (restando la edad al año actual)
Conceptos: Variables, entrada/salida de datos, operaciones matemáticas básicas.

2. Par o Impar
Enunciado: Escribe un programa que pida al usuario un número entero y le diga si es par o impar.
Conceptos: Operador módulo (%), condicional if-else.

3. El peaje
Enunciado: Pregunta al usuario la edad. Si es mayor o igual a 18 años, muestra el mensaje "Puedes conducir", de lo contrario, muestra "Aún no tienes edad para conducir".
Conceptos: Condicional if-else, operadores relacionales (>=).

4. El mayor de dos
Enunciado: Pide al usuario dos números diferentes y muestra por pantalla cuál de los dos es el mayor.
Conceptos: Variables, condicional if-else, comparación (>).

5. Positivo, negativo o cero
Enunciado: Solicita un número al usuario. El programa debe imprimir si el número es positivo, negativo o si es exactamente cero.
Conceptos: Condicionales múltiples (if, elif, else).




Nivel 2: Lógica Condicional Avanzada

Aquí se introducen múltiples condiciones, operadores lógicos (and, or) y anidamiento.

6. Categoría de edad
Enunciado: Pide la edad al usuario y clasifícalo según las siguientes categorías: 0-12 (Niño), 13-17 (Adolescente), 18-64 (Adulto), 65 o más (Adulto mayor).
Conceptos: Operadores lógicos (and) o anidamiento de elif.

7. Descuento en la tienda
Enunciado: Una tienda ofrece descuentos según el monto de la compra. Si es menor a $50, no hay descuento. Si está entre $50 y $100, hay un 5% de descuento. Si es mayor a $100, el descuento es del 10%. Pide el total de la compra y muestra el total a pagar.
Conceptos: Variables, if-elif-else, cálculos de porcentajes.

8. Año bisiesto
Enunciado: Pide al usuario que ingrese un año. El programa debe determinar si es bisiesto o no (Un año es bisiesto si es divisible por 4, excepto si es divisible por 100, a menos que también sea divisible por 400).
Conceptos: Operador módulo (%), operadores lógicos anidados (and, or).

9. Calculadora de IMC (Índice de Masa Corporal)
Enunciado: Pide al usuario su peso (en kg) y su altura (en metros). Calcula el IMC (peso/altura^2) y muestra en qué rango se encuentra: Bajo peso (<18.5), Normal (18.5 - 24.9), Sobrepeso (25 - 29.9) u Obesidad (>=30).
Conceptos: Fórmulas matemáticas, if-elif-else.

10. Aprobación de crédito
Enunciado: Pide al usuario su salario mensual y si tiene alguna deuda pendiente (sí/no). Para aprobar el crédito, el salario debe ser mayor a $1000 y no debe tener deudas. Imprime "Crédito Aprobado" o "Crédito Denegado".
Conceptos: Cadenas de texto en condicionales, operadores lógicos (and).




Nivel 3: Introducción a los Bucles

En esta sección se trabaja la repetición de tareas con for y while de forma aislada.

11. Cuenta regresiva
Enunciado: Pide al usuario un número entero positivo. Usa un bucle while para mostrar una cuenta regresiva desde ese número hasta 0, y al final imprime "¡Despegue!".
Conceptos: Bucle while, decremento de variables.

12. Suma de los primeros N números
Enunciado: Solicita un número N. Usa un bucle for para sumar todos los números desde el 1 hasta N y muestra el resultado final.
Conceptos: Bucle for con range(), variable acumuladora.

13. La tabla de multiplicar
Enunciado: Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10 utilizando un bucle for.
Conceptos: Bucle for, formato de cadenas (f-strings).

14. Adivina el PIN
Enunciado: Define una variable con un PIN secreto (ej. "1234"). Usa un bucle while para pedirle al usuario que ingrese el PIN. El programa no debe dejarlo avanzar hasta que ingrese el PIN correcto.
Conceptos: Bucle while, comparación de cadenas.

15. Contador de vocales
Enunciado: Pide al usuario que ingrese una frase. Utiliza un bucle for para recorrer cada letra de la frase y cuenta cuántas vocales (a, e, i, o, u) tiene. Imprime el total.
Conceptos: Bucle for sobre una cadena (string), condicionales dentro de un bucle, variable contador.




Nivel 4: Integración y Resolución de Problemas (Retos)

Ejercicios que combinan todo: variables, condicionales lógicos y bucles.

16. Adivina el número (con intentos)
Enunciado: El programa define un número secreto entre 1 y 20. El usuario tiene 5 intentos para adivinarlo (usando un bucle while o for). En cada intento, el programa debe decirle si el número ingresado es mayor o menor al número secreto. Si acierta, el bucle se detiene.
Conceptos: Bucle con límite, if-elif-else, interrupción de bucles (break).

17. Validador de números primos
Enunciado: Pide un número al usuario y determina si es primo (solo divisible por 1 y por sí mismo). Usa un bucle para intentar dividir el número por todos los números anteriores a él y un condicional para verificar el residuo.
Conceptos: Bucle for, operador módulo (%), uso de variables booleanas (banderas/flags).

18. Cajero Automático Básico
Enunciado: Simula un cajero. El saldo inicial es $1000. Usa un bucle while para mostrar un menú con tres opciones: 1. Consultar saldo, 2. Retirar dinero, 3. Salir. Si el usuario elige retirar, verifica que la cantidad sea menor o igual al saldo disponible antes de restar. El bucle termina solo cuando elige "Salir".
Conceptos: Menús interactivos con while, condicionales anidados, actualización de variables.

19. La caja registradora
Enunciado: Crea un programa que permita al usuario ingresar los precios de varios productos uno por uno. El programa debe seguir pidiendo precios usando un while hasta que el usuario ingrese un "0" para indicar que terminó. Al finalizar, si el total de la compra supera los $100, aplica un 10% de descuento. Muestra el total a pagar.
Conceptos: Bucle while con condición de salida, acumuladores, condicional al final.

20. Sucesión de Fibonacci
Enunciado: Pide al usuario cuántos términos de la sucesión de Fibonacci quiere generar. La sucesión comienza con 0 y 1, y cada número siguiente es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8...). Usa un bucle for para calcular y mostrar la serie.
Conceptos: Intercambio de variables temporales, lógica algorítmica, bucle for.

'''