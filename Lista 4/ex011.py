idades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for n in range(1,11):
    idade = int(input('Digite a {}º idade: '.format(n)))
    idades.append(idade)
print('A média entre as idades é: ', ((sum(idades))/10))
