# Importa el módulo math para usar funciones matemáticas
import math

# Función que calcula el área de un cuadrado
def area_cuadrado(lado):
    # Valida que el lado sea un número positivo
    if lado <= 0:
        raise ValueError("El lado debe ser un número positivo.")
    # Devuelve el área del cuadrado
    return lado ** 2

# Función que calcula el área de un círculo
def area_circulo(radio):
    # Valida que el radio sea un número positivo
    if radio <= 0:
        raise ValueError("El radio debe ser un número positivo.")
    # Devuelve el área del círculo
    return math.pi * (radio ** 2)

# Función que calcula el área de un triangulo
def area_triangulo(base, altura):
    # Valida que tanto la base como la altura sean positivas
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser números positivos.")
    # Devuelve el área del triangulo
    return (base * altura) / 2

# Función auciliar para pedir un número flotante al usuario
def pedir_float(mensaje):
    try:
        valor = float(input(mensaje))
        return valor
    except ValueError:
        # Si no es convertible a número, lanza un error personalizado
        raise ValueError("Entrada inválida. Debes ingresar un número.")

# Función principal del programa
def main():
    print("Calculadora de áreas:")
    print("1. Cuadrado")
    print("2. Círculo")
    print("3. Triángulo")

    # Solicita al usuario una opción del menú
    opcion = input("Selecciona una opción (1/2/3): ")

    try:
        if opcion == '1':
            lado = pedir_float("Ingresa el lado del cuadrado: ")
            resultado = area_cuadrado(lado)
            print(f"Área del cuadrado: {resultado:.2f}")
        elif opcion == '2':
            radio = pedir_float("Ingresa el radio del círculo: ")
            resultado = area_circulo(radio)
            print(f"Área del círculo: {resultado:.2f}")
        elif opcion == '3':
            base = pedir_float("Ingresa la base del triángulo: ")
            altura = pedir_float("Ingresa la altura del triángulo: ")
            resultado = area_triangulo(base, altura)
            print(f"Área del triángulo: {resultado:.2f}")
        else:
            print("Opción no válida. Por favor elige 1, 2 o 3.")

    # Captura y muestra cualquier error generado durante el proceso        
    except ValueError as e:
        print(f"Error: {e}")

# Ejecuta la función main solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
