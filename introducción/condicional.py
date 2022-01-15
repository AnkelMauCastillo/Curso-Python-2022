# Uso de if, elif y eval
#Bloque de codigo
# uso normal de if
valor1 = int(input("Dame un numero: "))

if valor1 > 0:
    print("El numero es positivo")

if valor1 < 0:
    print("El numero es negativo")
    print("Esto tambien es parte del bloque de codigo")
print("fin del ejemplo")

# uso de if con else
valor2 = int (input ("Dame un numero: "))

if valor2 >0:
  print ("El numero es positivo")
else:
  print ("El numero es negativo")
  print ("--------------------")

# Uso de if con elseif
valor3 = int (input ("Dame un numero: "))
if valor3 > 0 :
  print ("El numero es positivo")
elif valor3 == 0 :
  print ("El numero es neutro")
else :
  print ("El numero es negativo")    

