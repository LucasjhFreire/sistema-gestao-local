# main.py
# Importar funçoes

from utils import ler_int
from storage import carregar_dados, salvar_dados
from produtos import (
    cadastrar_produto,
    listar_produtos,
    buscar_produtos,
    registrar_mov
)
from relatorios import (
    relatorio_movimentacoes,
    relatorio_gerencial
)

# Inicializa carregando os dados salvos do JSON
produtos, movs = carregar_dados()

while True:
    print("\n===== SGL - Sistema de Gestão Local =====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Registrar Entrada")
    print("5 - Registrar Saída")
    print("6 - Relatório de Movimentações")
    print("7 - Relatório Gerencial")
    print("8 - Salvar e Sair")

    opcao = ler_int("Escolha uma opção: ", 1, 8)

    if opcao == 1:
        cadastrar_produto(produtos)

    elif opcao == 2:
        listar_produtos(produtos)

    elif opcao == 3:
        texto = input("Digite o nome para buscar: ")
        resultados = buscar_produtos(produtos, texto)

        if len(resultados) == 0:
            print("Nenhum produto encontrado.")
        else:
            print("\n===== RESULTADOS DA BUSCA =====")
            for produto in resultados:
                print(f"ID: {produto['id']} | Nome: {produto['nome']} | Categoria: {produto['categoria']} | Estoque: {produto['estoque']}")

    elif opcao == 4:
        registrar_mov(produtos, movs, "E")

    elif opcao == 5:
        registrar_mov(produtos, movs, "S")

    elif opcao == 6:
        relatorio_movimentacoes(produtos, movs)

    elif opcao == 7:
        relatorio_gerencial(produtos, movs)

    elif opcao == 8:
        salvar_dados(produtos, movs)
        print("Dados salvos com sucesso!")
        print("Encerrando programa...")
        break
