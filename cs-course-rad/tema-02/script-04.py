
arquivo = open("dados.txt", "r")

conteudo = arquivo.read()

print("Tipo do conteúdo:", type(conteudo))

print("Conteúdo do arquivo:")
print(repr(conteudo))

arquivo.close()
