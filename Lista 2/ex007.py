num = int(input('Digite um número inteiro: '))
soma = 0
i = 1
for c in range(num):
    soma = soma + i
    i = i + 1

for c in range(num + 1):
    print(c, end=' ')
    if c != num:
        print('+', end=' ')
print('=',soma)
