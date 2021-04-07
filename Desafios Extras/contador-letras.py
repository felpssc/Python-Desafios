txt = input('Insira um texto: ')
for i in range(ord('a'), ord('z')+1):
    print(f'A letra {chr(i)} aparece {txt.lower().count(chr(i))} vezes no texto.')