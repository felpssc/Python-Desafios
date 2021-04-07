num = int(input('Digite um número: '))
for n in range(1, num):
    print(" " * (num - n), " *" * n)
for n in range(num, 0, -1):
    print(" " * (num - n), " *" * n)
