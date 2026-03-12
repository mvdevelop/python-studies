
import tkinter as tk
from tkinter import messagebox

# função chamada quando clicar no botão
def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()

    curso = curso_var.get()

    atividades = []
    if esporte_var.get():
        atividades.append("Esporte")
    if musica_var.get():
        atividades.append("Música")

    if nome == "" or idade == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    resultado = f"Aluno: {nome}\nIdade: {idade}\nCurso: {curso}\nAtividades: {', '.join(atividades)}"

    listbox_alunos.insert(tk.END, resultado)

    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)


# criação da janela principal
janela = tk.Tk()
janela.title("Sistema Escolar")
janela.geometry("500x450")

# -----------------------------
# Label
# -----------------------------
titulo = tk.Label(janela, text="Cadastro de Alunos", font=("Arial", 16))
titulo.pack(pady=10)

# -----------------------------
# Entrada de nome
# -----------------------------
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

entry_nome = tk.Entry(janela)
entry_nome.pack()

# -----------------------------
# Entrada de idade
# -----------------------------
label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()

entry_idade = tk.Entry(janela)
entry_idade.pack()

# -----------------------------
# Radiobutton (curso)
# -----------------------------
label_curso = tk.Label(janela, text="Curso:")
label_curso.pack()

curso_var = tk.StringVar()
curso_var.set("Matemática")

radio1 = tk.Radiobutton(janela, text="Matemática", variable=curso_var, value="Matemática")
radio1.pack()

radio2 = tk.Radiobutton(janela, text="História", variable=curso_var, value="História")
radio2.pack()

radio3 = tk.Radiobutton(janela, text="Computação", variable=curso_var, value="Computação")
radio3.pack()

# -----------------------------
# Checkbuttons (atividades)
# -----------------------------
label_atividades = tk.Label(janela, text="Atividades:")
label_atividades.pack()

esporte_var = tk.BooleanVar()
musica_var = tk.BooleanVar()

check1 = tk.Checkbutton(janela, text="Esporte", variable=esporte_var)
check1.pack()

check2 = tk.Checkbutton(janela, text="Música", variable=musica_var)
check2.pack()

# -----------------------------
# Botão
# -----------------------------
botao = tk.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno)
botao.pack(pady=10)

# -----------------------------
# Listbox
# -----------------------------
label_lista = tk.Label(janela, text="Alunos cadastrados:")
label_lista.pack()

listbox_alunos = tk.Listbox(janela, width=60)
listbox_alunos.pack(pady=10)

# -----------------------------
# Loop principal
# -----------------------------
janela.mainloop()
