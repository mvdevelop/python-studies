
def zenit_polar_encode(text):
    # Criamos as strings de correspondência
    # O segredo é colocar as letras correspondentes na mesma posição
    de  = "zenitZENITpolarPOLAR"
    para = "polarPOLARzenitZENIT"
    
    # Criamos a tabela de tradução
    tabela = str.maketrans(de, para)
    
    # Aplicamos a tradução de uma só vez
    return text.translate(tabela)

def main():
    phrase = "The quick brown fox jumps over the lazy dog"
    
    # Aplicamos o Title Case antes da codificação conforme seu original
    phrase_titled = phrase.title()
 
    # Não é necessário dar split e join, o translate funciona na string inteira
    coded_phrase = zenit_polar_encode(phrase_titled)
    
    print(f"Original: {phrase_titled}")
    print(f"Coded:    {coded_phrase}")

if __name__ == "__main__":
    main()
