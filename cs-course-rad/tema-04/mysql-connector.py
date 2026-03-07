
# mysql-connector

import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senha",
        database="meubanco"
    )

    if connection.is_connected():
        print("Conectado ao MySQL com sucesso!")

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION();")

        version = cursor.fetchone()
        print("Versão do MySQL:", version)

except mysql.connector.Error as error:
    print("Erro ao conectar ao MySQL:", error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada")
