num = 0
while 1 > num or num > 10:
    num = int(input('Digite um número entre 1 e 10: '))
    if 1 > num or num > 10:
        print('--- Número digitado não está entre 1 e 10! ---')
for n in range(1,11):
    print(num, ' * ', n, ' = ', num * n)