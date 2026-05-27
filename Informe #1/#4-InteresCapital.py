#Calcular interes capital en PSEINT

# Una persona desea invertir su capital en un banco y desea saber
# cuánto dinero ganará después de un mes si el banco le pagará
# intereses del 2% mensual.

# Ingreso de datos
# 'capital' lo convertimos a float por si se ingresan valores con decimales
capital = float(input("ingrese el monto a invertir: "))
# 'dias' lo dejamos como entero (int)
dias = int(input("Ingrese el numero de días del mes a considerar: "))

# Definición del interés (2%)
interes = 0.02

# Cálculo de la ganancia
ganancia = (capital * dias) * interes

# Mostrar los resultados en pantalla
print("La ganancia por cobrar después del mes es de:")
print(ganancia)