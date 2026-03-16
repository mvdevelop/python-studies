
# estoque_loja.py

import psycopg2
from faker import Faker
import random

fake = Faker("pt_BR")

# ===============================
# Conexão com o banco de dados
# ===============================

def conectar():
    try:
        conn = psycopg2.connect(
            database="lojadb",
            user="postgres",
            password="123456",
            host="127.0.0.1",
            port="5432"
        )
        return conn
    except Exception as erro:
        print("Erro ao conectar:", erro)


# ===============================
# Criar tabela Produto
# ===============================

def criar_tabela():

    conn = conectar()
    cursor = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS produto(
        codigo SERIAL PRIMARY KEY,
        nome VARCHAR(100),
        preco NUMERIC(10,2)
    )
    """

    cursor.execute(sql)

    conn.commit()

    print("Tabela criada com sucesso!")

    cursor.close()
    conn.close()


# ===============================
# Inserir produtos aleatórios
# ===============================

def inserir_produtos(qtd):

    conn = conectar()
    cursor = conn.cursor()

    for i in range(qtd):

        nome = fake.word().capitalize()
        preco = round(random.uniform(10, 500), 2)

        sql = "INSERT INTO produto (nome, preco) VALUES (%s, %s)"

        cursor.execute(sql, (nome, preco))

    conn.commit()

    print(qtd, "produtos inseridos!")

    cursor.close()
    conn.close()


# ===============================
# Listar produtos
# ===============================

def listar_produtos():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produto")

    produtos = cursor.fetchall()

    print("\n=== LISTA DE PRODUTOS ===")

    for p in produtos:
        print(f"Código: {p[0]} | Nome: {p[1]} | Preço: R${p[2]}")

    cursor.close()
    conn.close()


# ===============================
# Menu da aplicação
# ===============================

def menu():

    while True:

        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Criar tabela")
        print("2 - Inserir produtos aleatórios")
        print("3 - Listar produtos")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tabela()

        elif opcao == "2":
            qtd = int(input("Quantidade de produtos para gerar: "))
            inserir_produtos(qtd)

        elif opcao == "3":
            listar_produtos()

        elif opcao == "4":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


# Executar programa
menu()
