
def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    if b == 0:
        return 'no esta definido'
    
    return a / b           


valorA = int(input ('Ingrese el valor a: '))
valorB = int(input ('Ingrese el valor b: '))

print (f'La suma de {valorA} y {valorB} es : {suma(valorA, valorB)}')
print (f'La resta de {valorA} y {valorB} es : {resta(valorA, valorB)}')
print (f'La division de {valorA} y {valorB} es : {division(valorA, valorB)}')
print (f'La multiplicacion de {valorA} y {valorB} es : {multiplicacion(valorA, valorB)}')