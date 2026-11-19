import utils, tarefas

def criar_menu(titulo, opcoes, tam=40):   #base do menu
    while True:
        print(f'+{"-" * tam}+')
        print(f'|{titulo:^{tam}}|')
        print(f'+{"-" * tam}+')

        for numero, descricao in opcoes.items():
            print(f'|{f'{numero} - {descricao}':<{tam}}|')

        print(f'+{"-" * tam}+')

        op = input("Escolha: ")

        if op in opcoes:
            utils.limpar_terminal()
            return op

        print('Opção inválida.')


def menu():
    opcoes = {
        '1': 'Add tarefas',
        '2': 'Concluir tarefas',
        '3': 'Tarefas pendentes',
        '4': 'Tarefas concluídas',
        '5': 'Listar tarefas',
        '6': 'Histórico do mês',
        '0': 'Sair'    }

    trf = tarefas.Tarefas()

    while True:
        op = criar_menu('MENU DE ORGANIZAÇÃO', opcoes)

        if op == '0':
            print('Encerrando...')
            break

        match op:

            case '1':
                trf.adicionar_tarefa()

            case '2':
                trf.concluir_tarefa()

            case '3':
                trf.tarefas_pendentes()

            case '4':
                trf.tarefas_concluidas()

            case '5':
                utils.lista_tarefas(trf.tarefas)

            case '6':
                utils.historico_mes(trf.tarefas)


