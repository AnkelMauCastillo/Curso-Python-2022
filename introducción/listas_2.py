#Operacciones y funciones sobre listas

frutas = ["Pera", "Platano", "Manzana"]
calificaciones = [6, 8, 9,10, 7]

# Longitud
print ("Logitud de la lista Frutas es: ",len (frutas))
print ("_"*10)

#Concatenacion
listaConcat = frutas + calificaciones

for elemento in listaConcat :
  print (elemento)
print ("-"*10)

# Membresia

print (7 in listaConcat)
print ("Manzanza" in listaConcat)
print ("-"*10)

listaIterada = frutas*2
print (listaIterada)
print ("-"*10)

# Slicing 
print ("Slicing")
lista2 = listaConcat[3:]

print (listaConcat)
print (lista2)
print ("-"*10)
