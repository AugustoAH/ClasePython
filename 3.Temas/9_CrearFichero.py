

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
