import json
import menu

try:
    menu.menu()
except json.JSONDecodeError:
    print('Erro: tarefas.json está vazio ou contém JSON inválido.')
    raise SystemExit(1)
