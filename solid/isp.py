
"""
    4️⃣ I — Interface Segregation Principle (ISP) - Nenhuma classe deve ser forçada a implementar métodos que não usa.

    ❌ Errado
    class Trabalhador:
        def trabalhar(self):
            pass

        def comer(self):
            pass


    class Robo(Trabalhador):
        def trabalhar(self):
            print("Trabalhando...")

        def comer(self):
            raise Exception("Robô não come!")
"""

# ✅ Correto
class Trabalhador:
    def trabalhar(self):
        pass


class Alimentavel:
    def comer(self):
        pass


class Humano(Trabalhador, Alimentavel):
    def trabalhar(self):
        print("Trabalhando...")

    def comer(self):
        print("Comendo...")


class Robo(Trabalhador):
    def trabalhar(self):
        print("Trabalhando...")

# 🟢 Interfaces separadas.
