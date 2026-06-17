# produtos.py
from utils import ler_int, ler_float


def proximo_id(lista):
    if len(lista) == 0:
        return 1

    maior_id = 0
    for item in lista:
        if item["id"] > maior_id:
            maior_id = item["id"]

    return maior_id + 1


def cadastrar_produto(produtos):
    print("\n===== CADASTRAR PRODUTO =====")
    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria (ex: Alimento, Limpeza, Outros): ").strip()

    preco = ler_float("Preço do produto: ", minimo=0.0)
    estoque = ler_int("Estoque inicial: ", minimo=0)

    novo_id = proximo_id(produtos)

    novo_produto = {
        "id": novo_id,
        "name": nome,  # Mantendo o padrão para o dicionário
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(novo_produto)
    print(f"Produto '{nome}' cadastrado com sucesso! (ID: {novo_id})")


def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("\n===== LISTA DE PRODUTOS =====")
    # BÔNUS: Ordenando por nome usando a função sorted
    produtos_ordenados = sorted(produtos, key=lambda p: p["nome"].lower())

    for p in produtos_ordenados:
        print(
            f"ID: {p['id']} | Nome: {p['nome']} | Categoria: {p['categoria']} | Preço: R$ {p['preco']:.2f} | Estoque: {p['estoque']}")


def buscar_produtos(produtos, texto):
    resultados = []
    texto_busca = texto.lower().strip()

    for p in produtos:
        if texto_busca in p["nome"].lower():
            resultados.append(p)

    return resultados


def registrar_mov(produtos, movs, tipo):
    if len(produtos) == 0:
        print("Não há produtos cadastrados para movimentar.")
        return

    print(f"\n===== REGISTRAR {'ENTRADA' if tipo == 'E' else 'SAÍDA'} DE ESTOQUE =====")
    id_busca = ler_int("Digite o ID do produto: ", minimo=1)

    produto_alvo = None
    for p in produtos:
        if p["id"] == id_busca:
            produto_alvo = p
            break

    if produto_alvo is None:
        print("Produto não encontrado com esse ID.")
        return

    print(f"Produto selecionado: {produto_alvo['nome']} (Estoque atual: {produto_alvo['estoque']})")

    while True:
        qtd = ler_int("Quantidade a movimentar: ", minimo=1)

        if tipo == "S" and qtd > produto_alvo["estoque"]:
            print(f"Erro! Estoque insuficiente. Você só possui {produto_alvo['estoque']} unidades.")
            print("Digite uma quantidade menor.")
            continue
        break

    data = input("Digite a data (AAAA-MM-DD) ou pressione Enter para usar a data de hoje: ").strip()
    if not data:
        data = "2026-06-12"

    obs = input("Observação (opcional): ").strip()

    if tipo == "E":
        produto_alvo["estoque"] += qtd
    else:
        produto_alvo["estoque"] -= qtd

    nova_movimentacao = {
        "id": proximo_id(movs),
        "produto_id": produto_alvo["id"],
        "tipo": tipo,
        "quantidade": qtd,
        "data": data,
        "observacao": obs if obs else "Sem observações"
    }

    movs.append(nova_movimentacao)
    print(f"Movimentação registrada com sucesso! Novo estoque: {produto_alvo['estoque']}")