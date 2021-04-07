lado1 = float(input('Digite o valor do 1º: '))
lado2 = float(input('Digite o valor do 2º lado: '))
lado3 = float(input('Digite o valor do 3º lado: '))
if (lado1 + lado2) > lado3 or (lado2 + lado3) > lado1 or (lado1 + lado3) > lado2:
    print('Os lados formam um triângulo',end=' ')
    if lado1 == lado2 and lado2 == lado3:
        print('Equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isóceles.')
    else:
        print('Escaleno.')
else:
    print('Os lados não formam um triângulo.')
