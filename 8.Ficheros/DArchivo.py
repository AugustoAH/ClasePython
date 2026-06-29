
import os
import sys
sys.dont_write_bytecode = True


def EliminarFicheros():
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
    seleccion = input("Ingrese el número del archivo que desea eliminar: ").strip()

    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(archivos)):
        print("\nSelección no válida.")
        return

    nombre_archivo = archivos[int(seleccion) - 1]
    ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

    # 4. Pedir confirmación antes de eliminar
    print(f"\nEstás a punto de eliminar: {os.path.abspath(ruta_completa)}")
    confirmacion = input("¿Confirmas la eliminación? Esta acción no se puede deshacer (s/n): ").strip().lower()

    if confirmacion != "s":
        print("\nOperación cancelada. No se eliminó ningún archivo.")
        return

    # 5. Eliminar el archivo
    try:
        os.remove(ruta_completa) #.remove(): elimina el archivo especificado en la ruta completa
        print(f"\n¡ÉXITO! El archivo '{nombre_archivo}' ha sido eliminado correctamente.")
    except PermissionError:
        print(f"\nError: No tienes permisos para eliminar '{nombre_archivo}'.")
    except Exception as e:
        print(f"\nOcurrió un error al eliminar el fichero: {e}")
