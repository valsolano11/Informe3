# maketrans()
# Sirve para crear reglas de reemplazo

tabla = str.maketrans("aeiou", "12345")
print("programacion".translate(tabla))

tabla2 = str.maketrans("abc", "789")
print("abracadabra".translate(tabla2))
