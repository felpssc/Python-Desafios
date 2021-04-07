def ultimo_elemento(lista):
    t = len(lista) - 1
    if len(lista) == 0:
        return None
    return lista[t]

lista = [1, 2, 3, 4, 5]

print(ultimo_elemento(lista))