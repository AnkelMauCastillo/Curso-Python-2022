def factorial (numero):
    if numero in [0,1]:
        return 1
    return numero * factorial(numero - 1)

numFactorial = int( input ("Ingresa un valor positivo: ")) 
print (f'El factorial de {numFactorial} es: {factorial(numFactorial)}')