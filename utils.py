import json

def salvar_dados(dicio, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dicio, f, indent=4, ensure_ascii=False)

def ler_dados(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)