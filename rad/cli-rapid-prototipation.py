
# 1️⃣ CLI em 2 minutos (prototipação rápida) - Ferramentas simples → entrega imediata.

def menu():
    print("1 - Somar")
    print("2 - Sair")

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", a + b)
    elif opcao == "2":
        break

"""
    ✅ Resultado imediato
    ✅ Sem arquitetura complexa
    ✅ Fácil ajuste com feedback

    Isso é RAD: primeiro funciona, depois melhora.
"""
