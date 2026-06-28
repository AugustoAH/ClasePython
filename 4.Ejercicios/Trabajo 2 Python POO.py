'''
Trabajo 2: Python Programación Orientada a Objetos

¿QUÉ HAY QUE HACER?
Desarrollar un sistema básico de inventario con POO en Python para gestionar productos y realizar operaciones de inventario.

PASOS A SEGUIR
Crea un archivo llamado sistema_inventario.py donde implementarás todo el código del sistema.

Define la clase Producto con un método constructor que inicialice los atributos nombre (str), precio (float) y cantidad (int). Incluye validaciones para que el precio sea mayor o igual que cero, el nombre no esté vacío y la cantidad sea mayor o igual a cero.

Añade a la clase Producto los siguientes métodos:

actualizar_precio(nuevo_precio): para modificar el precio validando que sea mayor o igual que cero
actualizar_cantidad(nueva_cantidad): para modificar la cantidad validando que sea mayor o igual a cero
calcular_valor_total(): que devuelva el valor total (precio × cantidad)
__str__(): para mostrar la información del producto de forma legible
Crea la clase Inventario con un constructor que inicialice una lista vacía para almacenar productos.

Implementa en la clase Inventario los siguientes métodos:

agregar_producto(producto): para añadir un objeto de tipo Producto a la lista
buscar_producto(nombre): para encontrar un producto por su nombre (búsqueda exacta, insensible a mayúsculas/minúsculas). Debe devolver el producto si lo encuentra o None si no existe
calcular_valor_inventario(): para sumar el valor total de todos los productos
listar_productos(): para mostrar todos los productos del inventario
Implementa un manejo de excepciones utilizando bloques try-except para capturar errores como valores inválidos (cantidades negativas), tipos de datos incorrectos o productos no encontrados.

Crea una función menu_principal() que muestre opciones al usuario (1. Agregar producto, 2. Buscar producto, 3. Listar productos, 4. Calcular valor total del inventario, 5. Salir) y procese la entrada del usuario en un bucle hasta que elija salir.

En la sección principal del programa (bajo if __name__ == "__main__":), instancia un objeto de la clase Inventario y llama a la función menu_principal() para iniciar la aplicación.

REQUISITOS
Crear una clase Producto con atributos para nombre, precio y cantidad
Implementar métodos para añadir, actualizar y mostrar información de productos
Desarrollar una clase Inventario que gestione una colección de productos
Implementar operaciones de inventario: añadir producto, buscar por nombre y calcular valor total
Manejar excepciones para entradas inválidas (cantidades negativas, nombres vacíos, etc.)
Crear un menú interactivo simple para probar las funcionalidades
Mostrar resultados de operaciones por consola de manera formateada
Validar que los datos ingresados sean del tipo correcto
'''


# =============================================================================
# CLASE PRODUCTO
# =============================================================================

class Producto:

    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero mayor o igual a cero.")

        self.nombre   = nombre.strip()
        self.precio   = float(precio)
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: float):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a cero.")
        self.precio = float(nuevo_precio)
        print(f"Precio de '{self.nombre}' actualizado a {self.precio:.2f} €.")

    def actualizar_cantidad(self, nueva_cantidad: int):
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser un entero mayor o igual a cero.")
        self.cantidad = nueva_cantidad
        print(f"Cantidad de '{self.nombre}' actualizada a {self.cantidad} unidades.")

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return (
            f"  Nombre   : {self.nombre}\n"
            f"  Precio   : {self.precio:.2f} €\n"
            f"  Cantidad : {self.cantidad} unidades\n"
            f"  Valor    : {self.calcular_valor_total():.2f} €"
        )


# =============================================================================
# CLASE INVENTARIO
# =============================================================================

class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        # Evitar duplicados por nombre
        if self.buscar_producto(producto.nombre):
            raise ValueError(f"Ya existe un producto con el nombre '{producto.nombre}'.")
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente.")

    def buscar_producto(self, nombre: str) -> Producto | None:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.strip().lower():
                return producto
        return None

    def calcular_valor_inventario(self) -> float:
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print(f"\n{'=' * 40}")
        print(f"  INVENTARIO ({len(self.productos)} producto/s)")
        print(f"{'=' * 40}")
        for i, producto in enumerate(self.productos, start=1):
            print(f"\n  [{i}]")
            print(producto)
        print(f"\n{'=' * 40}")
        print(f"  VALOR TOTAL: {self.calcular_valor_inventario():.2f} €")
        print(f"{'=' * 40}\n")


# =============================================================================
# MENÚ PRINCIPAL
# =============================================================================

def menu_principal(inventario: Inventario):

    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE INVENTARIO")
        print("=" * 40)
        print("  1. Agregar producto")
        print("  2. Buscar producto")
        print("  3. Listar productos")
        print("  4. Calcular valor total del inventario")
        print("  5. Salir")
        print("=" * 40)

        opcion = input("  Elige una opción: ").strip()

        # --- Opción 1: Agregar producto ---
        if opcion == "1":
            try:
                nombre   = input("  Nombre del producto: ")
                precio   = float(input("  Precio (€): "))
                cantidad = int(input("  Cantidad: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
            except ValueError as e:
                print(f"  Error: {e}")
            except TypeError as e:
                print(f"  Error de tipo: {e}")

        # --- Opción 2: Buscar producto ---
        elif opcion == "2":
            nombre = input("  Nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print("\n  Producto encontrado:")
                print(producto)
            else:
                print(f"  No se encontró ningún producto con el nombre '{nombre}'.")

        # --- Opción 3: Listar productos ---
        elif opcion == "3":
            inventario.listar_productos()

        # --- Opción 4: Calcular valor total ---
        elif opcion == "4":
            total = inventario.calcular_valor_inventario()
            print(f"\n  Valor total del inventario: {total:.2f} €")

        # --- Opción 5: Salir ---
        elif opcion == "5":
            print("\n  Cerrando el sistema. ¡Hasta luego!")
            break

        else:
            print("  Opción no válida. Elige un número del 1 al 5.")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)