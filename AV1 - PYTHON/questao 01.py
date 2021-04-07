ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O mês de fevereiro do ano {ano} tem 29 dias.')
else:
    print(f'O mês de fevereiro do ano {ano} tem 28 dias.')