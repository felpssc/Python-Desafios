import sys
quant_pessoas = int(input('Quantas pessoas deseja cadastrar: '))
idades = [quant_pessoas]
generos = [str(quant_pessoas)]
salarios = [float(quant_pessoas)]
quant_mulheres = 0
menor_salario = 0
pos_pessoa = 0
for n in range(quant_pessoas):
    idade = int(input('Digite a idade da {}º pessoa: '.format(n + 1)))
    idades.append(idade)
    if idade < 0:
        print('Idade negativa. Programa encerrado.')
        sys.exit()
    else:
        sexo = input('Digite o sexo da {}º pessoa. [M] para Masculino e [F] para feminino: '.format(n + 1))
        if sexo == 'F':
            quant_mulheres += 1
        generos.append(sexo.upper())
        salario = float(input('Digite o salário da {}º pessoa: R$'.format(n + 1)))
        if menor_salario < salario:
            menor_salario = salario
            pos_pessoa = n
        salarios.append(salario)

print('A média dos salários é de: R$', sum(salarios)/quant_pessoas)
print('A menor idade é {} anos e a maior é {} anos'.format(min(idades), max(idades)))
print('Existem {} mulheres na região.'.format(quant_mulheres))
print('A pessoa com o menor salário é do sexo {} e tem {} anos.'.format(generos.pop(pos_pessoa), idades[pos_pessoa]))
