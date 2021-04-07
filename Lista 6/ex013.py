def maior_elemento(lista):
    maior = 0
    for n in lista:
        if n > maior:
            maior = n
    return maior

lista = [2, 4, 86, 18, 9, 45]

print(maior_elemento(lista))