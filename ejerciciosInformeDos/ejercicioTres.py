# Ejercicio 3
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Verifica si los dos números ingresados son diferentes
if num1 != num2:
    # Si son diferentes, evalúa cuál de los dos es mayor
    if num1 > num2:
        print(f"El primer número {num1} es mayor que el segundo {num2}.")
    else:
        print(f"El segundo número {num2} es mayor que el primero {num1}.")
        
        # Si el segundo es mayor, revisa si es por lo menos el doble del primero
        if num2 >= (num1 * 2):
            print("Además, el segundo número es el doble o más que el primero.")
else:
    # Si no son diferentes, significa que son iguales
    print("Ambos números son iguales.")