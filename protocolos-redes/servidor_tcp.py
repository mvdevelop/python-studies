
# How to run: python servidor_tcp.py

import socket

HOST = "127.0.0.1"
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"Servidor TCP escutando em {HOST}:{PORT}")

while True:
    conexao, endereco = servidor.accept()
    print(f"Cliente conectado: {endereco}")

    mensagem = conexao.recv(1024).decode("utf-8")
    print(f"Mensagem recebida: {mensagem}")

    resposta = "Mensagem recebida pelo servidor TCP."
    conexao.send(resposta.encode("utf-8"))

    conexao.close()
    print("Conexão encerrada.\n")
