# Uso de in, verifica si un objeto existe adentro de un objeto contenedor iterable 

nombreF1 = str (input ("Dame un nombre del familiar: "))

nombre = str (input ("Dame tu nombre: "))

if nombre in ["Angel", "Eduardo", "Bernardino", "Mariana", nombreF1]: 
  print ("Conozco ese nombre")
else :
  print ("No conozco ese nombre")

# Uso de is, compara las instancias no los valores
arrayA = [2, 3, 5]
arrayB = [2, 3, 5]
arrayC = arrayA
arrayD = [2, 6, 9]

if arrayA == arrayB :
  print ("A y B tiene el mismo valor")
if arrayA is arrayB :
  print ("A y B son la misma instancia")
else :
  print ("a y B no son la misma instancia")
if arrayA is arrayC :
  print ("A y C son la misma instancia")
else :
  print ("Ay C no son la misma instancia")    
if arrayA is arrayD :
  print ("A y D son la misma instancia")
else :
  print ("A y D no son la misma instancia")


