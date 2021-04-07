import sys

cpf = input('Digite um CPF para consultar(sem pontos e traço): ')
c = 10
soma = 0
primeiro_digito = False
segundo_digito = False
##################################################
#### VERIFICA SE TODOS OS DÍGITOS SÃO IGUAIS  ####
##################################################
if cpf[0] == cpf[1] == cpf[2] == cpf[3] == cpf[4] == cpf[5] == cpf[6] == cpf[7] == cpf[8] == cpf[9] == cpf[10]:
    print('CPF INVÁLIDO!')
    sys.exit()
##################################################
#### VALIDAÇÃO DO PRIMEIRO DÍGITO VERIFICADOR ####
##################################################
for n in cpf:
    if c != 1 and c != 0:
        soma += int(n) * c
        c -= 1
if (soma * 10) % 11 == int(cpf[9]):
    primeiro_digito = True
##################################################
#### VALIDAÇÃO DO SEGUNDO DÍGITO VERIFICADOR #####
##################################################
soma = 0
c = 11
for n in cpf:
    if c != 1 and c != 0:
        soma += int(n) * c
        c -= 1
if (soma * 10) % 11 == int(cpf[10]):
    segundo_digito = True
##################################################
#### VERIFICA SE OS DOIS DIGITOS SÃO VÁLIDOS  ####
##################################################
if primeiro_digito and segundo_digito == True:
    print('CPF VÁLIDO!')
else:
    print('CPF INVÁLIDO!')
