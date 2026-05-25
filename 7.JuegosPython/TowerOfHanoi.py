import os

def limpiar_pantalla():
    # Limpia la Consola para dar el Efecto de Animación
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_torres(torres, n):
    
    # Dibuja el estado actual de las torres en la Consola
    limpiar_pantalla()
    print("\n"+"==="*15)
    print("TORRE DE HANOI".center(45))
    print("==="*15+"\n")

    # Ancho máximo que ocupará el disco más grande más un espacio de margen
    ancho_columna = n * 2 + 3

    # Dibujar desde arriba hacia abajo
    for i in range(n - 1, -1,-1):
        fila=""
        for poste in ['A','B','C']:  # Arreglo de 3 postes
            if i < len(torres[poste]):
                tamaño_disco = torres[poste][i]
                # Crear el dibujo del disco [===]
                disco_str ="[" + "=" * ((tamaño_disco * 2) - 1)+"]"
                # Centrar el disco dentro del ancho de la columna
                fila += disco_str.center(ancho_columna)
            else:
                # Si no hay disco, dibujar un espacio vacío
                fila += "|".center(ancho_columna)
        print(fila)
# Dibujar la base y las etiquetas de los postes
    print("-" * (ancho_columna * 3))
    print("A".center(ancho_columna) + "B".center(ancho_columna) + "C".center(ancho_columna))    
    print("\n"+"==="*15)

def jugar_hanoi(n=3):
    # Función Principal que controla el flujo del juego
    # Inicializar el estado del juego: El poste A tiene los discos 3, 2 y 1 (de mayor a menor)
    torres = {'A': list(range( n , 0 , -1 )), 'B': [], 'C': []}
    movimientos = 0 # Variable Local para contar el número de movimientos realizados

    while  len(torres['B']) < n:
        dibujar_torres(torres, n)
        print(f"Movimientos: {movimientos}\n")
        print("Intrucciones: Ingrese el poste de origen y el destino separado por un espacio")
        print("Ejemplo: A C para mover el disco superior a A hacia B")
        print("Escribe Q para salir del juego\n")

        entrada = input("Ingrese su movimiento: ").strip().upper()

        if entrada == 'Q':
            print("Gracias por jugar a la Torre de Hanoi. ¡Hasta luego!")
            return
        partes = entrada.split() # Dividir la entrada en partes para obtener el origen y destino
        if len(partes) != 2 or partes[0] not in torres or partes[1] not in torres:
            print("Entrada inválida. Por favor, asegúrate de usar las letras A, B o C")
            input("Presione Enter para continuar...")
            continue
        origen, destino = partes[0], partes[1]  # Obtener el poste de origen y destino

        #validar el movimiento: El poste de origen no debe estar vacío y el disco a mover debe 
        # ser más pequeño que el disco superior del poste de destino (si no está vacío)
        if not torres[origen]:
            print(f"El poste {origen} está vacío. No puedes mover un disco desde allí.")
            input("Presione Enter para continuar...")
            continue
        disco_a_mover = torres[origen][-1]  # Obtener el disco superior del poste de origen

        if torres[destino] and torres[destino][-1] < disco_a_mover:
            print(f"No puedes colocar un disco más grande sobre uno más pequeño en el poste {destino}.")
            input("Presione Enter para continuar...")
            continue
        
        # Si el movimiento es válido, realizarlo: quitar el disco del poste de origen y 
        # agregarlo al poste de destino
        torres[origen].pop()  # Quitar el disco del poste de origen
        torres[destino].append(disco_a_mover)  # Agregar el disco al poste de destino
        movimientos += 1  # Incrementar el contador de movimientos

    #Pantalla Final del Juego
    dibujar_torres(torres, n)
    print(f"¡Felicidades! Has completado la Torre de Hanoi en {movimientos} movimientos.")
    input("Presione Enter para salir...")

if __name__ == "__main__":
    #Puedes cambiar este número para jugar con más o menos discos 
    # (recomiendo no más de 5 para mantenerlo manejable)
    jugar_hanoi(3)