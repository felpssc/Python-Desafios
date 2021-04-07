def pares(v1, v2):
    lista = []
    for n in range(v1, v2 + 1):
        if n % 2 == 0:
            lista += [n]
    return lista

print(pares(0, 10))