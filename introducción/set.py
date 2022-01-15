'''
Sets
Es una colección no ordenada con elementos duplicados
Permiten operaciones matemáticas como unión, intersección, diferencia y diferencia simetrica
Se pueden crear set() o {}, un set vacio  solo con set()
'''

#creamos un set
colores = {'rojo', 'azul', 'anaranjado', 'amarillo', 'verde', 'violeta', 'cyan', 'blanco', 'negro'}

print (colores)

#verificamos si existe un elemento en el set
existe = 'verde' in colores
print (existe)

existe = 'cafe' in colores
print (existe)

#creamos un nuevo set para hacer operaciones
favoritos = {'azul', 'cyan', 'blanco', 'mostaza'}

print ("Unión", colores|favoritos)

print ("Intersección", colores&favoritos)

print ('Diferencia', colores - favoritos)

a = {0, 2, 4, 6, 8}
b = {1, 2, 3, 4, 6}

print ('Diferencia Simetrica', a^b)
print()
for color in colores :
    print (color)