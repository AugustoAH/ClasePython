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




if __name__ == "__main__":
    # Se llama a la función Jugar para iniciar el Programa
    #jugar_hanoi() # Función que inicia el juego de la Torre de Hanoi

    dibujar_torres({'A': [3, 2, 1], 'B': [], 'C': []}, 3)