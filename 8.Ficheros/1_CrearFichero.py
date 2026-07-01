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

Función que crea un fichero nuevo en la ruta indicada
def CrearFichero(ruta, contenido=""):
    try:
        # Modo 'x': crea el fichero solo si NO existe, si existe lanza FileExistsError
        with open(ruta, 'x', encoding='utf-8') as fichero:
            fichero.write(contenido)  # Escribe el contenido inicial (por defecto vacío)
        print(f"Fichero creado: {ruta}")
    except FileExistsError:
        # Si el fichero ya existía, avisamos pero el programa no se rompe
        print(f"El fichero ya existe: {ruta}")

LEER FICHEROS EN PYTHON
La lectura de ficheros es una operación fundamental en la programación, ya que permite acceder a
información almacenada en archivos de texto o binarios. Python ofrece varias formas de leer ficheros, siendo la más común el 
uso de la función open() junto con métodos como read(), readline() y readlines(). 
Estas funciones permiten leer el contenido completo del fichero, línea por línea o almacenar todas las líneas en una lista, 
respectivamente. Además, es importante manejar adecuadamente los errores y cerrar los ficheros después de su uso para evitar 
fugas de memoria y otros problemas. La lectura de ficheros es esencial para procesar datos, analizar información y 
desarrollar aplicaciones que dependan de archivos externos, como configuraciones, registros y datos de usuario.

Función que lee un fichero y devuelve sus líneas como una lista
def CargarLineas(ruta):
    # Modo 'readlines()': abre el fichero en modo lectura
    with open(ruta, 'r', encoding='utf-8') as fichero:
        lineas = fichero.readlines()  # Cada elemento de la lista es una línea del fichero
    return lineas  # Devuelve la lista de líneas

def CargarLineas(ruta):
    # Modo 'read': abre el fichero en modo lectura
    with open(ruta, 'r', encoding='utf-8') as fichero:
        contenido = fichero.read()  # Lee todo el contenido del fichero como una cadena
    return contenido  # Devuelve el contenido completo del fichero  

def CargarLineas(ruta):
    # Modo 'readline()': abre el fichero en modo lectura
    with open(ruta, 'r', encoding='utf-8') as fichero:
        linea = fichero.readline()  # Lee una línea del fichero
        while linea:
            print(linea.strip())  # Imprime la línea sin saltos de línea adicionales
            linea = fichero.readline()  # Lee la siguiente línea  

Función que lee un fichero, numera cada línea y guarda el resultado en otro fichero
def agregarNumLinea(ruta_in, ruta_out):
    lineas = CargarLineas(ruta_in)  # Carga las líneas del fichero de entrada
    num = 1                          # Contador que empieza en 1
    nuevo_texto = ""                 # Variable donde se acumula el texto numerado

    for linea in lineas:
        nueva_linea = str(num) + " " + linea  # Añade el número delante de cada línea
        nuevo_texto = nuevo_texto + nueva_linea  # Acumula la línea numerada
        num = num + 1  # Incrementa el contador

MODIFICAR FICHEROS EN PYTHON
La modificación de ficheros en Python es una operación que permite actualizar, agregar o eliminar contenido en archivos existentes.
Python proporciona varias formas de modificar ficheros, siendo las más comunes el uso de los modos de apertura 
'r+' (lectura y escritura) y 'a' (agregar al final del archivo). 
Al abrir un fichero en modo 'r+', se puede leer su contenido y luego escribir nuevas líneas o reemplazar partes del texto. 
Por otro lado, el modo 'a' permite añadir información al final del fichero sin sobrescribir el contenido existente. 
Es importante manejar adecuadamente los errores y cerrar los ficheros después de su uso para evitar problemas de integridad de datos. La modificación de ficheros es esencial para mantener la información actualizada y permitir la interacción dinámica con los datos almacenados en archivos, lo que es crucial para aplicaciones que requieren persistencia de datos y gestión de información.

Modo 'w': abre el fichero de salida en escritura (sobreescribe si ya existe)
    with open(ruta_out, 'w', encoding='utf-8') as fichero_out:
        fichero_out.write(nuevo_texto)  # Escribe todo el texto numerado


def CargarLineas(ruta):
    # Modo 'a': abre el fichero en modo lectura
    with open(ruta, 'a', encoding='utf-8') as fichero:
        lineas = fichero.readlines()  # Cada elemento de la lista es una línea del fichero
    return lineas  # Devuelve la lista de líneas

ELIMINAR FICHEROS EN PYTHON
La eliminación de ficheros en Python es una operación que permite borrar archivos del sistema de manera segura y controlada. 
Python ofrece la función os.remove() del módulo os para eliminar ficheros. Antes de eliminar un fichero, es recomendable 
verificar su existencia utilizando os.path.exists() para evitar errores. Además, es importante manejar adecuadamente 
las excepciones que puedan surgir durante la eliminación, como permisos insuficientes o archivos en uso. 
La eliminación de ficheros es esencial para liberar espacio en disco, mantener la organización de los datos y 
garantizar la seguridad de la información, especialmente en aplicaciones que generan archivos temporales o que requieren 
limpieza periódica de datos obsoletos.

Funcion que elimina un fichero en la ruta indicada
def EliminarFichero(ruta):
    try:
        os.remove(ruta)  # Intenta eliminar el fichero
        print(f"Fichero eliminado: {ruta}")
    except FileNotFoundError:
        # Si el fichero no existía, avisamos pero el programa no se rompe
        print(f"El fichero no existe: {ruta}")      


CRUD: CREATE, READ, UPDATE, DELETE > para crear, leer, actualizar y eliminar ficheros.

Ejercicio: 
Desarrolle un programa que permita la creación de un fichero de texto. El sistema debe solicitar al usuario la siguiente información:
•	La extensión o tipo de archivo deseado (ej. txt, csv, json, xml).
•	El contenido que se va a almacenar.
•	La ruta del directorio donde se guardará el documento.
Finalmente, el programa debe emitir una notificación confirmando si el fichero se creó correctamente o 
advirtiendo si ya existe un archivo en la ruta especificada.

Ademas el progama debe permitir al usuario leer el contenido del fichero creado, modificarlo y eliminarlo si así lo desea.

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
# --- Bloque principal ---

mi_ruta = "/Users/augusto/Documents/FundamentosProgramacion/3.Temas/poema.txt"
ruta_out = "/Users/augusto/Documents/FundamentosProgramacion/3.Temas/rima_linea.txt"

CrearFichero(ruta_out)           # Crea el fichero de salida si no existe
agregarNumLinea(mi_ruta, ruta_out)  # Numera las líneas del poema y las guarda
mi_lineas = CargarLineas(ruta_out)  # Carga el resultado para mostrarlo
print(mi_lineas)                    # Imprime la lista de líneas numeradas
'''