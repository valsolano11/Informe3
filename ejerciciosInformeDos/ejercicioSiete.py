# Ejercicio 7

temperatura = float(input("Ingrese la temperatura actual: "))

# Evalúa la primera condición: si hace calor
if temperatura > 27:
    print("Comprar helado")
# Si no se cumplió la primera, evalúa si hace frío
elif temperatura < 15:
    print("Comprar chocolate")
# Si ninguna de las anteriores fue verdadera, entra al caso por defecto
else:
    print("Comprar jugo de naranja")
    

print("Fin programa")