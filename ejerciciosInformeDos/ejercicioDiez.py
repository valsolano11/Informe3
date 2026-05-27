# Ejercicio 10
# # 1. Pedir el género de música
genero = input("Ingrese su género de música favorito: ").lower()

# # 2. Primera validación
if genero == "electronica" or genero == "pop":
    
    # # Si entró aquí, ahora pedimos el año
    year = int(input("¿En qué año naciste?: "))
    
    # # 3. Validación
    if year > 2000 and genero == "Pop":
        print("Tengo la camisa negra")
    else:
        print("Por siempre Daft punk")
        
else:
    # # Si el género no fue ni Electronica ni Pop
    print("Los únicos géneros buenos son Electronica y Pop")
    
# # 4. Mensaje final fuera de todos los bloques
print("Fin programa")