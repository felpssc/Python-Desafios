notas = [0, 0, 0]
for n in range(3):
    nota = float(input('Digite a {}º nota: '.format(n + 1)))
    notas.append(nota)
print('A média é: ', sum(notas)/3)