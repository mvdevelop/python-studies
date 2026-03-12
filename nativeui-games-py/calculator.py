
import tkinter as tk

def clicar(valor):
    entrada.set(entrada.get() + str(valor))

def limpar():
    entrada.set("")

def calcular():
    try:
        resultado = str(eval(entrada.get()))
        entrada.set(resultado)
    except:
        entrada.set("Erro")

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.StringVar()

display = tk.Entry(janela, textvariable=entrada, font=("Arial", 20), bd=10, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4)

botoes = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('+',4,2),('=',4,3)
]

for (texto,linha,coluna) in botoes:
    if texto == '=':
        comando = calcular
    else:
        comando = lambda t=texto: clicar(t)

    tk.Button(janela,text=texto,width=5,height=2,font=("Arial",18),
              command=comando).grid(row=linha,column=coluna)

tk.Button(janela,text="C",width=22,height=2,font=("Arial",14),
          command=limpar).grid(row=5,column=0,columnspan=4)

janela.mainloop()
