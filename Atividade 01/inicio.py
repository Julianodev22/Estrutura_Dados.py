from viagem import Viagem

# FUNÇÃO PARA CADASTRAR UMA NOVA VIAGEM


def novaViagem():
    id = input('Código do Voo: ')
    origem = input('Origem do Voo: ')
    destino = input('Destino: ')

    v = Viagem(id, origem, destino)
    conexao = input(
        'Insira uma conexão, se exisir, ou -1 para não adicionar mais conexões: ')

    while conexao != '-1':
        v.adicionarParada(conexao)
        conexao = input(
            'Insira uma conexão, se exisir, ou -1 para não adicionar mais conexões: ')

    viagens.append(v)


def buscarViagem(codVoo, lista):
    achou = False
    for i in lista:
        if codVoo == i.getId():
            print('\n')
            print(i)
            achou = True
            break
    if not achou:
        print('Destino não encontrado!')


def exibeViagens(lista):
    for i in lista:
        print(i)
        print('\n')
    print(f'Total de Viagens: {len(lista)}')


# INÍCIO DO PROGRAMA
viagens = []
opcao = int(input(
    'Bem-Vindo ao Sistema Schiavão Airlines\n\n1- Nova Viagem\n2- Buscar Viagem\n3- Sair do sistema\n\nSua opção: '))

while opcao > 0 and opcao < 3:
    if opcao == 1:
        novaViagem()
        opcao = int(
            input('\n\n1- Nova Viagem\n2- Buscar Viagem\n3- Sair do sistema\n\nSua opção: '))
    elif opcao == 2:
        codBusca = input('Insira o código do voo: ')
        buscarViagem(codBusca, viagens)
        opcao = int(
            input('\n\n1- Nova Viagem\n2- Buscar Viagem\n3- Sair do sistema\n\nSua opção: '))

exibeViagens(viagens)
