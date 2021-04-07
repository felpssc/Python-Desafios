import math
print('============== EQUAÇÃO 2º GRAU ================')
a = float(input('Digite o valor de -> a: '))
b = float(input('Digite o valor de -> b: '))
c = float(input('Digite o valor de -> c: '))
D = (b ** 2 - 4 * a * c)
x1 = (-b + D ** (1 / 2)) / (2 * a)
x2 = (-b - D ** (1 / 2)) / (2 * a)
print('Valor de x1: {0:.2f} '.format(x1))
print('Valor de x2: {0:.2f}'.format(x2))

