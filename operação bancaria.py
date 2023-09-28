from datetime import datetime


#registro da hora e data de cada ação
nome = input ('Digite o nome completo do funcionário: ')
hora = datetime.now()
hora = hora.strftime('%d/%m/%Y %H:%M')
saldo = 3100.00
painel1 = """
_________BANCO____________

  TIME IS MONEY! Oh Yeah
__________________________
"""
painel2 = """
[1] SACAR VALORES
[2] ADICIONAR VALORES
[3] EMPRESTIMO
[4] SALDO
[5] SAIR

Conta Salário
Agência 001
Conta 000508-9
"""

operacao = 0

while  operacao != 5:
    print (painel1)
    print (f'CLIENTE: {nome}\n')
    print (f'Último Acesso: {hora}\n')
    print (f'SALDO R$: {saldo}\n')
    print (painel2)
    if operacao == 1: # operação de saque da conta
        print (f'SALDO RS:{saldo}')
        sacar = float(input('Digite o valor a ser sacado: '))
        while sacar > saldo:
          sacar = float(input('VALOR INDISPONIVEL\nQUANTO DESEJA SACAR: '))
        saldo = saldo_sacar = saldo - sacar
    elif operacao == 2: #adicionar valores a conta
        print (f'SALDO RS:{saldo}')
        adicionar = float(input('Digite o valor a ser adicionado: '))
        saldo = saldo_adicionar = saldo + adicionar
    elif operacao == 3: #emprestimo direto
        print (f'SALDO RS:{saldo}')
        parcelas = int(input('Escolha a quantidade de parcelas até 48: '))  #entrada de parcelas

        limite_emprestimo = (saldo / 10) * parcelas
        valor_parcelas = limite_emprestimo / parcelas
        juros = (limite_emprestimo * 3/100) * parcelas
        total_emprestimo = limite_emprestimo + juros
        print (f'As parcelas são {parcelas}, com valor de {valor_parcelas :.2f},\nsomando um total de {limite_emprestimo}, você irá pagar um total de R${total_emprestimo}')
        escolha = input ('deseja fazer o emprestimo S/N? ').upper()
        if escolha == 'S':
            saldo = saldo + limite_emprestimo
    elif operacao == 4: # Saldo
        pass
    elif operacao == 5: # Sair do programa
        break
    operacao = int(input('OPÇÃO: \n')) #entrada de operação do painel2


print (painel1)
print ('Obrigado por usar nosso banco \n')