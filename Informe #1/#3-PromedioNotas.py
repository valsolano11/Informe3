#PROMEDIO DE NOTAS EN PSEINT

# Ingreso de datos (Equivale a 'imprimir' y 'leer')
# Usamos float() porque las notas tienen decimales (Como Real)
matematicas = float(input("ingrese la nota de matematicas: "))
castellano = float(input("ingrese la nota de castellano: "))
ingles = float(input("ingrese la nota de ingles: "))
sociales = float(input("ingrese la nota de sociales: "))

# Cálculo del promedio
promedio = (matematicas + castellano + ingles + sociales) / 4

# Imprimir el resultado del promedio
print(promedio)

# Condicional (Equivale a 'si / sino / finSi')
if promedio > 4.5:
    print("puedes tener la beca")
else:
    print("aún no puedes tener la beca, intenta el otro semestre")