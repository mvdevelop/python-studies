
# Agenda pg-connection.py

import psycopg2

# =============================
# Conexão com o banco
# =============================

def conectar():
    try:
        conn = psycopg2.connect(
            database="agenda_db",
            user="postgres",
            password="123456",
            host="127.0.0.1",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco:", e)


# =============================
# CREATE - Inserir contato
# =============================

def inserir_contato(nome, telefone):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO agenda (nome, telefone) VALUES (%s, %s)"

    cursor.execute(sql, (nome, telefone))

    conn.commit()

    print("Contato inserido com sucesso!")

    cursor.close()
    conn.close()


# =============================
# READ - Listar contatos
# =============================

def listar_contatos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM agenda")

    contatos = cursor.fetchall()

    print("\n--- Lista de Contatos ---")

    for contato in contatos:
        print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]}")

    cursor.close()
    conn.close()


# =============================
# UPDATE - Atualizar telefone
# =============================

def atualizar_contato(id, telefone):
    conn = conectar()
    cursor = conn.cursor()

    sql = "UPDATE agenda SET telefone = %s WHERE id = %s"

    cursor.execute(sql, (telefone, id))

    conn.commit()

    print("Contato atualizado!")

    cursor.close()
    conn.close()


# =============================
# DELETE - Excluir contato
# =============================

def excluir_contato(id):
    conn = conectar()
    cursor = conn.cursor()

    sql = "DELETE FROM agenda WHERE id = %s"

    cursor.execute(sql, (id,))

    conn.commit()

    print("Contato excluído!")

    cursor.close()
    conn.close()


# =============================
# Menu do sistema
# =============================

def menu():

    while True:

        print("\n===== AGENDA TELEFÔNICA =====")
        print("1 - Inserir contato")
        print("2 - Listar contatos")
        print("3 - Atualizar telefone")
        print("4 - Excluir contato")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            inserir_contato(nome, telefone)

        elif opcao == "2":
            listar_contatos()

        elif opcao == "3":
            id = input("ID do contato: ")
            telefone = input("Novo telefone: ")
            atualizar_contato(id, telefone)

        elif opcao == "4":
            id = input("ID do contato: ")
            excluir_contato(id)

        elif opcao == "5":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida!")


# Executar programa
menu()
