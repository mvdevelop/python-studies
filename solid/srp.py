
"""
    1️⃣ S — Single Responsibility Principle (SRP) - Uma classe deve ter apenas um motivo para mudar.

    ❌ Errado (faz tudo):
    class Relatorio:
        def gerar(self, dados):
            return f"Relatório: {dados}"

        def salvar_arquivo(self, conteudo):
            with open("relatorio.txt", "w") as f:
                f.write(conteudo)

        def enviar_email(self, conteudo):
            print("Enviando email...")

    🔴 Problema:
    Essa classe:
    - Gera relatório
    - Salva arquivo
    - Envia email

    Múltiplas responsabilidades detectadas.
"""

# ✅ Correto
class GeradorRelatorio:
    def gerar(self, dados):
        return f"Relatório: {dados}"


class SalvadorArquivo:
    def salvar(self, conteudo):
        with open("relatorio.txt", "w") as f:
            f.write(conteudo)


class EnviadorEmail:
    def enviar(self, conteudo):
        print("Enviando email...")

# 🟢 Agora cada classe tem uma responsabilidade.
