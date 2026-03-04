
with open("dados.txt", "r") as arquivo:
    print("Conteúdo do arquivo:")
    for line in arquivo:
        print(repr(line))
