def factorial (numero):
    if numero in [0,1]:
        return 1
    return numero * factorial(numero - 1)

def fibonacci (numero):
    if numero == 0 or numero == 1 :
        return 1
    return fibonacci (numero - 1) + fibonacci (numero - 2)   

numFactorial = int( input ("Ingresa un valor positivo: ")) 
print (f'El factorial de {numFactorial} es: {factorial(numFactorial)}')
print (f'El fibonacci de {numFactorial} es: {fibonacci(numFactorial)}')
