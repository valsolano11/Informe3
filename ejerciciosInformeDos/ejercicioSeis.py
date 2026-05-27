# Ejercicio 6
# # 1. Pedir la cantidad de votos válidos totales
votos_totales = int(input("Ingrese la cantidad de votos válidos (total): "))

# # 2. Pedir la cantidad de votos del partido
votos_partido = int(input("Ingrese la cantidad de votos de su partido: "))

# # 3. Calcular el umbral (3% de los votos válidos)
umbral = votos_totales * 0.03

# # 4. Validar si los votos del partido superan el umbral
if votos_partido > umbral:
    # # Si se cumple
    print("Tu partido tendrá curules")
else:
    # # En caso contrario
    print("Se quemaron")