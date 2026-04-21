'''
Ejercicio 1: Convertir hora de 12 horas a 24 horas
Se pide un algoritmo en Python que dada la hora de ingresada por un usuario como una cadena de texto
de la siguiente manera 2:03PM la transforme a un formato de 24 horas, es decir, 14:03. 
'''

hora_doce = "11:03PM" # Ejemplo de hora en formato 12 horas
hora_temp = hora_doce

if hora_doce[4] == "A" or hora_doce[5] == "A": # Verifica si la hora es AM
    print(hora_doce)
elif hora_doce[4] == "P" or hora_doce[5] == "P": # Verifica si la hora es PM
    if int(hora_doce[0]) >= 2 and int(hora_doce[1]) >= 0:
         print("Formato de hora no válido. Por favor, ingrese la hora en formato 12 horas (ejemplo: 2:03PM).")
    elif hora_doce[0] == "1" and hora_doce[1] == "2":
      hora_doce = "00"+hora_doce[2:]
      print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "1" and hora_doce[1] == "1":
        hora_doce = "23"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce)
    elif hora_doce[0] == "1" and hora_doce[1] == "0":
        hora_doce = "22"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce)
    elif hora_doce[0] == "9": 
        hora_doce = "21"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce)
    elif hora_doce[0] == "0" and hora_doce[1] == "9":
        hora_doce = "21"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce)
    elif hora_doce[0] == "8": 
        hora_doce = "20"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce)
    elif hora_doce[0] == "0" and hora_doce[1] == "8":
        hora_doce = "20"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce)
    elif hora_doce[0] == "7": 
        hora_doce = "19"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "0" and hora_doce[1] == "7":
        hora_doce = "19"+hora_doce[2:]
        print(hora_doce) 
    elif hora_doce[0] == "6": 
        hora_doce = "18"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce)  
    elif hora_doce[0] == "0" and hora_doce[1] == "6":
        hora_doce = "18"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "5": 
        hora_doce = "17"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "0" and hora_doce[1] == "5":
        hora_doce = "17"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "4": 
        hora_doce = "16"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "0" and hora_doce[1] == "4":
        hora_doce = "16"+hora_doce[2:]
        print(hora_doce) 
    elif hora_doce[0] == "3": 
        hora_doce = "15"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "0" and hora_doce[1] == "3":
        hora_doce = "15"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "2": 
        hora_doce = "14"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "0" and hora_doce[1] == "2":
        hora_doce = "14"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "1": 
        hora_doce = "13"+hora_doce[1:]
        print(hora_temp," -> ",hora_doce) 
    elif hora_doce[0] == "0" and hora_doce[1] == "1":
        hora_doce = "13"+hora_doce[2:]
        print(hora_temp," -> ",hora_doce) 
    else:
        print("Formato de hora no válido. Por favor, ingrese la hora en formato 12 horas (ejemplo: 2:03PM).")

#Otra Solución mas Avanzada en Python:

def convertir_formato_hora(hora_texto):
    # 1. Extraemos si es AM o PM (son los últimos dos caracteres de la cadena)
    periodo = hora_texto[-2:].upper()
    
    # 2. Extraemos solo la parte del tiempo (quitamos los últimos dos caracteres)
    tiempo = hora_texto[:-2]
    
    # 3. Separamos las horas de los minutos usando los dos puntos ":"
    partes = tiempo.split(':')
    hora = int(partes[0]) # Convertimos la hora a número (int) para poder hacer cálculos
    minuto = partes[1]    # Los minutos se quedan como texto porque no los modificamos
    
    # 4. Lógica principal de conversión
    if periodo == "AM":
        # Caso especial: las 12:XX AM son las 00:XX en formato 24 horas
        if hora == 12:
            hora = 0
            
    elif periodo == "PM":
        # A cualquier hora PM le sumamos 12, EXCEPTO si son las 12 PM (mediodía)
        if hora != 12:
            hora += 12
            
    # 5. Formateamos el resultado
    # Usamos f-strings de Python. {hora:02d} asegura que el número tenga siempre 2 dígitos (ej: "0" -> "00", "5" -> "05")
    resultado = f"{hora:02d}:{minuto}"
    
    return resultado

# --- Pruebas del algoritmo ---
print("2:03PM ->", convertir_formato_hora("2:03PM"))   # Resultado esperado: 14:03
print("11:45AM ->", convertir_formato_hora("11:45AM")) # Resultado esperado: 11:45
print("12:30AM ->", convertir_formato_hora("12:30AM")) # Resultado esperado: 00:30
print("12:15PM ->", convertir_formato_hora("12:15PM")) # Resultado esperado: 12:15
print("9:05AM ->", convertir_formato_hora("9:05AM"))   # Resultado esperado: 09:05

'''
Ejercicio 2: Triángulo rectángulo
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
rectángulo como el siguiente:
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

# Pedimos al usuario que ingrese un número entero
# (Si ingresas 5, obtendrás el triángulo exacto de tu ejemplo)
numero = int(input("Introduce la altura del triángulo (un número entero): "))

# El primer bucle (bucle externo) controla las filas del triángulo
# range(1, numero + 1) hace que la variable 'i' vaya desde 1 hasta el número ingresado
for i in range(1, numero + 1):
    
    # Calculamos con qué número impar debe empezar esta fila
    inicio = (2 * i) - 1
    
    # El segundo bucle (bucle interno) imprime los números de cada fila
    # Empieza en 'inicio', termina en 0 (exclusivo, llega hasta 1), y avanza en pasos de -2
    for j in range(inicio, 0, -2):
        # end=" " evita que Python haga un salto de línea después de cada número
        print(j, end=" ")
        
    # Una vez que termina de imprimir todos los números de una fila, 
    # hacemos un print() vacío para saltar a la siguiente línea
    print("")
