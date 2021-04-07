num = 0
while 12 > num or num > 20:
    num = int(input('Digite um número entre 12 e 10: '))
    if 1 > num or num > 10:
        print(num)
    else:
        print('--- Entrada Inválida! ---')