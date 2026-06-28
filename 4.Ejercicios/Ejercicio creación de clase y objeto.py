'''
Ejercicio creación de clase y objeto


OBJETIVO
Crear una clase Persona con atributos y un método para presentarse

INSTRUCCIONES
Crea una clase llamada Persona con los siguientes elementos:

Un constructor __init__ que reciba como parámetros nombre y edad y los almacene como atributos de instancia.

Un método llamado presentarse que devuelva un string con el formato: "Hola, me llamo {nombre} y tengo {edad} años".

Luego, crea una instancia de la clase Persona con tu nombre y edad, y llama al método presentarse para verificar que funciona correctamente.
'''


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"


# Crear instancia y verificar
persona1 = Persona("Augusto", 25)
print(persona1.presentarse())