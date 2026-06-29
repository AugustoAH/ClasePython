
import os # permite interactuar con el sistema operativo, como crear carpetas y manejar rutas de archivos

def CrearFicheros():
    # 1. Solicita al Usuario el nombre del fichero
    nombre_fichero = input("Ingrese el nombre del fichero (sin extensión): ").strip()
    while not nombre_fichero: # Validación para asegurarse de que el nombre no esté vacío
        print("El nombre del fichero no puede estar vacío. Intente nuevamente.")
        nombre_fichero = input("Ingrese el nombre del fichero (sin extensión): ").strip()
    
    # 2. Solicita al Usuario la extensión del fichero
    extension = input("Ingrese la extensión del fichero (ej. txt, csv, json, xml): ").strip().lower()
    while not extension: # Validación para asegurarse de que la extensión no esté vacía
        print("La extensión del fichero no puede estar vacía. Intente nuevamente.")
        extension = input("Ingrese la extensión del fichero (ej. txt, csv, json, xml): ").strip().lower()
    if extension.startswith('.'): # Si el usuario ingresa la extensión con un punto inicial, se elimina para evitar errores en la ruta final
        extension = extension[1:]  # Elimina el punto inicial si lo ingresa el usuario
    
    # 3. Solicita al Usuario la ruta del directorio donde se guardará el fichero
    print("\n3. ¿Dónde deseas guardar el fichero?")
    print("   (Presiona ENTER para guardarlo en la misma carpeta donde se ejecuta este programa)")
    ruta_directorio = input("Ruta de destino: ").strip()

    # Si el usuario no introduce ruta, se asigna el directorio actual ('.')
    if not ruta_directorio: # Validación para asegurarse de que la ruta no esté vacía
        ruta_directorio = "."

    # Verificar si la carpeta introducida existe; si no, intentar crearla
    if not os.path.exists(ruta_directorio): # path: Verifica si la ruta especificada / existe .exists(ruta): permite comprobar si la ruta especificada existe
        try:
            os.makedirs(ruta_directorio) # .makedirs(ruta): crea la carpeta especificada, incluyendo cualquier carpeta intermedia que no exista
            print(f"Nota: La carpeta especificada no existía, pero ha sido creada.")
        except Exception as e:
            print(f"Error crítico: No se pudo crear la ruta especificada. Detalle: {e}")
            return
    
    # Construir el nombre completo y la ruta absoluta final
    nombre_completo = f"{nombre_fichero}.{extension}"
    ruta_completa = os.path.join(ruta_directorio, nombre_completo) # .path.join(): combina la ruta del directorio y el nombre del fichero para formar la ruta completa de manera segura, independientemente del sistema operativo

    # 4. Solicitar el contenido del fichero
    print("\n4. Introduce el contenido que deseas almacenar.")
    print("   (Para finalizar, escribe la palabra FIN en una línea nueva y presiona Enter):")

    lineas = [] # Lista para almacenar las líneas de contenido introducidas por el usuario
    while True:
        linea = input()
        if linea.strip() == "FIN": # Si el usuario introduce "FIN", se rompe el bucle y se deja de solicitar contenido
            break
        lineas.append(linea) # Agrega la línea introducida a la lista de líneas

    # Unir las líneas introducidas con saltos de línea
    contenido_final = "\n".join(lineas) # .join(): une los elementos de la lista lineas en un solo string, separándolos con saltos de línea

    # 5. Crear el fichero en modo 'x': falla automáticamente si ya existe
    try:
        with open(ruta_completa, 'x', encoding='utf-8') as fichero:
            fichero.write(contenido_final)
        print("\n¡ÉXITO! El fichero se ha creado correctamente.")
        print(f"Ruta final: {os.path.abspath(ruta_completa)}")
    except FileExistsError:
        print(f"\nADVERTENCIA: El fichero '{nombre_completo}' ya existe en esa ruta. Utilice la Opción Modificar.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado al escribir el fichero: {e}")

