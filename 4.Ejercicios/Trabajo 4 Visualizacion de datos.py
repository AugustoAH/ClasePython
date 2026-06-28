'''
Trabajo 4: Visualización de datos con Matplotlib y Seaborn
Contexto
Pasos
Requisitos
Evaluación

RECURSOS DESCARGABLES
Necesitas descargar los siguientes recursos para realizar el ejercicio:

 
¿QUÉ HAY QUE HACER?
Creación de visualizaciones con Matplotlib y Seaborn para analizar un conjunto de datos de ventas minoristas.

CONTEXTO
Si usas Visual Studio Code en la plataforma, al abrirlo te aparecerá el dataset superstore_dataset2012.csv, si optas por usar tu propio entorno en tu ordenador y subir la solución en zip o github entonces puedes descargar manualmente el dataset pulsando aquí, para que lo puedas usar en tu ordenador.

PASOS A SEGUIR
Configura tu entorno de trabajo
Crea un nuevo archivo Python (.py) o un notebook Jupyter (.ipynb). Importa las bibliotecas necesarias (pandas, matplotlib, seaborn) y carga el dataset superstore_dataset2012.csv que ya está disponible en tu entorno.

Explora y prepara los datos
Realiza una exploración inicial del dataset para entender su estructura. Verifica los tipos de datos, valores nulos y realiza las transformaciones necesarias (como convertir fechas al formato adecuado).

Crea visualizaciones univariantes con Matplotlib
Implementa al menos un histograma o diagrama de barras utilizando Matplotlib para visualizar la distribución de una variable numérica (como Ventas o Beneficios) o la frecuencia de una variable categórica (como Categoría o Segmento).

Crea visualizaciones univariantes con Seaborn
Utiliza Seaborn para crear al menos un diagrama de caja (boxplot) o un gráfico de violín (violinplot) para visualizar la distribución de una variable numérica, posiblemente agrupada por una variable categórica.

Implementa gráficos bivariantes con Matplotlib
Crea un gráfico de dispersión o de líneas con Matplotlib para mostrar la relación entre dos variables numéricas (por ejemplo, Ventas vs. Beneficios) o la evolución temporal de una variable.

Implementa gráficos bivariantes con Seaborn
Utiliza Seaborn para crear un gráfico bivariante como un gráfico de barras agrupadas, un gráfico de dispersión con regresión (regplot) o un gráfico de líneas mejorado.

Crea una visualización multivariante con Seaborn
Implementa un heatmap de correlación o un pairplot para visualizar las relaciones entre múltiples variables numéricas del dataset.

Organiza visualizaciones en subplots
Crea una figura con múltiples subplots que muestre al menos 4 visualizaciones diferentes, organizadas de manera coherente y con un título general.

Personaliza las visualizaciones
Mejora la apariencia de tus gráficos añadiendo títulos descriptivos, etiquetas de ejes claras, leyendas cuando sea necesario y utilizando paletas de colores apropiadas.

Guarda y documenta tu trabajo
Guarda al menos una de tus visualizaciones como archivo de imagen. Añade comentarios a tu código explicando las conclusiones que se pueden extraer de cada visualización y cómo contribuyen al análisis general de los datos.

REQUISITOS
Crear al menos un gráfico univariante (histograma, diagrama de barras o diagrama de caja) utilizando Matplotlib
Crear al menos un gráfico univariante utilizando Seaborn
Implementar al menos un gráfico bivariante (dispersión, líneas o barras agrupadas) con Matplotlib
Implementar al menos un gráfico bivariante con Seaborn
Crear una visualización multivariante (como un gráfico de pares o un heatmap de correlación) con Seaborn
Personalizar los gráficos (títulos, etiquetas de ejes, paletas de colores)
Organizar múltiples visualizaciones en una figura usando subplots
Guardar al menos una figura generada como archivo de imagen
Incluir comentarios explicativos sobre las conclusiones obtenidas de cada visualización
Utilizar el dataset superstore_dataset2012.csv proporcionado

CÓMO SE EVALÚA
Tu solución se calificará según estos criterios:

Implementación de visualizaciones con Matplotlib
40%
Correcta creación de gráficos univariantes, bivariantes y multivariantes con Matplotlib.
Implementación de visualizaciones con Seaborn
40%
Implementación efectiva de visualizaciones univariantes, bivariantes, multivariantes con Seaborn
Preparación y manejo de datos con Pandas
20%
Correcta carga y preparación del dataset, incluyendo transformaciones necesarias como conversión de fechas, y manejo adecuado de los datos para las visualizaciones.

TECNOLOGÍAS A UTILIZAR
 Matplotlib
Matplotlib
 Seaborn
Seaborn
'''

import pandas as pd
import matplotlib
matplotlib.use("Agg")           # Backend sin ventana (compatible con cualquier entorno)
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# Carpeta de trabajo
RUTA_CSV    = "/Users/augusto/Documents/FundamentosProgramacion/4.Ejercicios/superstore_dataset2012.csv"
RUTA_SALIDA = "/Users/augusto/Documents/FundamentosProgramacion/4.Ejercicios/"

# Estilo visual global
sns.set_theme(style="whitegrid", palette="muted")

# =============================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# =============================================================================

df = pd.read_csv(RUTA_CSV, encoding="latin1")

# Convertir fechas a datetime (formato mixto para cubrir barras y guiones)
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=True)
df["Ship Date"]  = pd.to_datetime(df["Ship Date"],  format="mixed", dayfirst=True)

# Columna de año-mes para análisis temporal
df["YearMonth"] = df["Order Date"].dt.to_period("M")

# Eliminar filas con nulos en columnas clave
df = df.dropna(subset=["Sales", "Profit", "Category", "Segment", "Region"])

print(f"Dataset cargado: {df.shape[0]} filas x {df.shape[1]} columnas")
print(f"Categorías : {df['Category'].unique()}")
print(f"Segmentos  : {df['Segment'].unique()}")
print(f"Periodo    : {df['Order Date'].min().date()} → {df['Order Date'].max().date()}")

# =============================================================================
# 2. UNIVARIANTE CON MATPLOTLIB — Histograma de ventas
# =============================================================================
# Muestra la distribución de las ventas: la mayoría se concentra
# en valores bajos, con algunos pedidos de alto valor (cola derecha).

fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(df["Sales"], bins=60, color="#4C72B0", edgecolor="white", alpha=0.85)
ax.set_title("Distribución de ventas por pedido", fontsize=14, fontweight="bold")
ax.set_xlabel("Ventas (€)")
ax.set_ylabel("Frecuencia")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.set_xlim(left=0)

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "01_histograma_ventas.png", dpi=150)
plt.close()
print("Guardado: 01_histograma_ventas.png")

# =============================================================================
# 3. UNIVARIANTE CON SEABORN — Boxplot de Beneficio por Categoría
# =============================================================================
# Los boxplots revelan medianas, dispersión y outliers por categoría.
# Technology muestra mayor variabilidad en beneficios que Furniture.

fig, ax = plt.subplots(figsize=(9, 5))

sns.boxplot(data=df, x="Category", y="Profit", hue="Category",
            palette=["#4C72B0", "#DD8452", "#55A868"], legend=False, ax=ax)
ax.set_title("Distribución de beneficios por categoría", fontsize=14, fontweight="bold")
ax.set_xlabel("Categoría")
ax.set_ylabel("Beneficio (€)")
ax.axhline(0, color="red", linewidth=0.8, linestyle="--", label="Beneficio = 0")
ax.legend()

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "02_boxplot_beneficio_categoria.png", dpi=150)
plt.close()
print("Guardado: 02_boxplot_beneficio_categoria.png")

# =============================================================================
# 4. BIVARIANTE CON MATPLOTLIB — Dispersión Ventas vs Beneficio
# =============================================================================
# Se observa correlación positiva general, pero con una nube de puntos con
# beneficios negativos que indican pedidos con descuentos excesivos.

colores_cat = {"Furniture": "#4C72B0", "Office Supplies": "#DD8452", "Technology": "#55A868"}

fig, ax = plt.subplots(figsize=(9, 6))

for categoria, grupo in df.groupby("Category"):
    ax.scatter(
        grupo["Sales"], grupo["Profit"],
        label=categoria, alpha=0.4, s=18,
        color=colores_cat[categoria]
    )

ax.axhline(0, color="red", linewidth=0.8, linestyle="--")
ax.set_title("Ventas vs Beneficio por categoría", fontsize=14, fontweight="bold")
ax.set_xlabel("Ventas (€)")
ax.set_ylabel("Beneficio (€)")
ax.legend(title="Categoría")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "03_scatter_ventas_beneficio.png", dpi=150)
plt.close()
print("Guardado: 03_scatter_ventas_beneficio.png")

# =============================================================================
# 5. BIVARIANTE CON SEABORN — Ventas totales por Segmento y Categoría
# =============================================================================
# Consumer es el segmento con mayor volumen de ventas.
# Technology lidera en ingresos en todos los segmentos.

ventas_seg_cat = (
    df.groupby(["Segment", "Category"])["Sales"]
    .sum()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(9, 5))

sns.barplot(data=ventas_seg_cat, x="Segment", y="Sales",
            hue="Category", palette=["#4C72B0", "#DD8452", "#55A868"], ax=ax)
ax.set_title("Ventas totales por segmento y categoría", fontsize=14, fontweight="bold")
ax.set_xlabel("Segmento")
ax.set_ylabel("Ventas totales (€)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.legend(title="Categoría")

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "04_barras_segmento_categoria.png", dpi=150)
plt.close()
print("Guardado: 04_barras_segmento_categoria.png")

# =============================================================================
# 6. BIVARIANTE CON SEABORN — Evolución temporal de ventas mensuales
# =============================================================================
# Permite detectar tendencias y estacionalidades a lo largo del año.

ventas_mes = (
    df.groupby("YearMonth")["Sales"]
    .sum()
    .reset_index()
)
ventas_mes["YearMonth_str"] = ventas_mes["YearMonth"].astype(str)

fig, ax = plt.subplots(figsize=(12, 5))

sns.lineplot(data=ventas_mes, x="YearMonth_str", y="Sales",
             marker="o", color="#4C72B0", linewidth=2, ax=ax)
ax.set_title("Evolución mensual de ventas totales", fontsize=14, fontweight="bold")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas totales (€)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "05_linea_ventas_mensuales.png", dpi=150)
plt.close()
print("Guardado: 05_linea_ventas_mensuales.png")

# =============================================================================
# 6. MULTIVARIANTE CON MATPLOTLIB — Bubble chart (Ventas / Beneficio / Cantidad / Categoría)
# =============================================================================
# Gráfico multivariante puro con Matplotlib: representa 4 variables a la vez.
#   Eje X    → Ventas      (1ª variable numérica)
#   Eje Y    → Beneficio   (2ª variable numérica)
#   Tamaño   → Cantidad    (3ª variable numérica: burbujas más grandes = más unidades)
#   Color    → Categoría   (4ª variable categórica)
# Permite detectar de un vistazo qué categorías generan más beneficio por volumen
# y cuáles caen en pérdidas pese a ventas altas (zona por debajo del eje Y=0).

colores_cat  = {"Furniture": "#4C72B0", "Office Supplies": "#DD8452", "Technology": "#55A868"}
handles_leyenda = []

fig, ax = plt.subplots(figsize=(11, 7))

for categoria, grupo in df.groupby("Category"):
    sc = ax.scatter(
        grupo["Sales"],
        grupo["Profit"],
        s=grupo["Quantity"] * 8,        # tamaño proporcional a la cantidad
        c=colores_cat[categoria],
        alpha=0.45,
        edgecolors="white",
        linewidths=0.4,
        label=categoria
    )
    handles_leyenda.append(sc)

ax.axhline(0, color="red", linewidth=1, linestyle="--", alpha=0.7)
ax.set_title("Ventas vs Beneficio por Categoría\n(tamaño de burbuja = Cantidad vendida)",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Ventas (€)")
ax.set_ylabel("Beneficio (€)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.legend(title="Categoría", handles=handles_leyenda)

# Anotación explicativa
ax.annotate("Pedidos con pérdidas\n(descuentos altos)",
            xy=(200, -500), fontsize=9, color="red",
            arrowprops=dict(arrowstyle="->", color="red"),
            xytext=(800, -1200))

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "06_bubble_multivariante_matplotlib.png", dpi=150)
plt.close()
print("Guardado: 06_bubble_multivariante_matplotlib.png")

# =============================================================================
# 7. MULTIVARIANTE CON SEABORN — Heatmap de correlación
# =============================================================================
# El heatmap muestra qué variables numéricas están relacionadas entre sí.
# El descuento (Discount) tiene correlación negativa con el beneficio.

columnas_num = ["Sales", "Quantity", "Discount", "Profit", "Shipping Cost"]
correlacion  = df[columnas_num].corr()

fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(
    correlacion, annot=True, fmt=".2f",
    cmap="coolwarm", center=0,
    linewidths=0.5, ax=ax
)
ax.set_title("Mapa de correlación entre variables numéricas",
             fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "07_heatmap_correlacion.png", dpi=150)
plt.close()
print("Guardado: 07_heatmap_correlacion.png")

# =============================================================================
# 8. PANEL DE 4 SUBPLOTS — Resumen visual del análisis
# =============================================================================
# Vista compacta con las visualizaciones más relevantes en una sola figura.

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Análisis de ventas — RetailNow 2012",
             fontsize=16, fontweight="bold", y=1.01)

# --- Subplot 1: Ventas totales por categoría (barras) ---
ventas_cat = df.groupby("Category")["Sales"].sum().reset_index()
axes[0, 0].bar(ventas_cat["Category"], ventas_cat["Sales"],
               color=["#4C72B0", "#DD8452", "#55A868"], edgecolor="white")
axes[0, 0].set_title("Ventas totales por categoría")
axes[0, 0].set_ylabel("Ventas (€)")
axes[0, 0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

# --- Subplot 2: Boxplot Descuento por Categoría ---
sns.boxplot(data=df, x="Category", y="Discount", hue="Category",
            palette=["#4C72B0", "#DD8452", "#55A868"], legend=False, ax=axes[0, 1])
axes[0, 1].set_title("Distribución de descuentos por categoría")
axes[0, 1].set_ylabel("Descuento")
axes[0, 1].set_xlabel("Categoría")

# --- Subplot 3: Dispersión Descuento vs Beneficio ---
axes[1, 0].scatter(df["Discount"], df["Profit"],
                   alpha=0.3, s=12, color="#4C72B0")
axes[1, 0].axhline(0, color="red", linewidth=0.8, linestyle="--")
axes[1, 0].set_title("Descuento vs Beneficio")
axes[1, 0].set_xlabel("Descuento")
axes[1, 0].set_ylabel("Beneficio (€)")

# --- Subplot 4: Top 5 regiones por ventas (barras horizontales) ---
ventas_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .nlargest(5)
    .reset_index()
)
axes[1, 1].barh(ventas_region["Region"], ventas_region["Sales"],
                color="#4C72B0", edgecolor="white")
axes[1, 1].set_title("Top 5 regiones por ventas")
axes[1, 1].set_xlabel("Ventas (€)")
axes[1, 1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

plt.tight_layout()
plt.savefig(RUTA_SALIDA + "08_panel_subplots.png", dpi=150, bbox_inches="tight")
plt.close()
print("Guardado: 08_panel_subplots.png")

# =============================================================================
# RESUMEN DE CONCLUSIONES
# =============================================================================

print("\n" + "=" * 60)
print("  CONCLUSIONES DEL ANÁLISIS")
print("=" * 60)

top_cat  = df.groupby("Category")["Sales"].sum().idxmax()
peor_cat = df.groupby("Category")["Profit"].mean().idxmin()
region_top = df.groupby("Region")["Sales"].sum().idxmax()
pct_perdidas = (df["Profit"] < 0).mean() * 100

print(f"\n  Categoría con más ventas   : {top_cat}")
print(f"  Categoría menos rentable   : {peor_cat}")
print(f"  Región con más ventas      : {region_top}")
print(f"  % pedidos con pérdidas     : {pct_perdidas:.1f}%")
print("\n  El descuento tiene correlación negativa con el beneficio.")
print("  Reducir descuentos excesivos mejoraría la rentabilidad.")
print("\n  Imágenes guardadas en:")
print(f"  {RUTA_SALIDA}")
print("=" * 60)