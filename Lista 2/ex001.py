numeros = []
maior = []
for c in range(3):
    num = [int(input('Digite o {}º número inteiro: '.format(c + 1)))]
    numeros.append(num)
    if num > maior:
        maior = num
print('Os valores digitados foram: {}, {} e {}.'.format(numeros[0], numeros[1], numeros[2]))
print('O maior foi: {}'.format(maior))
