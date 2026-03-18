
# How to run: chat_cliente.py

import socket
import threading

HOST = "127.0.0.1"
PORT = 7000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

nome = input("Digite seu nome: ")

def receber():
    while True:
        try:
            mensagem = cliente.recv(1024).decode("utf-8")
            print(mensagem)
        except:
            print("Conexão encerrada.")
            cliente.close()
            break

def enviar():
    while True:
        texto = input()
        mensagem = f"{nome}: {texto}"
        cliente.send(mensagem.encode("utf-8"))

thread_receber = threading.Thread(target=receber)
thread_receber.start()

thread_enviar = threading.Thread(target=enviar)
thread_enviar.start()
