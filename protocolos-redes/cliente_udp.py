
# How to run: cliente_udp.py

import socket

HOST = "127.0.0.1"
PORT = 6000

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = input("Digite uma mensagem para o servidor UDP: ")
cliente.sendto(mensagem.encode("utf-8"), (HOST, PORT))

resposta, _ = cliente.recvfrom(1024)
print("Resposta do servidor:", resposta.decode("utf-8"))

cliente.close()
