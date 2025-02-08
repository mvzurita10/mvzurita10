contador = 0

while True:
    contador += 1
    print(f"Contador: {contador}")
    
    if contador == 10:  # Se detiene al llegar a 10
        print("¡Contador detenido!")
        break
