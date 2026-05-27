# Ejercicio 8
# # Solicitamos la cantidad de flores
cantidadFlores = int(input("Ingrese la cantidad de flores: "))

if (cantidadFlores >= 10):
    # # Si compra 10 o más, cada flor cuesta 8
    precioTotal = cantidadFlores * 8
    print("Total a pagar: " + str(precioTotal))
    
elif (cantidadFlores >= 5):
    # # Si compra entre 5 y 9, cada flor cuesta 10
    precioTotal = cantidadFlores * 10
    print("Total a pagar: " + str(precioTotal))
    
elif (cantidadFlores == 3):
    # # Si compra exactamente 3, son gratis
    print("No debes pagar nada, las flores son gratis")
    
else:
    # # Para cualquier otra cantidad (1, 2, 4), cada flor cuesta 15
    precioTotal = cantidadFlores * 15
    print("Total a pagar: " + str(precioTotal))
    

print("Fin programa")