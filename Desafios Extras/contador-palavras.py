frase = input('Digite uma frase: ')
espacos = 0
for n in frase:
    if n == " ":
        espacos += 1
print(f'Existem {espacos + 1} palavras nessa frase.')