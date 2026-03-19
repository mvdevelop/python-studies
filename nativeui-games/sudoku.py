
import tkinter as tk

janela = tk.Tk()
janela.title("Sudoku")

grid = []

for i in range(9):
    linha = []
    for j in range(9):
        e = tk.Entry(janela,width=3,font=("Arial",18),justify="center")
        e.grid(row=i,column=j,padx=2,pady=2)
        linha.append(e)
    grid.append(linha)

def limpar():
    for i in range(9):
        for j in range(9):
            grid[i][j].delete(0,tk.END)

tk.Button(janela,text="Limpar",command=limpar).grid(row=9,column=0,columnspan=9,sticky="we")

janela.mainloop()
