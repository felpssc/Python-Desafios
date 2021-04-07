valores = [9]
quantidade_dentro = 0
quantidade_fora = 0
for n in range(1, 11):
    valor = int(input('Digite o {}º número: '.format(n)))
    valores.append(valor)
    if valores[n] >= 10:
        quantidade_dentro += 1
    else:
        quantidade_fora += 1
print('Existem {} valores entre [10 e 20] e {} valores fora desse intervalo.'.format(quantidade_dentro, quantidade_fora))