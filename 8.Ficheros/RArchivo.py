
import os
import sys
sys.dont_write_bytecode = True


def LeerFicheros():
    # 1. Solicitar la ruta del directorio
    print("\n1. ¿En qué directorio se encuentra el archivo?")
    print("   (Presiona ENTER para buscar en la carpeta actual)")
    ruta_directorio = input("Ruta del directorio: ").strip()

    if not ruta_directorio:
        ruta_directorio = "."

    # Verificar que el directorio existe
    if not os.path.isdir(ruta_directorio): #.isdir(): verifica si la ruta especificada es un directorio válido
        print(f"\nError: El directorio no existe: {ruta_directorio}")
        return

    # 2. Listar los archivos disponibles en el directorio
    # os.listdir(): lista todos los elementos en el directorio especificado; os.path.isfile(): filtra solo los archivos, excluyendo carpetas y otros tipos de elementos
    archivos = [f for f in os.listdir(ruta_directorio) if os.path.isfile(os.path.join(ruta_directorio, f))] 

    if not archivos:
        print(f"\nNo se encontraron archivos en: {ruta_directorio}")
        return

    print(f"\n2. Archivos disponibles en {os.path.abspath(ruta_directorio)}:\n") #.abspath(): devuelve la ruta absoluta del directorio especificado
    for i, nombre in enumerate(archivos, start=1): #enumerate(): permite iterar sobre la lista de archivos y obtener tanto el índice (i) como el nombre del archivo (nombre)
        print(f"   [{i}] {nombre}")

    # 3. Solicitar al usuario que seleccione un archivo
    print()
    seleccion = input("Ingrese el número del archivo que desea leer: ").strip()

    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(archivos)):
        print("\nSelección no válida.")
        return

    nombre_archivo = archivos[int(seleccion) - 1]
    ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

    # 4. Leer y mostrar el contenido del archivo
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as fichero:
            contenido = fichero.read()
        print(f"\n{'='*50}")
        print(f"Archivo: {nombre_archivo}")
        print(f"{'='*50}\n")
        print(contenido)
        print(f"\n{'='*50}")
        print(f"Ruta completa: {os.path.abspath(ruta_completa)}")
    except UnicodeDecodeError:
        print(f"\nAdvertencia: El archivo '{nombre_archivo}' no es de texto legible (puede ser binario).")
    except Exception as e:
        print(f"\nOcurrió un error al leer el fichero: {e}")
