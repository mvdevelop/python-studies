
# How to run: scanner_portas.py

import socket

alvo = input("Digite o IP ou host alvo: ")
portas = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

print(f"\nEscaneando portas em {alvo}...\n")

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(1)

    resultado = cliente.connect_ex((alvo, porta))
    if resultado == 0:
        print(f"Porta {porta}: ABERTA")
    else:
        print(f"Porta {porta}: FECHADA")

    cliente.close()
