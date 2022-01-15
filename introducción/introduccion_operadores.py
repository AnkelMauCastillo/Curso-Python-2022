#esto es una impresión de mensaje comillas
print("Hola Mundo")

#esto es una  impresión de mensaje comillas simples
print('Hola Mundo comillas simples')
""" Hola Como estas es un comentario
"""

#Comienza ejercicios de operadores aritmeticos
print ("suma", 3+5)
a=4
b=6
#suma
print ("suma", a + b)
#resta
print ("Resta", a - b)
#multi
print ("Multiplicacion", a * b)
#div
print ("Division", a / b)
print ("Div", 4.5/4.6)
#Modulo
print ("Modulo", 6 % 2)
print ("Modulo", 6 % 4)
#Exponente
print ("Exponente", a**10);
c = 2
print ("Exponente", a**c, b**2)

"""
Operadores Relacionales
"""
#op >
print ("a>b", a > b)
#op <
print ("a < b", a < b)
#op >=
c=a
print (" a >= c", a >= c)

#op <= 
print ("a <= b", a <= b)

#op ==
print ("a == b", a == b)

#op != o <>
print ("a != b", a != b)
"""print ("a <> b", 5<>5) ya no es funcional en python 3
"""

"""
Variables
"""
#definir un entero
saldo = 5
print (saldo)
#definir un Flotante 
precio = 18.5
print (precio)
#definir con constructor
saldo = float(14)
print (saldo)
#definir directamente al hacer la operación
total = precio + saldo
print (total)
#definir un String
nombre = "Angel"
print (nombre)
#definir un bool
acierto = True
print (acierto)
#definir asignaciones multiples
calif1, calif2 = 10, 8
print (calif1)
print (calif2)

"""
print con variables
"""
print ("El alumno tiene uno tiene la calif de ", calif1 ," y el dos de ", calif2 )
# Tambien puede estar de la forma con uso de formateadores
print ("El primer alumno tiene calificacion de %d y el segunod de %d" %(calif1, calif2))
print ("%s el precio es de %f por articulo" %(nombre, precio))

print ("El precio es %.2f pesos" %precio)

# Creacion de una cedena de format
formato = "Una variable %r, otra variable %r"
print (formato %(precio, saldo))
print (formato %(nombre, acierto))
print (formato %(a, calif1))

# Imprimir multiples lineas a la vez
print (
  """
  Primer Linea
  Segunda Linea
  Tercer Linea
  """
)

#Python tambien tiene codigos de escape
print ("Voy a imprimir una \\ aqui")
print ("Si lo deseo pongo \' o \" en la impresion")
print ("Una linea \notra linea abajo")
print ("\t con salto de tabulador")