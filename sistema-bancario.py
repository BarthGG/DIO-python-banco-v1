menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
saques = []
LIMITE_SAQUE = 3

while True:
    opcao = input(menu).upper()

# DEPÓSITOS
    if opcao == 'D':
        print('Depósito')
        try:
            valor = float(input('Insita o valor a ser depositado: R$ '))
            if valor > 0:
                saldo += valor
                print('=' *50)
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
                print(f'Seu saldo agora é de R$ {saldo:.2f}')
                print('=' *50)
                extrato.append(f'Depósito de R$ {valor:.2f}')
            elif valor <= 0:
                print('=' *50)
                print('Você não pode depositar esse valor, tente novamente')
                print('=' *50)
        except:
            print('Digite apenas números')
# SAQUES
    elif opcao == 'S':
        print('Saque')
        try:
            valor = float(input('Insira o valor do saque: R$'))
            if len(saques) > 2:
                print('=' *50)
                print('Saque não realizado')
                print(f'Você excedeu o limite de {LIMITE_SAQUE} saques diários')
                print('=' *50)
            elif valor > limite:
                print('=' *50)
                print('Saque não realizado')
                print(f'O valor de saque não pode ser maior que o seu limite de saque de: R$ {limite:.2f}')
                print('=' *50)
            elif valor > saldo:
                print('=' *50)
                print('Sem saldo suficiente na conta')
                print(f'seu saldo: R$ {saldo:.2f}')
                print('=' *50)
            elif valor <= 0:
                print('=' *50)
                print('Você só pode sacar valores acima de zero')
                print('=' *50)
            elif valor <= saldo:
                saldo -= valor
                print('=' *50)
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
                print(f'Seu saldo agora é de R$ {saldo:.2f}')
                print('=' *50)
                extrato.append(f'Saque de R$ {valor:.2f}')
                saques.append(valor)
        except:
            print('Digite apenas números')

            
# EXTRATO
    elif opcao == 'E':
        print('Extrato')
        if len(extrato) == 0:
            print('=' *50)
            print('Não foram realizadas movimentações')
            print('=' *50)
        else:
            print('=' *50)
            print(extrato)
            print(f'Saldo atual: R$ {saldo:.2f}')
            print('=' *50)
# SAIR DO PROGRAMA
    elif opcao == 'Q':
        print('=' *50)
        print('Obrigado por utilizar nosso banco!')
        print('Saindo do sistema')
        print('=' *50)
        break

    else:
        print('Opção inválida, tente novamente')
