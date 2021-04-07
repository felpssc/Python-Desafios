palavra = input('Digite uma palavra: ')
isograma = False
for n in palavra:
    for j in palavra:
        if n != j:
            isograma = True
if isograma == True:
    print(f'A palavra {palavra} é um isograma.')

