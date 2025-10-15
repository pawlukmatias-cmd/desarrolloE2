print("""Strings intro a f-strings""")

nombre = "Magali"
apellido = "Pawluk"

mensaje_1 = f"Hola {nombre}, {apellido}"
print(mensaje_1)

mensaje_2 = "Hola {}, {}".format(apellido, nombre)
print(mensaje_2)

num_1 = 4
num_2 = 12

mensaje_3 = f"La suma de {num_1} y {num_2} es igual a {num_1 + num_2}"
print(mensaje_3)

# El comando (:\n) sigue escribiendo en el proximo renglon.
mensaje_3 = f"La suma de {num_1} y {num_2}:\n{num_1 + num_2}"
print(mensaje_3)

cadena = "Hola info - "
cadena_repetida = cadena * 3

texto_1 = "cinco"
longitud = len(texto_1)

print(type(texto_1))
print(longitud)

texto_2 = "Hola, Bienvenido al Info"
subcadena = texto_2[6:24] # Selecciona que caracteres mostrar con []
print(subcadena)

cadena_invertida = texto_2[::-1]
print(cadena_invertida)

cadena_mayusculas = texto_2.upper()
print(cadena_mayusculas)

cadena_minusculas = texto_2.lower()
print(cadena_minusculas)

nombre_2 = "diego balbuena"
cadena_capitalizada = nombre_2.capitalize()

cadena_tabulada = "Hola\mundo"
print(cadena_tabulada)

cadena_tabulada_2 = "\tHola\tinfo"
print(cadena_tabulada_2)

comillas_escaladas_simples = "Entonces 'creemos' que"
print(comillas_escaladas_simples)

comillas_escaladas_dobles = "Entonces \"suponemos\" lo siguiente"
print(comillas_escaladas_dobles)