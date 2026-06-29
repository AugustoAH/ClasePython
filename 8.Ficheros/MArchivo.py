
import os
import sys
sys.dont_write_bytecode = True


def ModificarFicheros():
    # 1. Solicitar la ruta del directorio
    print("\n1. ¿En qué directorio se encuentra el archivo?")
    print("   (Presiona ENTER para buscar en la carpeta actual)")
    ruta_directorio = input("Ruta del directorio: ").strip()

    if not ruta_directorio:
        ruta_directorio = "."

    # Verificar que el directorio existe
    if not os.path.isdir(ruta_directorio):
        print(f"\nError: El directorio no existe: {ruta_directorio}")
        return

    # 2. Listar los archivos disponibles en el directorio
    archivos = [f for f in os.listdir(ruta_directorio) if os.path.isfile(os.path.join(ruta_directorio, f))]

    if not archivos:
        print(f"\nNo se encontraron archivos en: {ruta_directorio}")
        return

    print(f"\n2. Archivos disponibles en {os.path.abspath(ruta_directorio)}:\n")
    for i, nombre in enumerate(archivos, start=1):
        print(f"   [{i}] {nombre}")

    # 3. Solicitar al usuario que seleccione un archivo
    print()
    seleccion = input("Ingrese el número del archivo que desea modificar: ").strip()

    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(archivos)):
        print("\nSelección no válida.")
        return

    nombre_archivo = archivos[int(seleccion) - 1]
    ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

    # 4. Mostrar el contenido actual del archivo
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as fichero:
            contenido_actual = fichero.read()
        print(f"\n{'='*50}")
        print(f"Contenido actual de '{nombre_archivo}':\n")
        print(contenido_actual)
        print(f"{'='*50}")
    except UnicodeDecodeError:
        print(f"\nAdvertencia: El archivo '{nombre_archivo}' no es de texto legible (puede ser binario).")
        return
    except Exception as e:
        print(f"\nOcurrió un error al leer el fichero: {e}")
        return

    # 5. Seleccionar el modo de modificación
    print("\n3. ¿Cómo deseas modificar el archivo?\n")
    print("   [1] Agregar contenido al final (modo anexar)")
    print("   [2] Reemplazar todo el contenido (modo sobreescribir)")
    print("   [0] Cancelar")
    print()
    modo = input("Seleccione una opción: ").strip()

    if modo == "0":
        print("\nOperación cancelada. No se realizó ningún cambio.")
        return
    elif modo not in ("1", "2"):
        print("\nOpción no válida.")
        return

    # 6. Solicitar el nuevo contenido
    print("\n4. Introduce el nuevo contenido.")
    print("   (Para finalizar, escribe la palabra FIN en una línea nueva y presiona Enter):")

    lineas = []
    while True:
        linea = input()
        if linea.strip() == "FIN":
            break
        lineas.append(linea)

    nuevo_contenido = "\n".join(lineas)

    # 7. Escribir los cambios según el modo elegido
    try:
        if modo == "1":
            # Modo 'a': agrega al final sin borrar el contenido existente
            with open(ruta_completa, 'a', encoding='utf-8') as fichero:
                fichero.write("\n" + nuevo_contenido)
            print(f"\n¡ÉXITO! Contenido agregado al final de '{nombre_archivo}'.")
        elif modo == "2":
            # Modo 'w': sobreescribe todo el contenido anterior
            with open(ruta_completa, 'w', encoding='utf-8') as fichero:
                fichero.write(nuevo_contenido)
            print(f"\n¡ÉXITO! Contenido del archivo '{nombre_archivo}' reemplazado correctamente.")

        print(f"Ruta completa: {os.path.abspath(ruta_completa)}")
    except Exception as e:
        print(f"\nOcurrió un error al modificar el fichero: {e}")
