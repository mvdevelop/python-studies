
# How to run: cliente_http.py

import socket

HOST = "example.com"
PORT = 80

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

requisicao = (
    "GET / HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "Connection: close\r\n\r\n"
)

cliente.send(requisicao.encode("utf-8"))

resposta = b""
while True:
    dados = cliente.recv(4096)
    if not dados:
        break
    resposta += dados

cliente.close()

print(resposta.decode("utf-8", errors="ignore"))
