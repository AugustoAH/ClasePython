'''
Ejercicio de herencia


OBJETIVO
Crear una jerarquía de clases para modelar diferentes tipos de vehículos

INSTRUCCIONES
Crea una jerarquía de clases para modelar vehículos. Debes implementar:

Una clase base Vehículo con los siguientes atributos y métodos:
Atributos: marca, modelo y año
Un método mostrar_info() que devuelva un string con la información básica del vehículo
Una clase derivada Automovil que herede de Vehículo y añada:
Un atributo adicional puertas (número de puertas)
Sobrescribe el método mostrar_info() para incluir el número de puertas
Una clase derivada Motocicleta que herede de Vehículo y añada:
Un atributo adicional cilindrada (en cc)
Sobrescribe el método mostrar_info() para incluir la cilindrada
Finalmente, crea una instancia de cada clase derivada y muestra su información usando el método mostrar_info().
'''


# =============================================================================
# Clase base
# =============================================================================

class Vehiculo:

    def __init__(self, marca, modelo, año):
        self.marca  = marca
        self.modelo = modelo
        self.año    = año

    def mostrar_info(self):
        return f"{self.año} {self.marca} {self.modelo}"


# =============================================================================
# Clases derivadas
# =============================================================================

class Automovil(Vehiculo):

    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)   # reutiliza el constructor de Vehiculo
        self.puertas = puertas

    def mostrar_info(self):
        base = super().mostrar_info()          # reutiliza el método de la clase base
        return f"{base} | {self.puertas} puertas"


class Motocicleta(Vehiculo):

    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} | {self.cilindrada} cc"


# =============================================================================
# Prueba
# =============================================================================

auto  = Automovil("Toyota", "Corolla", 2022, 4)
moto  = Motocicleta("Honda", "CBR600RR", 2021, 600)

print(auto.mostrar_info())
print(moto.mostrar_info())

