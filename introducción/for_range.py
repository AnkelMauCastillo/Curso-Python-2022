# Range genera una lista de progresiones  aritmeticas
#uso de range n elementos , de 0 a n-1

for i in range(10):
  print (i, end=" ")

print ()  

# usando rango para iteración
l = [10, 20, 30 ,40]
for i in range (len(l)) :
  print (l[i], end=" ")

print ()
# performing sum of natural
#number
sum = 0
for i in range (1,11) :
  sum += i  
print ("Suma de los primeros 10 numeros naturales:", sum)  

"""
Hay tres formas de llamar a range ():
range (parada) toma un argumento.
range (start, stop) toma dos argumentos.
rango (inicio, parada, paso) toma tres argumentos.
"""

# Programa Python para
# imprimir número entero
# usando range ()

# imprimiendo los primeros 10
# número entero
for i in range (10):
  print (i, end = " ")
print ()

# Programa Python para
# imprimir número natural
# usando rango

# imprimiendo un natural
# número hasta 20
for i in range (5, 20) :
  print (i, end=" ")
print ()


# Programa Python para
# imprime todo el número
# divisible por 3 y 5

# usando rango para imprimir el número
# divisible por 3
for i in range (0, 30, 3):
  print (i, end=" ")

print ()
# Programa Python para
# incremento con
# distancia()

# incrementado en 2
for i in range (2, 25, 2) :
  print (i, end=" ")
print ()

# incremented by 4
for i in range(0, 30, 4):
    print(i, end=" ")
print()

# Programa Python para
# decrementar con
# distancia()

# incrementado en -2
for i in range (25, 2, -2) :
  print (i, end=" ")
print ()  

# Programa Python para
# mostrar usando flotador
# número en rango ()
"""
# usando un número flotante
for i in range (3.3):
  print (i)
print ()
no valido 
"""
# Programa de Python para concatenar
# el resultado de dos funciones de rango
from itertools import chain

# Usando el método de cadena
print ("Concatenando el resultado")
res = chain(range(5), range(10, 20, 2))

for i in res:
	print(i, end=" ")

print ()

# Programa Python para demostrar
# función de rango

ele = range(10)[0]
print("First element:", ele)

ele = range(10)[-1]
print("\nLast element:", ele)

ele = range(10)[4]
print("\nFifth element:", ele)

print ()

for num in range(4):
    for i in range(num):
        print(num, end=" ")
    print()  # new line after each row to show pattern correctly

print ()

# Uso de for para iterar una lista
nombres = ["Angel", "Mauricio", "Edy", "Roberto"]

for nombre in nombres :
  print ("Hola", nombre)
print ()

# Uso de for con un rango
sumatoria = 0

for n in range (10):
  print (n)
  sumatoria +=1
print ("La Suma es: ", sumatoria)

# Otro for con rango
for n in range (5, 15) :
  print (n)
print ("-------")  

# Otro for pero ahora el rango es regresivo
for n in range (15, 5, -1) :
  print (n)





