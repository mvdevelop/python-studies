
# How to run: python servidor_udp.py

import socket

HOST = "127.0.0.1"
PORT = 6000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))

print(f"Servidor UDP escutando em {HOST}:{PORT}")

while True:
    dados, endereco = servidor.recvfrom(1024)
    mensagem = dados.decode("utf-8")
    print(f"Mensagem de {endereco}: {mensagem}")

    resposta = "Mensagem recebida via UDP."
    servidor.sendto(resposta.encode("utf-8"), endereco)
