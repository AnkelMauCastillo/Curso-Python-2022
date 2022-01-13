frutas = ['manzana', 'guayaba', 'pera', 'sandia']

for fruta in frutas:
    print(fruta)

"""
Iterables
En Python, un iterable es un objeto que se puede utilizar en un bucle definido. Si un objeto es iterable significa que se puede pasar como argumento a la función iter. El iterable que se pasa como parámetro a la función iter
regresa un iterator.
"""

cadena = iter('Cadena')  # cadena
lista = iter(['a', 'b', 'c', 'd'])  # lista
tupla = iter(('a', 'b', 'c', 'd'))  # tupla
conjunto = iter({'a', 'b', 'c', 'd'})  # conjunto
diccionario = iter({'a': 1, 'b': 2, 'c': 3})  # diccionario

lista = [cadena, lista, tupla, conjunto, diccionario]

for elemento in lista :
    print (elemento)

print ()    
iterador = iter(frutas)
print (next (iterador))
print (next (iterador))
print (next (iterador))
print (next (iterador))


#diccionarios
print ()
print ("Diccionarios")
frutas = {
    'pera' : 1,
    'manzana' :2,
    'mango' : 3,
    'calabaza' : 4
}

for fruta in frutas :
    print (fruta)

print (" por Keys")
for fruta in frutas.keys():
    print (fruta)
print ()
print (" por values")
for fruta in frutas.values():
    print (fruta)    

print ()
print ("por items")
for fruta in frutas.items():
    print (fruta)    

print ()
print ("print simple")
print (frutas)