numero1 = int(input('Introduce el primer número: '))
numero2 = int(input('Introduce el segundo número: '))
suma = 0

while numero1 > numero2:
    print('ERROR! Debe hacer que el primer número sea más pequeño que el segundo')
    numero1 = int(input('Introduce el primer número: '))
    numero2 = int(input('Introduce el segundo número: '))

for comprendidos in range(numero1, numero2+1):
        suma += comprendidos
        
print(f'La suma total de todos los enteros comprendidos entre {numero1} y {numero2} es de: {suma}')
    