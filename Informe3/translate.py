# translate()
# Sirve para reemplazar caracteres usando tablas

tabla = str.maketrans("aeiou", "@3140")
texto = "programacion"
print(texto.translate(tabla))

tabla2 = str.maketrans("xyz", "123")
codigo = "xylophone zebra"
print(codigo.translate(tabla2))
