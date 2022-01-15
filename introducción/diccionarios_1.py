"""
Diccionarios, estructura de datos asociativa no secuencial
Estructura de datos, tiene una llave y un valor asociado a esa llave
Las llaves deben de ser inutables y es posible tener llaves repetidas
Los valores pueden ser cualquier objeto valido en Python
Solo un valor por llave

"""
# Creación del diccionario y acceso
productos = {"ft01": "Manzana", "ft02": "Pera", "ft03": "Platanos", "ft04": "Ciruela"}

print (productos ["ft02"])

# Imprimir productos
for n in productos :
  print (n, productos[n])


#print (productos["No existe"])

# Actualizando una entrada
productos["ft03"] = "Mango"
print (productos)

# Adicionando una entrada
productos["ft05"] = "Kiwi"
print (productos)
print ("-_"*20)
# Copiamos el diccionario
productos2 = productos.copy()
print (productos2)

# Borrar un elemento
del productos["ft02"]
print (productos)

# Borrar todos los elementos del diccionario
productos.clear()
print (productos)

# Elimina el diccionario
del productos
#print (productos)