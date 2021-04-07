n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
operacao = str(input('Qual operação deseja realizar? [ + ] [ - ] [ * ] [ / ]'))
result = float()
if operacao == '+':
    print('Operação soma escolhida.')
    result = n1 + n1
    print('Resultado: ', result)
elif operacao == '-':
    print('Operação subtração escolhida.')
    result = n1 - n2
    print('Resultado: ', result)
elif operacao == '*':
    print('Operação mutiplicação escolhida.')
    result = n1 * n2
    print('Resultado: ', result)
else:
    print('Operação divisão escolhida.')
    result = n1 / n2
    print('Resultado: ', result)
    
if result % 2 == 0:
    print('número par.')
else:
    print('número ímpar.')
