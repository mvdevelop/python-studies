
import tkinter as tk
from tkinter import ttk, messagebox

class SistemaGestaoEscolar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão Escolar")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        self.criar_componentes()
        self.carregar_dados_iniciais()

    def criar_componentes(self):
        frame_form = tk.Frame(self.root, padx=10, pady=10)
        frame_form.pack(fill="x")

        tk.Label(frame_form, text="Nome do Aluno:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nome = tk.Entry(frame_form, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Nota 1:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_nota1 = tk.Entry(frame_form, width=15)
        self.entry_nota1.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Nota 2:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_nota2 = tk.Entry(frame_form, width=15)
        self.entry_nota2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(frame_form, text="Nota 3:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_nota3 = tk.Entry(frame_form, width=15)
        self.entry_nota3.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        btn_adicionar = tk.Button(
            frame_form,
            text="Cadastrar Aluno",
            width=20,
            command=self.cadastrar_aluno
        )
        btn_adicionar.grid(row=4, column=0, columnspan=2, pady=10)

        frame_tabela = tk.Frame(self.root, padx=10, pady=10)
        frame_tabela.pack(fill="both", expand=True)

        colunas = ("nome", "nota1", "nota2", "nota3", "media", "situacao")

        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=12)

        self.tree.heading("nome", text="Aluno")
        self.tree.heading("nota1", text="Nota 1")
        self.tree.heading("nota2", text="Nota 2")
        self.tree.heading("nota3", text="Nota 3")
        self.tree.heading("media", text="Média")
        self.tree.heading("situacao", text="Situação")

        self.tree.column("nome", width=250, anchor="center")
        self.tree.column("nota1", width=90, anchor="center")
        self.tree.column("nota2", width=90, anchor="center")
        self.tree.column("nota3", width=90, anchor="center")
        self.tree.column("media", width=90, anchor="center")
        self.tree.column("situacao", width=150, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def calcular_media(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3) / 3

    def definir_situacao(self, media):
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        return "Reprovado"

    def inserir_aluno_na_tabela(self, nome, nota1, nota2, nota3):
        media = self.calcular_media(nota1, nota2, nota3)
        situacao = self.definir_situacao(media)

        self.tree.insert(
            "",
            tk.END,
            values=(
                nome,
                f"{nota1:.1f}",
                f"{nota2:.1f}",
                f"{nota3:.1f}",
                f"{media:.1f}",
                situacao
            )
        )

    def carregar_dados_iniciais(self):
        alunos_iniciais = [
            ("Ana Souza", 8.0, 7.5, 9.0),
            ("Bruno Lima", 6.0, 5.5, 5.0),
            ("Carla Mendes", 4.0, 4.5, 5.0),
            ("Diego Silva", 7.0, 8.0, 6.5),
            ("Eduarda Alves", 9.0, 8.5, 9.5)
        ]

        for aluno in alunos_iniciais:
            self.inserir_aluno_na_tabela(*aluno)

    def cadastrar_aluno(self):
        nome = self.entry_nome.get().strip()
        nota1 = self.entry_nota1.get().strip()
        nota2 = self.entry_nota2.get().strip()
        nota3 = self.entry_nota3.get().strip()

        if not nome or not nota1 or not nota2 or not nota3:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)
        except ValueError:
            messagebox.showerror("Erro", "As notas devem ser numéricas.")
            return

        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
            messagebox.showwarning("Atenção", "As notas devem estar entre 0 e 10.")
            return

        self.inserir_aluno_na_tabela(nome, nota1, nota2, nota3)
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_nota1.delete(0, tk.END)
        self.entry_nota2.delete(0, tk.END)
        self.entry_nota3.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaGestaoEscolar(root)
    root.mainloop()
