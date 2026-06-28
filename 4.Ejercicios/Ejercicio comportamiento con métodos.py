'''
Ejercicio comportamiento con métodos


OBJETIVO
Implementar una clase Contador con métodos de instancia, clase y estáticos

INSTRUCCIONES
Crea una clase llamada Contador que gestione un valor numérico. La clase debe implementar:

Un atributo de clase contadores_creados que lleve la cuenta de cuántas instancias se han creado.

Un método de instancia incrementar() que aumente el valor del contador en 1 y devuelva el nuevo valor.

Un método de instancia decrementar() que disminuya el valor del contador en 1 y devuelva el nuevo valor. El contador nunca debe ser negativo.

Un método de clase @classmethod llamado reiniciar_contador_global() que ponga a cero el contador de instancias creadas.

Un método estático @staticmethod llamado es_par(número) que devuelva True si el número proporcionado es par, o False en caso contrario.

Puedes empezar con este esquema:

class Contador:
    # Atributo de clase para contar instancias
    contadores_creados = 0

    def __init__(self, valor_inicial=0):
        # Completa el constructor
        pass

    # Implementa los métodos requeridos
'''


class Contador:

    contadores_creados = 0  # variable de clase compartida

    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial
        Contador.contadores_creados += 1  # se incrementa al crear cada instancia

    # --- Métodos de instancia ---

    def incrementar(self):
        self.valor += 1
        return self.valor

    def decrementar(self):
        if self.valor > 0:            # garantiza que nunca sea negativo
            self.valor -= 1
        return self.valor

    # --- Método de clase ---

    @classmethod
    def reiniciar_contador_global(cls):
        cls.contadores_creados = 0    # cls apunta a la clase, no a una instancia

    # --- Método estático ---

    @staticmethod
    def es_par(numero):
        return numero % 2 == 0


# --- Prueba ---

c1 = Contador(10)
c2 = Contador(0)
c3 = Contador(5)

print(f"Contadores creados: {Contador.contadores_creados}")   # 3

print(f"\nc1 incrementar: {c1.incrementar()}")                # 11
print(f"c1 incrementar: {c1.incrementar()}")                  # 12
print(f"c1 decrementar: {c1.decrementar()}")                  # 11

print(f"\nc2 decrementar (valor=0, no baja de 0): {c2.decrementar()}")  # 0

print(f"\nc3 valor inicial: {c3.valor}")                      # 5
print(f"c3 es_par({c3.valor}): {Contador.es_par(c3.valor)}")  # False
print(f"es_par(8): {Contador.es_par(8)}")                     # True
print(f"es_par(7): {Contador.es_par(7)}")                     # False

Contador.reiniciar_contador_global()
print(f"\nTras reiniciar contador global: {Contador.contadores_creados}")  # 0

