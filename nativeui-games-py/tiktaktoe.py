
import tkinter as tk
from tkinter import messagebox

jogador = "X"
tabuleiro = [""] * 9

def verificar_vitoria():
    combinacoes = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != "":
            return tabuleiro[a]

    if "" not in tabuleiro:
        return "Empate"

    return None

def clicar(i):
    global jogador

    if tabuleiro[i] == "":
        tabuleiro[i] = jogador
        botoes[i]["text"] = jogador

        resultado = verificar_vitoria()

        if resultado:
            messagebox.showinfo("Fim", f"Resultado: {resultado}")
            resetar()
        else:
            jogador = "O" if jogador == "X" else "X"

def resetar():
    global jogador, tabuleiro
    jogador = "X"
    tabuleiro = [""]*9
    for b in botoes:
        b["text"] = ""

janela = tk.Tk()
janela.title("Jogo da Velha")

botoes = []

for i in range(9):
    b = tk.Button(janela,text="",width=10,height=4,
                  command=lambda i=i: clicar(i))
    b.grid(row=i//3,column=i%3)
    botoes.append(b)

janela.mainloop()
