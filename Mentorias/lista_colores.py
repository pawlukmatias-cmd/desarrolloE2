# Contar cantidad de apariciones de "x" color

# Creamos la lista:
lista_colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
print(f"La lista de colores es la siguiente:", lista_colores)

# Usamos .count para contar la cantidad de veces que se repite el rojo:
num_rojo = lista_colores.count("rojo")
print(f"La cantidad de veces que se repite el color rojo, es", num_rojo)

# Reemplazamos el "verde" por "amarillo":
nueva_lista_colores = ["amarillo" if color == "verde" else color for color in lista_colores]
print("Se cambió el color verde por amarillo en la lista general.")


# Imprimimos la nueva lista:
print(f"La nueva lista de colores es la siguiente:", nueva_lista_colores)