valor_hora = float(input('Digite quanto você ganha por hora: R$'))
horas_mês = int(input('Digite o número de horas trabalhadas por mês: '))
print('Trabalhando {} horas por semana ou {} por mês, seu salário será de R${}'.format(horas_mês / 5, horas_mês, horas_mês * valor_hora))