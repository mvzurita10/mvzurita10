while True:
    try:
        cantidad = int(input("¿Cuantos numeros quieres imprimir? "))
        if cantidad <= 0:
            print("Por favor ingresa un numero mayor que 0.")
            continue  
        break  
    except ValueError:
        print("Por favor ingresa un numero entero valido.")

for i in range(1, cantidad + 1):
    print(i)
