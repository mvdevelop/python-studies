
# How to run: chat_servidor.py

import socket
import threading

HOST = "127.0.0.1"
PORT = 7000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

clientes = []

def enviar_para_todos(mensagem, remetente):
    for cliente in clientes:
        if cliente != remetente:
            try:
                cliente.send(mensagem)
            except:
                clientes.remove(cliente)

def tratar_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            if not mensagem:
                break
            enviar_para_todos(mensagem, cliente)
        except:
            break

    clientes.remove(cliente)
    cliente.close()

print(f"Servidor de chat rodando em {HOST}:{PORT}")

while True:
    cliente, endereco = servidor.accept()
    print(f"Novo cliente conectado: {endereco}")
    clientes.append(cliente)

    thread = threading.Thread(target=tratar_cliente, args=(cliente,))
    thread.start()
