import json

def salvar_dados(dicio, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dicio, f, indent=4, ensure_ascii=False)

def ler_dados(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def lista_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa cadastrada.\n')
    else:
        for t in tarefas:
            status = 'Concluída [✔️  ]' if t['concluida'] == True else 'Pendente'
            print(f'N°: {t["N"]}\n')
            print(f'TAREFA: {t["tarefa"]} - STATUS: {status}')
            print('-' * 60)
