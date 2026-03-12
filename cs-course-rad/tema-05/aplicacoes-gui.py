
import tkinter as tk
from tkinter import messagebox, ttk

class AplicacaoGUI:
    def __init__(self):
        # Criação da janela principal (Widget Window)
        self.janela = tk.Tk()
        self.janela.title("Demonstração de Widgets GUI - Python")
        self.janela.geometry("800x700")
        self.janela.resizable(True, True)
        
        # Variáveis para os widgets
        self.var_radio = tk.StringVar()
        self.var_check1 = tk.IntVar()
        self.var_check2 = tk.IntVar()
        
        # Criar um notebook (abas) para organizar os exemplos
        self.notebook = ttk.Notebook(self.janela)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Criar as abas para cada categoria de widgets
        self.criar_aba_basicos()
        self.criar_aba_selecao()
        self.criar_aba_texto()
        self.criar_aba_controle()
        self.criar_aba_dialogos()
        
    def criar_aba_basicos(self):
        """Aba com widgets básicos: Label, Button, Entry"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Básicos")
        
        # Título da aba
        tk.Label(frame, text="Widgets Básicos", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para organizar os componentes
        frame_conteudo = tk.Frame(frame)
        frame_conteudo.pack(pady=10)
        
        # Label (Widget Label)
        tk.Label(frame_conteudo, text="Exemplo de Label:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        self.label_exemplo = tk.Label(frame_conteudo, text="Este é um widget Label", bg="lightblue", padx=10, pady=5)
        self.label_exemplo.grid(row=0, column=1, padx=10, pady=5)
        
        # Entry (Widget Entry)
        tk.Label(frame_conteudo, text="Exemplo de Entry:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        self.entry_exemplo = tk.Entry(frame_conteudo, width=30)
        self.entry_exemplo.grid(row=1, column=1, padx=10, pady=5)
        self.entry_exemplo.insert(0, "Digite algo aqui...")
        
        # Button (Widget Button)
        tk.Label(frame_conteudo, text="Exemplo de Button:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
        
        frame_botoes = tk.Frame(frame_conteudo)
        frame_botoes.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(frame_botoes, text="Mostrar Texto", command=self.mostrar_texto_entry, bg="green", fg="white").pack(side='left', padx=5)
        tk.Button(frame_botoes, text="Limpar", command=self.limpar_entry, bg="red", fg="white").pack(side='left', padx=5)
        
        # Label para mostrar resultado
        self.label_resultado = tk.Label(frame, text="", fg="blue")
        self.label_resultado.pack(pady=10)
        
        # Contador de segundos (Widget Button com contador)
        tk.Label(frame, text="Contador de Segundos:", font=('Arial', 10, 'bold')).pack()
        self.label_contador = tk.Label(frame, text="0", font=('Arial', 16), fg="blue")
        self.label_contador.pack(pady=5)
        
        self.contador_ativo = True
        tk.Button(frame, text="Parar Contador", command=self.parar_contador, bg="orange").pack(pady=5)
        self.iniciar_contador()
        
    def criar_aba_selecao(self):
        """Aba com widgets de seleção: Radiobutton, Checkbox, Combobox"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Seleção")
        
        # Título da aba
        tk.Label(frame, text="Widgets de Seleção", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para organizar os componentes
        frame_conteudo = tk.Frame(frame)
        frame_conteudo.pack(pady=10, padx=20, fill='both')
        
        # Radiobutton (Widget Radiobutton)
        tk.Label(frame_conteudo, text="Radiobutton (Escolha uma opção):", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', pady=10)
        
        frame_radio = tk.Frame(frame_conteudo)
        frame_radio.grid(row=0, column=1, sticky='w', pady=10)
        
        self.var_radio.set("opcao1")  # valor padrão
        
        tk.Radiobutton(frame_radio, text="Opção 1", variable=self.var_radio, value="opcao1").pack(anchor='w')
        tk.Radiobutton(frame_radio, text="Opção 2", variable=self.var_radio, value="opcao2").pack(anchor='w')
        tk.Radiobutton(frame_radio, text="Opção 3", variable=self.var_radio, value="opcao3").pack(anchor='w')
        
        # Checkbox (Widget Checkbox)
        tk.Label(frame_conteudo, text="Checkbox (Escolha múltiplas opções):", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=10)
        
        frame_check = tk.Frame(frame_conteudo)
        frame_check.grid(row=1, column=1, sticky='w', pady=10)
        
        tk.Checkbutton(frame_check, text="Opção Gerencial", variable=self.var_check1).pack(anchor='w')
        tk.Checkbutton(frame_check, text="Opção Técnica", variable=self.var_check2).pack(anchor='w')
        
        # Combobox (Widget Combobox)
        tk.Label(frame_conteudo, text="Combobox (Selecione um mês):", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky='w', pady=10)
        
        self.combobox = ttk.Combobox(frame_conteudo, width=27)
        self.combobox.grid(row=2, column=1, sticky='w', pady=10)
        
        # Adicionar meses ao combobox
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                 "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.combobox['values'] = meses
        self.combobox.set("Selecione um mês")
        
        # Botão para mostrar seleções
        tk.Button(frame_conteudo, text="Mostrar Seleções", command=self.mostrar_selecoes, bg="blue", fg="white").grid(row=3, columnspan=2, pady=20)
        
        # Label para mostrar resultados
        self.label_resultado_selecao = tk.Label(frame, text="", fg="green", justify='left')
        self.label_resultado_selecao.pack(pady=10)
        
    def criar_aba_texto(self):
        """Aba com widgets de texto: Text, Message"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Texto")
        
        # Título da aba
        tk.Label(frame, text="Widgets de Texto", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para organizar os componentes
        frame_conteudo = tk.Frame(frame)
        frame_conteudo.pack(pady=10, padx=20, fill='both')
        
        # Widget Text
        tk.Label(frame_conteudo, text="Widget Text (Área de texto multilinha):", font=('Arial', 10, 'bold')).pack(anchor='w')
        
        self.text_widget = tk.Text(frame_conteudo, height=5, width=60)
        self.text_widget.pack(pady=5)
        
        # Inserir texto no widget Text
        self.text_widget.insert('1.0', "Esta é a primeira linha do widget Text.\nEsta é a segunda linha.\n\nVocê pode editar este texto!")
        
        # Widget Message
        tk.Label(frame_conteudo, text="Widget Message (Mensagem formatada):", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(15,5))
        
        mensagem = "Este é um widget Message do Tkinter. Ele é útil para exibir mensagens de texto que podem ser quebradas automaticamente em múltiplas linhas, diferente do Label que exibe em uma única linha."
        
        self.message_widget = tk.Message(frame_conteudo, text=mensagem, width=400, bg="lightyellow", padx=10, pady=10)
        self.message_widget.pack(pady=5)
        
        # Configurar fonte do Message
        self.message_widget.config(font=('Arial', 10), fg="darkblue")
        
        # Botões para interagir
        frame_botoes = tk.Frame(frame)
        frame_botoes.pack(pady=20)
        
        tk.Button(frame_botoes, text="Obter Texto", command=self.obter_texto, bg="green", fg="white").pack(side='left', padx=5)
        tk.Button(frame_botoes, text="Limpar Text", command=self.limpar_text, bg="red", fg="white").pack(side='left', padx=5)
        
        self.label_resultado_texto = tk.Label(frame, text="", fg="blue")
        self.label_resultado_texto.pack(pady=10)
        
    def criar_aba_controle(self):
        """Aba com widgets de controle: Slider"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Controles")
        
        # Título da aba
        tk.Label(frame, text="Widgets de Controle", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para organizar os componentes
        frame_conteudo = tk.Frame(frame)
        frame_conteudo.pack(pady=10, padx=20, fill='both')
        
        # Widget Slider (Scale)
        tk.Label(frame_conteudo, text="Slider Horizontal (0-100):", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(5,0))
        
        self.slider_horizontal = tk.Scale(frame_conteudo, from_=0, to=100, orient='horizontal', length=300, tickinterval=20)
        self.slider_horizontal.pack(pady=10)
        self.slider_horizontal.set(50)  # valor inicial
        
        tk.Label(frame_conteudo, text="Slider Vertical (0-200):", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(15,0))
        
        frame_sliders = tk.Frame(frame_conteudo)
        frame_sliders.pack(pady=10)
        
        self.slider_vertical = tk.Scale(frame_sliders, from_=0, to=200, orient='vertical', length=200, tickinterval=50)
        self.slider_vertical.pack(side='left', padx=20)
        self.slider_vertical.set(100)  # valor inicial
        
        # Label para mostrar valores dos sliders
        self.label_valores_sliders = tk.Label(frame_sliders, text="Valores:\nHorizontal: 50\nVertical: 100", bg="lightgray", padx=20, pady=10)
        self.label_valores_sliders.pack(side='left', padx=20)
        
        # Botão para atualizar valores
        tk.Button(frame_conteudo, text="Atualizar Valores", command=self.atualizar_valores_sliders, bg="blue", fg="white").pack(pady=10)
        
        # Vincular atualização automática
        self.slider_horizontal.config(command=self.atualizar_valores_automatico)
        self.slider_vertical.config(command=self.atualizar_valores_automatico)
        
    def criar_aba_dialogos(self):
        """Aba com widgets de diálogo: Dialog/Messagebox"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Diálogos")
        
        # Título da aba
        tk.Label(frame, text="Widgets de Diálogo", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para organizar os botões
        frame_botoes = tk.Frame(frame)
        frame_botoes.pack(pady=30)
        
        # Botões para diferentes tipos de diálogo
        tk.Label(frame_botoes, text="Tipos de Messagebox:", font=('Arial', 12, 'bold')).grid(row=0, columnspan=2, pady=10)
        
        # Linha 1 de botões
        tk.Button(frame_botoes, text="Informação", command=self.mostrar_info, bg="lightblue", width=20).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(frame_botoes, text="Aviso", command=self.mostrar_aviso, bg="yellow", width=20).grid(row=1, column=1, padx=10, pady=5)
        
        # Linha 2 de botões
        tk.Button(frame_botoes, text="Erro", command=self.mostrar_erro, bg="red", fg="white", width=20).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(frame_botoes, text="Pergunta", command=self.mostrar_pergunta, bg="lightgreen", width=20).grid(row=2, column=1, padx=10, pady=5)
        
        # Botão Sair com confirmação
        tk.Label(frame, text="Exemplo de diálogo com opções:", font=('Arial', 10, 'bold')).pack(pady=(30,10))
        
        frame_sair = tk.Frame(frame)
        frame_sair.pack()
        
        tk.Button(frame_sair, text="Sair (com confirmação)", command=self.confirmar_saida, bg="darkred", fg="white", padx=20, pady=10).pack()
        
        # Label para mostrar resultado da interação
        self.label_resultado_dialogo = tk.Label(frame, text="", fg="purple", font=('Arial', 10))
        self.label_resultado_dialogo.pack(pady=20)
        
    # Métodos de funcionalidade
    def mostrar_texto_entry(self):
        texto = self.entry_exemplo.get()
        if texto:
            self.label_resultado.config(text=f"Você digitou: {texto}")
        else:
            self.label_resultado.config(text="Campo vazio!")
    
    def limpar_entry(self):
        self.entry_exemplo.delete(0, tk.END)
        self.label_resultado.config(text="Campo limpo!")
    
    def iniciar_contador(self):
        self.valor_contador = 0
        self.atualizar_contador()
    
    def atualizar_contador(self):
        if self.contador_ativo:
            self.valor_contador += 1
            self.label_contador.config(text=str(self.valor_contador))
            self.janela.after(1000, self.atualizar_contador)
    
    def parar_contador(self):
        self.contador_ativo = False
        self.label_contador.config(text="Contador parado!")
    
    def mostrar_selecoes(self):
        radio = self.var_radio.get()
        check1 = "Sim" if self.var_check1.get() == 1 else "Não"
        check2 = "Sim" if self.var_check2.get() == 1 else "Não"
        combo = self.combobox.get()
        
        texto = f"Radiobutton selecionado: {radio}\n"
        texto += f"Checkbox Gerencial: {check1}\n"
        texto += f"Checkbox Técnica: {check2}\n"
        texto += f"Combobox: {combo}"
        
        self.label_resultado_selecao.config(text=texto)
    
    def obter_texto(self):
        texto = self.text_widget.get('1.0', tk.END)
        self.label_resultado_texto.config(text=f"Texto obtido! ({len(texto)} caracteres)")
    
    def limpar_text(self):
        self.text_widget.delete('1.0', tk.END)
        self.label_resultado_texto.config(text="Text widget limpo!")
    
    def atualizar_valores_sliders(self):
        val_h = self.slider_horizontal.get()
        val_v = self.slider_vertical.get()
        self.label_valores_sliders.config(text=f"Valores:\nHorizontal: {val_h}\nVertical: {val_v}")
    
    def atualizar_valores_automatico(self, event=None):
        val_h = self.slider_horizontal.get()
        val_v = self.slider_vertical.get()
        self.label_valores_sliders.config(text=f"Valores:\nHorizontal: {val_h}\nVertical: {val_v}")
    
    # Métodos para diálogos
    def mostrar_info(self):
        messagebox.showinfo("Informação", "Esta é uma mensagem de informação!")
        self.label_resultado_dialogo.config(text="Diálogo de informação exibido")
    
    def mostrar_aviso(self):
        messagebox.showwarning("Aviso", "Este é um aviso importante!")
        self.label_resultado_dialogo.config(text="Diálogo de aviso exibido")
    
    def mostrar_erro(self):
        messagebox.showerror("Erro", "Ocorreu um erro na aplicação!")
        self.label_resultado_dialogo.config(text="Diálogo de erro exibido")
    
    def mostrar_pergunta(self):
        resposta = messagebox.askyesno("Pergunta", "Você concorda com os termos?")
        if resposta:
            self.label_resultado_dialogo.config(text="Usuário respondeu: Sim")
        else:
            self.label_resultado_dialogo.config(text="Usuário respondeu: Não")
    
    def confirmar_saida(self):
        resposta = messagebox.askyesnocancel("Confirmar Saída", "Realmente quer sair?")
        
        if resposta is True:
            self.label_resultado_dialogo.config(text="Usuário escolheu: Sim (Yes)")
            messagebox.showinfo("Info", "Ainda não foi implementado")
        elif resposta is False:
            self.label_resultado_dialogo.config(text="Usuário escolheu: Não (No) - Sair cancelado")
            messagebox.showinfo("Cancelado", "A opção de Sair foi cancelada")
        else:
            self.label_resultado_dialogo.config(text="Usuário escolheu: Cancelar")
    
    def executar(self):
        """Inicia o loop principal da aplicação"""
        self.janela.mainloop()

# Ponto de entrada do programa
if __name__ == "__main__":
    app = AplicacaoGUI()
    app.executar()
