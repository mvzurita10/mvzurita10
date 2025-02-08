while True:
    edad = input("Ingresa tu edad: ")
    if edad.isdigit() and int(edad) > 0:
        print(f"Edad valida: {edad}")
        if edad >= "18":
            print("Eres Mayor de edad.")
            break
        else:
            print("Eres menor de edad")
         # Se sale del bucle si la entrada es correcta
    print("Entrada no valida. Intentalo de nuevo.")

