
import random

def obtener_frase_suerte():
    """Devuelve una frase de suerte aleatoria."""
    frases = [
        "La suerte está de tu lado.",
        "Sal de ahi my friend :c.",
        "Si lo sueñas, lo cumpliras.",
        "El/Ella volvera contigo :o .",
        "El tiempo es oro, no lo desaproveches.",
        "Confia en tu instinto, creeme por algo lo piensas. "
    ]
    return random.choice(frases)

def main():
    """Función principal que ejecuta el programa."""
    bienvenida = input("Hola, Hoy veremos si tu suerte te acompaña... Presion ENTER para continuar.")
    nombre = input("Por favor, ingresa tu nombre: ")
    apellido = input("Por favor, ingresa tu apellido: ")


    mensaje_bienvenida = f"{bienvenida}"
    # Convertir a mayúsculas
    nombre_completo = f"{nombre} {apellido}".upper()

    # Obtener frase de suerte
    frase_suerte = obtener_frase_suerte()

    # Mostrar resultados
    print(f"{mensaje_bienvenida}")
    print(f"\nTu nombre completo en mayúsculas es: {nombre_completo}")
    print(f"Tu frase de suerte es: {frase_suerte}")

if __name__ == "__main__":
    main()