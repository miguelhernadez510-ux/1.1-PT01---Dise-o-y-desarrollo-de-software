import math

def suma_numeros():
    n = int(input("¿Cuántos números deseas sumar? "))
    total = 0
    for i in range(n):
        num = float(input(f"Ingrese número {i+1}: "))
        total += num
    print("La suma es:", total)

def producto_numeros():
    n = int(input("¿Cuántos números deseas multiplicar? "))
    producto = 1
    for i in range(n):
        num = float(input(f"Ingrese número {i+1}: "))
        producto *= num
    print("El producto es:", producto)

def division():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    if b != 0:
        print("El resultado de la división es:", a / b)
    else:
        print("Error: división entre cero.")

def factorial():
    n = int(input("Ingrese un número: "))
    if n >= 0:
        print(f"El factorial de {n} es:", math.factorial(n))
    else:
        print("Error: el número debe ser no negativo.")

def tabla_multiplicar():
    n = int(input("Ingrese el número de la tabla (1-10): "))
    if 1 <= n <= 10:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    else:
        print("Número fuera de rango. Debe estar entre 1 y 10.")

def cuadrado_cubo():
    n = float(input("Ingrese un número: "))
    print("Cuadrado:", n ** 2)
    print("Cubo:", n ** 3)

def promedio():
    numeros = []
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    if numeros:
        print("El promedio es:", sum(numeros) / len(numeros))
    else:
        print("No se ingresaron números.")

def max_min():
    lista = []
    n = int(input("¿Cuántos números deseas ingresar? "))
    for i in range(n):
        num = int(input(f"Ingrese número {i+1}: "))
        lista.append(num)
    print("Máximo:", max(lista))
    print("Mínimo:", min(lista))
    print("Total de valores ingresados:", len(lista))

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Suma de n números")
        print("2. Producto de n números")
        print("3. División entre 2 números")
        print("4. Factorial")
        print("5. Tabla de multiplicar")
        print("6. Cuadrado y cubo")
        print("7. Promedio de números")
        print("8. Máximo y mínimo")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            suma_numeros()
        elif opcion == "2":
            producto_numeros()
        elif opcion == "3":
            division()
        elif opcion == "4":
            factorial()
        elif opcion == "5":
            tabla_multiplicar()
        elif opcion == "6":
            cuadrado_cubo()
        elif opcion == "7":
            promedio()
        elif opcion == "8":
            max_min()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()