# Ejercicio 5
ladoCuadrado = float(input("Ingrese el lado del cuadrado: "))

# Valida que el lado ingresado sea una medida válida (mayor a cero)
if (ladoCuadrado > 0):
    # Calcula el área multiplicando lado por lado
    areaCuadrado = ladoCuadrado * ladoCuadrado
    print("El area es: " + str(areaCuadrado))
else:
    # Muestra un mensaje de error si el valor es cero o negativo
    print("Lado no puede ser menor o igual a cero")