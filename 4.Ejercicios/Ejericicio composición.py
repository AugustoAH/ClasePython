'''
Ejericicio composición


OBJETIVO
Crear un sistema de biblioteca usando composición en Python

INSTRUCCIONES
Implementa un sistema básico de biblioteca utilizando composición. Crea una clase Libro con atributos para título, autor y año de publicación. Luego, crea una clase Biblioteca que contenga una colección de libros (relación "tiene un"). La clase Biblioteca debe incluir métodos para:

Agregar un nuevo libro a la colección
Buscar libros por título (devolviendo todos los que contengan la cadena de búsqueda)
Contar cuántos libros hay de un autor específico
No utilices herencia para resolver este ejercicio, solo composición. Asegúrate de que la clase Biblioteca delegue apropiadamente en los objetos Libro que contiene.
'''


# =============================================================================
# Clase componente — Libro
# =============================================================================

class Libro:

    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor  = autor
        self.año    = año

    def __str__(self):
        return f'"{self.titulo}" — {self.autor} ({self.año})'


# =============================================================================
# Clase contenedora — Biblioteca (composición: "tiene una colección de Libros")
# =============================================================================

class Biblioteca:

    def __init__(self, nombre):
        self.nombre  = nombre
        self.libros  = []          # lista interna de objetos Libro

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_por_titulo(self, cadena):
        # Delega en cada objeto Libro comparando su atributo titulo
        resultado = [libro for libro in self.libros
                     if cadena.lower() in libro.titulo.lower()]
        return resultado

    def contar_por_autor(self, autor):
        # Delega en cada objeto Libro comparando su atributo autor
        return sum(1 for libro in self.libros
                   if libro.autor.lower() == autor.lower())


# =============================================================================
# Prueba
# =============================================================================

biblioteca = Biblioteca("Biblioteca Central")

biblioteca.agregar_libro(Libro("Cien años de soledad",    "Gabriel García Márquez", 1967))
biblioteca.agregar_libro(Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985))
biblioteca.agregar_libro(Libro("El Quijote",              "Miguel de Cervantes",    1605))
biblioteca.agregar_libro(Libro("La sombra del viento",    "Carlos Ruiz Zafón",      2001))
biblioteca.agregar_libro(Libro("El laberinto de los espíritus", "Carlos Ruiz Zafón", 2016))

# Buscar por título
print("Búsqueda por 'el':")
for libro in biblioteca.buscar_por_titulo("el"):
    print(f"  {libro}")

# Contar por autor
autor = "Gabriel García Márquez"
total = biblioteca.contar_por_autor(autor)
print(f"\nLibros de {autor}: {total}")

autor2 = "Carlos Ruiz Zafón"
total2 = biblioteca.contar_por_autor(autor2)
print(f"Libros de {autor2}: {total2}")

