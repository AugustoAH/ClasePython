'''
Ejercicio practicando self


OBJETIVO
Crear una clase con métodos que utilicen self para acceder a atributos de instancia

INSTRUCCIONES
Crea una clase llamada Libro con los siguientes requisitos:

El constructor debe inicializar tres atributos de instancia: titulo, autor y páginas.

Implementa un método llamado describir que devuelva un string con el formato: "[Titulo] escrito por [Autor] - [Páginas] páginas".

Implementa un método llamado es_largo que devuelva True si el libro tiene más de 300 páginas, y False en caso contrario.

Implementa un método llamado resumir que reciba un parámetro longitud y devuelva un string con el formato: "[Titulo] - Resumen de [longitud] caracteres". Si no se proporciona el parámetro longitud, debe usar un valor predeterminado de 50.

Prueba tu clase creando al menos dos instancias diferentes de Libro y llamando a todos sus métodos.
'''


class Libro:

    def __init__(self, titulo, autor, paginas):
        self.titulo  = titulo
        self.autor   = autor
        self.paginas = paginas

    def describir(self):
        return f"{self.titulo} escrito por {self.autor} - {self.paginas} páginas"

    def es_largo(self):
        return self.paginas > 300

    def resumir(self, longitud=50):
        return f"{self.titulo} - Resumen de {longitud} caracteres"


# --- Prueba con dos instancias ---

libro1 = Libro("El Quijote", "Miguel de Cervantes", 863)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

print("--- Libro 1 ---")
print(libro1.describir())
print(f"¿Es largo? {libro1.es_largo()}")
print(libro1.resumir())
print(libro1.resumir(longitud=100))

print("\n--- Libro 2 ---")
print(libro2.describir())
print(f"¿Es largo? {libro2.es_largo()}")
print(libro2.resumir())
print(libro2.resumir(longitud=30))