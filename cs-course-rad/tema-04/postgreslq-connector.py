
# postgresql-connector

import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="meubanco",
        user="postgres",
        password="senha",
        port="5432"
    )

    cursor = connection.cursor()

    print("Conectado ao PostgreSQL com sucesso!")

    cursor.execute("SELECT version();")
    version = cursor.fetchone()

    print("Versão do PostgreSQL:", version)

    cursor.close()
    connection.close()

except Exception as error:
    print("Erro ao conectar ao PostgreSQL:", error)
