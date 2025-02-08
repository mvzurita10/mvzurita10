contraseña_correcta = "miky0107"

while True:
    contraseña = input("Ingresa la contraseña: ")
    
    if contraseña == contraseña_correcta:
        print("✅ ¡Acceso concedido!")
        break  
    else:
        print("❌ Contraseña incorrecta, intenta de nuevo.")

