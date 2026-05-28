# format_map()
# Sirve para insertar datos desde diccionarios

usuario = {
    "nombre": "Carlos",
    "edad": 28,
    "pais": "Colombia"
}

print("Nombre: {nombre} | Edad: {edad} | País: {pais}".format_map(usuario))

empleado = {
    "nombre": "Laura",
    "cargo": "Desarrolladora",
    "salario": 5000
}

print("Empleado: {nombre} - Cargo: {cargo} - Salario: ${salario}".format_map(empleado))