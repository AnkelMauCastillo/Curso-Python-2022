# Operaciones y funciones con el diccionario

productos = {"ft01": "Manzana", "ft02": "Pera", "ft03": "Platano", "ft04": "Ciruela"}
productos2 = {"ft01": "Manzana", "ft02": "Chabacano", "ft03": "Platano", "ft04": "Ciruela"}
productos3 = {"ft01": "Manzana", "ft02": "Pera", "ft03": "Platano", "ft04": "Ciruela"}


# logitud
print (len(productos))

#Conversion a Cadena

cadena = str(productos)
cadena2 = "->" + cadena + "<-"
print (cadena2)
print ("-_"*50)

# Lista dee pares (llave, valor) como tuplas adetro de una lista
print (productos.items())

# Lista de llaves en el diccionario
print (productos.keys())

# Listta los valores en el diccionario
print (productos.values())

# Set default, se usa como get, pero damos un valor a colovcar
#default si la llave no existe
print (productos.setdefault("ft02", "No hay"))
print (productos.setdefault("No existe", "No hay en el servicio"))

print (productos)

# Otra forma de adicionar una entrada con update
productos.update({"ft07": "Albaricoque"})
print (productos)
