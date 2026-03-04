
minha_lista = ["Arroz", "feijão", "Macarrão"]

texto01 = ', '.join(minha_lista)
with open("dados.txt", 'w') as arquivo:
    arquivo.write(texto01)

texto02 = '\n'.join(minha_lista)
with open("dados.txt", 'w') as arquivo:
    arquivo.write(texto02)
