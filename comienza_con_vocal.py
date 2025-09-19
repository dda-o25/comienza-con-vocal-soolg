"""
Sol Valeria Gonzalez Castro 
17/09/2025
Determinar si una palabra comienza con una vocal
"""

# Entradas
palabra = input("Introduce una  palabra: ")

# Proceso
primera_letra = palabra[0].lower()
vocales = "aeiou"

# Salidas
if primera_letra in vocales:
    print ("Comienza con una vocal ")
else:
    print("No comienza con una vocal")
