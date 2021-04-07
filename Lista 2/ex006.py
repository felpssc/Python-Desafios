dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quatidade de horas: '))
minutos = int(input('Digite a quantidade de minutos:'))
segundos = int(input('Digite a quantidade de segundos: '))

dias *= 24 * 3600
horas *= 3600
minutos *= 60

print('Total de segundos: {}'.format(dias + horas + minutos + segundos))