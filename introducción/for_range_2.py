# Ejemplos Parte 2 For y range
value1 = int (input ("Dame un valor: "))
suma = 0

for n in range (1, value1 + 1) :
  suma += n
print (suma)  

# Ejemplo Continue
for n in range (10) :
  print (n)
  if n%2 == 0 :
    continue
  print ("Hola")  
print ()

print("Ejemplo con Break")
# Ejemplo con break
for n in range (10):
  print (n)
  if n == 5 :
    break
print ("-----------")    

# Ejemplo con else

value1 = int (input ("Dame un numero: "))

for n in range (10) :
  print (n)
  if n == value1 :
    break
else: 
  print ("Estoy en el else")
print ("Afuera del for/else")  