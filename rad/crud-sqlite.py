
# 3️⃣ CRUD rápido com SQLite (sem configurar servidor) - RAD evita setups complexos.

import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")

def criar_usuario(nome):
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

criar_usuario("Marcos")
print(listar_usuarios())

"""
    ✅ Banco pronto
    ✅ Sem instalar servidor
    ✅ Ideal para protótipo
"""
