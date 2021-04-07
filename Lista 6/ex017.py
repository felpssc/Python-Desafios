def soma_listas(lista, lista2):
    lista3 = []
    for n in range(0, len(lista)):
        lista3 += [lista[n] + lista2[n]]
    return lista3

lista5 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4]

print(soma_listas(lista5, lista2))

