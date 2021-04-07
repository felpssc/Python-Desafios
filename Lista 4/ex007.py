print('======= LOGIN DE ACESSO =======')
cod_armazenado = 1234   #valor constante
user = int(input('Digite o código de usuário: '))
if user == cod_armazenado:
    print('--- Usuário Inválido! ---')
else:
    senha = int(input('Digite a sua senha: '))
    if senha == 9999:
        print('# ACESSO PERMITIDO #')
    else:
        print('--- Senha Incorreta! ---')