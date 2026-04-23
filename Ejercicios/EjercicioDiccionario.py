'''
</>  Reto código

Objetivo: Crear un diccionario para almacenar información de contactos y acceder a sus datos

Crea un diccionario llamado contactos que contenga la información de tres personas. Para cada persona, almacena su nombre, 
teléfono y correo electrónico. Luego, realiza las siguientes operaciones:

    * Muestra el correo electrónico de la segunda persona que añadiste al diccionario.
    * Añade un nuevo contacto con la información que prefieras.
    * Modifica el número de teléfono de la primera persona que añadiste.
    * Utiliza un bucle para mostrar los nombres de todos los contactos.

Puedes empezar con algo como:

'''

contactos = {
    "persona1": {"nombre": "Alice", "telefono": "123-456-7890", "email": "alice@ejemplo.com"},
    "persona2": {"nombre": "Bob", "telefono": "098-765-4321", "email": "bob@ejemplo.com"},
    "persona3": {"nombre": "Charlie", "telefono": "555-555-5555", "email": "charlie@ejemplo.com"}
}
# Mostrar el correo electrónico de la segunda persona
print("Correo electrónico de la segunda persona:", contactos["persona2"]["email"])

# Añadir un nuevo contacto
contactos["persona4"] = {"nombre": "David", "telefono": "111-222-3333", "email": "david@ejemplo.com"}

# Modificar el número de teléfono de la primera persona
contactos["persona1"]["telefono"] = "999-888-7777"

# Mostrar los nombres de todos los contactos
print("Nombres de todos los contactos:")
for persona in contactos:
    print(contactos[persona]["nombre"]) 

#Otra Solución:
# Creación del diccionario de contactos con tres personas
contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona2": {"nombre": "Carlos", "telefono": "987654321", "email": "carlos@ejemplo.com"},
    "persona3": {"nombre": "Elena", "telefono": "555123456", "email": "elena@ejemplo.com"}
}
# 1. Mostrar el correo electrónico de la segunda persona
print("Correo electrónico de la segunda persona:")
print(contactos["persona2"]["email"])
print()
# 2. Añadir un nuevo contacto
contactos["persona4"] = {"nombre": "Miguel", "telefono": "666777888", "email": "miguel@ejemplo.com"}
print("Contacto añadido correctamente.")
print()
# 3. Modificar el número de teléfono de la primera persona
contactos["persona1"]["telefono"] = "111222333"
print("Teléfono de Ana modificado a:", contactos["persona1"]["telefono"])
print()
# 4. Mostrar los nombres de todos los contactos usando un bucle
print("Lista de todos los contactos:")
for clave, datos in contactos.items():
    print(f"- {datos['nombre']}")

