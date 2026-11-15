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
        print(">>> ADICIONAR TAREFA (0 ou Enter para sair) <<<\n")
        while True:
            tarefa = input("Tarefa: ").strip()

            if tarefa in ('0', ''):
                print('Encerrado.')
                break

            tarefa = tarefa.capitalize()
            self.tarefas.append({'tarefa': tarefa})
            utils.salvar_dados(self.tarefas, 'tarefas.json')
            print(f">>> Tarefa adicionada: {tarefa}\n")
            
