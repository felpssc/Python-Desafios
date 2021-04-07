def adicao(a, b):
    def adicao_1():
        r = a + b
        return r + 5
    return adicao_1()

print(adicao(2, 2))