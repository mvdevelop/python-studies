
with open("data.txt", "r") as arquivo:
    print("Conteúdo do arquivo:")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
