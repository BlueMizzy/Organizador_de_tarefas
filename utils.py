import json, os

def salvar_dados(dicio, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dicio, f, indent=4, ensure_ascii=False)

def ler_dados(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def lista_tarefas(tarefas, stts=None):    #lista as tarefas toda organizada.
    if stts is None:
        print('>>> LISTA DE TODAS AS TAREFAS <<<\n')
        if not tarefas:
            linha('Nenhuma tarefa cadastrada.\n')
        else:
            for t in tarefas:
                status = 'Concluída' if t['concluida'] == True else 'Pendente'
                print(f'N°: {t["N"]}')
                linha(f'TAREFA: {t["tarefa"]} - STATUS: {status}')
                print()

    if stts is not None:
        for t in tarefas:
            if t['concluida'] == stts:
                print(f'N°: {t["N"]}')
                linha(f'TAREFA: {t["tarefa"]}')
                print()


def historico_mes(tarefas, mes_escolhido):   #Mostra os históricos por mês
    for t in tarefas:
        if t['concluida']:
            mes_criacao = t['data_criacao'][3:5]

            if mes_criacao == mes_escolhido:
                print(f'\nN°: {t["N"]} - DATA DE CRIAÇÃO: {t["data_criacao"]}')
                linha(f'TAREFA: {t["tarefa"]} - STATUS: Concluída')
                print()

    
def limpar_terminal():  #limpa o terminal onde eu chamar a função.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def linha(frase):
    tam = len(frase) + 2
    borda = f'+{"-" * tam}+'
    print(borda)
    print(f'| {frase} |')
    print(borda)
