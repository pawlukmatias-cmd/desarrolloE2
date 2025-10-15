# Vamos a crear un diccionario de estudiante

# La estructura es la siguiente:
estudiante = {"Nombre": "Ana", "Edad": 20, "Materias": ["Matemática", "Historia"]}

# Mostramos solo el nombre y la edad:
print(estudiante["Nombre"], "tiene", estudiante["Edad"], "años")

# Agregamos una nueva materia:
estudiante["Materias"].append("Fisica")
print("Materia agregada")

print(estudiante.len)