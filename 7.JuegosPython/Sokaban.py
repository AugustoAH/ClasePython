'''
Taller Práctico de Programación: Clon de Sokoban en Terminal
1. Descripción del Proyecto

Sokoban es un juego de rompecabezas clásico donde el jugador controla a un trabajador en un almacén. El objetivo es empujar todas las cajas hacia las zonas de almacenamiento marcadas. 
Para este taller, desarrollarás una versión simplificada que se ejecutará directamente en la terminal, utilizando caracteres de texto para representar el mundo.

2. Objetivos del Taller

    Crear y manipular estructuras de datos bidimensionales (matrices/listas de listas).

    Diseñar e implementar lógica condicional para el manejo de colisiones y movimiento espacial.

    Desarrollar un bucle de juego interactivo (Game Loop) que procese la entrada del usuario y actualice el estado del programa.

3. Requerimientos Funcionales (Reglas del Juego)

Tu programa debe cumplir obligatoriamente con las siguientes reglas:

    R1 - Representación del Mapa: El mapa del juego debe ser una matriz precargada en el código. 
    Se deben usar estrictamente los siguientes caracteres para dibujar el nivel en la terminal:

        # : Pared (Límite infranqueable).

        @ : Jugador.

        $ : Caja.

        . : Meta (Zona de almacenamiento).

        * : Caja ubicada correctamente sobre una meta.

          (Espacio) : Suelo libre por donde el jugador se puede mover.

    R2 - Controles del Jugador: El programa debe solicitar al usuario una entrada por teclado en cada turno. 
    Las teclas permitidas son W (Arriba), A (Izquierda), S (Abajo), D (Derecha) y Q (Salir del juego). 
    El sistema debe aceptar las letras tanto en mayúsculas como en minúsculas.

    R3 - Lógica de Movimiento y Colisiones:

        El jugador solo puede moverse a un espacio adyacente (arriba, abajo, izquierda, derecha).

        El jugador no puede atravesar paredes (#).

        Si el jugador camina hacia una caja ($), la empujará al siguiente espacio en esa misma dirección, 
        si y solo si, ese espacio está vacío ( ) o es una meta (.).

        El jugador no puede empujar una caja si detrás de la caja hay una pared u otra caja 
        (no se pueden empujar dos cajas a la vez).

        El juevo debe tener como minimo 12 niveles, cada uno con un diseño diferente y creciente en dificultad.

    R4 - Interfaz Gráfica: En cada turno, la terminal debe limpiarse y redibujar el mapa actualizado 
    para dar la sensación de animación. Debajo del mapa, siempre deben imprimirse las instrucciones 
    de los controles.

4. Requerimientos No Funcionales (Estructura del Código)

Para aprobar este taller, tu código fuente debe cumplir con lo siguiente:

    Modularidad: No puedes escribir todo el código en un solo bloque secuencial. 
    Debes definir y utilizar, como mínimo, las siguientes funciones:

        dibujar_mapa(matriz): Encargada de imprimir el nivel en pantalla.

        obtener_posicion_jugador(matriz): Que recorra la matriz y retorne la fila y columna actual 
        del jugador.

        mover(direccion): Que contenga toda la lógica de validación de colisiones.

    Ausencia de errores de ejecución: El programa no debe cerrarse abruptamente (crash) si el usuario ingresa una tecla no válida o 
    si intenta empujar una caja fuera de los límites de la matriz (IndexError).

5. Entregables y Caso de Prueba Inicial

El estudiante deberá entregar el archivo sokoban.py. Para asegurar que todos comiencen con el mismo nivel de dificultad, 
el mapa de prueba obligatorio que debe estar quemado (hardcoded) en tu script al 
entregarlo es el siguiente:

#######
#     #
#  $  #
# .@  #
#     #
#######
Nota: Si tu lógica funciona correctamente en este mapa pequeño, 
debería funcionar en mapas más grandes.
'''