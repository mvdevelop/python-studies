
"""
    3️⃣ L — Liskov Substitution Principle (LSP) - Subclasses devem poder substituir a classe base sem quebrar o sistema.

    ❌ Errado
    class Passaro:
        def voar(self):
            print("Voando...")


    class Pinguim(Passaro):
        def voar(self):
            raise Exception("Pinguins não voam!")

    🔴 Problema: Pinguim não pode substituir Passaro.
"""

# ✅ Correto
class Passaro:
    pass


class PassaroVoador(Passaro):
    def voar(self):
        print("Voando...")


class Pinguim(Passaro):
    def nadar(self):
        print("Nadando...")

# 🟢 Agora não quebramos a substituição.
