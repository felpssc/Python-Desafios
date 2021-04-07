def dia(num):
    if num <= 0 or num > 7:
        return 'Dia Inválido!'
    if num == 1:
        return 'Domingo'
    if num == 2:
        return 'Segunda-Feira'
    if num == 3:
        return 'Terça-Feira'
    if num == 4:
        return 'Quarta-Feira'
    if num == 5:
        return 'Quinta-Feira'
    if num == 6:
        return 'Sexta-Feira'
    if num == 7:
        return 'Sábado'


print(dia(8))
