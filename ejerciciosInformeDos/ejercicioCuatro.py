# Ejercicio 4
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

edad_minima = 18

# Evalúa si la edad ingresada cumple con el mínimo requerido para votar
if edad >= edad_minima:
    print(f"Hola {nombre}, tienes {edad} años. ¡Ya puedes votar!.")
else:
    # Si no es mayor o igual a 18, ejecuta este bloque
    print(f"Lo siento {nombre}, aún eres menor de edad.")