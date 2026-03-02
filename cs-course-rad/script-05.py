
arquivo = open("dados.txt", "r")

conteudo = arquivo.readline()

print("Tipo do conteúdo:", type(conteudo))

print("Conteúdo do arquivo:")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo conteúdo do arquivo:")
print(repr(proximo_conteudo))

arquivo.close()
