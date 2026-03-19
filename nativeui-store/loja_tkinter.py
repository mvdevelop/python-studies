
import tkinter as tk
from tkinter import ttk, messagebox

class SistemaLoja:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Loja")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.produtos = []
        self.proximo_id = 1

        self.criar_interface()

    def criar_interface(self):
        frame_form = tk.Frame(self.root, padx=10, pady=10)
        frame_form.pack(fill="x")

        tk.Label(frame_form, text="Nome do Produto:").grid(row=0, column=0, sticky="w")
        self.entry_nome = tk.Entry(frame_form, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Preço:").grid(row=1, column=0, sticky="w")
        self.entry_preco = tk.Entry(frame_form, width=30)
        self.entry_preco.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Quantidade:").grid(row=2, column=0, sticky="w")
        self.entry_quantidade = tk.Entry(frame_form, width=30)
        self.entry_quantidade.grid(row=2, column=1, padx=5, pady=5)

        frame_botoes = tk.Frame(self.root, padx=10, pady=10)
        frame_botoes.pack(fill="x")

        tk.Button(frame_botoes, text="Adicionar", width=15, command=self.adicionar_produto).grid(row=0, column=0, padx=5)
        tk.Button(frame_botoes, text="Atualizar", width=15, command=self.atualizar_produto).grid(row=0, column=1, padx=5)
        tk.Button(frame_botoes, text="Excluir", width=15, command=self.excluir_produto).grid(row=0, column=2, padx=5)
        tk.Button(frame_botoes, text="Limpar", width=15, command=self.limpar_campos).grid(row=0, column=3, padx=5)

        frame_tabela = tk.Frame(self.root, padx=10, pady=10)
        frame_tabela.pack(fill="both", expand=True)

        colunas = ("id", "nome", "preco", "quantidade", "total")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=12)

        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Produto")
        self.tree.heading("preco", text="Preço")
        self.tree.heading("quantidade", text="Quantidade")
        self.tree.heading("total", text="Total em Estoque")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("nome", width=250, anchor="center")
        self.tree.column("preco", width=120, anchor="center")
        self.tree.column("quantidade", width=120, anchor="center")
        self.tree.column("total", width=150, anchor="center")

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_produto)

        self.label_total_estoque = tk.Label(self.root, text="Valor total do estoque: R$ 0.00", font=("Arial", 12, "bold"))
        self.label_total_estoque.pack(pady=10)

    def adicionar_produto(self):
        nome = self.entry_nome.get().strip()
        preco = self.entry_preco.get().strip()
        quantidade = self.entry_quantidade.get().strip()

        if not nome or not preco or not quantidade:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        try:
            preco = float(preco)
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser número e quantidade deve ser inteiro.")
            return

        total = preco * quantidade

        produto = {
            "id": self.proximo_id,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "total": total
        }

        self.produtos.append(produto)
        self.proximo_id += 1

        self.atualizar_tabela()
        self.limpar_campos()

    def atualizar_produto(self):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto para atualizar.")
            return

        nome = self.entry_nome.get().strip()
        preco = self.entry_preco.get().strip()
        quantidade = self.entry_quantidade.get().strip()

        if not nome or not preco or not quantidade:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        try:
            preco = float(preco)
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser número e quantidade deve ser inteiro.")
            return

        item = self.tree.item(item_selecionado)
        produto_id = int(item["values"][0])

        for produto in self.produtos:
            if produto["id"] == produto_id:
                produto["nome"] = nome
                produto["preco"] = preco
                produto["quantidade"] = quantidade
                produto["total"] = preco * quantidade
                break

        self.atualizar_tabela()
        self.limpar_campos()

    def excluir_produto(self):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir.")
            return

        item = self.tree.item(item_selecionado)
        produto_id = int(item["values"][0])

        self.produtos = [p for p in self.produtos if p["id"] != produto_id]

        self.atualizar_tabela()
        self.limpar_campos()

    def selecionar_produto(self, event):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            return

        item = self.tree.item(item_selecionado)
        valores = item["values"]

        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, valores[1])

        self.entry_preco.delete(0, tk.END)
        self.entry_preco.insert(0, valores[2])

        self.entry_quantidade.delete(0, tk.END)
        self.entry_quantidade.insert(0, valores[3])

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        total_geral = 0

        for produto in self.produtos:
            self.tree.insert("", tk.END, values=(
                produto["id"],
                produto["nome"],
                f"{produto['preco']:.2f}",
                produto["quantidade"],
                f"{produto['total']:.2f}"
            ))
            total_geral += produto["total"]

        self.label_total_estoque.config(text=f"Valor total do estoque: R$ {total_geral:.2f}")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaLoja(root)
    root.mainloop()
