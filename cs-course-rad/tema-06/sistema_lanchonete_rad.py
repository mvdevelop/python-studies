
# ==============================
# SISTEMA LANCHONETE - MODELO RAD
# ==============================

# Produtos pré-cadastrados
produtos = [
    {"nome": "Hamburguer", "preco": 10.0},
    {"nome": "Batata Frita", "preco": 7.0},
    {"nome": "Refrigerante", "preco": 5.0}
]

# Pedido atual
pedido = []


# ==============================
# Mostrar produtos
# ==============================

def mostrar_produtos():
    print("\n--- CARDÁPIO ---")
    for i, p in enumerate(produtos):
        print(f"{i + 1} - {p['nome']} (R${p['preco']})")


# ==============================
# Registrar pedido (PRIORIDADE 1)
# ==============================

def adicionar_item():
    mostrar_produtos()

    try:
        escolha = int(input("Escolha o produto: ")) - 1
        quantidade = int(input("Quantidade: "))

        produto = produtos[escolha]

        item = {
            "nome": produto["nome"],
            "quantidade": quantidade,
            "preco": produto["preco"],
            "total": quantidade * produto["preco"]
        }

        pedido.append(item)

        print("Item adicionado!")

    except:
        print("Erro ao adicionar item.")


# ==============================
# Calcular total (PRIORIDADE 2)
# ==============================

def calcular_total():
    total = sum(item["total"] for item in pedido)
    return total


# ==============================
# Excluir item (PRIORIDADE 3)
# ==============================

def remover_item():
    if not pedido:
        print("Pedido vazio.")
        return

    print("\n--- ITENS DO PEDIDO ---")
    for i, item in enumerate(pedido):
        print(f"{i + 1} - {item['nome']} x{item['quantidade']}")

    try:
        escolha = int(input("Escolha o item para remover: ")) - 1
        removido = pedido.pop(escolha)
        print(f"{removido['nome']} removido!")
    except:
        print("Erro ao remover item.")


# ==============================
# Resumo do pedido (PRIORIDADE 4)
# ==============================

def mostrar_resumo():
    if not pedido:
        print("Pedido vazio.")
        return

    print("\n--- RESUMO DO PEDIDO ---")

    for item in pedido:
        print(f"{item['nome']} x{item['quantidade']} = R${item['total']}")

    print(f"TOTAL: R${calcular_total()}")


# ==============================
# Cadastrar produto (PRIORIDADE 5)
# ==============================

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))

    produtos.append({"nome": nome, "preco": preco})

    print("Produto cadastrado!")


# ==============================
# Menu principal
# ==============================

def menu():
    while True:
        print("\n===== SABOR RÁPIDO =====")
        print("1 - Adicionar item ao pedido")
        print("2 - Remover item do pedido")
        print("3 - Ver resumo do pedido")
        print("4 - Cadastrar novo produto")
        print("5 - Finalizar pedido")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_item()

        elif opcao == "2":
            remover_item()

        elif opcao == "3":
            mostrar_resumo()

        elif opcao == "4":
            cadastrar_produto()

        elif opcao == "5":
            mostrar_resumo()
            print("Pedido finalizado!\n")
            pedido.clear()

        elif opcao == "6":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


# Executar sistema
menu()
