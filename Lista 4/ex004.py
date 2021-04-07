print('========= LIVRARIA =========')
print('Critérios de descontos:')
print('         Critério A: R$ 0,25 por livro + R$ 7,50 fixo')
print('         Critério B: R$ 0,50 por livro + R$ 2,50 fixo')

quantidade_livros = int(input('Quantos livros deseja comprar?'))
if (0.25 * quantidade_livros) + 7.50 > (0.50 * quantidade_livros) + 2.50:
    print('Para esta quantidade de livros o critério A será mais vantajoso.')
else:
    print('Para esta quantidade de livros o critério B será mais vantajoso.')
