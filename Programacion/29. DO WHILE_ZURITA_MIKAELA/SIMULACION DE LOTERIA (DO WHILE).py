import random

numero_ganador = random.randint(1, 10)  # Número ganador entre 1 y 10

print("¡Bienvenido a la lotería! Adivina el número (1-10).")

while True:
    intento = int(input("Ingresa tu número: "))
    
    if intento == numero_ganador:
        print(f" ¡Ganaste! El número era {numero_ganador}.")
        break  # Termina el bucle si el usuario acierta
    else:
        print(" Número incorrecto. Intenta de nuevo.")

