# Operadores booleanas

valueA = int(input ( ("Dame un numero: ")))

if valueA >= 5 and valueA <= 10 :
  print (valueA , "esta entre 5 y 10")

valueB = int (input ("Dame un numero que divida exactamente a 8: "))

if valueB == 1 or valueB == 2 or valueB == 4 or valueB == 8 :
  print ("Correcto")
else :
  print ("Incorrecto")

if not (valueB == 1) :
  print ("El uno divide a todos exactamente")

