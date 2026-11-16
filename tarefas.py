import utils

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
                'concluida': False
            })
            utils.salvar_dados(self.tarefas, 'tarefas.json')
            print(f'>>> Tarefa adicionada: {tarefa}\n')
            

    def concluir_tarefa(self):
        print('>>> CONCLUIR TAREFA (0 ou Enter para sair) <<<\n')

        utils.lista_tarefas(self.tarefas)   
        numero = input('Tarefa que deseja concluir: ').strip()

        if numero in ('0', ''):
            print('Encerrado.')
            return

        for t in self.tarefas:
            if t['N'] == int(numero):
                t['concluida'] = True
                utils.salvar_dados(self.tarefas, 'tarefas.json')
                print(f'>>> Tarefa concluída: {t["tarefa"]} [✔️  ]\n')
