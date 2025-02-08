while True:
    print("\nMenu:")
    print("1. Sumar")
    print("2. Resta")
    print("3. Salir")
    
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        print("Ingrese los numeros para la suma:")
        a = int(input("Ingrese n1: "))
        b = int(input("Ingrese n2: "))
        suma = a + b
        print(f"La suma es: {suma}")
    elif opcion == "2":
        print("Ingrese los numeros para la resta:")
        a = int(input("Ingrese n1: "))
        b = int(input("Ingrese n2: "))
        suma = a - b
        print(f"La resta es: {suma}")
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Sale del bucle si el usuario elige salir
    else:
        print("Opcion no valida, intenta de nuevo.")
