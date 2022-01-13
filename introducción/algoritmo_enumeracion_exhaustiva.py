objetivo = int(input("Escoge un Entero: "))
respuesta = 0

while respuesta**2 < objetivo:
    print (respuesta)
    respuesta += 1

if respuesta**2 == objetivo:

    print(f"La raiz cuadra de {objetivo} es {respuesta}")
else:
    print(f'{objetivo} no tiene raiz exacta')
