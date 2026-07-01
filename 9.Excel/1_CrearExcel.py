import openpyxl

'''
MANIPULACIÓN DE ARCHIVOS EXCEL CON OPENPYXL
openpyxl es una librería de Python que permite leer, escribir y modificar
archivos Excel (.xlsx) sin necesidad de tener Excel instalado.

Conceptos clave:
  wb  (Workbook)  → representa el archivo Excel completo
  ws  (Worksheet) → representa una hoja dentro del archivo Excel
  ws[fila][col]   → accede a una celda por índice numérico (base 0 en col, base 1 en fila)
  ws["A1"]        → accede a una celda por su referencia de Excel (base 1 en ambos)
'''
# =============================================================================
# FUNCIÓN: cargar hoja de un archivo Excel
# =============================================================================

def cargarHoja(ruta, hoja):
    wb = openpyxl.load_workbook(ruta)  # abre el archivo Excel existente
    ws = wb[hoja]                      # selecciona la hoja por nombre
    return (wb, ws)                    # devuelve el libro y la hoja como una tupla


# =============================================================================
# 1. CARGAR EL ARCHIVO Y LA HOJA
# =============================================================================

ruta_pelis = "/Users/augusto/Documents/FundamentosProgramacion/9.Excel/pelis.xlsx"
hoja_pelis = "pelis"
(wb, ws) = cargarHoja(ruta_pelis, hoja_pelis) 

print(f"Archivo cargado : {ruta_pelis}") #imprime la ruta del archivo cargado
print(f"Hoja activa     : {hoja_pelis}\n")     #imprime el nombre de la hoja activa

# =============================================================================
# 2. LEER CELDAS — dos formas de acceder al mismo valor
# =============================================================================

print("--- Lectura de la celda A1 (dos formas equivalentes) ---")
print(f"  ws[1][1].value → {ws[1][1].value}")   # índice numérico: fila 1, columna 1
print(f"  ws['B1'].value → {ws['B1'].value}\n")  # referencia de Excel

'''
NOTA: Al usar la biblioteca openpyxl, es importante recordar que los índices de fila comienzan en 1, 
mientras que los índices de columna comienzan en 0 cuando se accede a las celdas mediante índices numéricos. 
Por otro lado, al usar referencias de Excel (como "A1", "B1"), ambos índices comienzan en 1. 
Esto puede causar confusión si no se tiene cuidado al acceder a las celdas.
'''

# =============================================================================
# 3. PROPIEDADES DE LA HOJA
# =============================================================================

print("--- Dimensiones de la hoja ---")
print(f"  Filas con datos    : {ws.max_row}")      # .max_row devuelve el número de la última fila que contiene datos
print(f"  Columnas con datos : {ws.max_column}\n") # .max_column devuelve el número de la última columna que contiene datos
print(f"  Dimensiones de la hoja : {ws.dimensions}\n") # .dimensions devuelve un rango de celdas que contiene datos (ej. "A1:D5")
print(f"  Celdas en columna A : {len(ws['A'])}")  # devuelve el número de celdas en la columna A (incluyendo vacías)
print(f"  Celdas en fila 1 : {len(ws['1'])}")  # devuelve el número de celdas en la fila 1 (incluyendo vacías)

# =============================================================================
# 4. RECORRER FILAS — dos formas equivalentes
# =============================================================================

print("--- Columna A completa (iterando filas con ws) ---")
for fila in ws:                       # recorre todas las filas de la hoja
    print(f"  {fila[0].value}")       # fila[0] = primera celda de cada fila

print("\n--- Columna A completa (iterando valores con ws.values) ---")
for fila in ws.values:                # recorre los valores de todas las filas de la hoja
    print(f"  {fila[0]}")             # fila[0] = primer valor de la tupla de cada fila


# =============================================================================
# 5. MODIFICAR CELDAS — agregar cabeceras que faltaban
# =============================================================================

print("\n--- Modificando cabeceras de la hoja ---")

ws[1][1].value = "Director"      # columna B, fila 1 — por índice numérico
ws["B1"]       = "Director"      # misma celda — por referencia de Excel
ws["D1"]       = "Comentarios"   # columna D, fila 1 — por referencia de Excel
ws[1][3].value = "Comentarios"   # misma celda — por índice numérico

print("  B1 → Director")
print("  D1 → Comentarios")


# =============================================================================
# 6. AGREGAR UNA NUEVA FILA AL FINAL
# =============================================================================

print("\n--- Agregando nueva fila ---")

nueva_fila = ["El Padrino", "Francis Ford Coppola", 1972, "Película de culto"] # lista con los valores de la nueva fila
ws.append(nueva_fila)            # ws.append() inserta la lista como una nueva fila al final

print(f"  Fila agregada : {nueva_fila}")
print(f"  Total filas ahora    : {ws.max_row}")
print(f"  Total columnas ahora : {ws.max_column}")


# =============================================================================
# 7. GUARDAR LOS CAMBIOS EN UN ARCHIVO NUEVO
# =============================================================================

ruta_out1 = "/Users/augusto/Documents/FundamentosProgramacion/9.Excel/pelis_out1.xlsx"
wb.save(ruta_out1)               # wb.save() escribe todos los cambios en disco

print(f"\nArchivo guardado en : {ruta_out1}")


# =============================================================================
# 8. INSERTAR Y ELIMINAR FILAS / COLUMNAS
# =============================================================================
# Estos métodos reorganizan la hoja desplazando el contenido existente.
# Todos reciben dos parámetros: posición (base 1) y cantidad.
#
# ws.insert_rows(pos, amount=1)
#   Inserta filas ANTES de la posición indicada, empujando las demás hacia abajo.
#   Ejemplo: ws.insert_rows(2, 3)
#     Antes  → fila 1: cabecera | fila 2: dato A | fila 3: dato B
#     Después → fila 1: cabecera | filas 2-4: vacías | fila 5: dato A | fila 6: dato B
#
# ws.delete_rows(pos, amount=1)
#   Elimina filas desde la posición indicada, subiendo las demás hacia arriba.
#   Ejemplo: ws.delete_rows(2, 1)
#     Antes  → fila 1: cabecera | fila 2: dato A | fila 3: dato B
#     Después → fila 1: cabecera | fila 2: dato B
#
# ws.insert_cols(pos, amount=1)
#   Inserta columnas ANTES de la posición indicada, empujando las demás hacia la derecha.
#   Ejemplo: ws.insert_cols(2, 1)
#     Antes  → col A: Título | col B: Año
#     Después → col A: Título | col B: vacía | col C: Año
#
# ws.delete_cols(pos, amount=1)
#   Elimina columnas desde la posición indicada, desplazando las demás hacia la izquierda.
#   Ejemplo: ws.delete_cols(2, 1)
#     Antes  → col A: Título | col B: vacía | col C: Año
#     Después → col A: Título | col B: Año

# =============================================================================
# 9. PARÁMETROS PARA GENERAR ESTADÍSTICAS DE UNA COLUMNA
# =============================================================================
# Estos son los parámetros que necesitará la próxima función para leer una
# columna de datos, calcular estadísticas (ej. suma, promedio, máximo) y
# guardar el resultado en una hoja nueva.
#
# ruta_in    → ruta del libro Excel que contiene los datos de origen.
#              Ejemplo: "/Users/augusto/.../pelis.xlsx"
#
# hoja_in    → nombre de la hoja dentro de ruta_in que contiene los datos
#              que vamos a analizar.
#              Ejemplo: "pelis"
#
# columna    → índice de la columna sobre la que se calcularán las
#              estadísticas (ej. la columna que contiene los años o precios).
#              Ejemplo: 3  →  columna C
#
# ruta_out   → ruta donde se guardará el libro con el resultado.
#                - Si es DIFERENTE a ruta_in, se crea un archivo nuevo y el
#                  original queda intacto.
#                - Si es IGUAL a ruta_in, el archivo original se sobreescribe
#                  con los cambios.
#
# hoja_out   → nombre de la hoja nueva que se creará para guardar las
#              estadísticas calculadas.
#              Ejemplo: "estadisticas"

# =============================================================================
# 10. FUNCIÓN: construir diccionario de frecuencias por columna
# =============================================================================
# Recorre todas las filas de datos (omitiendo la cabecera) y cuenta cuántas
# veces aparece cada valor distinto en la columna indicada.
# Devuelve un diccionario  { valor: cantidad_de_apariciones }
# Ejemplo con col=2 (columna C = Año):
#   { 1972: 3, 1994: 2, 2001: 5, ... }

def crearDiccEst(ruta_in, hoja_in, col):
    (wb, ws_in) = cargarHoja(ruta_in, hoja_in)  # abre el archivo y selecciona la hoja. wb se necesita para guardar cambios más adelante y ws_in es la hoja de datos que vamos a analizar
    estadisticas = {}                            # diccionario vacío donde se acumularán los conteos

    # ws_in[2:ws_in.max_row] recorre desde la fila 2 hasta la última con datos,
    # saltando la fila 1 que contiene las cabeceras (Título, Director, Año...)
    for fila in ws_in[2:ws_in.max_row]:
        valor = fila[col].value                  # extrae el valor de la celda en la columna indicada

        if valor in estadisticas:                # condición: si el valor ya existe en el diccionario
            estadisticas[valor] += 1             # el valor ya existía → incrementa su contador
        else:                                    # caso contrario  lo agrega al diccionario con contador inicial 1
            estadisticas[valor] = 1              # primera vez que aparece → inicializa en 1

    return estadisticas                          # devuelve { valor: nº de apariciones }


# =============================================================================
# 11. FUNCIÓN: escribir el diccionario de estadísticas en una hoja nueva
# =============================================================================
# Crea una hoja nueva dentro del libro wb, escribe la cabecera y luego
# cada par (valor, cantidad) del diccionario como una fila.
# Finalmente guarda el libro en ruta_out.

def guardarEst(wb, dicc, ruta_out, hoja_out):
    ws_out = wb.create_sheet(hoja_out)           # añade una hoja nueva al libro con el nombre indicado
    nombres = ["Valor", "Apariciones"]           # lista con los nombres de las columnas
    ws_out.append(nombres)                       # primera fila → cabecera de la tabla

    # Recorre el diccionario e inserta una fila por cada valor único encontrado
    for clave, valor in dicc.items():            # dicc.items() devuelve una lista de tuplas (clave, valor) para recorrer el diccionario
        fila = [str(clave), str(valor)]          # crea una lista con el valor y su cantidad de apariciones
        ws_out.append(fila)                      # convierte a str para compatibilidad con Excel
    wb.save(ruta_out)                            # escribe el libro completo (con la hoja nueva) en disco
    print(f"  Estadísticas guardadas en : {ruta_out}  →  hoja '{hoja_out}'")


# =============================================================================
# 12. FUNCIÓN ORQUESTADORA: calcular y guardar estadísticas en un solo paso
# =============================================================================
# Une crearDiccEst y guardarEst para ejecutar todo el proceso en una llamada.
# Parámetros:
#   ruta_in  → archivo Excel con los datos de origen
#   hoja_in  → nombre de la hoja con los datos
#   col      → índice de columna a analizar (0 = A, 1 = B, 2 = C ...)
#   ruta_out → archivo Excel donde se guardarán las estadísticas
#   hoja_out → nombre de la hoja nueva que se creará con los resultados

def crearEstadisticas(ruta_in, hoja_in, col, ruta_out, hoja_out):
    estadisticas = crearDiccEst(ruta_in, hoja_in, col)  # paso 1: genera el diccionario de frecuencias
    guardarEst(wb, estadisticas, ruta_out, hoja_out)     # paso 2: escribe el diccionario en Excel


# =============================================================================
# EJECUCIÓN: estadísticas de la columna 2 (Año) del archivo pelis_out1.xlsx
# =============================================================================

ruta_out2  = "/Users/augusto/Documents/FundamentosProgramacion/9.Excel/pelis_estadisticas.xlsx" # archivo nuevo para no modificar el original
hoja_estad = "estadisticas" # nombre de la hoja nueva que se creará con los resultados

print("\n--- Generando estadísticas de la columna Año ---")

# Parámetros de crearEstadisticas():
#
#   ruta_in  = ruta_out1   → archivo Excel de entrada que contiene los datos a analizar
#                             (pelis_out1.xlsx, generado en la sección 7 con la fila nueva incluida)
#
#   hoja_in  = hoja_pelis  → nombre de la hoja dentro de ruta_in donde están los datos
#                             (en este caso la hoja "pelis")
#
#   col      = 2           → índice de la columna a analizar (base 0: A=0, B=1, C=2)
#                             col=2 apunta a la columna C → Año de la película
#
#   ruta_out = ruta_out2   → archivo Excel de salida donde se guardarán las estadísticas
#                             (pelis_estadisticas.xlsx, archivo nuevo para no modificar el original)
#
#   hoja_out = hoja_estad  → nombre de la hoja nueva que se creará con los resultados
#                             (en este caso la hoja "estadisticas")

crearEstadisticas(ruta_out1, hoja_pelis, 2, ruta_out2, hoja_estad) # llama a la función orquestadora para generar y guardar las estadísticas

# =============================================================================
# OTRA FORMA DE HACERLO funcion crearDiccEst() mediante la funcion iter_rows() de openpyxl, 
# que permite recorrer las filas de la hoja de manera más eficiente y flexible.
# =============================================================================

def crearDiccEst_v2(ruta_in, hoja_in, col):
    (wb, ws_in) = cargarHoja(ruta_in, hoja_in)  # abre el archivo y selecciona la hoja
    estadisticas = {}                            # diccionario vacío donde se acumularán los conteos

    # iter_rows() permite recorrer las filas de manera más eficiente y flexible
    for fila in ws_in.iter_rows(min_row=2, min_col=col, max_col=col, values_only=True):  # recorre desde la fila 2 hasta la última con datos, solo la columna indicada
        valor = fila[0]                          # extrae el valor de la celda en la columna indicada

        if valor in estadisticas:                # condición: si el valor ya existe en el diccionario
            estadisticas[valor] += 1             # el valor ya existía → incrementa su contador
        else:                                    # caso contrario  lo agrega al diccionario con contador inicial 1
            estadisticas[valor] = 1              # primera vez que aparece → inicializa en 1

    return estadisticas                          # devuelve { valor: nº de apariciones }

# =============================================================================
# EJECUCIÓN: estadísticas de la columna 3 (Año) del archivo pelis_out3.xlsx
# =============================================================================

def crearEstadisticas_v2(ruta_in, hoja_in, col, ruta_out, hoja_out):
    estadisticas = crearDiccEst_v2(ruta_in, hoja_in, col)  # paso 1: genera el diccionario de frecuencias
    guardarEst(wb, estadisticas, ruta_out, hoja_out)     # paso 2: escribe el diccionario en Excel


ruta_out3  = "/Users/augusto/Documents/FundamentosProgramacion/9.Excel/pelis_out3.xlsx" # archivo nuevo para no modificar el original
crearEstadisticas_v2(ruta_out1, hoja_pelis, 3, ruta_out3, hoja_estad) # llama a la función orquestadora para generar y guardar las estadísticas



# =============================================================================
# VERSIÓN 3 — crearDiccEst usando iter_cols()
# =============================================================================
# Hace lo mismo que v1 y v2 pero recorre la hoja por COLUMNAS en lugar de
# por filas. La diferencia clave frente a iter_rows():
#
#   iter_rows() → cada iteración devuelve UNA FILA  → accedes al valor con fila[0]
#   iter_cols() → cada iteración devuelve UNA COLUMNA completa (todos sus valores)
#                 → recorres los valores con un bucle interno
#
# iter_cols() parámetros usados:
#   min_row=2          → empieza en la fila 2, saltando la cabecera (fila 1)
#   min_col=col        → columna mínima a leer
#   max_col=col        → columna máxima a leer → solo lee UNA columna
#   values_only=True   → devuelve los valores directamente, NO objetos Cell
#
# Resultado: como min_col == max_col, el bucle externo itera UNA SOLA VEZ
# y entrega todos los valores de esa columna en una tupla llamada "columna".
# El bucle interno recorre esa tupla valor a valor.

def crearDiccEst_v3(ruta_in, hoja_in, col):     #función que genera un diccionario de estadísticas usando iter_cols()
    (wb, ws_in) = cargarHoja(ruta_in, hoja_in)  # abre el archivo y selecciona la hoja
    estadisticas = {}                           # diccionario vacío donde se acumularán los conteos

    # El bucle externo itera por columnas → solo hay UNA columna (min_col == max_col)
    # "columna" es una tupla con TODOS los valores de esa columna: (1972, 1994, 2001, ...)
    for columna in ws_in.iter_cols(min_row=2, min_col=col, max_col=col, values_only=True):

        # El bucle interno recorre cada valor dentro de la columna
        for valor in columna:                   # valor = cada año de película directamente
            if valor in estadisticas:           # si el valor ya existe en el diccionario
                estadisticas[valor] += 1        # incrementa su contador de apariciones
            else:
                estadisticas[valor] = 1         # primera vez que aparece → inicializa en 1

    return estadisticas                         # devuelve { valor: nº de apariciones }


# =============================================================================
# VERSIÓN 3 — crearEstadisticas_v3 (orquestadora que usa crearDiccEst_v3)
# =============================================================================
# Idéntica en estructura a v1 y v2 — solo cambia la función interna que
# genera el diccionario (usa iter_cols en lugar de slice o iter_rows).
# El resultado final en Excel es el mismo en las tres versiones.

def crearEstadisticas_v3(ruta_in, hoja_in, col, ruta_out, hoja_out):
    estadisticas = crearDiccEst_v3(ruta_in, hoja_in, col)  # paso 1: genera diccionario con iter_cols()
    guardarEst(wb, estadisticas, ruta_out, hoja_out)        # paso 2: escribe el diccionario en Excel


# Parámetros de crearEstadisticas_v3():
#   ruta_in  = ruta_out1   → archivo Excel de entrada con los datos a analizar
#   hoja_in  = hoja_pelis  → hoja "pelis" dentro del archivo
#   col      = 3           → columna C (base 1 con iter_cols: 1=A, 2=B, 3=C) → Año
#   ruta_out = ruta_out4   → archivo de salida nuevo: pelis_out4.xlsx
#   hoja_out = hoja_estad  → hoja de resultados: "estadisticas"

ruta_out4 = "/Users/augusto/Documents/FundamentosProgramacion/9.Excel/pelis_out4.xlsx" # archivo nuevo para no modificar el original

print("\n--- Generando estadísticas v3 (iter_cols) de la columna Año ---")
crearEstadisticas_v3(ruta_out1, hoja_pelis, 3, ruta_out4, hoja_estad) # llama a la función orquestadora para generar y guardar las estadísticas usando iter_cols()

# =============================================================================
# CARGAR HOJA COMPLETA COMO MATRIZ (lista de listas)
# =============================================================================
# Una "matriz" en Python es una lista de listas: cada elemento de la lista
# exterior es una fila, y cada elemento de esa fila es el valor de una celda.
#
# Estructura del resultado:
#   [
#     ["Título",     "Director",              "Año",  "Comentarios"],  ← fila 1 (cabecera)
#     ["Titanic",    "James Cameron",          1997,   "..."],          ← fila 2
#     ["El Padrino", "Francis Ford Coppola",   1972,   "..."],          ← fila 3
#     ...
#   ]
#
# ¿Por qué usar lista de listas en lugar de leer celda a celda?
#   → Permite trabajar con toda la hoja en memoria como estructura Python,
#     sin depender de openpyxl para cada acceso posterior.
#   → Útil para filtrar, ordenar o transformar los datos con listas por comprensión.

def cargarHojaComoMatriz(ruta, hoja):
    #(_, ws) = cargarHoja(ruta, hoja)   # abre el archivo y selecciona la hoja
    wb = openpyxl.load_workbook(ruta)  # abre el archivo Excel existente
    ws = wb[hoja]                      # selecciona la hoja por nombre
    matriz = []                         # lista vacía que acumulará las filas

    # ws.values devuelve cada fila como una TUPLA de valores (inmutable).
    # list(fila) convierte esa tupla en una LISTA (mutable), permitiendo
    # modificar los valores de cada fila más adelante si fuera necesario.
    for fila in ws.values:
        matriz.append(list(fila))       # agrega cada fila convertida a lista

    return matriz                       # devuelve la hoja completa como lista de listas


# =============================================================================
# EJECUCIÓN: cargar pelis_out1.xlsx como matriz e imprimirla fila a fila
# =============================================================================

print("\n--- Hoja cargada como matriz (lista de listas) ---")

matriz_pelis = cargarHojaComoMatriz(ruta_out1, hoja_pelis)

for fila in matriz_pelis:
    print(f"  {fila}")