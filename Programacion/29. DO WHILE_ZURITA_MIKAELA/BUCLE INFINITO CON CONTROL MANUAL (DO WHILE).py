while True:
    print("\nMenu de Comida:")
    print("1. Comida rapida")
    print("2. Comida hecha en casa")
    print("3. Salir")
    
    opcion = input("Selecciona una opcion (1/2/3): ")
    
    if opcion == "1":
        print("\nComida rapida:")
        print("a. Hamburguesa")
        print("b. Pizza")
        print("c. Tacos")
        opcion_rapida = input("Selecciona un plato (a/b/c): ")
        
        if opcion_rapida == "a":
            print("Has elegido Hamburguesa. ¡Disfruta!")
        elif opcion_rapida == "b":
            print("Has elegido Pizza. ¡Buen provecho!")
        elif opcion_rapida == "c":
            print("Has elegido Tacos. ¡Deliciosos!")
        else:
            print("Opcion no valida en comida rapida.")
            
    elif opcion == "2":
        print("\nComida hecha en casa:")
        print("a. Spaghetti")
        print("b. Ensalada")
        print("c. Pollo al horno")
        opcion_casera = input("Selecciona un plato (a/b/c): ")
        
        if opcion_casera == "a":
            print("Has elegido Spaghetti. ¡Que sabroso!")
        elif opcion_casera == "b":
            print("Has elegido Ensalada. ¡Muy saludable!")
        elif opcion_casera == "c":
            print("Has elegido Pollo al horno. ¡Exquisito!")
        else:
            print("Opción no valida en comida hecha en casa.")
    
    elif opcion == "3":
        print("¡Hasta luego! Que tengas un buen dia.")
        break  # Sale del bucle cuando elige "Salir"
    
    else:
        print("Opción no valida, por favor selecciona una opcion valida.")




