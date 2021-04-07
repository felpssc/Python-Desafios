import sys
import os
continuar = True
agenda = []
def agenda_telefonica():
    while(continuar):
        print('========= CONTATOS =========')
        print('[1] - Adicionar contato')
        print('[2] - Remover contato')
        print('[3] - Ver agenda')
        print('[4] - Sair')
        option = int(input('Selecione uma opção: '))

        if option == 1:
            os.system("clear")
            print('======= Insira o nome e número do contato')
            nome = input('Digite o nome: ')
            numero = int(input(f'Digite o número do contato {nome}: '))
            contato = []
            contato += [nome, numero]
            agenda.append(contato)

        elif option == 2:
            if len(agenda) == 0:
              os.system("clear")
              print('Agenda vazia, não é possível remover contato')
              agenda_telefonica()
            os.system("clear")
            print(agenda)
            for n in range(0, len(agenda)):
              print(n)
            pos = input('Selecione a posição do contato que deseja remover ( [n] para cancelar ): ')
            if pos == 'n':
              agenda_telefonica()
            else:
              p = int(pos)
              del(agenda[p])

        elif option == 3:
            os.system("clear")
            print(agenda)

        elif option == 4:
            os.system("clear")
            print('Programa encerrado...')
            sys.exit()
        else:
            print('Opção Inválida!')

agenda_telefonica()