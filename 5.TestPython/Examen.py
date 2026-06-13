A = 5
B = 4
suma = 0

print("\n")
print(f"{'Iteración i':<13} | {'¿A > B?':<9} | {'Valor de A':<12} | {'Valor de B':<12} | {'Valor de suma':<13}")
print("-" * 75)

for i in range(1, 5):
    if A > B:
        cumple = "Sí"
        suma = suma + A
        A = A - 1
        B = B + i
    else:
        cumple = "No"
        suma = suma + B
        B = B - 2
        A = A + i
    
    #print(f"Iteración {i}: A = {A}, B = {B}, suma = {suma}")
    # Impresión de cada fila alineada perfectamente con los encabezados
    print(f"{i:<13} | {cumple:<9} | {A:<12} | {B:<12} | {suma:<13}")


print("-" * 75)
print(f"Resultado final: {suma}")
print("\n")