import os

def suma():
    try:
        n1 = float(input("Ingresa el primer número: "))
        n2 = float(input("Ingresa el segundo número: "))
        result = n1 + n2
        print(f"La suma es: {result}")
    except ValueError:
        print("Error: Ingresa números válidos.")
    else:
        print("Operación realizada con éxito.")

def resta():
    try:
        n1 = float(input("Ingresa el minuendo: "))
        n2 = float(input("Ingresa el sustraendo: "))
        result = n1 - n2
        print(f"La resta es: {result}")
    except ValueError:
        print("Error: Ingresa números válidos.")
    else:
        print("Operación realizada con éxito.")

def producto():
    try:
        n1 = float(input("Ingresa el primer factor: "))
        n2 = float(input("Ingresa el segundo factor: "))
        result = n1 * n2
        print(f"El producto es: {result}")
    except ValueError:
        print("Error: Ingresa números válidos.")
    else:
        print("Operación realizada con éxito.")

def division():
    try:
        n1 = float(input("Ingresa el dividendo: "))
        n2 = float(input("Ingresa el divisor: "))
        result = n1 / n2
        print(f"La división es: {result}")
    except ValueError:
        print("Error: Ingresa números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print("Operación realizada con éxito.")

# Main loop to allow multiple inputs
while True:
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Producto")
    print("4. División")
    print("5. Salir")

    choice = input("Selecciona una operación (1-5): ")

    if choice == '1':
        suma()
    elif choice == '2':
        resta()
    elif choice == '3':
        producto()
    elif choice == '4':
        division()
    elif choice == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Exit the loop and end the program
    else:
        print("Selección no válida. Intenta de nuevo.")

    another_calculation = input("¿Quieres hacer otra operación? (s/n): ").lower()
    if another_calculation != 's':
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Exit the loop and end the program

    # Clear console screen
    os.system('cls' if os.name == 'nt' else 'clear')
