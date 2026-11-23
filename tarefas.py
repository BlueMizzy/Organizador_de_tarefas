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
                'conclusao': False,
                'data_criacao': datetime.now().strftime("%d-%m-%Y"),
                'data_conclusao': None
            })
            utils.salvar_dados(self.tarefas, 'tarefas.json')
            print(f'>>> Tarefa adicionada: {tarefa}\n')
            

    def concluir_tarefa(self):
        print('>>> CONCLUIR TAREFA (0 ou Enter para sair) <<<\n')

        utils.lista_tarefas(self.tarefas, stts=False)

        while True:
            entrada = input('Tarefa que deseja concluir: ').strip()

            if entrada in ('0', ''):
                print('Encerrado.')
                return

            try:
                numero = int(entrada)
            except ValueError:
                print('\nDigite apenas um número.')
                continue

            tarefa_escolhida = next(
                (t for t in self.tarefas if t['N'] == numero),
                None
            )

            if tarefa_escolhida is None:
                print('Não encontrei uma tarefa com esse número.')
                continue

            if tarefa_escolhida['conclusao']:
                print(f'>>> Tarefa já foi concluída: {tarefa_escolhida["tarefa"]}\n')
                return

            tarefa_escolhida['conclusao'] = True
            tarefa_escolhida['data_conclusao'] = datetime.now().strftime("%d-%m-%Y")

            utils.salvar_dados(self.tarefas, 'tarefas.json')
            print(f'>>> Tarefa concluída: {tarefa_escolhida["tarefa"]}\n')
            return


    def tarefas_concluidas(self):
        print('>>> TAREFAS CONCLUÍDAS <<<\n')
        utils.lista_tarefas(self.tarefas, stts=True)


    def tarefas_pendentes(self):
        print('>>> TAREFAS PENDENTES <<<\n')
        utils.lista_tarefas(self.tarefas, stts=False)
