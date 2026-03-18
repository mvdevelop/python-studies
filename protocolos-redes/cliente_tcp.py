
# How to run: python cliente_tcp.py

import socket

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

mensagem = input("Digite uma mensagem para o servidor: ")
cliente.send(mensagem.encode("utf-8"))

resposta = cliente.recv(1024).decode("utf-8")
print("Resposta do servidor:", resposta)

cliente.close()
