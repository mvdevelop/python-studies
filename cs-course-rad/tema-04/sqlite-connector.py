
# sqlite-connector

import sqlite3

try:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    print("Conectado ao SQLite com sucesso!")

    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()

    print("Versão do SQLite:", version)

    connection.close()

except sqlite3.Error as error:
    print("Erro ao conectar ao SQLite:", error)
