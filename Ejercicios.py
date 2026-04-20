'''
Ejercicio 1: Convertir hora de 12 horas a 24 horas
Se pide un algoritmo en Python que dada la hora de ingresada por un usuario como una cadena de texto
de la siguiente manera 2:03PM la transforme a un formato de 24 horas, es decir, 14:03. 
'''

#print("--- Convertir hora de 12 horas a 24 horas ---")
#print("Ingrese la hora en formato 12 horas (ejemplo: 2:03PM): ")
#hora_doce= input()

hora_doce = "01:03PM" # Ejemplo de hora en formato 12 horas

#print(len(hora_doce)) # Imprime la longitud de la cadena hora_doce  

if hora_doce[4] == "A" or hora_doce[5] == "A": # Verifica si la hora es AM
    print(hora_doce)
elif hora_doce[4] == "P" or hora_doce[5] == "P": # Verifica si la hora es PM
    if hora_doce[0] == "1": 
       hora_doce = "13"+hora_doce[1:] # Convierte la hora a formato 24 horas
    elif hora_doce[0] == "2": 
       hora_doce = "14"+hora_doce[1:] 
    elif hora_doce[0] == "3": 
       hora_doce = "15"+hora_doce[1:] 
    elif hora_doce[0] == "4": 
       hora_doce = "16"+hora_doce[1:] 
    elif hora_doce[0] == "5": 
       hora_doce = "17"+hora_doce[1:] 
    elif hora_doce[0] == "6": 
       hora_doce = "18"+hora_doce[1:] 
    elif hora_doce[0] == "7": 
       hora_doce = "19"+hora_doce[1:] 
    elif hora_doce[0] == "8": 
       hora_doce = "20"+hora_doce[1:] 
    elif hora_doce[0] == "9": 
       hora_doce = "21"+hora_doce[1:] 
    elif hora_doce[0] == "10": 
       hora_doce = "22"+hora_doce[1:]   
    elif hora_doce[0] == "11": 
       hora_doce = "23"+hora_doce[1:] 
    elif hora_doce[0] == "12": 
       hora_doce = "00"+hora_doce[1:]

print(hora_doce) 
'''
if hora_doce[-2:] == "PM": # Verifica si la hora es PM
    hora_24 = int(hora_doce[:-2].split(":")[0]) + 12 # Convierte la hora a formato 24 horas
    if hora_24 == 24: # Si la hora es 12 PM, se ajusta a 12 en formato 24 horas
        hora_24 = 12
else: # Si la hora es AM
    hora_24 = int(hora_doce[:-2].split(":")[0]) # Convierte la hora a formato 24 horas
    if hora_24 == 12: # Si la hora es 12 AM, se ajusta a 0 en formato 24 horas
        hora_24 = 0
'''

#for i in range(len(hora_doce)):
#    print(hora_doce[i]) # Imprime cada carácter de la cadena hora_doce uno por uno





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
