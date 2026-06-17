# relatorios.py

def relatorio_movimentacoes(produtos, movs):
    if len(movs) == 0:
        print("Nenhuma movimentação cadastrada.")
        return

    total_entradas = 0
    total_saidas = 0

    print("\n===== RELATÓRIO DE MOVIMENTAÇÕES =====")

    for mov in movs:
        nome_produto = "Produto não encontrado"

        for produto in produtos:
            if produto["id"] == mov["produto_id"]:
                nome_produto = produto["nome"]
                break

        print(f"\nID: {mov['id']}")
        print(f"Data: {mov['data']}")
        print(f"Tipo: {mov['tipo']}")
        print(f"Produto: {nome_produto}")
        print(f"Quantidade: {mov['quantidade']}")
        print(f"Observação: {mov['observacao']}")

        if mov["tipo"] == "E":
            total_entradas += mov["quantidade"]
        else:
            total_saidas += mov["quantidade"]

    print("\n===== TOTAIS =====")
    print("Total de Entradas:", total_entradas)
    print("Total de Saídas:", total_saidas)


def relatorio_gerencial(produtos, movs):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("\n===== RELATÓRIO GERENCIAL =====")

    maior_estoque = max(produto["estoque"] for produto in produtos)
    menor_estoque = min(produto["estoque"] for produto in produtos)

    print("\nProduto(s) com MAIOR estoque:")
    for produto in produtos:
        if produto["estoque"] == maior_estoque:
            print(f"- {produto['nome']} ({produto['estoque']} unidades)")

    print("\nProduto(s) com MENOR estoque:")
    for produto in produtos:
        if produto["estoque"] == menor_estoque:
            print(f"- {produto['nome']} ({produto['estoque']} unidades)")

    valor_total = 0
    for produto in produtos:
        valor_total += produto["estoque"] * produto["preco"]

    print(f"\nValor total em estoque: R$ {valor_total:.2f}")

    categorias = {}
    for produto in produtos:
        categoria = produto["categoria"]
        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

    print("\nQuantidade de produtos por categoria:")
    for categoria, quantidade in categorias.items():
        print(f"- {categoria}: {quantidade}")

    produtos_ordenados = sorted(
        produtos,
        key=lambda p: p["estoque"] * p["preco"],
        reverse=True
    )

    print("\nTop 3 produtos com maior valor em estoque:")
    for produto in produtos_ordenados[:3]:
        valor = produto["estoque"] * produto["preco"]
        print(f"- {produto['nome']} - R$ {valor:.2f}")