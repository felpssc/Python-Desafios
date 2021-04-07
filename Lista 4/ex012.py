quantidade_pares = 0
for n in range(1, 11):
    valor = int(input('Digite o {}º número: '.format(n)))
    if valor % 2 == 0:
        quantidade_pares += 1
print('Existem {} números pares e {} números ímpares.'.format(quantidade_pares, 10 - quantidade_pares))
