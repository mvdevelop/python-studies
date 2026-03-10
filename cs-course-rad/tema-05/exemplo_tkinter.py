
"""
Exemplo de aplicação com Tkinter
Framework GUI padrão do Python
"""

import tkinter as tk
from tkinter import messagebox

def saudacao():
    nome = entrada_nome.get()
    if nome:
        messagebox.showinfo("Saudação", f"Olá, {nome}! Bem-vindo ao Tkinter!")
    else:
        messagebox.showwarning("Atenção", "Por favor, digite seu nome.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo Tkinter")
janela.geometry("400x300")
janela.configure(bg="#f0f0f0")

# Título
titulo = tk.Label(
    janela,
    text="Aplicação GUI com Tkinter",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333333"
)
titulo.pack(pady=20)

# Subtítulo
subtitulo = tk.Label(
    janela,
    text="Framework padrão do Python",
    font=("Arial", 10),
    bg="#f0f0f0",
    fg="#666666"
)
subtitulo.pack(pady=5)

# Frame para o conteúdo
frame = tk.Frame(janela, bg="#f0f0f0")
frame.pack(pady=20)

# Label de instrução
label_nome = tk.Label(
    frame,
    text="Digite seu nome:",
    font=("Arial", 11),
    bg="#f0f0f0"
)
label_nome.pack(pady=5)

# Campo de entrada
entrada_nome = tk.Entry(
    frame,
    font=("Arial", 11),
    width=30,
    bd=2,
    relief=tk.GROOVE
)
entrada_nome.pack(pady=5)

# Botão de ação
botao_saudacao = tk.Button(
    frame,
    text="Clique aqui",
    command=saudacao,
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=5,
    bd=0,
    cursor="hand2"
)
botao_saudacao.pack(pady=15)

# Informação adicional
info = tk.Label(
    janela,
    text="Tkinter já vem instalado com Python!",
    font=("Arial", 9, "italic"),
    bg="#f0f0f0",
    fg="#888888"
)
info.pack(side=tk.BOTTOM, pady=10)

# Iniciar o loop principal
janela.mainloop()
