# Ejercicio 9
# # 1. Pedir al usuario el año de nacimiento (convertido a entero)
year = int(input("Ingrese el año en que naciste: "))

# # 2. Validar si está entre 1994 y 2010
if year >= 1994 and year <= 2010:
    print("Eres Generación Z")
    
# # 3. Si no, validar si está entre 1981 y 1993
elif year >= 1981 and year <= 1993:
    print("Eres Millennial")
    
# # 4. De lo contrario
else:
    print("Eres de otra generación")    