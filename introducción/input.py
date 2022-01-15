# Pedir infromación al usuario
# usando input
# al escribir cadenas hay que ponerlas con ""

nombre = input ("Dame tu nombre: ")
base = int(input ("Dame la base "))
altura = int(input ("Dame la altura "))
radio = input ("Dame el radio ")
area = base*altura
perimetro = 2 * (base + altura)
print ("Hola", nombre, " el area es: ", area, " y el perimetro es: ", perimetro)

# experimentando
nombre = str (input ("Dame tu nombre: "))
base = float (input ("Dame la base: "))
altura = float (input ("Dame la altura: "))
area = base * altura
area2 = int(area)
perimetro = 2 * (base + altura)
print ("Hola", nombre, " el area es: ", area, " y el perimetro es: ", perimetro)

# Comparando entradas con input y raw_input este ultimo no es funcional en python 3.x
print ("Con input")
print (radio, type(radio))
print (base, type(base))
print (area2, type(area2))
