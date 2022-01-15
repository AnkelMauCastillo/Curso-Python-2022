# Creación de listas

frutas = ["pera", "manzana" , "ciruela" , "platano"]
calificaciones = [8, 9, 10, 9 ,8]
Servicios = ["internet", 389.67, "Calle 4", True]

for elemento in frutas :
  print (elemento)
print ("______________")

promedio = 0
for elemento in calificaciones :
  print (elemento)
  promedio += elemento 
print ("Su promedio es: ", promedio/len(calificaciones))
print ("---------------------")
for elemento in Servicios :
  print (elemento)
print ("___________-")

# Acceder lista por indice

print (frutas[0])
print (frutas[2])
#para acceder al enesimo elemento se coloca un -1
print (frutas[-1])

# Actulizar un valor de la lista
print ("-"*10)

print ("Original")

for elemento in frutas :
  print (elemento)
print ("-"*20)  

frutas[2] = "albaricoque"

for elemento in frutas :
  print (elemento)
print ("-_"*20)  

# Borrando un elemento
del frutas[2]

for elemento in frutas :
  print (elemento)

print (frutas[2])

print ("-_/"*12)
