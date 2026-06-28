
'''
1. read(): Lee todo de golpe
El método read() toma todo el contenido del archivo desde la posición actual del cursor hasta el final y lo devuelve como una única y gran 
cadena de texto (string).

> Cuándo usarlo: Es ideal cuando trabajas con archivos pequeños y necesitas analizar todo el texto a la vez (por ejemplo, para contar 
palabras o buscar un patrón en todo el documento).

> El peligro: Si intentas usar read() en un archivo muy pesado (por ejemplo, un log de 5 GB), tu programa consumirá demasiada memoria RAM y 
probablemente colapsará.

Nota extra: Si le pasas un número como argumento, por ejemplo read(10), leerá exactamente esa cantidad de caracteres (o bytes).
'''
# Forma de Cargar un archivo de texto en Python con read()
print("Cargar un archivo de texto en Python con read()")
def CargarString(ruta):
    with open(ruta, 'r', encoding='utf-8') as fichero:
        texto = fichero.read()
    return texto

mi_ruta = "/Users/augusto/Documents/FundamentosProgramacion/3.Temas/poema.txt"
mi_texto = CargarString(mi_ruta)
print(mi_texto)
print("----------------------------------------------------")

'''
2. readline(): Lee línea por línea
El método readline() lee solo una línea del archivo cada vez que lo llamas. Se detiene en el momento en que encuentra un salto de línea (\n) 
o el final del archivo.

> Cuándo usarlo: Es perfecto para leer archivos grandes de forma segura y eficiente, ya que solo carga en la memoria RAM una línea a la vez.

> Cómo funciona: Si lo llamas varias veces seguidas, el "cursor" de Python recuerda dónde se quedó y te irá dando la línea 1, luego la 2, luego la 3, etc.
'''

# Forma de Cargar un archivo de texto en Python con readline()
print("Cargar un archivo de texto en Python con readline()")
def CargarLineas(ruta):
    with open(ruta, 'r', encoding='utf-8') as fichero:
        lineas = fichero.readlines()
    return lineas

mi_ruta = "/Users/augusto/Documents/FundamentosProgramacion/3.Temas/poema.txt"
mi_lineas = CargarLineas(mi_ruta)
print(mi_lineas)
print("----------------------------------------------------")
'''
3. Iterar sobre el archivo: La forma más eficiente
En Python, los objetos de archivo son iterables. Esto significa que puedes recorrerlos directamente en un bucle for, línea por línea, 
sin necesidad de cargar todo el contenido en memoria.
> Cuándo usarlo: Es la forma más eficiente y recomendada para leer archivos grandes, ya que solo mantiene en memoria la línea actual y 
no todo el archivo.
> Cómo funciona: Cada vez que el bucle for itera, Python lee la siguiente línea del archivo hasta llegar al final.
'''

# Forma recomendada de cargar un archivo de texto en Python
print("Cargar un archivo de texto en Python de forma recomendada")
def CargarLineasRecomendado(ruta):
    with open(ruta, "r",encoding="utf-8") as f:
        for linea in f:
            print(linea) 

mi_linea_recomendado = CargarLineasRecomendado(mi_ruta)
print("----------------------------------------------------")