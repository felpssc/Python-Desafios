maior_numero = 0
multiplicacao = 1
for n in range(5):
    numero = int(input('Digite um número: '))
    if numero > maior_numero:
        maior_numero = numero
for n in range(maior_numero, 1, -1):
    multiplicacao = multiplicacao * n
print(f'{maior_numero}! = {multiplicacao}')
