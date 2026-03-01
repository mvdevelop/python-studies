
"""
    5️⃣ D — Dependency Inversion Principle (DIP) - Dependa de abstrações, não de implementações concretas.

    ❌ Errado
    class MySQLDatabase:
        def conectar(self):
            print("Conectando ao MySQL")


    class Aplicacao:
        def __init__(self):
            self.db = MySQLDatabase()

        def iniciar(self):
            self.db.conectar()

    🔴 Aplicação depende diretamente do MySQL.
"""

# ✅ Correto
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def conectar(self):
        pass


class MySQLDatabase(Database):
    def conectar(self):
        print("Conectando ao MySQL")


class PostgreSQLDatabase(Database):
    def conectar(self):
        print("Conectando ao PostgreSQL")


class Aplicacao:
    def __init__(self, db: Database):
        self.db = db

    def iniciar(self):
        self.db.conectar()

"""
    Uso:

    db = PostgreSQLDatabase()
    app = Aplicacao(db)
    app.iniciar()
"""

# 🟢 Agora podemos trocar o banco sem alterar a aplicação.
