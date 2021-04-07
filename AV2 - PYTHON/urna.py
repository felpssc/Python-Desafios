import os

nomes_candidatos = ['Fernando Roubalheira', 'Paulo Vacilo', 'Henrique Caloteiro']
numeros_candidatos = ['157', '355', '017']
votos = []
senhaSecreta = 'fimeleicao'

def menu_urna():
    print("====== ELEIÇÃO PARA PREFEITO =======")
    print('Digite o número do candidato desejado.')
    print(f'[{numeros_candidatos[0]}] - {nomes_candidatos[0]}')
    print(f'[{numeros_candidatos[1]}] - {nomes_candidatos[1]}')
    print(f'[{numeros_candidatos[2]}] - {nomes_candidatos[2]}')
    print('[0] - Para votar em branco')
    votacao()

def resultados():
    qnt_eleitores = len(votos)
    votos_branco = votos.count('0')
    votos_nulo = votos.count('nulo')
    votos_valido = votos.count('157') + votos.count('355') + votos.count('017')
    votos_candidato_1 = votos.count('157')
    votos_candidato_2 = votos.count('355')
    votos_candidato_3 = votos.count('017')
    print(f'Número de eleitores que compareceram: {qnt_eleitores}')
    print(f'Número de votos válidos: {votos_valido}')
    print(f'Número de votos nulo: {votos_nulo}')
    print(f'Número de votos branco: {votos_branco}')
    print(f'Número de votos para o candidato {nomes_candidatos[0]}: {votos_candidato_1}')
    print(f'Número de votos para o candidato {nomes_candidatos[1]}: {votos_candidato_2}')
    print(f'Número de votos para o candidato {nomes_candidatos[2]}: {votos_candidato_3}')
    candidato_eleito()



def votacao():
    nulos = 0
    corrigir = 's'
    while corrigir != 'n':
        voto = input('Seu voto: ').lower()
        if voto == senhaSecreta:
            os.system('clear')
            print('===== ELEIÇÕES ENCERRADAS =====')
            resultados()
            return
        if voto == '0' or voto == '157' or voto == '355' or voto == '017':
            corrigir = input('Corrigir? [s] / [n]: ').lower()
            if corrigir == 'n':
                votos.append(voto)
                os.system('clear')
                menu_urna()
            elif corrigir == 's':
                votacao
            else:
                print('Comando Inválido!')
                votacao()
        else:
            corrigir = input('Corrigir? [s] / [n]: ').lower()
            if corrigir == 'n':
                votos.append('nulo')
                os.system('clear')
                menu_urna()
            elif corrigir == 's':
                votacao
            else:
                print('Comando Inválido!')
                votacao()



def candidato_eleito():
    votos_candidato_1 = votos.count('157')
    votos_candidato_2 = votos.count('355')
    votos_candidato_3 = votos.count('017')
    if votos_candidato_1 > votos_candidato_2 and votos_candidato_1 > votos_candidato_3:
        print(f'Candidato eleito no pleito: {nomes_candidatos[0]}')
    elif votos_candidato_2 > votos_candidato_1 and votos_candidato_2 > votos_candidato_3:
        print(f'Candidato eleito no pleito: {nomes_candidatos[1]}')
    elif votos_candidato_3 > votos_candidato_2 and votos_candidato_3 > votos_candidato_1:
        print(f'Candidato eleito no pleito: {nomes_candidatos[2]}')
    else:
        print('RESULTADO: Empate!')




def eleicao():
    menu_urna()


eleicao()