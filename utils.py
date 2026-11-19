import json, os

def salvar_dados(dicio, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dicio, f, indent=4, ensure_ascii=False)

def ler_dados(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def lista_tarefas(tarefas, stts=None):    #lista as tarefas toda organizada.
    if stts == None:
        if not tarefas:
            print('Nenhuma tarefa cadastrada.\n')
        else:
            for t in tarefas:
                status = 'Concluída [✔️  ]' if t['concluida'] == True else 'Pendente'
                print(f'N°: {t["N"]}\n')
                print(f'TAREFA: {t["tarefa"]} - STATUS: {status}')
                print('-' * 60)

    if stts is not None:
        for t in tarefas:
            if t['concluida'] == stts:
                print(f'N°: {t["N"]}\n')
                print(f'TAREFA: {t["tarefa"]}')
                print('-' * 40)


def historico_mes(tarefas):   #Mostra os históricos por mês
    mes_especifico = input('Digite o mês (MM) para ver o histórico de tarefas concluídas: ').strip()

    for t in tarefas:
        if t['concluida'] == True:
            mes = t['data_criacao'][3:5]
            if mes == mes_especifico:
                print(f'\nN°: {t["N"]} - DATA DE CRIAÇÃO: {t["data_criacao"]}\n')
                print(f'TAREFA: {t["tarefa"]} - STATUS: Concluída [✔️  ]')
                print('-' * 60)

    
def limpar_terminal():  #limpa o terminal onde eu chamar a função.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

