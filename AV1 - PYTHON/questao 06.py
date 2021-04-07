quantidade_negativos = 0
soma = 0
valores_positivos = []
for n in range(20):
    valor = int(input('Digite um valor: '))
    if valor < 0:
        quantidade_negativos += 1
        soma += valor
    else:
        valores_positivos.append(valor)
print(f'Os valores positivos digitados são: {valores_positivos}')
print(f'Média dos valores negativos: {soma / quantidade_negativos}')
