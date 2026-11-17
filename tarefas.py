import utils
from datetime import datetime

class Tarefas:
    def __init__(self):
        try:
            dados = utils.ler_dados('tarefas.json')
        except FileNotFoundError:
            dados = []

        if isinstance(dados, dict):
            dados = [dados]

        self.tarefas = dados


    def adicionar_tarefa(self):
        print('>>> ADICIONAR TAREFA (0 ou Enter para sair) <<<\n')
        while True:
            tarefa = input('Tarefa: ').strip()

            if tarefa in ('0', ''):
                print('Encerrado.')
                break

            tarefa = tarefa.capitalize()
            self.tarefas.append({
                'N': len(self.tarefas) + 1,
                'tarefa': tarefa,
                'concluida': False,
                'data_criacao': datetime.now().strftime("%d-%m-%Y")
            })
            utils.salvar_dados(self.tarefas, 'tarefas.json')
            print(f'>>> Tarefa adicionada: {tarefa}\n')
            

    def concluir_tarefa(self):
        print('>>> CONCLUIR TAREFA (0 ou Enter para sair) <<<\n')

        utils.lista_tarefas(self.tarefas, stts=False)   
        numero = input('Tarefa que deseja concluir: ').strip()

        if numero in ('0', ''):
            print('Encerrado.')
            return

        for t in self.tarefas:
            if t['N'] == int(numero):
                if t['concluida'] == True:
                    print(f'>>> Tarefa já foi concluída: {t["tarefa"]} [✔️  ]\n')
                    return
                
                t['concluida'] = True
                utils.salvar_dados(self.tarefas, 'tarefas.json')
                print(f'>>> Tarefa concluída: {t["tarefa"]} [✔️  ]\n')


    def tarefas_concluidas(self):
        print('>>> TAREFAS CONCLUÍDAS <<<\n')
        utils.lista_tarefas(self.tarefas, stts=True)


    def tarefas_pendentes(self):
        print('>>> TAREFAS PENDENTES <<<\n')
        utils.lista_tarefas(self.tarefas, stts=False)
