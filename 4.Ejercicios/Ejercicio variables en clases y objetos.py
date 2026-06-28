'''
Ejercicio variables en clases y objetos


OBJETIVO
Crear una clase con variables de clase e instancia para gestionar un sistema de biblioteca

INSTRUCCIONES
Crea una clase llamada Biblioteca que gestione libros utilizando variables de clase e instancia adecuadamente.

La clase debe tener:

Una variable de clase total_libros inicializada en 0 que lleve la cuenta de todos los libros en el sistema.
Una variable de clase nombre_biblioteca con el valor "Biblioteca Central".
En el método __init__, recibe el parámetro nombre_sección (por ejemplo "Ficción", "Historia", etc.) y crea una variable de instancia para almacenarlo.
En el método __init__, inicializa una variable de instancia libros como una lista vacía para almacenar los libros de esa sección.
Un método agregar_libro(self, titulo) que añada el título a la lista de libros de la sección e incremente la variable de clase total_libros.
Un método obtener_informe(self) que devuelva un string con el formato: "Sección [nombre_sección] de [nombre_biblioteca]: [cantidad] libros".
Finalmente, crea dos instancias de la clase con diferentes secciones, agrega algunos libros a cada una y muestra sus informes para verificar que la variable de clase se comparte correctamente.
'''


class Biblioteca:

    # Variables de clase: compartidas por todas las instancias
    total_libros      = 0
    nombre_biblioteca = "Biblioteca Central"

    def __init__(self, nombre_seccion):
        # Variables de instancia: únicas para cada sección
        self.nombre_seccion = nombre_seccion
        self.libros         = []

    def agregar_libro(self, titulo):
        self.libros.append(titulo)
        Biblioteca.total_libros += 1   # se actualiza en la clase, no en la instancia

    def obtener_informe(self):
        cantidad = len(self.libros)
        return (f"Sección {self.nombre_seccion} de "
                f"{Biblioteca.nombre_biblioteca}: {cantidad} libros")


# --- Prueba con dos secciones ---

seccion_ficcion  = Biblioteca("Ficción")
seccion_historia = Biblioteca("Historia")

seccion_ficcion.agregar_libro("El Quijote")
seccion_ficcion.agregar_libro("Cien años de soledad")
seccion_ficcion.agregar_libro("1984")

seccion_historia.agregar_libro("Sapiens")
seccion_historia.agregar_libro("El arte de la guerra")

print(seccion_ficcion.obtener_informe())
print(seccion_historia.obtener_informe())

# La variable de clase refleja el total acumulado de ambas secciones
print(f"\nTotal de libros en {Biblioteca.nombre_biblioteca}: {Biblioteca.total_libros}")
