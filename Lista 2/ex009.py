capacidade = float(input('Digite a capacidade do elevador em KG: '))
p1 = float(input('Digite o peso da 1º pessoa: '))
p2 = float(input('Digite o peso da 2º pessoa: '))
p3 = float(input('Digite o peso da 3º pessoa: '))
p4 = float(input('Digite o peso da 4º pessoa: '))
p5 = float(input('Digite o peso da 5º pessoa: '))
soma = float(p1 + p2 + p3 + p4 + p5)
if soma > capacidade:
    print('Peso Total: ', soma)
    print('O elevador excedeu a carga máxima!')
else:
    print('Peso Total: ', soma)
    print('O elevador está liberado para subir!')

