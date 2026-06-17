# storage.py

# Importar JSON

import json

def carregar_dados():
    try:
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)
    except:
        produtos = []

    try:
        with open("movs.json", "r", encoding="utf-8") as arquivo:
            movs = json.load(arquivo)
    except:
        movs = []

    return produtos, movs


def salvar_dados(produtos, movs):
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=2, ensure_ascii=False)

    with open("movs.json", "w", encoding="utf-8") as arquivo:
        json.dump(movs, arquivo, indent=2, ensure_ascii=False)