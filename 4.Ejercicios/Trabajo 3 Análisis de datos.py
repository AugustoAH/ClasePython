'''
Trabajo 3: Análisis de datos con Numpy y Pandas

RECURSOS DESCARGABLES
Necesitas descargar los siguientes recursos para realizar el ejercicio:

 
¿QUÉ HAY QUE HACER?
Este reto consiste en analizar los datos de ventas, los inventarios y la satisfacción del cliente para una cadena de tiendas minoristas; utilizando Pandas, para la manipulación de datos, y Numpy, para realizar cálculos estadísticos y simulaciones. El objetivo es ayudar a optimizar el rendimiento de las tiendas a través del análisis de estos datos.

PASOS A SEGUIR
La empresa ficticia RetailNow, que gestiona una cadena de tiendas minoristas, desea realizar un análisis detallado del rendimiento de sus diferentes sucursales en varias ciudades. Para ello, han recopilado datos de las ventas, los inventarios y la satisfacción del cliente en archivos CSV. Tu misión será procesar, explorar y analizar estos datos usando Pandas y Numpy para ayudar a la dirección a tomar decisiones estratégicas sobre la optimización del rendimiento de las tiendas.

1. Preparar el entorno de trabajo:
Abre Visual Studio Code y asegúrate de tener instalado el plugin de Jupyter.
Crea un nuevo archivo Jupyter Notebook llamado analisis_red_tiendas.ipynb.
2. Importar las librerías necesarias:
Importa las librerías Pandas y Numpy que necesitarás para realizar el análisis.
3. Cargar los datos (lectura y procesamiento de datos - Pandas):
Utiliza Pandas para cargar los archivos CSV: sales.csv, inventories.csv y satisfaction.csv.
Guarda los datos en tres DataFrames distintos.
Limpia los datos eliminando filas con valores nulos utilizando el método dropna(). Esto te permitirá trabajar solo con datos válidos.
4. Exploración de datos (Pandas)
Calcula las ventas totales por producto y por tienda.
Calcula los ingresos totales por tienda, multiplicando la cantidad vendida por el precio unitario.
Genera un resumen estadístico de las ventas utilizando el método describe() para obtener la media, mediana y otras métricas clave.
Si los productos están clasificados por categorías, calcula el promedio de ventas por tienda y categoría de productos.
Utiliza groupby() en Pandas para calcular las ventas totales por tienda o por categoría.
5. Análisis de inventarios (Pandas)
Calcula la rotación de inventarios para cada tienda. Esto se hace dividiendo las ventas totales por el stock disponible de cada producto.
Almacena los resultados en una nueva columna dentro del DataFrame de inventarios.
Filtra y muestra las tiendas con niveles críticos de inventario, es decir, aquellas tiendas donde el porcentaje de productos vendidos sea menor al 10% del stock disponible.
Utiliza groupby() y operaciones matemáticas para calcular la rotación de inventarios.
Aplica filtros con Pandas para identificar las tiendas con niveles críticos.
6. Satisfacción del cliente (Pandas)
Realiza un análisis de la satisfacción de los clientes en cada tienda. Relaciona estos datos con el rendimiento de las ventas.
Filtra las tiendas con niveles bajos de satisfacción (< 60%) y haz recomendaciones para mejorar el rendimiento de estas tiendas.
7. Operaciones con Numpy
Usar Numpy para realizar los siguientes cálculos sobre las ventas:
Mediana de las ventas totales.
Desviación estándar de las ventas totales.
Para los cálculos, convierte la columna Total_Ventas del DataFrame de Pandas a un array de Numpy usando .to_numpy (o .values si lo prefieres).
Genera arrays aleatorios utilizando la biblioteca Numpy para simular proyecciones de ventas futuras.
Usa el módulo de aleatoriedad de Numpy y asegúrate de establecer una semilla (seed) para obtener resultados reproducibles.
Estructura del proyecto
Archivo principal: analisis_red_tiendas.ipynb
Este notebook será el archivo donde se importan y procesan los datos, se realizan los análisis solicitados, y se muestran los resultados. Incluirá el procesamiento con Pandas y cálculos con Numpy.

Archivos CSV:
sales.csv: datos de ventas.
inventories.csv: datos de inventarios.
satisfaction.csv: datos de satisfacción de clientes.

REQUISITOS
El proyecto debe cumplir con los siguientes requisitos:

Utilizar el lenguaje de programación Python.
Utilizar las librerías Pandas y Numpy para el análisis de datos y las operaciones numéricas.
Implementar el proyecto en Visual Studio Code utilizando el plugin de Jupyter para trabajar con archivos .ipynb.
Cargar los datos desde los archivos CSV que están presentes en el proyecto. Las rutas de los archivos deben ser absolutas, como se muestra a continuación:
/workspace/sales.csv
/workspace/inventories.csv
/workspace/satisfaction.csv
Procesamiento de los datos:
Limpiar los datos eliminando filas con valores nulos.
Asegurar que los DataFrames tengan la estructura correcta y estén listos para su análisis.
Realizar los siguientes análisis estadísticos utilizando Pandas:
Calcular las ventas totales por tienda.
Calcular la rotación de inventarios por tienda.
Filtrar las tiendas con inventarios críticos (menos del 10% en ventas respecto al inventario disponible).
Analizar la satisfacción del cliente y filtrar las tiendas con una satisfacción menor al 60%.
Realizar cálculos numéricos con Numpy:
Calcular la mediana de las ventas totales.
Calcular la desviación estándar de las ventas.
Simular proyecciones de ventas futuras usando arrays aleatorios de Numpy.
El código debe estar bien organizado y comentado, explicando los pasos importantes del análisis y las operaciones realizadas.
El proyecto debe contener un archivo Jupyter Notebook (.ipynb) donde se implementen y expliquen los pasos, análisis y resultados obtenidos en cada sección.

'''

import pandas as pd
import numpy as np

# Rutas de los archivos CSV
RUTA_VENTAS       = "/Users/augusto/Documents/FundamentosProgramacion/4.Ejercicios/sales.csv"
RUTA_INVENTARIOS  = "/Users/augusto/Documents/FundamentosProgramacion/4.Ejercicios/inventories.csv"
RUTA_SATISFACCION = "/Users/augusto/Documents/FundamentosProgramacion/4.Ejercicios/satisfaction.csv"

# =============================================================================
# 1. CARGAR Y LIMPIAR DATOS
# =============================================================================

print("=" * 60)
print("  1. CARGA Y LIMPIEZA DE DATOS")
print("=" * 60)

df_ventas       = pd.read_csv(RUTA_VENTAS)
df_inventarios  = pd.read_csv(RUTA_INVENTARIOS)
df_satisfaccion = pd.read_csv(RUTA_SATISFACCION)

# Eliminar filas con valores nulos
df_ventas       = df_ventas.dropna()
df_inventarios  = df_inventarios.dropna()
df_satisfaccion = df_satisfaccion.dropna()

print(f"\nVentas cargadas      : {len(df_ventas)} registros")
print(f"Inventarios cargados : {len(df_inventarios)} registros")
print(f"Satisfacción cargada : {len(df_satisfaccion)} registros")

print("\nVista previa - Ventas:")
print(df_ventas.head())
print("\nVista previa - Inventarios:")
print(df_inventarios.head())
print("\nVista previa - Satisfacción:")
print(df_satisfaccion.head())

# =============================================================================
# 2. EXPLORACIÓN DE DATOS (PANDAS)
# =============================================================================

print("\n" + "=" * 60)
print("  2. EXPLORACIÓN DE DATOS")
print("=" * 60)

# Columna de ingresos: Cantidad_Vendida × Precio_Unitario
df_ventas["Total_Ventas"] = df_ventas["Cantidad_Vendida"] * df_ventas["Precio_Unitario"]

# Ventas totales por producto
ventas_por_producto = (
    df_ventas.groupby("Producto")["Total_Ventas"]
    .sum()
    .reset_index()
)
print("\nVentas totales por producto:")
print(ventas_por_producto.to_string(index=False))

# Ventas totales por tienda
ventas_por_tienda = (
    df_ventas.groupby("ID_Tienda")["Total_Ventas"]
    .sum()
    .reset_index()
)
print("\nVentas totales por tienda:")
print(ventas_por_tienda.to_string(index=False))

# Resumen estadístico de la columna Total_Ventas
print("\nResumen estadístico de Total_Ventas:")
print(df_ventas["Total_Ventas"].describe().to_string())

# =============================================================================
# 3. ANÁLISIS DE INVENTARIOS (PANDAS)
# =============================================================================

print("\n" + "=" * 60)
print("  3. ANÁLISIS DE INVENTARIOS")
print("=" * 60)

# Agrupar ventas por tienda y producto para cruzar con inventarios
ventas_agrupadas = (
    df_ventas.groupby(["ID_Tienda", "Producto"])["Cantidad_Vendida"]
    .sum()
    .reset_index()
)

# Combinar ventas e inventarios por tienda y producto
df_combinado = pd.merge(
    ventas_agrupadas,
    df_inventarios[["ID_Tienda", "Producto", "Stock_Disponible"]],
    on=["ID_Tienda", "Producto"],
    how="inner"
)

# Rotación: Cantidad_Vendida / Stock_Disponible
df_combinado["Rotacion_Inventario"] = (
    df_combinado["Cantidad_Vendida"] / df_combinado["Stock_Disponible"]
)

print("\nRotación de inventario por tienda y producto:")
print(df_combinado[["ID_Tienda", "Producto", "Cantidad_Vendida",
                     "Stock_Disponible", "Rotacion_Inventario"]].to_string(index=False))

# Inventario crítico: ventas < 10% del stock disponible
inventario_critico = df_combinado[df_combinado["Rotacion_Inventario"] < 0.10]
print("\nTiendas con inventario crítico (ventas < 10% del stock):")
if inventario_critico.empty:
    print("  No se encontraron tiendas con inventario crítico.")
else:
    print(inventario_critico[["ID_Tienda", "Producto",
                               "Cantidad_Vendida", "Stock_Disponible",
                               "Rotacion_Inventario"]].to_string(index=False))

# =============================================================================
# 4. SATISFACCIÓN DEL CLIENTE (PANDAS)
# =============================================================================

print("\n" + "=" * 60)
print("  4. SATISFACCIÓN DEL CLIENTE")
print("=" * 60)

# Cruzar ventas totales con satisfacción por tienda
df_resumen = pd.merge(
    ventas_por_tienda,
    df_satisfaccion[["ID_Tienda", "Satisfacción_Promedio"]],
    on="ID_Tienda",
    how="left"
)

print("\nVentas totales y satisfacción por tienda:")
print(df_resumen.to_string(index=False))

# Tiendas con satisfacción baja (< 60%)
satisfaccion_baja = df_resumen[df_resumen["Satisfacción_Promedio"] < 60]
print("\nTiendas con satisfacción menor al 60%:")
if satisfaccion_baja.empty:
    print("  Ninguna tienda presenta satisfacción baja.")
else:
    print(satisfaccion_baja.to_string(index=False))
    print("\n  Recomendación: revisar atención al cliente, tiempos de espera")
    print("  y disponibilidad de productos en estas tiendas.")

# =============================================================================
# 5. OPERACIONES CON NUMPY
# =============================================================================

print("\n" + "=" * 60)
print("  5. CÁLCULOS CON NUMPY")
print("=" * 60)

# Convertir Total_Ventas a array de Numpy
array_ventas = ventas_por_tienda["Total_Ventas"].to_numpy()

media    = np.mean(array_ventas)
mediana  = np.median(array_ventas)
desv_std = np.std(array_ventas)

print(f"\nArray de ventas por tienda : {array_ventas}")
print(f"  Media                    : {media:.2f}")
print(f"  Mediana                  : {mediana:.2f}")
print(f"  Desviación estándar      : {desv_std:.2f}")

# Proyección de ventas futuras con distribución normal (seed para reproducibilidad)
np.random.seed(42)
proyeccion = np.abs(np.random.normal(loc=media, scale=desv_std, size=5))

print("\nProyección de ventas futuras para 5 tiendas (simulación Numpy):")
for i, valor in enumerate(proyeccion, start=1):
    print(f"  Tienda {i}: {valor:.2f} €")

print("\n" + "=" * 60)
print("  ANÁLISIS COMPLETADO")
print("=" * 60)

'''
Trabajo 3: Análisis de datos con Numpy y Pandas
Pasos
Requisitos
Evaluación

RECURSOS DESCARGABLES
Necesitas descargar los siguientes recursos para realizar el ejercicio:

 
¿QUÉ HAY QUE HACER?
Este reto consiste en analizar los datos de ventas, los inventarios y la satisfacción del cliente para una cadena de tiendas minoristas; utilizando Pandas, para la manipulación de datos, y Numpy, para realizar cálculos estadísticos y simulaciones. El objetivo es ayudar a optimizar el rendimiento de las tiendas a través del análisis de estos datos.

PASOS A SEGUIR
La empresa ficticia RetailNow, que gestiona una cadena de tiendas minoristas, desea realizar un análisis detallado del rendimiento de sus diferentes sucursales en varias ciudades. Para ello, han recopilado datos de las ventas, los inventarios y la satisfacción del cliente en archivos CSV. Tu misión será procesar, explorar y analizar estos datos usando Pandas y Numpy para ayudar a la dirección a tomar decisiones estratégicas sobre la optimización del rendimiento de las tiendas.

1. Preparar el entorno de trabajo:
Abre Visual Studio Code y asegúrate de tener instalado el plugin de Jupyter.
Crea un nuevo archivo Jupyter Notebook llamado analisis_red_tiendas.ipynb.
2. Importar las librerías necesarias:
Importa las librerías Pandas y Numpy que necesitarás para realizar el análisis.
3. Cargar los datos (lectura y procesamiento de datos - Pandas):
Utiliza Pandas para cargar los archivos CSV: sales.csv, inventories.csv y satisfaction.csv.
Guarda los datos en tres DataFrames distintos.
Limpia los datos eliminando filas con valores nulos utilizando el método dropna(). Esto te permitirá trabajar solo con datos válidos.
4. Exploración de datos (Pandas)
Calcula las ventas totales por producto y por tienda.
Calcula los ingresos totales por tienda, multiplicando la cantidad vendida por el precio unitario.
Genera un resumen estadístico de las ventas utilizando el método describe() para obtener la media, mediana y otras métricas clave.
Si los productos están clasificados por categorías, calcula el promedio de ventas por tienda y categoría de productos.
Utiliza groupby() en Pandas para calcular las ventas totales por tienda o por categoría.
5. Análisis de inventarios (Pandas)
Calcula la rotación de inventarios para cada tienda. Esto se hace dividiendo las ventas totales por el stock disponible de cada producto.
Almacena los resultados en una nueva columna dentro del DataFrame de inventarios.
Filtra y muestra las tiendas con niveles críticos de inventario, es decir, aquellas tiendas donde el porcentaje de productos vendidos sea menor al 10% del stock disponible.
Utiliza groupby() y operaciones matemáticas para calcular la rotación de inventarios.
Aplica filtros con Pandas para identificar las tiendas con niveles críticos.
6. Satisfacción del cliente (Pandas)
Realiza un análisis de la satisfacción de los clientes en cada tienda. Relaciona estos datos con el rendimiento de las ventas.
Filtra las tiendas con niveles bajos de satisfacción (< 60%) y haz recomendaciones para mejorar el rendimiento de estas tiendas.
7. Operaciones con Numpy
Usar Numpy para realizar los siguientes cálculos sobre las ventas:
Mediana de las ventas totales.
Desviación estándar de las ventas totales.
Para los cálculos, convierte la columna Total_Ventas del DataFrame de Pandas a un array de Numpy usando .to_numpy (o .values si lo prefieres).
Genera arrays aleatorios utilizando la biblioteca Numpy para simular proyecciones de ventas futuras.
Usa el módulo de aleatoriedad de Numpy y asegúrate de establecer una semilla (seed) para obtener resultados reproducibles.
Estructura del proyecto
Archivo principal: analisis_red_tiendas.ipynb
Este notebook será el archivo donde se importan y procesan los datos, se realizan los análisis solicitados, y se muestran los resultados. Incluirá el procesamiento con Pandas y cálculos con Numpy.

Archivos CSV:
sales.csv: datos de ventas.
inventories.csv: datos de inventarios.
satisfaction.csv: datos de satisfacción de clientes.

REQUISITOS
El proyecto debe cumplir con los siguientes requisitos:

Utilizar el lenguaje de programación Python.
Utilizar las librerías Pandas y Numpy para el análisis de datos y las operaciones numéricas.
Implementar el proyecto en Visual Studio Code utilizando el plugin de Jupyter para trabajar con archivos .ipynb.
Cargar los datos desde los archivos CSV que están presentes en el proyecto. Las rutas de los archivos deben ser absolutas, como se muestra a continuación:
/workspace/sales.csv
/workspace/inventories.csv
/workspace/satisfaction.csv
Procesamiento de los datos:
Limpiar los datos eliminando filas con valores nulos.
Asegurar que los DataFrames tengan la estructura correcta y estén listos para su análisis.
Realizar los siguientes análisis estadísticos utilizando Pandas:
Calcular las ventas totales por tienda.
Calcular la rotación de inventarios por tienda.
Filtrar las tiendas con inventarios críticos (menos del 10% en ventas respecto al inventario disponible).
Analizar la satisfacción del cliente y filtrar las tiendas con una satisfacción menor al 60%.
Realizar cálculos numéricos con Numpy:
Calcular la mediana de las ventas totales.
Calcular la desviación estándar de las ventas.
Simular proyecciones de ventas futuras usando arrays aleatorios de Numpy.
El código debe estar bien organizado y comentado, explicando los pasos importantes del análisis y las operaciones realizadas.
El proyecto debe contener un archivo Jupyter Notebook (.ipynb) donde se implementen y expliquen los pasos, análisis y resultados obtenidos en cada sección.

CÓMO SE EVALÚA
Tu solución se calificará según estos criterios:

Carga y manejo de datos (Pandas)
30%
Cargar correctamente los datos de los archivos CSV (sales.csv, inventories.csv, satisfaction.csv) en Pandas. Limpiar los datos eliminando filas con valores nulos y verificar que los DataFrames tengan la estructura correcta para el análisis.
Análisis de datos (Pandas)
30%
Realizar correctamente el análisis de ventas totales, rotación de inventarios y satisfacción del cliente. Filtrar correctamente las tiendas con niveles críticos de inventario (<10%) y con baja satisfacción del cliente (<60%).
Cálculos estadísticos (Numpy)
20%
Utilizar Numpy para calcular la mediana y desviación estándar sobre las ventas. El objetivo es comprobar que sabes usar Numpy, aunque la operación se pueda hacer igualmente en Pandas debes usar Numpy.
Simulación de datos (Numpy)
20%
Simular proyecciones de ventas futuras utilizando arrays aleatorios de Numpy y calcular estadísticas básicas sobre esas proyecciones.
'''