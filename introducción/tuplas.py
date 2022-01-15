""""
Las tuplas son tambien secuenias de objetos , pero umutables, se utilizan () en lugar []. Si no se usan se toma por default la tupla.
Los elementos se separan por comas, incluso si es solo un elemento.
Son mas rapidos  que las listas.
Si la infromación no va cambiar es la opción a utilizar.
Se pueden usar como llaves para los diccionarios
"""

#funcion comparacion de listas
def cmp (a, b):
  return bool (a > b) - bool (a < b)


# Creacion de una tupla
meses = ("Enero", "Febrero", "Marzo", "Abril")
unDato = (5,)

#Acceso a la tupla
print (meses)
print (meses[1:3])

for m in meses :
  print (m)

#esto no es valido 
#meses[1]="otro mes"  

# Concatenacion
nuevaTupla = meses + unDato

print (nuevaTupla)

# No se puede borrar un elemento en particular
# pero si la tupla completa
del nuevaTupla
#print (nuevaTupla)

# Convertir una list a una tupla
miLista = [":)", ":|", ":/", ":("]
miTupla = tuple(miLista)

print (miTupla)

# Convertir una tupla a una lisa
miLista = list(miTupla)
print (miLista)

# Operaciones con tuplas
#Son similares a las de las listas

print (len(meses))

otro = (5, 6, 7)*4
print (otro)

print (5 in otro)
print (9 in otro)

print ("----"*10)

tuple1, tuple2 = (100, 'hola'), (300, 'adios')

print (cmp(tuple1, tuple2))
print (cmp(tuple2, tuple1))
tuple3 = tuple2 + (50, 'saludos',);
print (tuple3)
print (cmp (tuple2, tuple3))


