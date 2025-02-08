intentos = 0
while True:  
    numero = int(input("Adivina un numero entre 1 y 10: "))
    
    while numero < 1 or numero > 10:  
        print("Numero fuera de rango, intenta de nuevo.")
        numero = int(input("Adivina un numero entre 1 y 10: "))
    
    intentos += 1
    if numero == 7:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break  
    else:
        print("Incorrecto, intenta otra vez.")
