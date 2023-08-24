menu = """
[C]  Criar Conta
[D]  Depositar
[S]  Sacar
[E]  Extrato
[Q]  Sair
[1]  Consultar Usuários

=> """

saldo = 0
numero_saques = 0
limite = 500
extrato = []
saques = []
usuarios = {}

LIMITE_SAQUE = 3

# FUNÇÕES
def dadosCliente():
    print('Insira seus dados abaixo')
    cpf = str(input('Seu CPF: '))
    if cpf not in usuarios:
        nome = str(input('Seu nome: '))
        logradouro = str(input('Logradouro: '))
        numero = str(input('Numero da casa: '))
        bairro = str(input('Bairro: '))
        novo_usuario = {'nome':nome,'logradouro':logradouro, 'numero':numero, 'bairro':bairro, 'saldo_user':0, 'movimentacoes':{}, 'agencia':('0001'),'saques':[]}
        usuarios[cpf] = novo_usuario
        print('-'*50)
        print(f'''
        Conta criada com sucesso!
              Nome:    {nome}
              CPF:     {cpf}
              Agencia: {usuarios[cpf]['agencia']}
        ''')
        print('-'*50)
        #print(f'Usuário com CPF {cpf} criado com sucesso')
    else:
        print('-'*50)
        print('Esse usuário já existe')
        print('-'*50)
def criar_usuario():
    print('Olá, seja vem vindo ao Banco Brasileiro, vamos criar seu cadastro')
    dadosCliente()

def fazer_deposito():
    global saldo
    print('Depósito')
    try:
        cpf = input('Insira seu cpf: ')
        if cpf in usuarios:
            nome_user = usuarios[cpf]['nome']
            print(f'Olá {nome_user}!')
            valor = float(input('Insita o valor a ser depositado: R$ '))
            if valor > 0:
                usuarios[cpf]['saldo_user'] += valor
                print('=' *50)
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
                show_saldo = usuarios[cpf]['saldo_user']
                print(f'Seu saldo agora é de R$ {show_saldo:.2f}')
                print('=' *50)

                if 'movimentacoes' not in usuarios[cpf]:
                    usuarios[cpf]['movimentacoes'] = {}

                usuarios[cpf]['movimentacoes'][f'Depósito de'] = valor
                
            elif valor <= 0:
                print('=' *50)
                print('Você não pode depositar esse valor, tente novamente')
                print('=' *50)
        else:
            print('Usuário não encontrado')
    except Exception as erro:
        print('Digite apenas números')
        print(erro)


def fazer_saque():
    global saldo
    print('Saque')
    try:
        cpf = input('Insira seu CPF: ')
        if cpf in usuarios:
            print(f'Olá {usuarios[cpf]["nome"]}')
            valor = float(input('Insira o valor do saque: R$'))
            if len(usuarios[cpf]['saques']) > 2:
                print('=' *50)
                print('Saque não realizado')
                print(f'Você excedeu o limite de {LIMITE_SAQUE} saques diários')
                print('=' *50)
            elif valor > limite:
                print('=' *50)
                print('Saque não realizado')
                print(f'O valor de saque não pode ser maior que o seu limite de saque de: R$ {limite:.2f}')
                print('=' *50)
            elif valor > usuarios[cpf]['saldo_user']:
                print('=' *50)
                print('Sem saldo suficiente na conta')
                print(f'seu saldo: R$ {usuarios[cpf]["saldo_user"]:.2f}')
                print('=' *50)
            elif valor <= 0:
                print('=' *50)
                print('Você só pode sacar valores acima de zero')
                print('=' *50)
            elif valor <= usuarios[cpf]['saldo_user']:
                usuarios[cpf]['saldo_user'] -= valor
                print('=' *50)
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
                print(f'Seu saldo agora é de R$ {usuarios[cpf]["saldo_user"]:.2f}')
                print('=' *50)
                if 'saques' not in usuarios[cpf]:
                    usuarios[cpf]['saques'] = []
                usuarios[cpf]['saques'].append(f'Saque de R$ {valor:.2f}')
                if 'movimentacoes' not in usuarios[cpf]:
                    usuarios[cpf]['movimentacoes'] = {}
                usuarios[cpf]['movimentacoes'][f'Saque de'] = valor

        else:
             print('Usuário não encontrado')
    except Exception as erro:
        print('Saque não realizado')
        print(erro)

def ver_extrato(cpf):
    print('Extrato')
    nome = usuarios[cpf]['nome']
    print(f'Extrato de {nome}')
    if len(usuarios[cpf]['movimentacoes']) == 0:
        print('=' *50)
        print('Não foram realizadas movimentações')
        print('=' *50)
    else:
        print('=' *50)
        print(usuarios[cpf]['movimentacoes'])
        print(f'Saldo atual: R$ {usuarios[cpf]["saldo_user"]}')
        print('=' *50)

# INÍCIO DO PROGRAMA
while True:
    opcao = input(menu).upper()
    #CRIAR USUÁRIO
    if opcao == 'C':
        criar_usuario()
    # DEPÓSITOS
    elif opcao == 'D':
        fazer_deposito()
    # SAQUES
    elif opcao == 'S':
        fazer_saque()
    # EXTRATO
    elif opcao == 'E':
        cpf = input('Insira o CPF: ')
        if cpf in usuarios:
            ver_extrato(cpf)
    # SAIR DO PROGRAMAd
    elif opcao == 'Q':
        print('=' *50)
        print('Obrigado por utilizar nosso banco!')
        print('Saindo do sistema')
        print('=' *50)
        break
    elif opcao == '1':
        print(usuarios)
        
    else:
        print('Opção inválida, tente novamente')
