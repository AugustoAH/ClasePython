import sys # permite modificar el comportamiento del intérprete de Python
sys.dont_write_bytecode = True # permite que no se generen archivos .pyc al ejecutar el script

import EstilosMenu # importación del módulo EstilosMenu.py para mostrar el menú con estilo
import XArchivo # importación del módulo XArchivo.py que contiene la función CrearFicheros()
import RArchivo # importación del módulo RArchivo.py que contiene la función LeerFicheros() 
import MArchivo # importación del módulo MArchivo.py que contiene la función ModificarFicheros()
import DArchivo # importación del módulo DArchivo.py que contiene la función EliminarFicheros()
'''
CREAR Y MANIPULAR FICHEROS EN PYTHON
La creación de ficheros es una tarea importante para facilitar el almacenamiento de información en los 
programas. La idea es depositar en estos archivos datos que puedan ser recuperados y que sean de consumo 
frecuente para la configuración, análisis y monitoreo. Es por este motivo que resulta fundamental conocer 
las funciones que nos permiten crear, leer, escribir y eliminar ficheros de manera eficiente y segura.

CRUD: CREATE, READ, UPDATE, DELETE > para crear, leer, actualizar y eliminar ficheros.

Ejercicio: 
Desarrolle un programa que permita la creación de un fichero de texto. El sistema debe solicitar al usuario la siguiente información:
•	La extensión o tipo de archivo deseado (ej. txt, csv, json, xml).
•	El contenido que se va a almacenar.
•	La ruta del directorio donde se guardará el documento.
Finalmente, el programa debe emitir una notificación confirmando si el fichero se creó correctamente o 
advirtiendo si ya existe un archivo en la ruta especificada.

# Función que crea un fichero nuevo en la ruta indicada
def CrearFichero(ruta, contenido=""):
    try:
        # Modo 'x': crea el fichero solo si NO existe, si existe lanza FileExistsError
        with open(ruta, 'x', encoding='utf-8') as fichero:
            fichero.write(contenido)  # Escribe el contenido inicial (por defecto vacío)
        print(f"Fichero creado: {ruta}")
    except FileExistsError:
        # Si el fichero ya existía, avisamos pero el programa no se rompe
        print(f"El fichero ya existe: {ruta}")

'''

while True:
    #EstilosMenu.mostrar_menu()
    #EstilosMenu.mostrar_menu_color()
    EstilosMenu.mostrar_menu_rich()

    menu = input("\nOpción deseada: ").strip()

    if menu == "1":
        XArchivo.CrearFicheros()
    elif menu == "2":
        RArchivo.LeerFicheros()
    elif menu == "3":
        MArchivo.ModificarFicheros()
    elif menu == "4":
        DArchivo.EliminarFicheros()
    elif menu == "0":
        print("\nSaliendo del programa. ¡Hasta luego!\n")
        break
    else:
        print("\nOpción no válida. Intente de nuevo.")











'''
# Función que lee un fichero y devuelve sus líneas como una lista
def CargarLineas(ruta):
    # Modo 'r': abre el fichero en modo lectura
    with open(ruta, 'r', encoding='utf-8') as fichero:
        lineas = fichero.readlines()  # Cada elemento de la lista es una línea del fichero
    return lineas  # Devuelve la lista de líneas


# Función que lee un fichero, numera cada línea y guarda el resultado en otro fichero
def agregarNumLinea(ruta_in, ruta_out):
    lineas = CargarLineas(ruta_in)  # Carga las líneas del fichero de entrada
    num = 1                          # Contador que empieza en 1
    nuevo_texto = ""                 # Variable donde se acumula el texto numerado

    for linea in lineas:
        nueva_linea = str(num) + " " + linea  # Añade el número delante de cada línea
        nuevo_texto = nuevo_texto + nueva_linea  # Acumula la línea numerada
        num = num + 1                            # Incrementa el contador

    # Modo 'w': abre el fichero de salida en escritura (sobreescribe si ya existe)
    with open(ruta_out, 'w', encoding='utf-8') as fichero_out:
        fichero_out.write(nuevo_texto)  # Escribe todo el texto numerado


# --- Bloque principal ---

mi_ruta = "/Users/augusto/Documents/FundamentosProgramacion/3.Temas/poema.txt"
ruta_out = "/Users/augusto/Documents/FundamentosProgramacion/3.Temas/rima_linea.txt"

CrearFichero(ruta_out)           # Crea el fichero de salida si no existe
agregarNumLinea(mi_ruta, ruta_out)  # Numera las líneas del poema y las guarda
mi_lineas = CargarLineas(ruta_out)  # Carga el resultado para mostrarlo
print(mi_lineas)                    # Imprime la lista de líneas numeradas
'''