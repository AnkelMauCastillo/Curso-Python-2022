
def suma (a, b):
    """Suma dos valores a y b.

    param int a cualquier entero
    param int b cualquier entero
    return la suma de a y b
    """
    return a + b


valorA = int(input ('Ingrese el valor a: '))
valorB = int(input ('Ingrese el valor b: '))

print (f'La suma de {valorA} y {valorB} es : {suma(valorA, valorB)}')
