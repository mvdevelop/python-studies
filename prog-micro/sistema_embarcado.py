
def menu():
    print("\n=== SISTEMA ===")
    print("1 - Ler sensor")
    print("2 - Ligar LED")
    print("3 - Desligar LED")
    print("4 - Sair")

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        print("Sensor lido: OK")

    elif opcao == "2":
        print("LED LIGADO")

    elif opcao == "3":
        print("LED DESLIGADO")

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")
