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
        tarefas_exibidas = tarefas
    else:
        tarefas_exibidas = [t for t in tarefas if t['conclusao'] == stts]

    if not tarefas_exibidas:
        mensagem = 'Nenhuma tarefa cadastrada.' if stts is None else 'Nenhuma tarefa encontrada.'
        linha(mensagem)
        return

    for t in tarefas_exibidas:
        status = 'Concluída' if t['conclusao'] else 'Pendente'
        print(f'N°: {t["N"]}')
        if stts is None:
            linha(f'TAREFA: {t["tarefa"]} - STATUS: {status}')
        else:
            linha(f'TAREFA: {t["tarefa"]}')
        print()


def historico_mes(tarefas, mes_escolhido):   #Mostra os históricos por mês
    mes_texto = f'{mes_escolhido:02d}'
    tarefas_do_mes = [
        t for t in tarefas
        if t['conclusao'] and t['data_conclusao'][3:5] == mes_texto
    ]

    if not tarefas_do_mes:
        print('Nenhuma tarefa concluída encontrada nesse mês.')
        return

    for t in tarefas_do_mes:
        print(f'\nN°: {t["N"]} - DATA DE CRIAÇÃO: {t["data_criacao"]} - DATA DE CONCLUSÃO: {t["data_conclusao"]}')
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
