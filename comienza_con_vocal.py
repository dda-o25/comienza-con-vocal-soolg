"""
Sol Valeria Gonzalez Castro 
17/09/2025
Determinar si una palabra comienza con una vocal
"""

# Entradas
palabra = input("Introduce una  palabra: ")

# Proceso
vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
if palabra and palabra [0] in vocales:
    mensaje = f"'{palabra}' comienza con una vocal"
else:
    mensaje = f"'{palabra}' no comienza con una vocal"

# Salidas
print(mensaje)